# encoding: utf-8
# module QuantConnect.Data.Market calls itself Market
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Market
import QuantConnect.Orders
import System
import System.Collections.Generic
import System.IO
import typing

# no functions
# classes

class Bar(System.object, QuantConnect.Data.Market.IBar):
    """
    Base Bar Class: Open, High, Low, Close and Period.
    
    Bar()
    Bar(open: Decimal, high: Decimal, low: Decimal, close: Decimal)
    """
    def Clone(self) -> QuantConnect.Data.Market.Bar:
        pass

    def ToString(self) -> str:
        pass

    def Update(self, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, open: float, high: float, low: float, close: float) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Close: float

    High: float

    Low: float

    Open: float



class BarDirection(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """ enum BarDirection, values: Falling (2), NoDelta (1), Rising (0) """
    value__: int
    Falling: BarDirection
    NoDelta: BarDirection
    Rising: BarDirection


class DataDictionary(QuantConnect.ExtendedDictionary[T], QuantConnect.Interfaces.IExtendedDictionary[Symbol, T], System.Collections.Generic.IDictionary[Symbol, T], System.Collections.Generic.ICollection[KeyValuePair[Symbol, T]], System.Collections.Generic.IEnumerable[KeyValuePair[Symbol, T]], System.Collections.IEnumerable):
    """
    DataDictionary[T]()
    DataDictionary[T](data: IEnumerable[T], keySelector: Func[T, Symbol])
    DataDictionary[T](time: DateTime)
    """
    @typing.overload
    def Add(self, item: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Data.Market.T]) -> None:
        pass

    @typing.overload
    def Add(self, key: QuantConnect.Symbol, value: QuantConnect.Data.Market.T) -> None:
        pass

    def Add(self, *args) -> None:
        pass

    def Clear(self) -> None:
        pass

    def Contains(self, item: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Data.Market.T]) -> bool:
        pass

    def ContainsKey(self, key: QuantConnect.Symbol) -> bool:
        pass

    def CopyTo(self, array: typing.List[System.Collections.Generic.KeyValuePair], arrayIndex: int) -> None:
        pass

    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Data.Market.T]]:
        pass

    def GetValue(self, key: QuantConnect.Symbol) -> QuantConnect.Data.Market.T:
        pass

    @typing.overload
    def Remove(self, item: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Data.Market.T]) -> bool:
        pass

    @typing.overload
    def Remove(self, key: QuantConnect.Symbol) -> bool:
        pass

    def Remove(self, *args) -> bool:
        pass

    def TryGetValue(self, key: QuantConnect.Symbol, value: QuantConnect.Data.Market.T) -> bool:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, data: typing.List[QuantConnect.Data.Market.T], keySelector: typing.Callable[[QuantConnect.Data.Market.T], QuantConnect.Symbol]) -> None:
        pass

    @typing.overload
    def __new__(self, time: datetime.datetime) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Count: int

    IsReadOnly: bool

    Keys: typing.List[QuantConnect.Symbol]

    Time: datetime.datetime

    Values: typing.List[QuantConnect.Data.Market.T]


    Item: indexer#


class DataDictionaryExtensions(System.object):
    """ Provides extension methods for the DataDictionary class """
    @staticmethod
    def Add(dictionary: QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.T], data: QuantConnect.Data.Market.T) -> None:
        pass

    __all__: list


class Delisting(QuantConnect.Data.BaseData, QuantConnect.Data.IBaseData):
    """
    Delisting event of a security
    
    Delisting()
    Delisting(symbol: Symbol, date: DateTime, price: Decimal, type: DelistingType)
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
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, stream: System.IO.StreamReader, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, datafeed: QuantConnect.DataFeedEndpoint) -> QuantConnect.Data.BaseData:
        pass

    def Reader(self, *args) -> QuantConnect.Data.BaseData:
        pass

    def SetOrderTicket(self, ticket: QuantConnect.Orders.OrderTicket) -> None:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, date: datetime.datetime, price: float, type: QuantConnect.DelistingType) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Ticket: QuantConnect.Orders.OrderTicket

    Type: QuantConnect.DelistingType



class Delistings(QuantConnect.Data.Market.DataDictionary[Delisting], QuantConnect.Interfaces.IExtendedDictionary[Symbol, Delisting], System.Collections.Generic.IDictionary[Symbol, Delisting], System.Collections.Generic.ICollection[KeyValuePair[Symbol, Delisting]], System.Collections.Generic.IEnumerable[KeyValuePair[Symbol, Delisting]], System.Collections.IEnumerable):
    """
    Collections of QuantConnect.Data.Market.Delisting keyed by QuantConnect.Symbol
    
    Delistings()
    Delistings(frontier: DateTime)
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


