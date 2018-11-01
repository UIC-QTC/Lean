/*
 * QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
 * Lean Algorithmic Trading Engine v2.0. Copyright 2014 QuantConnect Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
*/

using System;
using System.Globalization;
using System.IO;
using System.Linq;
using QuantConnect.Logging;
using QuantConnect.Orders;
using QuantConnect.Orders.Fees;

namespace QuantConnect.Securities.Future
{
    /// <summary>
    /// Represents a simple margining model for margining futures. Margin file contains Initial and Maintenance margins
    /// </summary>
    public class FutureMarginModel : SecurityMarginModel
    {
        private static readonly object DataFolderSymbolLock = new object();

        // historical database of margin requirements
        private MarginRequirementsEntry[] _marginRequirementsHistory;
        private int _marginCurrentIndex;

        /// <summary>
        /// Initializes a new instance of the <see cref="FutureMarginModel"/>
        /// </summary>
        /// <param name="requiredFreeBuyingPowerPercent">The percentage used to determine the required unused buying power for the account.</param>
        public FutureMarginModel(decimal requiredFreeBuyingPowerPercent = 0)
        {
            RequiredFreeBuyingPowerPercent = requiredFreeBuyingPowerPercent;
        }

        /// <summary>
        /// Gets the current leverage of the security
        /// </summary>
        /// <param name="security">The security to get leverage for</param>
        /// <returns>The current leverage in the security</returns>
        public override decimal GetLeverage(Security security)
        {
            var marginRequirement = GetMaintenanceMarginRequirement(security, security.Holdings.HoldingsCost);
            return marginRequirement == 0 ? 1m : 1 / marginRequirement;
        }

        /// <summary>
        /// Sets the leverage for the applicable securities, i.e, futures
        /// </summary>
        /// <remarks>
        /// This is added to maintain backwards compatibility with the old margin/leverage system
        /// </remarks>
        /// <param name="security"></param>
        /// <param name="leverage">The new leverage</param>
        public override void SetLeverage(Security security, decimal leverage)
        {
            // Futures are leveraged products and different leverage cannot be set by user.
            throw new InvalidOperationException("Futures are leveraged products and different leverage cannot be set by user");
        }

        /// <summary>
        /// The percentage of the holding's absolute cost that must be held in free cash in order to avoid a margin call
        /// </summary>
        public override decimal GetMaintenanceMarginRequirement(Security security)
        {
            return GetMaintenanceMarginRequirement(security, security.Holdings.HoldingsCost);
        }

        /// <summary>
        /// The percentage of an order's absolute cost that must be held in free cash in order to place the order
        /// </summary>
        private decimal GetInitialMarginRequirement(Security security, decimal holdingValue)
        {
            if (security?.GetLastData() == null || holdingValue == 0m)
                return 0m;

            var symbol = security.Symbol;
            var date = security.GetLastData().Time.Date;
            var marginReq = GetCurrentMarginRequirements(symbol, date);

            return marginReq.InitialOvernight / holdingValue;
        }

        /// <summary>
        /// The percentage of the holding's absolute cost that must be held in free cash in order to avoid a margin call
        /// </summary>
        private decimal GetMaintenanceMarginRequirement(Security security, decimal holdingValue)
        {
            if (security?.GetLastData() == null || holdingValue == 0m)
                return 0m;

            var symbol = security.Symbol;
            var date = security.GetLastData().Time.Date;
            var marginReq = GetCurrentMarginRequirements(symbol, date);

            return marginReq.MaintenanceOvernight / holdingValue;
        }

        /// <summary>
        /// Gets the total margin required to execute the specified order in units of the account currency including fees
        /// </summary>
        /// <param name="context">A context object containing the security and the order</param>
        /// <returns>The total margin in terms of the currency quoted in the order</returns>
        protected override Margin GetInitialMarginRequiredForOrder(InitialMarginRequiredForOrderContext context)
        {
            var security = context.Security;
            var order = context.Order;

            //Get the order value from the non-abstract order classes (MarketOrder, LimitOrder, StopMarketOrder)
            //Market order is approximated from the current security price and set in the MarketOrder Method in QCAlgorithm.
            var orderFees = security.FeeModel.GetOrderFee(security, order);
            var value = order.GetValue(security);
            var orderValue = value * GetInitialMarginRequirement(security, value);

            var initialMarginRequired = orderValue + Math.Sign(orderValue) * orderFees;
            return context.ResultInAccountCurrency(initialMarginRequired);
        }

        /// <summary>
        /// Gets the margin currently alloted to the specified holding
        /// </summary>
        /// <param name="context">A context object containing the security</param>
        /// <returns>The maintenance margin required for the </returns>
        protected override Margin GetMaintenanceMargin(MaintenanceMarginContext context)
        {
            var security = context.Security;

            if (security?.GetLastData() == null || security.Holdings.HoldingsCost == 0m)
            {
                return context.ResultInAccountCurrency(0m);
            }

            var symbol = security.Symbol;
            var date = security.GetLastData().Time.Date;
            var marginReq = GetCurrentMarginRequirements(symbol, date);

            var maintenanceMargin = marginReq.MaintenanceOvernight * Math.Sign(security.Holdings.HoldingsCost);
            return context.ResultInAccountCurrency(maintenanceMargin);
        }

