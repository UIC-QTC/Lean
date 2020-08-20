from .__Market_4 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Orders
import QuantConnect.Data.Market
import QuantConnect.Data
import QuantConnect
import datetime



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
    Classic: 'RenkoType'
    Wicked: 'RenkoType'


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