class Dividend(QuantConnect.Data.BaseData, QuantConnect.Data.IBaseData):
    """
    Dividend event from a security
    
    Dividend()
    Dividend(symbol: Symbol, date: DateTime, distribution: Decimal, referencePrice: Decimal)
    """
    @typing.overload
    def Clone(self) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Clone(self, fillForward: bool) -> QuantConnect.Data.BaseData:
        pass

    def Clone(self, *args) -> QuantConnect.Data.BaseData:
        pass

    @staticmethod
    def ComputeDistribution(close: float, priceFactorRatio: float, decimalPlaces: int) -> float:
        pass

    @staticmethod
    def Create(symbol: QuantConnect.Symbol, date: datetime.datetime, referencePrice: float, priceFactorRatio: float) -> QuantConnect.Data.Market.Dividend:
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
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, stream: System.IO.StreamReader, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, datafeed: QuantConnect.DataFeedEndpoint) -> QuantConnect.Data.BaseData:
        pass

    def Reader(self, *args) -> QuantConnect.Data.BaseData:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, date: datetime.datetime, distribution: float, referencePrice: float) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Distribution: float

    ReferencePrice: float



class Dividends(QuantConnect.Data.Market.DataDictionary[Dividend], QuantConnect.Interfaces.IExtendedDictionary[Symbol, Dividend], System.Collections.Generic.IDictionary[Symbol, Dividend], System.Collections.Generic.ICollection[KeyValuePair[Symbol, Dividend]], System.Collections.Generic.IEnumerable[KeyValuePair[Symbol, Dividend]], System.Collections.IEnumerable):
    """
    Collection of dividends keyed by QuantConnect.Symbol
    
    Dividends()
    Dividends(frontier: DateTime)
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


class FuturesChain(QuantConnect.Data.BaseData, QuantConnect.Data.IBaseData, System.Collections.Generic.IEnumerable[FuturesContract], System.Collections.IEnumerable):
    """
    Represents an entire chain of futures contracts for a single underlying
                This type is System.Collections.Generic.IEnumerable
    
    FuturesChain(canonicalFutureSymbol: Symbol, time: DateTime)
    FuturesChain(canonicalFutureSymbol: Symbol, time: DateTime, trades: IEnumerable[BaseData], quotes: IEnumerable[BaseData], contracts: IEnumerable[FuturesContract], filteredContracts: IEnumerable[Symbol])
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
    def GetAux(self, symbol: QuantConnect.Symbol) -> QuantConnect.Data.Market.T:
        pass

    @typing.overload
    def GetAux(self) -> QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.T]:
        pass

    def GetAux(self, *args) -> QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.T]:
        pass

    @typing.overload
    def GetAuxList(self) -> System.Collections.Generic.Dictionary[QuantConnect.Symbol, typing.List[QuantConnect.Data.BaseData]]:
        pass

    @typing.overload
    def GetAuxList(self, symbol: QuantConnect.Symbol) -> typing.List[QuantConnect.Data.Market.T]:
        pass

    def GetAuxList(self, *args) -> typing.List[QuantConnect.Data.Market.T]:
        pass

    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.Market.FuturesContract]:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, canonicalFutureSymbol: QuantConnect.Symbol, time: datetime.datetime) -> None:
        pass

    @typing.overload
    def __new__(self, canonicalFutureSymbol: QuantConnect.Symbol, time: datetime.datetime, trades: typing.List[QuantConnect.Data.BaseData], quotes: typing.List[QuantConnect.Data.BaseData], contracts: typing.List[QuantConnect.Data.Market.FuturesContract], filteredContracts: typing.List[QuantConnect.Symbol]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Contracts: QuantConnect.Data.Market.FuturesContracts

    FilteredContracts: System.Collections.Generic.HashSet[QuantConnect.Symbol]

    QuoteBars: QuantConnect.Data.Market.QuoteBars

    Ticks: QuantConnect.Data.Market.Ticks

    TradeBars: QuantConnect.Data.Market.TradeBars

    Underlying: QuantConnect.Data.BaseData



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


class OptionChain(QuantConnect.Data.BaseData, QuantConnect.Data.IBaseData, System.Collections.Generic.IEnumerable[OptionContract], System.Collections.IEnumerable):
    """
    Represents an entire chain of option contracts for a single underying security.
                This type is System.Collections.Generic.IEnumerable
    
    OptionChain(canonicalOptionSymbol: Symbol, time: DateTime)
    OptionChain(canonicalOptionSymbol: Symbol, time: DateTime, underlying: BaseData, trades: IEnumerable[BaseData], quotes: IEnumerable[BaseData], contracts: IEnumerable[OptionContract], filteredContracts: IEnumerable[Symbol])
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
    def GetAux(self, symbol: QuantConnect.Symbol) -> QuantConnect.Data.Market.T:
        pass

    @typing.overload
    def GetAux(self) -> QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.T]:
        pass

    def GetAux(self, *args) -> QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.T]:
        pass

    @typing.overload
    def GetAuxList(self) -> System.Collections.Generic.Dictionary[QuantConnect.Symbol, typing.List[QuantConnect.Data.BaseData]]:
        pass

    @typing.overload
    def GetAuxList(self, symbol: QuantConnect.Symbol) -> typing.List[QuantConnect.Data.Market.T]:
        pass

    def GetAuxList(self, *args) -> typing.List[QuantConnect.Data.Market.T]:
        pass

    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.Market.OptionContract]:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, canonicalOptionSymbol: QuantConnect.Symbol, time: datetime.datetime) -> None:
        pass

    @typing.overload
    def __new__(self, canonicalOptionSymbol: QuantConnect.Symbol, time: datetime.datetime, underlying: QuantConnect.Data.BaseData, trades: typing.List[QuantConnect.Data.BaseData], quotes: typing.List[QuantConnect.Data.BaseData], contracts: typing.List[QuantConnect.Data.Market.OptionContract], filteredContracts: typing.List[QuantConnect.Symbol]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Contracts: QuantConnect.Data.Market.OptionContracts

    FilteredContracts: System.Collections.Generic.HashSet[QuantConnect.Symbol]

    QuoteBars: QuantConnect.Data.Market.QuoteBars

    Ticks: QuantConnect.Data.Market.Ticks

    TradeBars: QuantConnect.Data.Market.TradeBars

    Underlying: QuantConnect.Data.BaseData



class OptionChains(QuantConnect.Data.Market.DataDictionary[OptionChain], QuantConnect.Interfaces.IExtendedDictionary[Symbol, OptionChain], System.Collections.Generic.IDictionary[Symbol, OptionChain], System.Collections.Generic.ICollection[KeyValuePair[Symbol, OptionChain]], System.Collections.Generic.IEnumerable[KeyValuePair[Symbol, OptionChain]], System.Collections.IEnumerable):
    """
    Collection of QuantConnect.Data.Market.OptionChain keyed by canonical option symbol
    
    OptionChains()
    OptionChains(time: DateTime)
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


class OptionContract(System.object):
    """
    Defines a single option contract at a specific expiration and strike price
    
    OptionContract(symbol: Symbol, underlyingSymbol: Symbol)
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

    Greeks: QuantConnect.Data.Market.Greeks

    ImpliedVolatility: float

    LastPrice: float

    OpenInterest: float

    Right: QuantConnect.OptionRight

    Strike: float

    Style: QuantConnect.OptionStyle

    Symbol: QuantConnect.Symbol

    TheoreticalPrice: float

    Time: datetime.datetime

    UnderlyingLastPrice: float

    UnderlyingSymbol: QuantConnect.Symbol

    Volume: int



class OptionContracts(QuantConnect.Data.Market.DataDictionary[OptionContract], QuantConnect.Interfaces.IExtendedDictionary[Symbol, OptionContract], System.Collections.Generic.IDictionary[Symbol, OptionContract], System.Collections.Generic.ICollection[KeyValuePair[Symbol, OptionContract]], System.Collections.Generic.IEnumerable[KeyValuePair[Symbol, OptionContract]], System.Collections.IEnumerable):
    """
    Collection of QuantConnect.Data.Market.OptionContract keyed by option symbol
    
    OptionContracts()
    OptionContracts(time: DateTime)
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


class QuoteBar(QuantConnect.Data.BaseData, QuantConnect.Data.IBaseData, QuantConnect.Data.Market.IBaseDataBar, QuantConnect.Data.Market.IBar):
    """
    QuoteBar class for second and minute resolution data:
                An OHLC implementation of the QuantConnect BaseData class with parameters for candles.
    
    QuoteBar()
    QuoteBar(time: DateTime, symbol: Symbol, bid: IBar, lastBidSize: Decimal, ask: IBar, lastAskSize: Decimal, period: Nullable[TimeSpan])
    """
    @typing.overload
    def Clone(self) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Clone(self, fillForward: bool) -> QuantConnect.Data.BaseData:
        pass

    def Clone(self, *args) -> QuantConnect.Data.BaseData:
        pass

    def Collapse(self) -> QuantConnect.Data.Market.TradeBar:
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
    def ParseCfd(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime) -> QuantConnect.Data.Market.QuoteBar:
        pass

    @typing.overload
    def ParseCfd(self, config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: datetime.datetime) -> QuantConnect.Data.Market.QuoteBar:
        pass

    def ParseCfd(self, *args) -> QuantConnect.Data.Market.QuoteBar:
        pass

    @typing.overload
    def ParseEquity(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime) -> QuantConnect.Data.Market.QuoteBar:
        pass

    @typing.overload
    def ParseEquity(self, config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: datetime.datetime) -> QuantConnect.Data.Market.QuoteBar:
        pass

    def ParseEquity(self, *args) -> QuantConnect.Data.Market.QuoteBar:
        pass

    @typing.overload
    def ParseForex(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime) -> QuantConnect.Data.Market.QuoteBar:
        pass

    @typing.overload
    def ParseForex(self, config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: datetime.datetime) -> QuantConnect.Data.Market.QuoteBar:
        pass

    def ParseForex(self, *args) -> QuantConnect.Data.Market.QuoteBar:
        pass

    @typing.overload
    def ParseFuture(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime) -> QuantConnect.Data.Market.QuoteBar:
        pass

    @typing.overload
    def ParseFuture(self, config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: datetime.datetime) -> QuantConnect.Data.Market.QuoteBar:
        pass

    def ParseFuture(self, *args) -> QuantConnect.Data.Market.QuoteBar:
        pass

    @typing.overload
    def ParseOption(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime) -> QuantConnect.Data.Market.QuoteBar:
        pass

    @typing.overload
    def ParseOption(self, config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: datetime.datetime) -> QuantConnect.Data.Market.QuoteBar:
        pass

    def ParseOption(self, *args) -> QuantConnect.Data.Market.QuoteBar:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, stream: System.IO.StreamReader, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.BaseData:
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
    def __new__(self, time: datetime.datetime, symbol: QuantConnect.Symbol, bid: QuantConnect.Data.Market.IBar, lastBidSize: float, ask: QuantConnect.Data.Market.IBar, lastAskSize: float, period: typing.Optional[datetime.timedelta]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Ask: QuantConnect.Data.Market.Bar

    Bid: QuantConnect.Data.Market.Bar

    Close: float

    EndTime: datetime.datetime

    High: float

    LastAskSize: float

    LastBidSize: float

    Low: float

    Open: float

    Period: datetime.timedelta



class QuoteBars(QuantConnect.Data.Market.DataDictionary[QuoteBar], QuantConnect.Interfaces.IExtendedDictionary[Symbol, QuoteBar], System.Collections.Generic.IDictionary[Symbol, QuoteBar], System.Collections.Generic.ICollection[KeyValuePair[Symbol, QuoteBar]], System.Collections.Generic.IEnumerable[KeyValuePair[Symbol, QuoteBar]], System.Collections.IEnumerable):
    """
    Collection of QuantConnect.Data.Market.QuoteBar keyed by symbol
    
    QuoteBars()
    QuoteBars(time: DateTime)
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


class RenkoBar(QuantConnect.Data.BaseData, QuantConnect.Data.IBaseData, QuantConnect.Data.Market.IBaseDataBar, QuantConnect.Data.Market.IBar):
    """
    Represents a bar sectioned not by time, but by some amount of movement in a value (for example, Closing price moving in $10 bar sizes)
    
    RenkoBar()
    RenkoBar(symbol: Symbol, time: DateTime, brickSize: Decimal, open: Decimal, volume: Decimal)
    RenkoBar(symbol: Symbol, start: DateTime, endTime: DateTime, brickSize: Decimal, open: Decimal, high: Decimal, low: Decimal, close: Decimal)
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
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, stream: System.IO.StreamReader, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, datafeed: QuantConnect.DataFeedEndpoint) -> QuantConnect.Data.BaseData:
        pass

    def Reader(self, *args) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Update(self, time: datetime.datetime, currentValue: float, volumeSinceLastUpdate: float) -> bool:
        pass

    @typing.overload
    def Update(self, lastTrade: float, bidPrice: float, askPrice: float, volume: float, bidSize: float, askSize: float) -> None:
        pass

    def Update(self, *args) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, time: datetime.datetime, brickSize: float, open: float, volume: float) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, start: datetime.datetime, endTime: datetime.datetime, brickSize: float, open: float, high: float, low: float, close: float) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    BrickSize: float

    Close: float

    Direction: QuantConnect.Data.Market.BarDirection

    End: datetime.datetime

    EndTime: datetime.datetime

    High: float

    IsClosed: bool

    Low: float

    Open: float

    Spread: float

    Start: datetime.datetime

    Type: QuantConnect.Data.Market.RenkoType

    Volume: float



