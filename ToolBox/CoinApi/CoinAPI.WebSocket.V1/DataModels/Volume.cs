using System;

namespace CoinAPI.WebSocket.V1.DataModels
{
    public struct Volume
    {
        public DateTime time_coinapi { get; set; }
        public string period_id { get; set; }
        public SymbolVolume[] volume_by_symbol { get; set; }
    }
    public struct SymbolVolume
    {
        public string symbol_id { get; set; }
        public string asset_id_base { get; set; }
        public string asset_id_quote { get; set; }
        public decimal volume_base { get; set; }
        public decimal volume_quote { get; set; }
    }
}
