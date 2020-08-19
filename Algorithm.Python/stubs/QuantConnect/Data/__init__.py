# encoding: utf-8
# module QuantConnect.Data calls itself Data
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import NodaTime
import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Consolidators
import QuantConnect.Data.Market
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Packets
import QuantConnect.Securities
import System
import System.Collections.Generic
import System.Dynamic
import System.IO
import System.Linq.Expressions
import System.Reflection
import typing

# no functions
# classes

class BaseData(System.object, QuantConnect.Data.IBaseData):
    """
    Abstract base data class of QuantConnect. It is intended to be extended to define
                generic user customizable data types while at the same time implementing the basics of data where possible
    
    BaseData()
    """
    @typing.overload
    def Clone(self) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Clone(self, fillForward: bool) -> QuantConnect.Data.BaseData:
        pass

    def Clone(self, *args) -> QuantConnect.Data.BaseData:
        pass

    def DataTimeZone(self) -> NodaTime.DateTimeZone:
        pass

    def DefaultResolution(self) -> QuantConnect.Resolution:
        pass

    @staticmethod
    def DeserializeMessage(serialized: str) -> typing.List[QuantConnect.Data.BaseData]:
        pass

    @typing.overload
    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        pass

    @typing.overload
    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, datafeed: QuantConnect.DataFeedEndpoint) -> str:
        pass

    def GetSource(self, *args) -> str:
        pass

    def IsSparseData(self) -> bool:
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

    def RequiresMapping(self) -> bool:
        pass

    def SupportedResolutions(self) -> typing.List[QuantConnect.Resolution]:
        pass

    def ToString(self) -> str:
        pass

    def Update(self, lastTrade: float, bidPrice: float, askPrice: float, volume: float, bidSize: float, askSize: float) -> None:
        pass

    def UpdateAsk(self, askPrice: float, askSize: float) -> None:
        pass

    def UpdateBid(self, bidPrice: float, bidSize: float) -> None:
        pass

    def UpdateQuote(self, bidPrice: float, bidSize: float, askPrice: float, askSize: float) -> None:
        pass

    def UpdateTrade(self, lastTrade: float, tradeSize: float) -> None:
        pass

    DataType: QuantConnect.MarketDataType

    EndTime: datetime.datetime

    IsFillForward: bool

    Price: float

    Symbol: QuantConnect.Symbol

    Time: datetime.datetime

    Value: float


    AllResolutions: List[Resolution]
    DailyResolution: List[Resolution]
    MinuteResolution: List[Resolution]


class DynamicData(QuantConnect.Data.BaseData, QuantConnect.Data.IBaseData, System.Dynamic.IDynamicMetaObjectProvider):
    """ Dynamic Data Class: Accept flexible data, adapting to the columns provided by source. """
    @typing.overload
    def Clone(self) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Clone(self, fillForward: bool) -> QuantConnect.Data.BaseData:
        pass

    def Clone(self, *args) -> QuantConnect.Data.BaseData:
        pass

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression) -> System.Dynamic.DynamicMetaObject:
        pass

    def GetProperty(self, name: str) -> object:
        pass

    def GetStorageDictionary(self) -> System.Collections.Generic.IDictionary[str, object]:
        pass

    def HasProperty(self, name: str) -> bool:
        pass

    def SetProperty(self, name: str, value: object) -> object:
        pass


