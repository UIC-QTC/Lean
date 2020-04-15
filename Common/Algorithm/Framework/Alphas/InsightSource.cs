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

using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;

namespace QuantConnect.Algorithm.Framework.Alphas
{
    /// <summary>
    /// Insight prediction source, in sample, out of sample, live trading.
    /// </summary>
    [JsonConverter(typeof(StringEnumConverter), true)]
    public enum InsightSource
    {
        /// <summary>
        /// Insights generated from backtesting across historical data.
        /// </summary>
        [EnumMember(Value = "in sample")] InSample,

        /// <summary>
        /// Insights from running a backtest on out of sample data.
        /// </summary>
        [EnumMember(Value = "out of sample")] OutOfSample,

        /// <summary>
        /// Insights from forward trading environment recorded at the moment they were generated
        /// </summary>
        [EnumMember(Value = "live trading")] LiveTrading
    }
}