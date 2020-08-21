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

using System;
using Newtonsoft.Json;
using QuantConnect.Brokerages;
using QuantConnect.Configuration;
using QuantConnect.Logging;

namespace QuantConnect.ToolBox.Polygon
{
    public class PolygonWebSocketClientWrapper : WebSocketClientWrapper
    {
        private const string BaseUrl = "wss://socket.polygon.io";

        private readonly string _apiKey = Config.Get("polygon-api-key");

        private readonly ISymbolMapper _symbolMapper;
        private readonly SecurityType _securityType;
        private readonly Action<string> _messageHandler;

        public PolygonWebSocketClientWrapper(ISymbolMapper symbolMapper, SecurityType securityType, Action<string> messageHandler)
        {
            _symbolMapper = symbolMapper;
            _securityType = securityType;
            _messageHandler = messageHandler;

            var url = GetWebSocketUrl(securityType);
            Initialize(url);

            Open += OnOpen;
            Closed += OnClosed;
            Message += OnMessage;
            Error += OnError;

            Connect();
        }

        public void Subscribe(Symbol symbol, bool subscribe)
        {
            var ticker = _symbolMapper.GetBrokerageSymbol(symbol);

            if (symbol.SecurityType == SecurityType.Equity || symbol.SecurityType == SecurityType.Crypto)
            {
                // trades
                Send(JsonConvert.SerializeObject(
                    new
                    {
                        action = subscribe ? "subscribe" : "unsubscribe",
                        @params = $"{GetSubscriptionPrefix(symbol.SecurityType, TickType.Trade)}.{ticker}"
                    }));
            }

            // quotes
            Send(JsonConvert.SerializeObject(
                new
                {
                    action = subscribe ? "subscribe" : "unsubscribe",
                    @params = $"{GetSubscriptionPrefix(symbol.SecurityType, TickType.Quote)}.{ticker}"
                }));
        }

        private void OnError(object sender, WebSocketError e)
        {
            Log.Error(e.Message);
        }

        private void OnMessage(object sender, WebSocketMessage e)
        {
            _messageHandler(e.Message);
        }

        private void OnClosed(object sender, WebSocketCloseData e)
        {
            Log.Trace($"PolygonDataQueueHandler.OnClosed({_securityType}): {e.Reason}");
        }

        private void OnOpen(object sender, EventArgs e)
        {
            Log.Trace($"PolygonDataQueueHandler.OnOpen({_securityType}): connection open");

            var json = JsonConvert.SerializeObject(
                new
                {
                    action = "auth",
                    @params = _apiKey
                });
            Send(json);
        }

        private string GetSubscriptionPrefix(SecurityType securityType, TickType tickType)
        {
            switch (securityType)
            {
                case SecurityType.Forex:
                    return "C";

                case SecurityType.Equity:
                    return tickType == TickType.Quote ? "Q" : "T";

                case SecurityType.Crypto:
                    return tickType == TickType.Quote ? "XQ" : "XT";

                default:
                    throw new Exception($"Unsupported security type: {securityType}");
            }
        }

        private string GetWebSocketUrl(SecurityType securityType)
        {
            switch (securityType)
            {
                case SecurityType.Equity:
                    return BaseUrl + "/stocks";

                case SecurityType.Forex:
                    return BaseUrl + "/forex";

                case SecurityType.Crypto:
                    return BaseUrl + "/crypto";

                default:
                    throw new Exception($"Unsupported security type: {securityType}");
            }
        }
    }
}
