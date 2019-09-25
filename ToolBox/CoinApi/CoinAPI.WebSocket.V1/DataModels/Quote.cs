using System;

namespace CoinAPI.WebSocket.V1.DataModels
{
    public struct Quote
    {
        public string symbol_id { get; set; }
        public long sequence { get; set; }
        public DateTime time_exchange { get; set; }
        public DateTime time_coinapi { get; set; }
        public decimal ask_price { get; set; }
        public decimal ask_size { get; set; }
        public decimal bid_size { get; set; }
        public decimal bid_price { get; set; }
    }
}
