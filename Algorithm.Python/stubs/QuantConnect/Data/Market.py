from .__Market_1 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Orders
import QuantConnect.Data.Market
import QuantConnect.Data
import QuantConnect
import datetime

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
    Falling: 'BarDirection'
    NoDelta: 'BarDirection'
    Rising: 'BarDirection'


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