class RenkoType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    The type of the RenkoBar
    
    enum RenkoType, values: Classic (0), Wicked (1)
    """
    value__: int
    Classic: RenkoType
    Wicked: RenkoType


class Split(QuantConnect.Data.BaseData, QuantConnect.Data.IBaseData):
    """
    Split event from a security
    
    Split()
    Split(symbol: Symbol, date: DateTime, price: Decimal, splitFactor: Decimal, type: SplitType)
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
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, stream: System.IO.StreamReader, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, datafeed: QuantConnect.DataFeedEndpoint) -> QuantConnect.Data.BaseData:
        pass

    def Reader(self, *args) -> QuantConnect.Data.BaseData:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, date: datetime.datetime, price: float, splitFactor: float, type: QuantConnect.SplitType) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    ReferencePrice: float

    SplitFactor: float

    Type: QuantConnect.SplitType



class Splits(QuantConnect.Data.Market.DataDictionary[Split], QuantConnect.Interfaces.IExtendedDictionary[Symbol, Split], System.Collections.Generic.IDictionary[Symbol, Split], System.Collections.Generic.ICollection[KeyValuePair[Symbol, Split]], System.Collections.Generic.IEnumerable[KeyValuePair[Symbol, Split]], System.Collections.IEnumerable):
    """
    Collection of splits keyed by QuantConnect.Symbol
    
    Splits()
    Splits(frontier: DateTime)
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


class SymbolChangedEvent(QuantConnect.Data.BaseData, QuantConnect.Data.IBaseData):
    """
    Symbol changed event of a security. This is generated when a symbol is remapped for a given
                security, for example, at EOD 2014.04.02 GOOG turned into GOOGL, but are the same
    
    SymbolChangedEvent()
    SymbolChangedEvent(requestedSymbol: Symbol, date: DateTime, oldSymbol: str, newSymbol: str)
    """
    @typing.overload
    def Clone(self) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Clone(self, fillForward: bool) -> QuantConnect.Data.BaseData:
        pass

    def Clone(self, *args) -> QuantConnect.Data.BaseData:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, requestedSymbol: QuantConnect.Symbol, date: datetime.datetime, oldSymbol: str, newSymbol: str) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    NewSymbol: str

    OldSymbol: str



class SymbolChangedEvents(QuantConnect.Data.Market.DataDictionary[SymbolChangedEvent], QuantConnect.Interfaces.IExtendedDictionary[Symbol, SymbolChangedEvent], System.Collections.Generic.IDictionary[Symbol, SymbolChangedEvent], System.Collections.Generic.ICollection[KeyValuePair[Symbol, SymbolChangedEvent]], System.Collections.Generic.IEnumerable[KeyValuePair[Symbol, SymbolChangedEvent]], System.Collections.IEnumerable):
    """
    Collection of QuantConnect.Data.Market.SymbolChangedEvent keyed by the original, requested symbol
    
    SymbolChangedEvents()
    SymbolChangedEvents(frontier: DateTime)
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


