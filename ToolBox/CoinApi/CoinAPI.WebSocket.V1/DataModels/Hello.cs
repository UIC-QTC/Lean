using System;

namespace CoinAPI.WebSocket.V1.DataModels
{
    public struct Hello
    {
        public Guid apikey { get; set; }
        public bool heartbeat { get; set; }
        public string[] subscribe_data_type { get; set; }
        public string[] subscribe_filter_period_id { get; set; }
        public string[] subscribe_filter_symbol_id { get; set; }
        public string[] subscribe_filter_asset_id { get; set; }
        public string[] subscribe_filter_exchange_id { get; set; }
        public int? subscribe_update_limit_ms_quote { get; set; }
        public int? subscribe_update_limit_ms_book_snapshot { get; set; }
    }
}