class FileFormat(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Specifies the format of data in a subscription
    
    enum FileFormat, values: Binary (1), Collection (3), Csv (0), Index (4), ZipEntryName (2)
    """
    value__: int
    Binary: FileFormat
    Collection: FileFormat
    Csv: FileFormat
    Index: FileFormat
    ZipEntryName: FileFormat


class GetSetPropertyDynamicMetaObject(System.Dynamic.DynamicMetaObject):
    """
    Provides an implementation of System.Dynamic.DynamicMetaObject that uses get/set methods to update
                values in the dynamic object.
    
    GetSetPropertyDynamicMetaObject(expression: Expression, value: object, setPropertyMethodInfo: MethodInfo, getPropertyMethodInfo: MethodInfo)
    """
    def BindGetMember(self, binder: System.Dynamic.GetMemberBinder) -> System.Dynamic.DynamicMetaObject:
        pass

    def BindSetMember(self, binder: System.Dynamic.SetMemberBinder, value: System.Dynamic.DynamicMetaObject) -> System.Dynamic.DynamicMetaObject:
        pass

    @staticmethod # known case of __new__
    def __new__(self, expression: System.Linq.Expressions.Expression, value: object, setPropertyMethodInfo: System.Reflection.MethodInfo, getPropertyMethodInfo: System.Reflection.MethodInfo) -> None:
        pass


class HistoryProviderBase(System.object, QuantConnect.Interfaces.IHistoryProvider, QuantConnect.Interfaces.IDataProviderEvents):
    """ Provides a base type for all history providers """
    def GetHistory(self, requests: typing.List[QuantConnect.Data.HistoryRequest], sliceTimeZone: NodaTime.DateTimeZone) -> typing.List[QuantConnect.Data.Slice]:
        pass

    def Initialize(self, parameters: QuantConnect.Data.HistoryProviderInitializeParameters) -> None:
        pass

    DataPointCount: int


    DownloadFailed: BoundEvent
    InvalidConfigurationDetected: BoundEvent
    NumericalPrecisionLimited: BoundEvent
    ReaderErrorDetected: BoundEvent
    StartDateLimited: BoundEvent


class HistoryProviderInitializeParameters(System.object):
    """
    Represents the set of parameters for the QuantConnect.Interfaces.IHistoryProvider.Initialize(QuantConnect.Data.HistoryProviderInitializeParameters) method
    
    HistoryProviderInitializeParameters(job: AlgorithmNodePacket, api: IApi, dataProvider: IDataProvider, dataCacheProvider: IDataCacheProvider, mapFileProvider: IMapFileProvider, factorFileProvider: IFactorFileProvider, statusUpdateAction: Action[int], parallelHistoryRequestsEnabled: bool, dataPermissionManager: IDataPermissionManager)
    """
    @staticmethod # known case of __new__
    def __new__(self, job: QuantConnect.Packets.AlgorithmNodePacket, api: QuantConnect.Interfaces.IApi, dataProvider: QuantConnect.Interfaces.IDataProvider, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, statusUpdateAction: typing.Callable[[int], None], parallelHistoryRequestsEnabled: bool, dataPermissionManager: QuantConnect.Interfaces.IDataPermissionManager) -> None:
        pass

    Api: QuantConnect.Interfaces.IApi

    DataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider

    DataPermissionManager: QuantConnect.Interfaces.IDataPermissionManager

    DataProvider: QuantConnect.Interfaces.IDataProvider

    FactorFileProvider: QuantConnect.Interfaces.IFactorFileProvider

    Job: QuantConnect.Packets.AlgorithmNodePacket

    MapFileProvider: QuantConnect.Interfaces.IMapFileProvider

    ParallelHistoryRequestsEnabled: bool

    StatusUpdateAction: typing.Callable[[int], None]



class HistoryRequest(System.object):
    """
    Represents a request for historical data
    
    HistoryRequest(startTimeUtc: DateTime, endTimeUtc: DateTime, dataType: Type, symbol: Symbol, resolution: Resolution, exchangeHours: SecurityExchangeHours, dataTimeZone: DateTimeZone, fillForwardResolution: Nullable[Resolution], includeExtendedMarketHours: bool, isCustomData: bool, dataNormalizationMode: DataNormalizationMode, tickType: TickType)
    HistoryRequest(config: SubscriptionDataConfig, hours: SecurityExchangeHours, startTimeUtc: DateTime, endTimeUtc: DateTime)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, startTimeUtc: datetime.datetime, endTimeUtc: datetime.datetime, dataType: type, symbol: QuantConnect.Symbol, resolution: QuantConnect.Resolution, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, dataTimeZone: NodaTime.DateTimeZone, fillForwardResolution: typing.Optional[QuantConnect.Resolution], includeExtendedMarketHours: bool, isCustomData: bool, dataNormalizationMode: QuantConnect.DataNormalizationMode, tickType: QuantConnect.TickType) -> None:
        pass

    @typing.overload
    def __new__(self, config: QuantConnect.Data.SubscriptionDataConfig, hours: QuantConnect.Securities.SecurityExchangeHours, startTimeUtc: datetime.datetime, endTimeUtc: datetime.datetime) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    DataNormalizationMode: QuantConnect.DataNormalizationMode

    DataTimeZone: NodaTime.DateTimeZone

    DataType: type

    EndTimeUtc: datetime.datetime

    ExchangeHours: QuantConnect.Securities.SecurityExchangeHours

    FillForwardResolution: typing.Optional[QuantConnect.Resolution]

    IncludeExtendedMarketHours: bool

    IsCustomData: bool

    Resolution: QuantConnect.Resolution

    StartTimeUtc: datetime.datetime

    Symbol: QuantConnect.Symbol

    TickType: QuantConnect.TickType



