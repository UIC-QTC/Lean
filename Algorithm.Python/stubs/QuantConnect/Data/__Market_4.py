import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Orders
import QuantConnect.Data.Market
import QuantConnect.Data
import QuantConnect
import datetime



class TradeBars(QuantConnect.Data.Market.DataDictionary[TradeBar], QuantConnect.Interfaces.IExtendedDictionary[Symbol, TradeBar], System.Collections.Generic.IDictionary[Symbol, TradeBar], System.Collections.Generic.ICollection[KeyValuePair[Symbol, TradeBar]], System.Collections.Generic.IEnumerable[KeyValuePair[Symbol, TradeBar]], System.Collections.IEnumerable):
    """
    Collection of TradeBars to create a data type for generic data handler:

    

    TradeBars()

    TradeBars(frontier: DateTime)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, frontier: datetime.datetime) -> None:
        pass

    def __new__(self, *args) -> None:
        pass


    Item: indexer#
