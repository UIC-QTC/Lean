from .__Market_2 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Orders
import QuantConnect.Data.Market
import QuantConnect.Data
import QuantConnect
import datetime



class FuturesChains(QuantConnect.Data.Market.DataDictionary[FuturesChain], QuantConnect.Interfaces.IExtendedDictionary[Symbol, FuturesChain], System.Collections.Generic.IDictionary[Symbol, FuturesChain], System.Collections.Generic.ICollection[KeyValuePair[Symbol, FuturesChain]], System.Collections.Generic.IEnumerable[KeyValuePair[Symbol, FuturesChain]], System.Collections.IEnumerable):
    """
    Collection of QuantConnect.Data.Market.FuturesChain keyed by canonical futures symbol

    

    FuturesChains()

    FuturesChains(time: DateTime)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, time: datetime.datetime) -> None:
        pass

    def __new__(self, *args) -> None:
        pass


    Item: indexer#


class FuturesContract(System.object):
    """
    Defines a single futures contract at a specific expiration

    

    FuturesContract(symbol: Symbol, underlyingSymbol: Symbol)
    """
    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    def __new__(self, symbol: QuantConnect.Symbol, underlyingSymbol: QuantConnect.Symbol) -> None:
        pass

    AskPrice: float

    AskSize: int

    BidPrice: float

    BidSize: int

    Expiry: datetime.datetime

    LastPrice: float

    OpenInterest: float

    Symbol: QuantConnect.Symbol

    Time: datetime.datetime

    UnderlyingSymbol: QuantConnect.Symbol

    Volume: int



class FuturesContracts(QuantConnect.Data.Market.DataDictionary[FuturesContract], QuantConnect.Interfaces.IExtendedDictionary[Symbol, FuturesContract], System.Collections.Generic.IDictionary[Symbol, FuturesContract], System.Collections.Generic.ICollection[KeyValuePair[Symbol, FuturesContract]], System.Collections.Generic.IEnumerable[KeyValuePair[Symbol, FuturesContract]], System.Collections.IEnumerable):
    """
    Collection of QuantConnect.Data.Market.FuturesContract keyed by futures symbol

    

    FuturesContracts()

    FuturesContracts(time: DateTime)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, time: datetime.datetime) -> None:
        pass

    def __new__(self, *args) -> None:
        pass


    Item: indexer#


