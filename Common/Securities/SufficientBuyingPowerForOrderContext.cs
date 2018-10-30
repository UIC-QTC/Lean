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

using QuantConnect.Orders;

namespace QuantConnect.Securities
{
    /// <summary>
    /// Defines the parameters for <see cref="IBuyingPowerModel.HasSufficientBuyingPowerForOrder"/>
    /// </summary>
    public class SufficientBuyingPowerForOrderContext
    {
        /// <summary>
        /// Gets the order
        /// </summary>
        public Order Order { get; }

        /// <summary>
        /// Gets the security
        /// </summary>
        public Security Security { get; }

        /// <summary>
        /// Gets the algorithm's portfolio
        /// </summary>
        public SecurityPortfolioManager Portfolio { get; }

        /// <summary>
        /// Initializes a new instance of the <see cref="SufficientBuyingPowerForOrderContext"/> class
        /// </summary>
        /// <param name="portfolio">The algorithm's portfolio</param>
        /// <param name="security">The security</param>
        /// <param name="order">The order</param>
        public SufficientBuyingPowerForOrderContext(SecurityPortfolioManager portfolio, Security security, Order order)
        {
            Portfolio = portfolio;
            Security = security;
            Order = order;
        }

        /// <summary>
        /// Creates the result declaring that the algorithm has sufficient buying power for the order
        /// </summary>
        /// <returns>Result object indicating that we have sufficient buying power</returns>
        public HasSufficientBuyingPowerForOrderResult HasSufficientBuyingPower()
        {
            return new HasSufficientBuyingPowerForOrderResult(true);
        }

        /// <summary>
        /// Creates the result declaring that the algorithm does NOT have sufficient buying power for the order
        /// </summary>
        /// <param name="reason">A user friendly reason as to why we don't have sufficient buying power</param>
        /// <returns>Result object indicating that we do NOT have sufficient buying power</returns>
        public HasSufficientBuyingPowerForOrderResult HasInsufficientBuyingPower(string reason)
        {
            return new HasSufficientBuyingPowerForOrderResult(false, reason);
        }
    }
}