class HistoryRequestFactory(System.object):
    """
    Helper class used to create new QuantConnect.Data.HistoryRequest
    
    HistoryRequestFactory(algorithm: IAlgorithm)
    """
    def CreateHistoryRequest(self, subscription: QuantConnect.Data.SubscriptionDataConfig, startAlgoTz: datetime.datetime, endAlgoTz: datetime.datetime, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, resolution: typing.Optional[QuantConnect.Resolution]) -> QuantConnect.Data.HistoryRequest:
        pass

    def GetStartTimeAlgoTz(self, symbol: QuantConnect.Symbol, periods: int, resolution: QuantConnect.Resolution, exchange: QuantConnect.Securities.SecurityExchangeHours) -> datetime.datetime:
        pass

    @staticmethod # known case of __new__
    def __new__(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        pass


class IBaseData:
    """ Base Data Class: Type, Timestamp, Key -- Base Features. """
    def Clone(self) -> QuantConnect.Data.BaseData:
        pass

    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, datafeed: QuantConnect.DataFeedEndpoint) -> str:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, dataFeed: QuantConnect.DataFeedEndpoint) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, stream: System.IO.StreamReader, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.BaseData:
        pass

    def Reader(self, *args) -> QuantConnect.Data.BaseData:
        pass

    def RequiresMapping(self) -> bool:
        pass

    DataType: QuantConnect.MarketDataType

    EndTime: datetime.datetime

    Price: float

    Symbol: QuantConnect.Symbol

    Time: datetime.datetime

    Value: float



class IndexedBaseData(QuantConnect.Data.BaseData, QuantConnect.Data.IBaseData):
    """
    Abstract indexed base data class of QuantConnect.
                It is intended to be extended to define customizable data types which are stored
                using an intermediate index source
    """
    @typing.overload
    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        pass

    @typing.overload
    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, datafeed: QuantConnect.DataFeedEndpoint) -> str:
        pass

    def GetSource(self, *args) -> str:
        pass

    def GetSourceForAnIndex(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, index: str, isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        pass


class ISubscriptionEnumeratorFactory:
    """ Create an System.Collections.Generic.IEnumerator """
    def CreateEnumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, dataProvider: QuantConnect.Interfaces.IDataProvider) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        pass