        /// <summary>
        /// Gets the margin cash available for a trade
        /// </summary>
        /// <param name="context">A context object containing the algorithm's portfolio, the security and the desired order direction</param>
        /// <returns>The margin available for the trade</returns>
        protected override Margin GetMarginRemaining(MarginRemainingContext context)
        {
            var security = context.Security;
            var portfolio = context.Portfolio;
            var direction = context.Direction;

            var result = portfolio.MarginRemaining;

            if (direction != OrderDirection.Hold)
            {
                var holdings = security.Holdings;
                //If the order is in the same direction as holdings, our remaining cash is our cash
                //In the opposite direction, our remaining cash is 2 x current value of assets + our cash
                var maintenanceMargin = GetMaintenanceMargin(new MaintenanceMarginContext(security)).Value;
                if (holdings.IsLong)
                {
                    switch (direction)
                    {
                        case OrderDirection.Sell:
                            result +=
                                // portion of margin to close the existing position
                                maintenanceMargin +
                                // portion of margin to open the new position
                                security.Holdings.AbsoluteHoldingsValue * GetInitialMarginRequirement(security, security.Holdings.HoldingsValue);
                            break;
                    }
                }
                else if (holdings.IsShort)
                {
                    switch (direction)
                    {
                        case OrderDirection.Buy:
                            result +=
                                // portion of margin to close the existing position
                                maintenanceMargin +
                                // portion of margin to open the new position
                                security.Holdings.AbsoluteHoldingsValue * GetInitialMarginRequirement(security, security.Holdings.HoldingsValue);
                            break;
                    }
                }
            }

            result -= portfolio.TotalPortfolioValue * RequiredFreeBuyingPowerPercent;
            var marginRemaining = result < 0 ? 0 : result;
            return context.ResultInAccountCurrency(marginRemaining);
        }

        /// <summary>
        /// The percentage of an order's absolute cost that must be held in free cash in order to place the order
        /// </summary>
        protected override decimal GetInitialMarginRequirement(Security security)
        {
            return GetInitialMarginRequirement(security, security.Holdings.HoldingsCost);
        }

        private MarginRequirementsEntry GetCurrentMarginRequirements (Symbol symbol, DateTime date)
        {
            if (_marginRequirementsHistory == null)
            {
                _marginRequirementsHistory = LoadMarginRequirementsHistory(symbol);
                _marginCurrentIndex = 0;
            }

            while (_marginCurrentIndex + 1 < _marginRequirementsHistory.Length &&
                _marginRequirementsHistory[_marginCurrentIndex + 1].Date <= date )
            {
                _marginCurrentIndex++;
            }

            return _marginRequirementsHistory[_marginCurrentIndex];
        }

        /// <summary>
        /// Gets the sorted list of historical margin changes produced by reading in the margin requirements
        /// data found in /Data/symbol-margin/
        /// </summary>
        /// <returns>Sorted list of historical margin changes</returns>
        private MarginRequirementsEntry[] LoadMarginRequirementsHistory(Symbol symbol)
        {
            lock (DataFolderSymbolLock)
            {
                var directory = Path.Combine(Globals.DataFolder,
                                            symbol.SecurityType.ToLower(),
                                            symbol.ID.Market.ToLower(),
                                            "margins");
                return FromCsvFile(Path.Combine(directory, symbol.ID.Symbol + ".csv"));
            }
        }

        /// <summary>
        /// Reads margin requirements file and returns a sorted list of historical margin changes
        /// </summary>
        /// <param name="file">The csv file to be read</param>
        /// <returns>Sorted list of historical margin changes</returns>
        private MarginRequirementsEntry[] FromCsvFile(string file)
        {
            if (!File.Exists(file))
            {
                Log.Trace("Unable to locate future margin requirements file. Defaulting to zero margin for this symbol. File: {0}" , file);

                return new[] {
                                new MarginRequirementsEntry
                                {
                                  Date = DateTime.MinValue
                                }
                            };
            }

            // skip the first header line, also skip #'s as these are comment lines

            return File.ReadLines(file)
                .Where(x => !x.StartsWith("#") && !string.IsNullOrWhiteSpace(x))
                .Skip(1)
                .Select(FromCsvLine)
                .OrderBy(x => x.Date)
                .ToArray();
        }

        /// <summary>
        /// Creates a new instance of <see cref="MarginRequirementsEntry"/> from the specified csv line
        /// </summary>
        /// <param name="csvLine">The csv line to be parsed</param>
        /// <returns>A new <see cref="MarginRequirementsEntry"/> for the specified csv line</returns>
        private MarginRequirementsEntry FromCsvLine(string csvLine)
        {
            var line = csvLine.Split(',');
            var date = DateTime.MinValue;

            if(!DateTime.TryParseExact(line[0], DateFormat.EightCharacter, CultureInfo.InvariantCulture, DateTimeStyles.None, out date))
            {
                Log.Trace("Couldn't parse date/time while reading future margin requirement file. Date {0}. Line: {1}", line[0], csvLine);
            }

            var initial = 0m;

            if (!decimal.TryParse(line[1], out initial))
            {
                Log.Trace("Couldn't parse Initial margin requirements while reading future margin requirement file. Date {0}. Line: {1}", line[1], csvLine);
            }

            var maintenance = 0m;

            if (!decimal.TryParse(line[2], out maintenance))
            {
                Log.Trace("Couldn't parse Maintenance margin requirements while reading future margin requirement file. Date {0}. Line: {1}", line[2], csvLine);
            }

            return new MarginRequirementsEntry()
                    {
                        Date = date,
                        InitialOvernight = initial,
                        MaintenanceOvernight = maintenance
                    };
        }

        // Private POCO class for modeling margin requirements at given date
        class MarginRequirementsEntry
        {
            /// <summary>
            /// Date of margin requirements change
            /// </summary>
            public DateTime Date;

            /// <summary>
            /// Initial overnight margin for the contract effective from the date of change
            /// </summary>
            public decimal InitialOvernight;

            /// <summary>
            /// Maintenance overnight margin for the contract effective from the date of change
            /// </summary>
            public decimal MaintenanceOvernight;
        }
    }
}