using QuantConnect.Util;
using System;
using System.Collections.Concurrent;
using System.IO;
using System.Linq;
using System.Threading;

namespace QuantConnect
{
    internal class SidFigiMapper
    {
        private Lazy<ConcurrentDictionary<SecurityIdentifier, string>> _sidFigiMap = new Lazy<ConcurrentDictionary<SecurityIdentifier, string>>(Initialize, LazyThreadSafetyMode.ExecutionAndPublication);
        public bool MapLoaded => _sidFigiMap.IsValueCreated;

        private static ConcurrentDictionary<SecurityIdentifier, string> Initialize()
        {
            var sidFigiMapFile = new FileInfo(Path.Combine(Globals.DataFolder, SecurityType.Equity.SecurityTypeToLower(),
                Market.USA.ToLowerInvariant(), "map_files", "symbol_figi_map.csv"));

            if (sidFigiMapFile.Exists)
            {
                var map = File.ReadAllLines(sidFigiMapFile.FullName)
                    .Select(r => r.Split(','))
                    .ToDictionary(sf => SecurityIdentifier.Parse(sf[0]), sf => sf[1]);
                return new ConcurrentDictionary<SecurityIdentifier, string>(map);
            }

            return null;
        }

        public string LookUpFigi(SecurityIdentifier sid)
        {
            if (sid.SecurityType == SecurityType.Equity && !_sidFigiMap.Value.IsNullOrEmpty())
            {
                string figi;
                if (_sidFigiMap.Value.TryGetValue(sid, out figi))
                {
                    return figi;
                }
            }

            return string.Empty;
        }
    }
}