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

using QuantConnect.Securities;

namespace QuantConnect.Orders.Fees
{
    /// <summary>
    /// Defines the parameters to <see cref="IFeeModel.GetOrderFee"/> and provides helper methods for creating fee objects.
    /// </summary>
    /// <remarks>
    /// The helper methods provided here also provide a shim for better backwards compatibility support by acting as factory functions
    /// within a scope that we have control over the dependencies. So if in the future the dependency requirements change, we'll be able
    /// to continue to support these methods providing compile-time backwards compatibility for user fee models
    /// </remarks>
    public class OrderFeeContext
    {
        /// <summary>
        /// Gets the security
        /// </summary>
        public Security Security { get; }

        /// <summary>
        /// Gets the order
        /// </summary>
        public Order Order { get; }

        /// <summary>
        /// Gets the currency converter to be provided when constructing <see cref="CashAmount"/> objects for fees
        /// </summary>
        public ICurrencyConverter CurrencyConverter { get; }

        /// <summary>
        /// Initializes a new instance of the <see cref="OrderFeeContext"/> class
        /// </summary>
        /// <param name="security">The security</param>
        /// <param name="order">The order</param>
        /// <param name="currencyConverter">The currency convertered to be used when constructing <see cref="CashAmount"/> objects for fees</param>
        public OrderFeeContext(Security security, Order order, ICurrencyConverter currencyConverter)
        {
            Security = security;
            Order = order;
            CurrencyConverter = currencyConverter;
        }

        /// <summary>
        /// Creates a new instance of <see cref="CashAmount"/> representing the specified fee in units of the account currency
        /// </summary>
        /// <param name="fee">The orer fee in units of the account currency</param>
        /// <returns>A <see cref="CashAmount"/> representing the computed order fee</returns>
        public OrderFee CreateFeeInAccountCurrency(decimal fee)
        {
            return new OrderFee(new CashAmount(fee, CurrencyConverter.AccountCurrency, CurrencyConverter));
        }

        /// <summary>
        /// Creates a new instance of <see cref="CashAmount"/> representing the specified fee in units of the specified currency
        /// </summary>
        /// <param name="fee">The orer fee in units of the specified currency</param>
        /// <param name="currency">The currency the fee is denominated in</param>
        /// <returns>A <see cref="CashAmount"/> representing the computed order fee</returns>
        public OrderFee CreateFee(decimal fee, string currency)
        {
            return new OrderFee(new CashAmount(fee, currency, CurrencyConverter));
        }

        /// <summary>
        /// Creates a new instance of <see cref="CashAmount"/> representing zero fee
        /// </summary>
        /// <returns>A <see cref="CashAmount"/> representing zero fee</returns>
        public OrderFee CreateZeroFee()
        {
            return new OrderFee(new CashAmount(0, CurrencyConverter.AccountCurrency, CurrencyConverter));
        }
    }
}