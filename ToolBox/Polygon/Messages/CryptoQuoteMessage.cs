﻿/*
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

using Newtonsoft.Json;

namespace QuantConnect.ToolBox.Polygon.Messages
{
    public class CryptoQuoteMessage : BaseMessage
    {
        [JsonProperty("pair")]
        public string Symbol { get; set; }

        [JsonProperty("lp")]
        public decimal LastTradePrice { get; set; }

        [JsonProperty("ls")]
        public decimal LastTradeSize { get; set; }

        [JsonProperty("bp")]
        public decimal BidPrice { get; set; }

        [JsonProperty("bs")]
        public decimal BidSize { get; set; }

        [JsonProperty("ap")]
        public decimal AskPrice { get; set; }

        [JsonProperty("as")]
        public decimal AskSize { get; set; }

        [JsonProperty("t")]
        public long ExchangeTimestamp { get; set; }

        [JsonProperty("x")]
        public int ExchangeId { get; set; }

        [JsonProperty("r")]
        public long ReceivedTimestamp { get; set; }
    }
}
