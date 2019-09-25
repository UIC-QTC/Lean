using System;
using System.Collections.Generic;
using System.Text;

namespace CoinAPI.WebSocket.V1.DataModels
{
    public struct Trade
    {
        public string symbol_id { get; set; }
        public long sequence { get; set; }
        public DateTime time_exchange { get; set; }
        public DateTime time_coinapi { get; set; }
        public string uuid { get; set; }
        public decimal price { get; set; }
        public decimal size { get; set; }
        public string taker_side { get; set; }
    }
}