class Greeks(System.object):
    """
    Defines the greeks

    

    Greeks()

    Greeks(delta: Decimal, gamma: Decimal, vega: Decimal, theta: Decimal, rho: Decimal, lambda: Decimal)

    Greeks(delta: Func[Decimal], gamma: Func[Decimal], vega: Func[Decimal], theta: Func[Decimal], rho: Func[Decimal], lambda: Func[Decimal])

    Greeks(deltaGamma: Func[Tuple[Decimal, Decimal]], vega: Func[Decimal], theta: Func[Decimal], rho: Func[Decimal], lambda: Func[Decimal])
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, delta: float, gamma: float, vega: float, theta: float, rho: float, lambda_: float) -> None:
        pass

    @typing.overload
    def __new__(self, delta: typing.Callable[[], float], gamma: typing.Callable[[], float], vega: typing.Callable[[], float], theta: typing.Callable[[], float], rho: typing.Callable[[], float], lambda_: typing.Callable[[], float]) -> None:
        pass

    @typing.overload
    def __new__(self, deltaGamma: typing.Callable[[], System.Tuple[float, float]], vega: typing.Callable[[], float], theta: typing.Callable[[], float], rho: typing.Callable[[], float], lambda_: typing.Callable[[], float]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Delta: float

    Gamma: float

    Lambda: float

    Rho: float

    Theta: float

    Vega: float



class IBar:
    """ Generic bar interface with Open, High, Low and Close. """
    Close: float

    High: float

    Low: float

    Open: float



class IBaseDataBar(QuantConnect.Data.IBaseData, QuantConnect.Data.Market.IBar):
    """ Represents a type that is both a bar and base data """

class Tick(QuantConnect.Data.BaseData, QuantConnect.Data.IBaseData):
    """
    Tick class is the base representation for tick data. It is grouped into a Ticks object

                which implements IDictionary and passed into an OnData event handler.

    

    Tick()

    Tick(original: Tick)

    Tick(time: DateTime, symbol: Symbol, bid: Decimal, ask: Decimal)

    Tick(time: DateTime, symbol: Symbol, last: Decimal, bid: Decimal, ask: Decimal)

    Tick(symbol: Symbol, line: str)

    Tick(symbol: Symbol, line: str, baseDate: DateTime)

    Tick(config: SubscriptionDataConfig, reader: StreamReader, date: DateTime)

    Tick(config: SubscriptionDataConfig, line: str, date: DateTime)
    """
    @typing.overload
    def Clone(self) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Clone(self, fillForward: bool) -> QuantConnect.Data.BaseData:
        pass

    def Clone(self, *args) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        pass

    @typing.overload
    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, datafeed: QuantConnect.DataFeedEndpoint) -> str:
        pass

    def GetSource(self, *args) -> str:
        pass

    def IsValid(self) -> bool:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, reader: System.IO.StreamReader, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, datafeed: QuantConnect.DataFeedEndpoint) -> QuantConnect.Data.BaseData:
        pass

    def Reader(self, *args) -> QuantConnect.Data.BaseData:
        pass

    def ToString(self) -> str:
        pass

    def Update(self, lastTrade: float, bidPrice: float, askPrice: float, volume: float, bidSize: float, askSize: float) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, original: QuantConnect.Data.Market.Tick) -> None:
        pass

    @typing.overload
    def __new__(self, time: datetime.datetime, symbol: QuantConnect.Symbol, bid: float, ask: float) -> None:
        pass

    @typing.overload
    def __new__(self, time: datetime.datetime, symbol: QuantConnect.Symbol, last: float, bid: float, ask: float) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, line: str) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, line: str, baseDate: datetime.datetime) -> None:
        pass

    @typing.overload
    def __new__(self, config: QuantConnect.Data.SubscriptionDataConfig, reader: System.IO.StreamReader, date: datetime.datetime) -> None:
        pass

    @typing.overload
    def __new__(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    LastPrice: float

    AskPrice: float
    AskSize: float
    BidPrice: float
    BidSize: float
    Exchange: str
    Quantity: float
    SaleCondition: str
    Suspicious: bool
    TickType: QuantConnect.TickType


class OpenInterest(QuantConnect.Data.Market.Tick, QuantConnect.Data.IBaseData):
    """
    Defines a data type that represents open interest for given security

    

    OpenInterest()

    OpenInterest(original: OpenInterest)

    OpenInterest(time: DateTime, symbol: Symbol, openInterest: Decimal)

    OpenInterest(config: SubscriptionDataConfig, symbol: Symbol, line: str, baseDate: DateTime)

    OpenInterest(config: SubscriptionDataConfig, line: str, date: DateTime)
    """
    @typing.overload
    def Clone(self) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Clone(self, fillForward: bool) -> QuantConnect.Data.BaseData:
        pass

    def Clone(self, *args) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        pass

    @typing.overload
    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, datafeed: QuantConnect.DataFeedEndpoint) -> str:
        pass

    def GetSource(self, *args) -> str:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, reader: System.IO.StreamReader, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, datafeed: QuantConnect.DataFeedEndpoint) -> QuantConnect.Data.BaseData:
        pass

    def Reader(self, *args) -> QuantConnect.Data.BaseData:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, original: QuantConnect.Data.Market.OpenInterest) -> None:
        pass

    @typing.overload
    def __new__(self, time: datetime.datetime, symbol: QuantConnect.Symbol, openInterest: float) -> None:
        pass

    @typing.overload
    def __new__(self, config: QuantConnect.Data.SubscriptionDataConfig, symbol: QuantConnect.Symbol, line: str, baseDate: datetime.datetime) -> None:
        pass

    @typing.overload
    def __new__(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime) -> None:
        pass

    def __new__(self, *args) -> None:
        pass