class Slice(QuantConnect.ExtendedDictionary[object], QuantConnect.Interfaces.IExtendedDictionary[Symbol, object], System.Collections.Generic.IEnumerable[KeyValuePair[Symbol, BaseData]], System.Collections.IEnumerable):
    """
    Provides a data structure for all of an algorithm's data at a single time step
    
    Slice(time: DateTime, data: IEnumerable[BaseData])
    Slice(time: DateTime, data: List[BaseData])
    Slice(time: DateTime, data: IEnumerable[BaseData], tradeBars: TradeBars, quoteBars: QuoteBars, ticks: Ticks, optionChains: OptionChains, futuresChains: FuturesChains, splits: Splits, dividends: Dividends, delistings: Delistings, symbolChanges: SymbolChangedEvents, hasData: Nullable[bool])
    """
    def ContainsKey(self, symbol: QuantConnect.Symbol) -> bool:
        pass

    @typing.overload
    def Get(self) -> QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.T]:
        pass

    @typing.overload
    def Get(self, type: type) -> object:
        pass

    @typing.overload
    def Get(self, symbol: QuantConnect.Symbol) -> QuantConnect.Data.T:
        pass

    def Get(self, *args) -> QuantConnect.Data.T:
        pass

    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Data.BaseData]]:
        pass

    def TryGetValue(self, symbol: QuantConnect.Symbol, data: System.Object) -> bool:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, time: datetime.datetime, data: typing.List[QuantConnect.Data.BaseData]) -> None:
        pass

    @typing.overload
    def __new__(self, time: datetime.datetime, data: typing.List[QuantConnect.Data.BaseData]) -> None:
        pass

    @typing.overload
    def __new__(self, time: datetime.datetime, data: typing.List[QuantConnect.Data.BaseData], tradeBars: QuantConnect.Data.Market.TradeBars, quoteBars: QuantConnect.Data.Market.QuoteBars, ticks: QuantConnect.Data.Market.Ticks, optionChains: QuantConnect.Data.Market.OptionChains, futuresChains: QuantConnect.Data.Market.FuturesChains, splits: QuantConnect.Data.Market.Splits, dividends: QuantConnect.Data.Market.Dividends, delistings: QuantConnect.Data.Market.Delistings, symbolChanges: QuantConnect.Data.Market.SymbolChangedEvents, hasData: typing.Optional[bool]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Bars: QuantConnect.Data.Market.TradeBars

    Count: int

    Delistings: QuantConnect.Data.Market.Delistings

    Dividends: QuantConnect.Data.Market.Dividends

    FutureChains: QuantConnect.Data.Market.FuturesChains

    FuturesChains: QuantConnect.Data.Market.FuturesChains

    HasData: bool

    Keys: typing.List[QuantConnect.Symbol]

    OptionChains: QuantConnect.Data.Market.OptionChains

    QuoteBars: QuantConnect.Data.Market.QuoteBars

    Splits: QuantConnect.Data.Market.Splits

    SymbolChangedEvents: QuantConnect.Data.Market.SymbolChangedEvents

    Ticks: QuantConnect.Data.Market.Ticks

    Time: datetime.datetime

    Values: typing.List[QuantConnect.Data.BaseData]


    Item: indexer#


class SliceExtensions(System.object):
    """ Provides extension methods to slice enumerables """
    @staticmethod
    @typing.overload
    def Get(slices: typing.List[QuantConnect.Data.Slice], symbol: QuantConnect.Symbol) -> typing.List[QuantConnect.Data.Market.TradeBar]:
        pass

    @staticmethod
    @typing.overload
    def Get(dataDictionaries: typing.List[QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.T]], symbol: QuantConnect.Symbol) -> typing.List[QuantConnect.Data.T]:
        pass

    @staticmethod
    @typing.overload
    def Get(dataDictionaries: typing.List[QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.T]], symbol: QuantConnect.Symbol, field: str) -> typing.List[float]:
        pass

    @staticmethod
    @typing.overload
    def Get(slices: typing.List[QuantConnect.Data.Slice]) -> typing.List[QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.T]]:
        pass

    @staticmethod
    @typing.overload
    def Get(slices: typing.List[QuantConnect.Data.Slice], symbol: QuantConnect.Symbol) -> typing.List[QuantConnect.Data.T]:
        pass

    @staticmethod
    @typing.overload
    def Get(slices: typing.List[QuantConnect.Data.Slice], symbol: QuantConnect.Symbol, field: typing.Callable[[QuantConnect.Data.BaseData], float]) -> typing.List[float]:
        pass

    def Get(self, *args) -> typing.List[float]:
        pass

    @staticmethod
    def PushThrough(slices: typing.List[QuantConnect.Data.Slice], handler: typing.Callable[[QuantConnect.Data.BaseData], None]) -> None:
        pass

    @staticmethod
    @typing.overload
    def PushThroughConsolidators(slices: typing.List[QuantConnect.Data.Slice], consolidatorsBySymbol: System.Collections.Generic.Dictionary[QuantConnect.Symbol, QuantConnect.Data.Consolidators.IDataConsolidator]) -> None:
        pass

    @staticmethod
    @typing.overload
    def PushThroughConsolidators(slices: typing.List[QuantConnect.Data.Slice], consolidatorsProvider: typing.Callable[[QuantConnect.Symbol], QuantConnect.Data.Consolidators.IDataConsolidator]) -> None:
        pass

    def PushThroughConsolidators(self, *args) -> None:
        pass

    @staticmethod
    def Ticks(slices: typing.List[QuantConnect.Data.Slice]) -> typing.List[QuantConnect.Data.Market.Ticks]:
        pass

    @staticmethod
    def ToDoubleArray(decimals: typing.List[float]) -> typing.List[float]:
        pass

    @staticmethod
    def TradeBars(slices: typing.List[QuantConnect.Data.Slice]) -> typing.List[QuantConnect.Data.Market.TradeBars]:
        pass

    __all__: list


