from .__Market_3 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Orders
import QuantConnect.Data.Market
import QuantConnect.Data
import QuantConnect
import datetime


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
