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

namespace QuantConnect.Securities
{
    /// <summary>
    /// Defines the parameters for <see cref="IBuyingPowerModel.GetMaximumOrderQuantityForTargetValue"/>
    /// </summary>
    public class MaximumOrderQuantityForTargetValueContext
    {
        /// <summary>
        /// Gets the target holdings as a percentage of <see cref="SecurityPortfolioManager.TotalPortfolioValue"/>
        /// </summary>
        public decimal Target { get; }

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
        /// <param name="target">The target holdings as a percentage of total portfolio value</param>
        public MaximumOrderQuantityForTargetValueContext(SecurityPortfolioManager portfolio, Security security, decimal target)
        {
            Portfolio = portfolio;
            Security = security;
            Target = target;
        }

        /// <summary>
        /// Creates a result defining the maximum order quantity the algorithm ca
        /// </summary>
        /// <param name="maximumOrderQuantity">The maximum order quantity</param>
        /// <returns>A success result with the specified maximum order quantity</returns>
        public GetMaximumOrderQuantityForTargetValueResult Result(decimal maximumOrderQuantity)
        {
            return new GetMaximumOrderQuantityForTargetValueResult(maximumOrderQuantity);
        }

        /// <summary>
        /// Creates an error result with the specified reason
        /// </summary>
        /// <param name="reason">The reason for the error</param>
        /// <returns>An error result with the specified reason</returns>
        public GetMaximumOrderQuantityForTargetValueResult Error(string reason)
        {
            return new GetMaximumOrderQuantityForTargetValueResult(0m, reason, true);
        }

        /// <summary>
        /// Creates a zero valued result with the specified reason
        /// </summary>
        /// <param name="reason">The reason for the error</param>
        /// <returns>A success result with the zero quantity and the specified reason for zero quantity</returns>
        public GetMaximumOrderQuantityForTargetValueResult Zero(string reason)
        {
            return new GetMaximumOrderQuantityForTargetValueResult(0m, reason, false);
        }
    }
}