class SubscriptionDataConfig(System.object, System.IEquatable[SubscriptionDataConfig]):
    """
    Subscription data required including the type of data.
    
    SubscriptionDataConfig(objectType: Type, symbol: Symbol, resolution: Resolution, dataTimeZone: DateTimeZone, exchangeTimeZone: DateTimeZone, fillForward: bool, extendedHours: bool, isInternalFeed: bool, isCustom: bool, tickType: Nullable[TickType], isFilteredSubscription: bool, dataNormalizationMode: DataNormalizationMode)
    SubscriptionDataConfig(config: SubscriptionDataConfig, objectType: Type, symbol: Symbol, resolution: Nullable[Resolution], dataTimeZone: DateTimeZone, exchangeTimeZone: DateTimeZone, fillForward: Nullable[bool], extendedHours: Nullable[bool], isInternalFeed: Nullable[bool], isCustom: Nullable[bool], tickType: Nullable[TickType], isFilteredSubscription: Nullable[bool], dataNormalizationMode: Nullable[DataNormalizationMode])
    """
    @typing.overload
    def Equals(self, other: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        pass

    @typing.overload
    def Equals(self, obj: object) -> bool:
        pass

    def Equals(self, *args) -> bool:
        pass

    def GetHashCode(self) -> int:
        pass

    def GetNormalizedPrice(self, price: float) -> float:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, objectType: type, symbol: QuantConnect.Symbol, resolution: QuantConnect.Resolution, dataTimeZone: NodaTime.DateTimeZone, exchangeTimeZone: NodaTime.DateTimeZone, fillForward: bool, extendedHours: bool, isInternalFeed: bool, isCustom: bool, tickType: typing.Optional[QuantConnect.TickType], isFilteredSubscription: bool, dataNormalizationMode: QuantConnect.DataNormalizationMode) -> None:
        pass

    @typing.overload
    def __new__(self, config: QuantConnect.Data.SubscriptionDataConfig, objectType: type, symbol: QuantConnect.Symbol, resolution: typing.Optional[QuantConnect.Resolution], dataTimeZone: NodaTime.DateTimeZone, exchangeTimeZone: NodaTime.DateTimeZone, fillForward: typing.Optional[bool], extendedHours: typing.Optional[bool], isInternalFeed: typing.Optional[bool], isCustom: typing.Optional[bool], tickType: typing.Optional[QuantConnect.TickType], isFilteredSubscription: typing.Optional[bool], dataNormalizationMode: typing.Optional[QuantConnect.DataNormalizationMode]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    MappedSymbol: str

    Symbol: QuantConnect.Symbol

    Consolidators: System.Collections.Generic.ISet[QuantConnect.Data.Consolidators.IDataConsolidator]
    DataNormalizationMode: QuantConnect.DataNormalizationMode
    DataTimeZone: NodaTime.DateTimeZone
    ExchangeTimeZone: NodaTime.DateTimeZone
    ExtendedMarketHours: bool
    FillDataForward: bool
    Increment: datetime.timedelta
    IsCustomData: bool
    IsFilteredSubscription: bool
    IsInternalFeed: bool
    Market: str
    PriceScaleFactor: float
    Resolution: QuantConnect.Resolution
    SecurityType: QuantConnect.SecurityType
    SumOfDividends: float
    TickType: QuantConnect.TickType
    Type: type


class SubscriptionDataConfigExtensions(System.object):
    """
    Helper methods used to determine different configurations properties
                for a given set of QuantConnect.Data.SubscriptionDataConfig
    """
    @staticmethod
    def DataNormalizationMode(subscriptionDataConfigs: typing.List[QuantConnect.Data.SubscriptionDataConfig]) -> QuantConnect.DataNormalizationMode:
        pass

    @staticmethod
    def GetBaseDataInstance(config: QuantConnect.Data.SubscriptionDataConfig) -> QuantConnect.Data.BaseData:
        pass

    @staticmethod
    def GetHighestResolution(subscriptionDataConfigs: typing.List[QuantConnect.Data.SubscriptionDataConfig]) -> QuantConnect.Resolution:
        pass

    @staticmethod
    def IsCustomData(subscriptionDataConfigs: typing.List[QuantConnect.Data.SubscriptionDataConfig]) -> bool:
        pass

    @staticmethod
    def IsExtendedMarketHours(subscriptionDataConfigs: typing.List[QuantConnect.Data.SubscriptionDataConfig]) -> bool:
        pass

    @staticmethod
    def IsFillForward(subscriptionDataConfigs: typing.List[QuantConnect.Data.SubscriptionDataConfig]) -> bool:
        pass

    @staticmethod
    def SetDataNormalizationMode(subscriptionDataConfigs: typing.List[QuantConnect.Data.SubscriptionDataConfig], mode: QuantConnect.DataNormalizationMode) -> None:
        pass

    @staticmethod
    def TickerShouldBeMapped(config: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        pass

    __all__: list


class SubscriptionDataConfigList(System.Collections.Generic.List[SubscriptionDataConfig], System.Collections.Generic.IList[SubscriptionDataConfig], System.Collections.Generic.ICollection[SubscriptionDataConfig], System.Collections.Generic.IEnumerable[SubscriptionDataConfig], System.Collections.IEnumerable, System.Collections.IList, System.Collections.ICollection, System.Collections.Generic.IReadOnlyList[SubscriptionDataConfig], System.Collections.Generic.IReadOnlyCollection[SubscriptionDataConfig]):
    """
    Provides convenient methods for holding several QuantConnect.Data.SubscriptionDataConfig
    
    SubscriptionDataConfigList(symbol: Symbol)
    """
    def SetDataNormalizationMode(self, normalizationMode: QuantConnect.DataNormalizationMode) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, symbol: QuantConnect.Symbol) -> None:
        pass

    IsInternalFeed: bool

    Symbol: QuantConnect.Symbol



class SubscriptionDataSource(System.object, System.IEquatable[SubscriptionDataSource]):
    """
    Represents the source location and transport medium for a subscription
    
    SubscriptionDataSource(source: str, transportMedium: SubscriptionTransportMedium)
    SubscriptionDataSource(source: str, transportMedium: SubscriptionTransportMedium, format: FileFormat)
    SubscriptionDataSource(source: str, transportMedium: SubscriptionTransportMedium, format: FileFormat, headers: IEnumerable[KeyValuePair[str, str]])
    """
    @typing.overload
    def Equals(self, other: QuantConnect.Data.SubscriptionDataSource) -> bool:
        pass

    @typing.overload
    def Equals(self, obj: object) -> bool:
        pass

    def Equals(self, *args) -> bool:
        pass

    def GetHashCode(self) -> int:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, source: str, transportMedium: QuantConnect.SubscriptionTransportMedium) -> None:
        pass

    @typing.overload
    def __new__(self, source: str, transportMedium: QuantConnect.SubscriptionTransportMedium, format: QuantConnect.Data.FileFormat) -> None:
        pass

    @typing.overload
    def __new__(self, source: str, transportMedium: QuantConnect.SubscriptionTransportMedium, format: QuantConnect.Data.FileFormat, headers: typing.List[System.Collections.Generic.KeyValuePair[str, str]]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Format: QuantConnect.Data.FileFormat
    Headers: typing.List[System.Collections.Generic.KeyValuePair[str, str]]
    Source: str
    TransportMedium: QuantConnect.SubscriptionTransportMedium

class SubscriptionManager(System.object):
    """
    Enumerable Subscription Management Class
    
    SubscriptionManager()
    """
    @typing.overload
    def Add(self, symbol: QuantConnect.Symbol, resolution: QuantConnect.Resolution, timeZone: NodaTime.DateTimeZone, exchangeTimeZone: NodaTime.DateTimeZone, isCustomData: bool, fillDataForward: bool, extendedMarketHours: bool) -> QuantConnect.Data.SubscriptionDataConfig:
        pass

    @typing.overload
    def Add(self, dataType: type, tickType: QuantConnect.TickType, symbol: QuantConnect.Symbol, resolution: QuantConnect.Resolution, dataTimeZone: NodaTime.DateTimeZone, exchangeTimeZone: NodaTime.DateTimeZone, isCustomData: bool, fillDataForward: bool, extendedMarketHours: bool, isInternalFeed: bool, isFilteredSubscription: bool, dataNormalizationMode: QuantConnect.DataNormalizationMode) -> QuantConnect.Data.SubscriptionDataConfig:
        pass

    def Add(self, *args) -> QuantConnect.Data.SubscriptionDataConfig:
        pass

    def AddConsolidator(self, symbol: QuantConnect.Symbol, consolidator: QuantConnect.Data.Consolidators.IDataConsolidator) -> None:
        pass

    @staticmethod
    def DefaultDataTypes() -> System.Collections.Generic.Dictionary[QuantConnect.SecurityType, typing.List[QuantConnect.TickType]]:
        pass

    def GetDataTypesForSecurity(self, securityType: QuantConnect.SecurityType) -> typing.List[QuantConnect.TickType]:
        pass

    @staticmethod
    def IsSubscriptionValidForConsolidator(subscription: QuantConnect.Data.SubscriptionDataConfig, consolidator: QuantConnect.Data.Consolidators.IDataConsolidator) -> bool:
        pass

    def LookupSubscriptionConfigDataTypes(self, symbolSecurityType: QuantConnect.SecurityType, resolution: QuantConnect.Resolution, isCanonical: bool) -> typing.List[System.Tuple[type, QuantConnect.TickType]]:
        pass

    def RemoveConsolidator(self, symbol: QuantConnect.Symbol, consolidator: QuantConnect.Data.Consolidators.IDataConsolidator) -> None:
        pass

    def SetDataManager(self, subscriptionManager: QuantConnect.Interfaces.IAlgorithmSubscriptionManager) -> None:
        pass

    AvailableDataTypes: System.Collections.Generic.Dictionary[QuantConnect.SecurityType, typing.List[QuantConnect.TickType]]

    Count: int

    SubscriptionDataConfigService: QuantConnect.Interfaces.ISubscriptionDataConfigService

    Subscriptions: typing.List[QuantConnect.Data.SubscriptionDataConfig]



# variables with complex values