class Ticks(QuantConnect.Data.Market.DataDictionary[List[Tick]], QuantConnect.Interfaces.IExtendedDictionary[Symbol, List[Tick]], System.Collections.Generic.IDictionary[Symbol, List[Tick]], System.Collections.Generic.ICollection[KeyValuePair[Symbol, List[Tick]]], System.Collections.Generic.IEnumerable[KeyValuePair[Symbol, List[Tick]]], System.Collections.IEnumerable):
    """
    Ticks collection which implements an IDictionary-string-list of ticks. This way users can iterate over the string indexed ticks of the requested symbol.
    
    Ticks()
    Ticks(frontier: DateTime)
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


class TradeBar(QuantConnect.Data.BaseData, QuantConnect.Data.IBaseData, QuantConnect.Data.Market.IBaseDataBar, QuantConnect.Data.Market.IBar):
    """
    TradeBar class for second and minute resolution data:
                An OHLC implementation of the QuantConnect BaseData class with parameters for candles.
    
    TradeBar()
    TradeBar(original: TradeBar)
    TradeBar(time: DateTime, symbol: Symbol, open: Decimal, high: Decimal, low: Decimal, close: Decimal, volume: Decimal, period: Nullable[TimeSpan])
    """
    @typing.overload
    def Clone(self, fillForward: bool) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Clone(self) -> QuantConnect.Data.BaseData:
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

    @staticmethod
    def Parse(config: QuantConnect.Data.SubscriptionDataConfig, line: str, baseDate: datetime.datetime) -> QuantConnect.Data.Market.TradeBar:
        pass

    @staticmethod
    @typing.overload
    def ParseCfd(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime) -> QuantConnect.Data.Market.T:
        pass

    @staticmethod
    @typing.overload
    def ParseCfd(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime) -> QuantConnect.Data.Market.TradeBar:
        pass

    @staticmethod
    @typing.overload
    def ParseCfd(config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: datetime.datetime) -> QuantConnect.Data.Market.TradeBar:
        pass

    def ParseCfd(self, *args) -> QuantConnect.Data.Market.TradeBar:
        pass

    @staticmethod
    @typing.overload
    def ParseCrypto(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime) -> QuantConnect.Data.Market.T:
        pass

    @staticmethod
    @typing.overload
    def ParseCrypto(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime) -> QuantConnect.Data.Market.TradeBar:
        pass

    @staticmethod
    @typing.overload
    def ParseCrypto(config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: datetime.datetime) -> QuantConnect.Data.Market.TradeBar:
        pass

    def ParseCrypto(self, *args) -> QuantConnect.Data.Market.TradeBar:
        pass

    @staticmethod
    @typing.overload
    def ParseEquity(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime) -> QuantConnect.Data.Market.T:
        pass

    @staticmethod
    @typing.overload
    def ParseEquity(config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: datetime.datetime) -> QuantConnect.Data.Market.TradeBar:
        pass

    @staticmethod
    @typing.overload
    def ParseEquity(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime) -> QuantConnect.Data.Market.TradeBar:
        pass

    def ParseEquity(self, *args) -> QuantConnect.Data.Market.TradeBar:
        pass

    @staticmethod
    @typing.overload
    def ParseForex(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime) -> QuantConnect.Data.Market.T:
        pass

    @staticmethod
    @typing.overload
    def ParseForex(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime) -> QuantConnect.Data.Market.TradeBar:
        pass

    @staticmethod
    @typing.overload
    def ParseForex(config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: datetime.datetime) -> QuantConnect.Data.Market.TradeBar:
        pass

    def ParseForex(self, *args) -> QuantConnect.Data.Market.TradeBar:
        pass

    @staticmethod
    @typing.overload
    def ParseFuture(config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: datetime.datetime) -> QuantConnect.Data.Market.T:
        pass

    @staticmethod
    @typing.overload
    def ParseFuture(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime) -> QuantConnect.Data.Market.T:
        pass

    @staticmethod
    @typing.overload
    def ParseFuture(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime) -> QuantConnect.Data.Market.TradeBar:
        pass

    @staticmethod
    @typing.overload
    def ParseFuture(config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: datetime.datetime) -> QuantConnect.Data.Market.TradeBar:
        pass

    def ParseFuture(self, *args) -> QuantConnect.Data.Market.TradeBar:
        pass

    @staticmethod
    @typing.overload
    def ParseOption(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime) -> QuantConnect.Data.Market.T:
        pass

    @staticmethod
    @typing.overload
    def ParseOption(config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: datetime.datetime) -> QuantConnect.Data.Market.T:
        pass

    @staticmethod
    @typing.overload
    def ParseOption(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime) -> QuantConnect.Data.Market.TradeBar:
        pass

    @staticmethod
    @typing.overload
    def ParseOption(config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: datetime.datetime) -> QuantConnect.Data.Market.TradeBar:
        pass

    def ParseOption(self, *args) -> QuantConnect.Data.Market.TradeBar:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, stream: System.IO.StreamReader, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.BaseData:
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
    def __new__(self, original: QuantConnect.Data.Market.TradeBar) -> None:
        pass

    @typing.overload
    def __new__(self, time: datetime.datetime, symbol: QuantConnect.Symbol, open: float, high: float, low: float, close: float, volume: float, period: typing.Optional[datetime.timedelta]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Close: float

    EndTime: datetime.datetime

    High: float

    Low: float

    Open: float

    Period: datetime.timedelta

    Volume: float



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


