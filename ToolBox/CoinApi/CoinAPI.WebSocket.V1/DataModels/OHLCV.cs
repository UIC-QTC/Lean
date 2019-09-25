using System;

namespace CoinAPI.WebSocket.V1.DataModels
{
    public struct OHLCV
    {
        public string symbol_id { get; set; }
        public long sequence { get; set; }
        public string period_id { get; set; }
        public DateTime time_period_start { get; set; }
        public DateTime time_period_end { get; set; }
        public DateTime? time_open { get; set; }
        public DateTime? time_close { get; set; }
        public decimal? price_open { get; set; }
        public decimal? price_high { get; set; }
        public decimal? price_low { get; set; }
        public decimal? price_close { get; set; }
        public decimal volume_traded { get; set; }
        public long trades_count { get; set; }
    }
}
