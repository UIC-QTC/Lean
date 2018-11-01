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
using QuantConnect.Logging;
using QuantConnect.Orders;
using QuantConnect.Orders.Fees;

namespace QuantConnect.Securities
{
    /// <summary>
    /// Provides a base class for all buying power models
    /// </summary>
    public class BuyingPowerModel : IBuyingPowerModel
    {
        private decimal _initialMarginRequirement;
        private decimal _maintenanceMarginRequirement;
        /// <summary>
        /// The percentage used to determine the required unused buying power for the account.
        /// </summary>
        protected decimal RequiredFreeBuyingPowerPercent;

        /// <summary>
        /// Initializes a new instance of the <see cref="BuyingPowerModel"/> with no leverage (1x)
        /// </summary>
        public BuyingPowerModel()
            : this(1m)
        {
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="BuyingPowerModel"/>
        /// </summary>
        /// <param name="initialMarginRequirement">The percentage of an order's absolute cost
        /// that must be held in free cash in order to place the order</param>
        /// <param name="maintenanceMarginRequirement">The percentage of the holding's absolute
        /// cost that must be held in free cash in order to avoid a margin call</param>
        /// <param name="requiredFreeBuyingPowerPercent">The percentage used to determine the required
        /// unused buying power for the account.</param>
        public BuyingPowerModel(
            decimal initialMarginRequirement,
            decimal maintenanceMarginRequirement,
            decimal requiredFreeBuyingPowerPercent
            )
        {
            if (initialMarginRequirement < 0 || initialMarginRequirement > 1)
            {
                throw new ArgumentException("Initial margin requirement must be between 0 and 1");
            }

            if (maintenanceMarginRequirement < 0 || maintenanceMarginRequirement > 1)
            {
                throw new ArgumentException("Maintenance margin requirement must be between 0 and 1");
            }

            if (requiredFreeBuyingPowerPercent < 0 || requiredFreeBuyingPowerPercent > 1)
            {
                throw new ArgumentException("Free Buying Power Percent requirement must be between 0 and 1");
            }

            _initialMarginRequirement = initialMarginRequirement;
            _maintenanceMarginRequirement = maintenanceMarginRequirement;
            RequiredFreeBuyingPowerPercent = requiredFreeBuyingPowerPercent;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="BuyingPowerModel"/>
        /// </summary>
        /// <param name="leverage">The leverage</param>
        /// <param name="requiredFreeBuyingPowerPercent">The percentage used to determine the required
        /// unused buying power for the account.</param>
        public BuyingPowerModel(decimal leverage, decimal requiredFreeBuyingPowerPercent = 0)
        {
            if (leverage < 1)
            {
                throw new ArgumentException("Leverage must be greater than or equal to 1.");
            }

            if (requiredFreeBuyingPowerPercent < 0 || requiredFreeBuyingPowerPercent > 1)
            {
                throw new ArgumentException("Free Buying Power Percent requirement must be between 0 and 1");
            }

            _initialMarginRequirement = 1 / leverage;
            _maintenanceMarginRequirement = 1 / leverage;
            RequiredFreeBuyingPowerPercent = requiredFreeBuyingPowerPercent;
        }

        /// <summary>
        /// Gets the current leverage of the security
        /// </summary>
        /// <param name="security">The security to get leverage for</param>
        /// <returns>The current leverage in the security</returns>
        public virtual decimal GetLeverage(Security security)
        {
            return 1 / GetMaintenanceMarginRequirement(security);
        }

        /// <summary>
        /// Sets the leverage for the applicable securities, i.e, equities
        /// </summary>
        /// <remarks>
        /// This is added to maintain backwards compatibility with the old margin/leverage system
        /// </remarks>
        /// <param name="security"></param>
        /// <param name="leverage">The new leverage</param>
        public virtual void SetLeverage(Security security, decimal leverage)
        {
            if (leverage < 1)
            {
                throw new ArgumentException("Leverage must be greater than or equal to 1.");
            }

            var margin = 1 / leverage;
            _initialMarginRequirement = margin;
            _maintenanceMarginRequirement = margin;
        }

        /// <summary>
        /// The percentage of the holding's absolute cost that must be held in free cash in order to avoid a margin call
        /// </summary>
        public virtual decimal GetMaintenanceMarginRequirement(Security security)
        {
            return _maintenanceMarginRequirement;
        }

        /// <summary>
        /// Check if there is sufficient buying power to execute this order.
        /// </summary>
        /// <param name="context">A context object containing the algorithm's portfolio, the order to check and the order's security</param>
        /// <returns>Returns buying power information for an order</returns>
        public virtual HasSufficientBuyingPowerForOrderResult HasSufficientBuyingPowerForOrder(
            SufficientBuyingPowerForOrderContext context
            )
        {
            var portfolio = context.Portfolio;
            var security = context.Security;
            var order = context.Order;

            // short circuit the div 0 case
            if (order.Quantity == 0)
            {
                return context.HasSufficientBuyingPower();
            }

            var ticket = portfolio.Transactions.GetOrderTicket(order.Id);
            if (ticket == null)
            {
                var reason = $"Null order ticket for id: {order.Id}";
                Log.Error($"SecurityMarginModel.HasSufficientBuyingPowerForOrder(): {reason}");
                return context.HasInsufficientBuyingPower(reason);
            }

            if (order.Type == OrderType.OptionExercise)
            {
                // for option assignment and exercise orders we look into the requirements to process the underlying security transaction
                var option = (Option.Option) security;
                var underlying = option.Underlying;

                if (option.IsAutoExercised(underlying.Close))
                {
                    var quantity = option.GetExerciseQuantity(order.Quantity);

                    var newOrder = new LimitOrder
                    {
                        Id = order.Id,
                        Time = order.Time,
                        LimitPrice = option.StrikePrice,
                        Symbol = underlying.Symbol,
                        Quantity = option.Symbol.ID.OptionRight == OptionRight.Call ? quantity : -quantity
                    };

                    // we continue with this call for underlying
                    return underlying.BuyingPowerModel.HasSufficientBuyingPowerForOrder(
                        new SufficientBuyingPowerForOrderContext(portfolio, security, newOrder)
                    );
                }

                return context.HasSufficientBuyingPower();
            }

            // When order only reduces or closes a security position, capital is always sufficient
            if (security.Holdings.Quantity * order.Quantity < 0 && Math.Abs(security.Holdings.Quantity) >= Math.Abs(order.Quantity))
            {
                return context.HasSufficientBuyingPower();
            }

            var freeMargin = GetMarginRemaining(new MarginRemainingContext(portfolio, security, order.Direction)).Value;
            var initialMarginRequiredForOrder = GetInitialMarginRequiredForOrder(new InitialMarginRequiredForOrderContext(security, order)).Value;

            // pro-rate the initial margin required for order based on how much has already been filled
            var percentUnfilled = (Math.Abs(order.Quantity) - Math.Abs(ticket.QuantityFilled)) / Math.Abs(order.Quantity);
            var initialMarginRequiredForRemainderOfOrder = percentUnfilled * initialMarginRequiredForOrder;

            if (Math.Abs(initialMarginRequiredForRemainderOfOrder) > freeMargin)
            {
                var reason =$"Id: {order.Id}, " +
                    $"Initial Margin: {initialMarginRequiredForRemainderOfOrder.Normalize()}, " +
                    $"Free Margin: {freeMargin.Normalize()}";

                Log.Error($"SecurityMarginModel.HasSufficientBuyingPowerForOrder(): {reason}");
                return context.HasInsufficientBuyingPower(reason);
            }

            return context.HasSufficientBuyingPower();
        }

        /// <summary>
        /// Get the maximum market order quantity to obtain a position with a given value in account currency.
        /// Will not take into account buying power.
        /// </summary>
        /// <param name="context">A context object containing the algorithm's portfolio, the target holdings as percentage of total portfolio value and the order's security</param>
        /// <returns>Returns the maximum allowed market order quantity and if zero, also the reason</returns>
        public virtual GetMaximumOrderQuantityForTargetValueResult GetMaximumOrderQuantityForTargetValue(
            MaximumOrderQuantityForTargetValueContext context
            )
        {
            var portfolio = context.Portfolio;
            var security = context.Security;
            var target = context.Target;

            // adjust target portfolio value to comply with required Free Buying Power Percent
            var totalPortfolioValueLessFreeBuyingPowerPercent = portfolio.TotalPortfolioValue - portfolio.TotalPortfolioValue * RequiredFreeBuyingPowerPercent;
            var targetPortfolioValue = target * totalPortfolioValueLessFreeBuyingPowerPercent;

            // if targeting zero, simply return the negative of the quantity
            if (targetPortfolioValue == 0)
            {
                return context.Result(-security.Holdings.Quantity);
            }

            var currentHoldingsValue = security.Holdings.HoldingsValue;

            // remove directionality, we'll work in the land of absolutes
            var targetOrderValue = Math.Abs(targetPortfolioValue - currentHoldingsValue);
            var direction = targetPortfolioValue > currentHoldingsValue ? OrderDirection.Buy : OrderDirection.Sell;

            // determine the unit price in terms of the account currency
            var unitPrice = new MarketOrder(security.Symbol, 1, DateTime.UtcNow).GetValue(security);
            if (unitPrice == 0)
            {
                return context.Error(
                    $"The price of the {security.Symbol.Value} security is zero because it does not have any market " +
                    "data yet. When the security price is set this security will be ready for trading."
                );
            }

            // calculate the total margin available
            var marginRemaining = GetMarginRemaining(new MarginRemainingContext(portfolio, security, direction)).Value;
            if (marginRemaining <= 0)
            {
                return context.Error(
                    "The portfolio does not have enough margin available."
                );
            }

            // continue iterating while we do not have enough margin for the order
            decimal orderValue = 0;
            decimal orderFees = 0;
            // compute the initial order quantity
            var orderQuantity = targetOrderValue / unitPrice;

            // rounding off Order Quantity to the nearest multiple of Lot Size
            orderQuantity -= orderQuantity % security.SymbolProperties.LotSize;
            if (orderQuantity == 0)
            {
                return context.Zero(
                    $"The order quantity is less than the lot size of {security.SymbolProperties.LotSize} and has been rounded to zero."
                );
            }

            var loopCount = 0;
            // Just in case...
            var lastOrderQuantity = 0m;
            do
            {
                // Each loop will reduce the order quantity based on the difference between orderValue and targetOrderValue
                if (orderValue > targetOrderValue)
                {
                    var currentOrderValuePerUnit = orderValue / orderQuantity;
                    var amountOfOrdersToRemove = (orderValue - targetOrderValue) / currentOrderValuePerUnit;
                    if (amountOfOrdersToRemove < security.SymbolProperties.LotSize)
                    {
                        // we will always substract at leat 1 LotSize
                        amountOfOrdersToRemove = security.SymbolProperties.LotSize;
                    }

                    orderQuantity -= amountOfOrdersToRemove;
                    orderQuantity -= orderQuantity % security.SymbolProperties.LotSize;
                }

                if (orderQuantity <= 0)
                {
                    return context.Error(
                        $"The order quantity is less than the lot size of {security.SymbolProperties.LotSize} " +
                        $"and has been rounded to zero.Target order value {targetOrderValue}. Order fees " +
                        $"{orderFees}. Order quantity {orderQuantity}."
                    );
                }

                // generate the order
                var order = new MarketOrder(security.Symbol, orderQuantity, DateTime.UtcNow);
                orderFees = security.FeeModel.GetOrderFee(security, order);

                // The TPV, take out the fees(unscaled) => yields available value for trading(less fees)
                // then scale that by the target -- finally remove currentHoldingsValue to get targetOrderValue
                targetOrderValue = Math.Abs(
                    (portfolio.TotalPortfolioValue - orderFees - portfolio.TotalPortfolioValue * RequiredFreeBuyingPowerPercent)
                    * target - currentHoldingsValue
                );

                // After the first loop we need to recalculate order quantity since now we have fees included
                if (loopCount == 0)
                {
                    // re compute the initial order quantity
                    orderQuantity = targetOrderValue / unitPrice;
                    orderQuantity -= orderQuantity % security.SymbolProperties.LotSize;
                }
                else
                {
                    // Start safe check after first loop
                    if (lastOrderQuantity == orderQuantity)
                    {
                        throw new Exception(
                            $"GetMaximumOrderQuantityForTargetValue failed to converge to target order value {targetOrderValue}. " +
                            $"Current order value is {orderValue}. Order quantity {orderQuantity}. Lot size is {security.SymbolProperties.LotSize}. " +
                            $"Order fees {orderFees}. Security symbol {security.Symbol}"
                        );
                    }

                    lastOrderQuantity = orderQuantity;
                }

                orderValue = orderQuantity * unitPrice;
                loopCount++;
                // we always have to loop at least twice
            }
            while (loopCount < 2 || orderValue > targetOrderValue);

            // add directionality back in
            orderQuantity = (direction == OrderDirection.Sell ? -1 : 1) * orderQuantity;
            return context.Result(orderQuantity);
        }

        /// <summary>
        /// Gets the amount of buying power reserved to maintain the specified position
        /// </summary>
        /// <param name="context">A context object containing the security</param>
        /// <returns>The reserved buying power in account currency</returns>
        public virtual ReservedBuyingPowerForPosition GetReservedBuyingPowerForPosition(ReservedBuyingPowerForPositionContext context)
        {
            var maintenanceMargin = GetMaintenanceMargin(new MaintenanceMarginContext(context.Security));
            return context.ResultInAccountCurrency(maintenanceMargin.Value);
        }

        /// <summary>
        /// Gets the buying power available for a trade
        /// </summary>
        /// <param name="context">A context object containing the algorithm's potrfolio, security, and order direction</param>
        /// <returns>The buying power available for the trade</returns>
        public virtual BuyingPower GetBuyingPower(BuyingPowerContext context)
        {
            var marginRemaining = GetMarginRemaining(new MarginRemainingContext(context.Portfolio, context.Security, context.Direction));
            return context.ResultInAccountCurrency(marginRemaining.Value);
        }

        /// <summary>
        /// Gets the total margin required to execute the specified order in units of the account currency including fees
        /// </summary>
        /// <param name="context">A context object containing the security and the order</param>
        /// <returns>The total margin in terms of the currency quoted in the order</returns>
        protected virtual Margin GetInitialMarginRequiredForOrder(InitialMarginRequiredForOrderContext context)
        {
            var security = context.Security;
            var order = context.Order;

            //Get the order value from the non-abstract order classes (MarketOrder, LimitOrder, StopMarketOrder)
            //Market order is approximated from the current security price and set in the MarketOrder Method in QCAlgorithm.
            var orderFees = security.FeeModel.GetOrderFee(security, order);

            var orderValue = order.GetValue(security) * GetInitialMarginRequirement(security);
            var marginRequired = orderValue + Math.Sign(orderValue) * orderFees;
            return context.ResultInAccountCurrency(marginRequired);
        }

        /// <summary>
        /// Gets the margin currently alloted to the specified holding
        /// </summary>
        /// <param name="context">A context object containing the security</param>
        /// <returns>The maintenance margin required for the </returns>
        protected virtual Margin GetMaintenanceMargin(MaintenanceMarginContext context)
        {
            var security = context.Security;
            var maintenanceMargin = security.Holdings.AbsoluteHoldingsCost * GetMaintenanceMarginRequirement(security);
            return context.ResultInAccountCurrency(maintenanceMargin);
        }

        /// <summary>
        /// Gets the margin cash available for a trade
        /// </summary>
        /// <param name="context">A context object containing the algorithm's portfolio, the security and the desired order direction</param>
        /// <returns>The margin available for the trade</returns>
        protected virtual Margin GetMarginRemaining(MarginRemainingContext context)
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
                                security.Holdings.AbsoluteHoldingsValue * GetInitialMarginRequirement(security);
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
                                security.Holdings.AbsoluteHoldingsValue * GetInitialMarginRequirement(security);
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
        protected virtual decimal GetInitialMarginRequirement(Security security)
        {
            return _initialMarginRequirement;
        }

        /// <summary>
        /// Defines the result for <see cref="GetMaintenanceMargin"/>, <see cref="GetMarginRemaining"/> and <see cref="GetInitialMarginRequiredForOrder"/>
        /// </summary>
        protected class Margin
        {
            /// <summary>
            /// Gets the initial margin requirement
            /// </summary>
            public decimal Value { get; }

            /// <summary>
            /// Initializes a new instance of the <see cref="Margin"/> class
            /// </summary>
            /// <param name="value">The initial margin requirement</param>
            public Margin(decimal value)
            {
                Value = value;
            }
        }

        /// <summary>
        /// Defines the parameters for<see cref="BuyingPowerModel.GetMaintenanceMargin"/> and <see cref="BuyingPowerModel.GetMarginRemaining"/>
        /// </summary>
        protected class MaintenanceMarginContext
        {
            /// <summary>
            /// Gets the security
            /// </summary>
            public Security Security { get; }

            /// <summary>
            /// Initializes a new instance of the <see cref="MaintenanceMarginContext"/> class
            /// </summary>
            /// <param name="security"></param>
            public MaintenanceMarginContext(Security security)
            {
                Security = security;
            }

            /// <summary>
            /// Creates the result using the specified maintenance margin
            /// </summary>
            /// <param name="maintenanceMargin">The maintenance margin for the specified security</param>
            /// <param name="currency">The currency units the margin is denominated in</param>
            /// <returns>The maintenance margin for the security</returns>
            public Margin Result(decimal maintenanceMargin, string currency)
            {
                // TODO: Properly account for 'currency' - not accounted for currently as only performing mechanical refactoring
                return new Margin(maintenanceMargin);
            }

            /// <summary>
            /// Creates the result using the specified maintenance margin
            /// </summary>
            /// <param name="maintenanceMargin">The maintenance margin for the specified security</param>
            /// <returns>The maintenance margin for the security</returns>
            public Margin ResultInAccountCurrency(decimal maintenanceMargin)
            {
                return new Margin(maintenanceMargin);
            }
        }

        /// <summary>
        /// Defines the parameters for <see cref="BuyingPowerModel.GetMarginRemaining"/>
        /// </summary>
        protected class MarginRemainingContext
        {
            /// <summary>
            /// Gets the security
            /// </summary>
            public Security Security { get; }

            /// <summary>
            /// Gets the algorithm's portfolio
            /// </summary>
            public SecurityPortfolioManager Portfolio { get; }

            /// <summary>
            /// Gets the direction in which remaining margin is to be computed
            /// </summary>
            public OrderDirection Direction { get; }

            /// <summary>
            /// Initializes a new instance of the <see cref="MarginRemainingContext"/> class
            /// </summary>
            /// <param name="portfolio"></param>
            /// <param name="security">The security</param>
            /// <param name="direction"></param>
            public MarginRemainingContext(SecurityPortfolioManager portfolio, Security security, OrderDirection direction)
            {
                Security = security;
                Portfolio = portfolio;
                Direction = direction;
            }

            /// <summary>
            /// Creates the result using the specified remaining margin
            /// </summary>
            /// <param name="remainingMargin">The remaining margin available for a trade in the requested direction</param>
            /// <param name="currency">The currency units the margin is denominated in</param>
            /// <returns>The initial margin required for the order</returns>
            public Margin Result(decimal remainingMargin, string currency)
            {
                // TODO: Properly account for 'currency' - not accounted for currently as only performing mechanical refactoring
                return new Margin(remainingMargin);
            }

            /// <summary>
            /// Creates the result using the specified initial margin in units of the account currency
            /// </summary>
            /// <param name="initialMargin">The initial margin required for the order</param>
            /// <returns>The initial margin required for the order</returns>
            public Margin ResultInAccountCurrency(decimal initialMargin)
            {
                return new Margin(initialMargin);
            }
        }

        /// <summary>
        /// Defines the parameters for <see cref="BuyingPowerModel.GetInitialMarginRequiredForOrder"/>
        /// </summary>
        protected class InitialMarginRequiredForOrderContext
        {
            /// <summary>
            /// Gets the security
            /// </summary>
            public Security Security { get; }

            /// <summary>
            /// Gets the order for which initial margin is to be computed
            /// </summary>
            public Order Order { get; }

            /// <summary>
            /// Initializes a new instance of the <see cref="InitialMarginRequiredForOrderContext"/> class
            /// </summary>
            /// <param name="security">The security</param>
            /// <param name="order">The order to compute initial margin for</param>
            public InitialMarginRequiredForOrderContext(Security security, Order order)
            {
                Security = security;
                Order = order;
            }

            /// <summary>
            /// Creates the result using the specified initial margin
            /// </summary>
            /// <param name="initialMargin">The initial margin required for the order</param>
            /// <param name="currency">The currency units the margin is denominated in</param>
            /// <returns>The initial margin required for the order</returns>
            public Margin Result(decimal initialMargin, string currency)
            {
                // TODO: Properly account for 'currency' - not accounted for currently as only performing mechanical refactoring
                return new Margin(initialMargin);
            }

            /// <summary>
            /// Creates the result using the specified initial margin in units of the account currency
            /// </summary>
            /// <param name="initialMargin">The initial margin required for the order</param>
            /// <returns>The initial margin required for the order</returns>
            public Margin ResultInAccountCurrency(decimal initialMargin)
            {
                return new Margin(initialMargin);
            }
        }
    }
}