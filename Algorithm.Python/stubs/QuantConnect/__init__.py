# encoding: utf-8
# module QuantConnect
# from QuantConnect.Algorithm, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null, QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import Newtonsoft.Json
import NodaTime
import Python.Runtime
import QuantConnect
import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.Data
import QuantConnect.Data.Market
import QuantConnect.Interfaces
import QuantConnect.Orders
import QuantConnect.Packets
import QuantConnect.Scheduling
import QuantConnect.Securities
import QuantConnect.Util
import System
import System.Collections
import System.Collections.Concurrent
import System.Collections.Generic
import System.Drawing
import System.Globalization
import System.IO
import System.Text
import System.Threading
import System.Threading.Tasks
import System.Timers
import typing

# no functions
# classes

class AccountType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Account type: margin or cash
    
    enum AccountType, values: Cash (1), Margin (0)
    """
    value__: int
    Cash: AccountType
    Margin: AccountType


class AlgorithmControl(System.object):
    """
    Wrapper for algorithm status enum to include the charting subscription.
    
    AlgorithmControl()
    """
    ChartSubscription: str
    HasSubscribers: bool
    Initialized: bool
    Status: QuantConnect.AlgorithmStatus

class AlgorithmSettings(System.object, QuantConnect.Interfaces.IAlgorithmSettings):
    """
    This class includes user settings for the algorithm which can be changed in the QuantConnect.Interfaces.IAlgorithm.Initialize method
    
    AlgorithmSettings()
    """
    DataSubscriptionLimit: int

    FreePortfolioValue: float

    FreePortfolioValuePercentage: float

    LiquidateEnabled: bool

    MaxAbsolutePortfolioTargetPercentage: float

    MinAbsolutePortfolioTargetPercentage: float

    RebalancePortfolioOnInsightChanges: typing.Optional[bool]

    RebalancePortfolioOnSecurityChanges: typing.Optional[bool]

    StalePriceTimeSpan: datetime.timedelta



class AlgorithmStatus(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    States of a live deployment.
    
    enum AlgorithmStatus, values: Completed (6), Deleted (5), DeployError (0), History (11), Initializing (10), InQueue (1), Invalid (8), Liquidated (4), LoggingIn (9), Running (2), RuntimeError (7), Stopped (3)
    """
    value__: int
    Completed: AlgorithmStatus
    Deleted: AlgorithmStatus
    DeployError: AlgorithmStatus
    History: AlgorithmStatus
    Initializing: AlgorithmStatus
    InQueue: AlgorithmStatus
    Invalid: AlgorithmStatus
    Liquidated: AlgorithmStatus
    LoggingIn: AlgorithmStatus
    Running: AlgorithmStatus
    RuntimeError: AlgorithmStatus
    Stopped: AlgorithmStatus


class AlphaRuntimeStatistics(System.object):
    """
    Contains insight population run time statistics
    
    AlphaRuntimeStatistics(accountCurrencyProvider: IAccountCurrencyProvider)
    AlphaRuntimeStatistics()
    """
    def SetDate(self, now: datetime.datetime) -> None:
        pass

    def SetStartDate(self, algorithmStartDate: datetime.datetime) -> None:
        pass

    def ToDictionary(self) -> System.Collections.Generic.Dictionary[str, str]:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, accountCurrencyProvider: QuantConnect.Interfaces.IAccountCurrencyProvider) -> None:
        pass

    @typing.overload
    def __new__(self) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    EstimatedMonthlyAlphaValue: float

    FitnessScore: float

    KellyCriterionEstimate: float

    KellyCriterionProbabilityValue: float

    LongCount: int

    LongShortRatio: float

    MeanPopulationEstimatedInsightValue: float

    MeanPopulationScore: QuantConnect.Algorithm.Framework.Alphas.InsightScore

    PortfolioTurnover: float

    ReturnOverMaxDrawdown: float

    RollingAveragedPopulationScore: QuantConnect.Algorithm.Framework.Alphas.InsightScore

    ShortCount: int

    SortinoRatio: float

    TotalAccumulatedEstimatedAlphaValue: float

    TotalInsightsAnalysisCompleted: int

    TotalInsightsClosed: int

    TotalInsightsGenerated: int



class BrokerageEnvironment(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Represents the types of environments supported by brokerages for trading
    
    enum BrokerageEnvironment, values: Live (0), Paper (1)
    """
    value__: int
    Live: BrokerageEnvironment
    Paper: BrokerageEnvironment


class ChannelStatus(System.object):
    """ Defines the different channel status values """
    Occupied: str
    Vacated: str
    __all__: list


class Chart(System.object):
    """
    Single Parent Chart Object for Custom Charting
    
    Chart()
    Chart(name: str, type: ChartType)
    Chart(name: str)
    """
    def AddSeries(self, series: QuantConnect.Series) -> None:
        pass

    def Clone(self) -> QuantConnect.Chart:
        pass

    def GetUpdates(self) -> QuantConnect.Chart:
        pass

    def TryAddAndGetSeries(self, name: str, type: QuantConnect.SeriesType, index: int, unit: str, color: System.Drawing.Color, symbol: QuantConnect.ScatterMarkerSymbol, forceAddNew: bool) -> QuantConnect.Series:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, type: QuantConnect.ChartType) -> None:
        pass

    @typing.overload
    def __new__(self, name: str) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    ChartType: QuantConnect.ChartType
    Name: str
    Series: System.Collections.Generic.Dictionary[str, QuantConnect.Series]

class ChartPoint(System.object):
    """
    Single Chart Point Value Type for QCAlgorithm.Plot();
    
    ChartPoint()
    ChartPoint(xValue: Int64, yValue: Decimal)
    ChartPoint(time: DateTime, value: Decimal)
    ChartPoint(point: ChartPoint)
    """
    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, xValue: int, yValue: float) -> None:
        pass

    @typing.overload
    def __new__(self, time: datetime.datetime, value: float) -> None:
        pass

    @typing.overload
    def __new__(self, point: QuantConnect.ChartPoint) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    x: int
    y: float

class ChartType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Type of chart - should we draw the series as overlayed or stacked
    
    enum ChartType, values: Overlay (0), Stacked (1)
    """
    value__: int
    Overlay: ChartType
    Stacked: ChartType


class Currencies(System.object):
    """ Provides commonly used currency pairs and symbols """
    @staticmethod
    def GetCurrencySymbol(currency: str) -> str:
        pass

    CfdCurrencyPairs: List[str]
    CryptoCurrencyPairs: List[str]
    CurrencyPairs: List[str]
    CurrencySymbols: Dictionary[str, str]
    NullCurrency: str
    USD: str
    __all__: list


class DataFeedEndpoint(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Datafeed enum options for selecting the source of the datafeed.
    
    enum DataFeedEndpoint, values: Backtesting (0), Database (3), FileSystem (1), LiveTrading (2)
    """
    value__: int
    Backtesting: DataFeedEndpoint
    Database: DataFeedEndpoint
    FileSystem: DataFeedEndpoint
    LiveTrading: DataFeedEndpoint


class DataNormalizationMode(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Specifies how data is normalized before being sent into an algorithm
    
    enum DataNormalizationMode, values: Adjusted (1), Raw (0), SplitAdjusted (2), TotalReturn (3)
    """
    value__: int
    Adjusted: DataNormalizationMode
    Raw: DataNormalizationMode
    SplitAdjusted: DataNormalizationMode
    TotalReturn: DataNormalizationMode


class DateFormat(System.object):
    """ Shortcut date format strings """
    DB: str
    EightCharacter: str
    Forex: str
    JsonFormat: str
    SixCharacter: str
    TwelveCharacter: str
    UI: str
    US: str
    USDateOnly: str
    USShort: str
    USShortDateOnly: str
    YearMonth: str
    __all__: list


class DelistingType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Specifies the type of QuantConnect.Data.Market.Delisting data
    
    enum DelistingType, values: Delisted (1), Warning (0)
    """
    value__: int
    Delisted: DelistingType
    Warning: DelistingType


class DownloadFailedEventArgs(System.EventArgs):
    """
    Event arguments for the QuantConnect.Interfaces.IDataProviderEvents.DownloadFailed event
    
    DownloadFailedEventArgs(message: str, stackTrace: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, message: str, stackTrace: str) -> None:
        pass

    Message: str

    StackTrace: str



class Expiry(System.object):
    """ Provides static functions that can be used to compute a future System.DateTime (expiry) given a System.DateTime. """
    __all__: list


class ExtendedDictionary(System.object, QuantConnect.Interfaces.IExtendedDictionary[Symbol, T]):
    # no doc
    def clear(self) -> None:
        pass

    def Clear(self) -> None:
        pass

    def copy(self) -> Python.Runtime.PyDict:
        pass

    @typing.overload
    def fromkeys(self, sequence: typing.List[QuantConnect.Symbol]) -> Python.Runtime.PyDict:
        pass

    @typing.overload
    def fromkeys(self, sequence: typing.List[QuantConnect.Symbol], value: QuantConnect.T) -> Python.Runtime.PyDict:
        pass

    def fromkeys(self, *args) -> Python.Runtime.PyDict:
        pass

    @typing.overload
    def get(self, symbol: QuantConnect.Symbol) -> QuantConnect.T:
        pass

    @typing.overload
    def get(self, symbol: QuantConnect.Symbol, value: QuantConnect.T) -> QuantConnect.T:
        pass

    def get(self, *args) -> QuantConnect.T:
        pass

    def items(self) -> Python.Runtime.PyList:
        pass

    def keys(self) -> Python.Runtime.PyList:
        pass

    @typing.overload
    def pop(self, symbol: QuantConnect.Symbol) -> QuantConnect.T:
        pass

    @typing.overload
    def pop(self, symbol: QuantConnect.Symbol, default_value: QuantConnect.T) -> QuantConnect.T:
        pass

    def pop(self, *args) -> QuantConnect.T:
        pass

    def popitem(self) -> Python.Runtime.PyTuple:
        pass

    def Remove(self, symbol: QuantConnect.Symbol) -> bool:
        pass

    @typing.overload
    def setdefault(self, symbol: QuantConnect.Symbol) -> QuantConnect.T:
        pass

    @typing.overload
    def setdefault(self, symbol: QuantConnect.Symbol, default_value: QuantConnect.T) -> QuantConnect.T:
        pass

    def setdefault(self, *args) -> QuantConnect.T:
        pass

    def TryGetValue(self, symbol: QuantConnect.Symbol, value: QuantConnect.T) -> bool:
        pass

    def update(self, other: Python.Runtime.PyObject) -> None:
        pass

    def values(self) -> Python.Runtime.PyList:
        pass

    IsReadOnly: bool


    Item: indexer#


class Extensions(System.object):
    """ Extensions function collections - group all static extensions functions here. """
    @staticmethod
    @typing.overload
    def Add(dictionary: System.Collections.Generic.IDictionary[QuantConnect.TKey, QuantConnect.TCollection], key: QuantConnect.TKey, element: QuantConnect.TElement) -> None:
        pass

    @staticmethod
    @typing.overload
    def Add(dictionary: QuantConnect.Data.Market.Ticks, key: QuantConnect.Symbol, tick: QuantConnect.Data.Market.Tick) -> None:
        pass

    def Add(self, *args) -> None:
        pass

    @staticmethod
    @typing.overload
    def AddOrUpdate(dictionary: System.Collections.Concurrent.ConcurrentDictionary[QuantConnect.K, QuantConnect.V], key: QuantConnect.K, value: QuantConnect.V) -> None:
        pass

    @staticmethod
    @typing.overload
    def AddOrUpdate(dictionary: System.Collections.Concurrent.ConcurrentDictionary[QuantConnect.TKey, System.Lazy[QuantConnect.TValue]], key: QuantConnect.TKey, addValueFactory: typing.Callable[[QuantConnect.TKey], QuantConnect.TValue], updateValueFactory: typing.Callable[[QuantConnect.TKey, QuantConnect.TValue], QuantConnect.TValue]) -> QuantConnect.TValue:
        pass

    def AddOrUpdate(self, *args) -> QuantConnect.TValue:
        pass

    @staticmethod
    def Batch(resultPackets: typing.List[QuantConnect.Packets.AlphaResultPacket]) -> QuantConnect.Packets.AlphaResultPacket:
        pass

    @staticmethod
    def BatchBy(enumerable: typing.List[QuantConnect.T], batchSize: int) -> typing.List[typing.List[QuantConnect.T]]:
        pass

    @staticmethod
    def Clear(queue: System.Collections.Concurrent.ConcurrentQueue[QuantConnect.T]) -> None:
        pass

    @staticmethod
    def ConvertFromUtc(time: datetime.datetime, to: NodaTime.DateTimeZone, strict: bool) -> datetime.datetime:
        pass

    @staticmethod
    @typing.overload
    def ConvertTo(time: datetime.datetime, from_: NodaTime.DateTimeZone, to: NodaTime.DateTimeZone, strict: bool) -> datetime.datetime:
        pass

    @staticmethod
    @typing.overload
    def ConvertTo(value: str) -> QuantConnect.T:
        pass

    @staticmethod
    @typing.overload
    def ConvertTo(value: str, type: type) -> object:
        pass

    def ConvertTo(self, *args) -> object:
        pass

    @staticmethod
    def ConvertToDelegate(pyObject: Python.Runtime.PyObject) -> QuantConnect.T:
        pass

    @staticmethod
    def ConvertToDictionary(pyObject: Python.Runtime.PyObject) -> System.Collections.Generic.Dictionary[QuantConnect.TKey, QuantConnect.TValue]:
        pass

    @staticmethod
    def ConvertToSymbolEnumerable(pyObject: Python.Runtime.PyObject) -> typing.List[QuantConnect.Symbol]:
        pass

    @staticmethod
    def ConvertToUniverseSelectionStringDelegate(selector: typing.Callable[[QuantConnect.T], object]) -> typing.Callable[[QuantConnect.T], typing.List[str]]:
        pass

    @staticmethod
    def ConvertToUniverseSelectionSymbolDelegate(selector: typing.Callable[[QuantConnect.T], object]) -> typing.Callable[[QuantConnect.T], typing.List[QuantConnect.Symbol]]:
        pass

    @staticmethod
    def ConvertToUtc(time: datetime.datetime, from_: NodaTime.DateTimeZone, strict: bool) -> datetime.datetime:
        pass

    @staticmethod
    def CreateType(pyObject: Python.Runtime.PyObject) -> type:
        pass

    @staticmethod
    def ExchangeRoundDown(dateTime: datetime.datetime, interval: datetime.timedelta, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, extendedMarket: bool) -> datetime.datetime:
        pass

    @staticmethod
    def ExchangeRoundDownInTimeZone(dateTime: datetime.datetime, interval: datetime.timedelta, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, roundingTimeZone: NodaTime.DateTimeZone, extendedMarket: bool) -> datetime.datetime:
        pass

    @staticmethod
    def GetAndDispose(instance: Python.Runtime.PyObject) -> QuantConnect.T:
        pass

    @staticmethod
    def GetBaseDataInstance(type: type) -> QuantConnect.Data.BaseData:
        pass

    @staticmethod
    def GetBetterTypeName(type: type) -> str:
        pass

    @staticmethod
    def GetBytes(str: str) -> typing.List[bytes]:
        pass

    @staticmethod
    def GetDecimalEpsilon() -> float:
        pass

    @staticmethod
    def GetEnumString(value: int, pyObject: Python.Runtime.PyObject) -> str:
        pass

    @staticmethod
    def GetExtension(str: str) -> str:
        pass

    @staticmethod
    def GetHash(orders: System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order]) -> int:
        pass

    @staticmethod
    def GetMD5Hash(stream: System.IO.Stream) -> typing.List[bytes]:
        pass

    @staticmethod
    def GetPythonMethod(instance: Python.Runtime.PyObject, name: str) -> object:
        pass

    @staticmethod
    def GetString(bytes: typing.List[bytes], encoding: System.Text.Encoding) -> str:
        pass

    @staticmethod
    def GetStringBetweenChars(value: str, left: str, right: str) -> str:
        pass

    @staticmethod
    def GetZeroPriceMessage(symbol: QuantConnect.Symbol) -> str:
        pass

    @staticmethod
    def IsCommonBusinessDay(date: datetime.datetime) -> bool:
        pass

    @staticmethod
    @typing.overload
    def IsEmpty(series: QuantConnect.Series) -> bool:
        pass

    @staticmethod
    @typing.overload
    def IsEmpty(chart: QuantConnect.Chart) -> bool:
        pass

    def IsEmpty(self, *args) -> bool:
        pass

    @staticmethod
    def IsNaNOrZero(value: float) -> bool:
        pass

    @staticmethod
    def IsSubclassOfGeneric(type: type, possibleSuperType: type) -> bool:
        pass

    @staticmethod
    def IsValid(securityType: QuantConnect.SecurityType) -> bool:
        pass

    @staticmethod
    def LazyToUpper(data: str) -> str:
        pass

    @staticmethod
    def MatchesTypeName(type: type, typeName: str) -> bool:
        pass

    @staticmethod
    def Move(list: typing.List[QuantConnect.T], oldIndex: int, newIndex: int) -> None:
        pass

    @staticmethod
    def Normalize(input: float) -> float:
        pass

    @staticmethod
    def NormalizeToStr(input: float) -> str:
        pass

    @staticmethod
    def OrderTargetsByMarginImpact(targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget], algorithm: QuantConnect.Interfaces.IAlgorithm, targetIsDelta: bool) -> typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        pass

    @staticmethod
    def ProcessUntilEmpty(collection: System.Collections.Concurrent.IProducerConsumerCollection[QuantConnect.T], handler: typing.Callable[[QuantConnect.T], None]) -> None:
        pass

    @staticmethod
    def RemoveFromEnd(s: str, ending: str) -> str:
        pass

    @staticmethod
    def Reset(timer: System.Timers.Timer) -> None:
        pass

    @staticmethod
    def ResolutionToLower(resolution: QuantConnect.Resolution) -> str:
        pass

    @staticmethod
    @typing.overload
    def Round(time: datetime.timedelta, roundingInterval: datetime.timedelta, roundingType: System.MidpointRounding) -> datetime.timedelta:
        pass

    @staticmethod
    @typing.overload
    def Round(time: datetime.timedelta, roundingInterval: datetime.timedelta) -> datetime.timedelta:
        pass

    @staticmethod
    @typing.overload
    def Round(datetime: datetime.datetime, roundingInterval: datetime.timedelta) -> datetime.datetime:
        pass

    def Round(self, *args) -> datetime.datetime:
        pass

    @staticmethod
    def RoundDown(dateTime: datetime.datetime, interval: datetime.timedelta) -> datetime.datetime:
        pass

    @staticmethod
    def RoundDownInTimeZone(dateTime: datetime.datetime, roundingInterval: datetime.timedelta, sourceTimeZone: NodaTime.DateTimeZone, roundingTimeZone: NodaTime.DateTimeZone) -> datetime.datetime:
        pass

    @staticmethod
    @typing.overload
    def RoundToSignificantDigits(d: float, digits: int) -> float:
        pass

    @staticmethod
    @typing.overload
    def RoundToSignificantDigits(d: float, digits: int) -> float:
        pass

    def RoundToSignificantDigits(self, *args) -> float:
        pass

    @staticmethod
    def RoundUp(time: datetime.datetime, d: datetime.timedelta) -> datetime.datetime:
        pass

    @staticmethod
    def SafeDecimalCast(input: float) -> float:
        pass

    @staticmethod
    def SecurityTypeToLower(securityType: QuantConnect.SecurityType) -> str:
        pass

    @staticmethod
    def SingleOrAlgorithmTypeName(names: typing.List[str], algorithmTypeName: str) -> str:
        pass

    @staticmethod
    def SmartRounding(input: float) -> float:
        pass

    @staticmethod
    def StopSafely(thread: System.Threading.Thread, timeout: datetime.timedelta, token: System.Threading.CancellationTokenSource) -> None:
        pass

    @staticmethod
    def SynchronouslyAwaitTask(task: System.Threading.Tasks.Task) -> None:
        pass

    @staticmethod
    def SynchronouslyAwaitTaskResult(task: System.Threading.Tasks.Task[QuantConnect.TResult]) -> QuantConnect.TResult:
        pass

    @staticmethod
    def TickTypeToLower(tickType: QuantConnect.TickType) -> str:
        pass

    @staticmethod
    def ToCamelCase(value: str) -> str:
        pass

    @staticmethod
    def ToCsv(str: str, size: int) -> typing.List[str]:
        pass

    @staticmethod
    def ToCsvData(str: str, size: int, delimiter: str) -> typing.List[str]:
        pass

    @staticmethod
    def ToDecimal(str: str) -> float:
        pass

    @staticmethod
    def ToDecimalAllowExponent(str: str) -> float:
        pass

    @staticmethod
    def ToFunc(dateRule: QuantConnect.Scheduling.IDateRule) -> typing.Callable[[datetime.datetime], typing.Optional[datetime.datetime]]:
        pass

    @staticmethod
    def ToHigherResolutionEquivalent(timeSpan: datetime.timedelta, requireExactMatch: bool) -> QuantConnect.Resolution:
        pass

    @staticmethod
    def ToInt32(str: str) -> int:
        pass

    @staticmethod
    def ToInt64(str: str) -> int:
        pass

    @staticmethod
    def ToLower(enum: System.Enum) -> str:
        pass

    @staticmethod
    def ToMD5(str: str) -> str:
        pass

    @staticmethod
    def ToOrderTicket(order: QuantConnect.Orders.Order, transactionManager: QuantConnect.Securities.SecurityTransactionManager) -> QuantConnect.Orders.OrderTicket:
        pass

    @staticmethod
    def ToPyList(enumerable: System.Collections.IEnumerable) -> Python.Runtime.PyList:
        pass

    @staticmethod
    def ToSafeString(pyObject: Python.Runtime.PyObject) -> str:
        pass

    @staticmethod
    def ToSHA256(data: str) -> str:
        pass

    @staticmethod
    def ToStream(str: str) -> System.IO.Stream:
        pass

    @staticmethod
    def ToStringPerformance(optionRight: QuantConnect.OptionRight) -> str:
        pass

    @staticmethod
    def ToTimeSpan(resolution: QuantConnect.Resolution) -> datetime.timedelta:
        pass

    @staticmethod
    def TruncateTo3DecimalPlaces(value: float) -> float:
        pass

    @staticmethod
    def TryConvert(pyObject: Python.Runtime.PyObject, result: QuantConnect.T, allowPythonDerivative: bool) -> bool:
        pass

    @staticmethod
    def TryConvertToDelegate(pyObject: Python.Runtime.PyObject, result: QuantConnect.T) -> bool:
        pass

    @staticmethod
    @typing.overload
    def WaitOne(waitHandle: System.Threading.WaitHandle, cancellationToken: System.Threading.CancellationToken) -> bool:
        pass

    @staticmethod
    @typing.overload
    def WaitOne(waitHandle: System.Threading.WaitHandle, timeout: datetime.timedelta, cancellationToken: System.Threading.CancellationToken) -> bool:
        pass

    @staticmethod
    @typing.overload
    def WaitOne(waitHandle: System.Threading.WaitHandle, millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken) -> bool:
        pass

    def WaitOne(self, *args) -> bool:
        pass

    @staticmethod
    def WithEmbeddedHtmlAnchors(source: str) -> str:
        pass

    __all__: list


class Field(System.object):
    """ Provides static properties to be used as selectors with the indicator system """
    __all__: list


class Globals(System.object):
    """ Provides application level constant values """
    @staticmethod
    def Reset() -> None:
        pass

    Cache: str
    CacheDataFolder: str
    DataFolder: str
    Version: str
    __all__: list


class Holding(System.object):
    """
    Singular holding of assets from backend live nodes:
    
    Holding()
    Holding(security: Security)
    """
    def Clone(self) -> QuantConnect.Holding:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, security: QuantConnect.Securities.Security) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    AveragePrice: float
    ConversionRate: typing.Optional[float]
    CurrencySymbol: str
    MarketPrice: float
    MarketValue: float
    Quantity: float
    Symbol: QuantConnect.Symbol
    Type: QuantConnect.SecurityType
    UnrealizedPnL: float

class IIsolatorLimitResultProvider:
    """
    Provides an abstraction for managing isolator limit results.
                This is originally intended to be used by the training feature to permit a single
                algorithm time loop to extend past the default of ten minutes
    """
    def IsWithinLimit(self) -> QuantConnect.IsolatorLimitResult:
        pass

    def RequestAdditionalTime(self, minutes: int) -> None:
        pass

    def TryRequestAdditionalTime(self, minutes: int) -> bool:
        pass


class InvalidConfigurationDetectedEventArgs(System.EventArgs):
    """
    Event arguments for the QuantConnect.Interfaces.IDataProviderEvents.InvalidConfigurationDetected event
    
    InvalidConfigurationDetectedEventArgs(message: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, message: str) -> None:
        pass

    Message: str



class Isolator(System.object):
    """
    Isolator class - create a new instance of the algorithm and ensure it doesn't
                exceed memory or time execution limits.
    
    Isolator()
    """
    @typing.overload
    def ExecuteWithTimeLimit(self, timeSpan: datetime.timedelta, withinCustomLimits: typing.Callable[[], QuantConnect.IsolatorLimitResult], codeBlock: System.Action, memoryCap: int, sleepIntervalMillis: int, workerThread: QuantConnect.Util.WorkerThread) -> bool:
        pass

    @typing.overload
    def ExecuteWithTimeLimit(self, timeSpan: datetime.timedelta, codeBlock: System.Action, memoryCap: int, sleepIntervalMillis: int, workerThread: QuantConnect.Util.WorkerThread) -> bool:
        pass

    def ExecuteWithTimeLimit(self, *args) -> bool:
        pass

    CancellationToken: System.Threading.CancellationToken

    CancellationTokenSource: System.Threading.CancellationTokenSource

    IsCancellationRequested: bool



class IsolatorLimitResult(System.object):
    """
    Represents the result of the QuantConnect.Isolator limiter callback
    
    IsolatorLimitResult(currentTimeStepElapsed: TimeSpan, errorMessage: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, currentTimeStepElapsed: datetime.timedelta, errorMessage: str) -> None:
        pass

    CurrentTimeStepElapsed: datetime.timedelta

    ErrorMessage: str

    IsWithinCustomLimits: bool



class IsolatorLimitResultProvider(System.object):
    """ Provides access to the QuantConnect.IsolatorLimitResultProvider.NullIsolatorLimitResultProvider and extension methods supporting QuantConnect.Scheduling.ScheduledEvent """
    @staticmethod
    @typing.overload
    def Consume(isolatorLimitProvider: QuantConnect.IIsolatorLimitResultProvider, scheduledEvent: QuantConnect.Scheduling.ScheduledEvent, scanTimeUtc: datetime.datetime, timeMonitor: QuantConnect.Scheduling.TimeMonitor) -> None:
        pass

    @staticmethod
    @typing.overload
    def Consume(isolatorLimitProvider: QuantConnect.IIsolatorLimitResultProvider, timeProvider: QuantConnect.ITimeProvider, code: System.Action, timeMonitor: QuantConnect.Scheduling.TimeMonitor) -> None:
        pass

    def Consume(self, *args) -> None:
        pass

    Null: NullIsolatorLimitResultProvider
    __all__: list


class ITimeProvider:
    """
    Provides access to the current time in UTC. This doesn't necessarily
                need to be wall-clock time, but rather the current time in some system
    """
    def GetUtcNow(self) -> datetime.datetime:
        pass


class Language(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Multilanguage support enum: which language is this project for the interop bridge converter.
    
    enum Language, values: CSharp (0), FSharp (1), Java (3), Python (4), VisualBasic (2)
    """
    value__: int
    CSharp: Language
    FSharp: Language
    Java: Language
    Python: Language
    VisualBasic: Language


class LocalTimeKeeper(System.object):
    """
    Represents the current local time. This object is created via the QuantConnect.TimeKeeper to
                manage conversions to local time.
    """
    LocalTime: datetime.datetime

    TimeZone: NodaTime.DateTimeZone


    TimeUpdated: BoundEvent


class Market(System.object):
    """ Markets Collection: Soon to be expanded to a collection of items specifying the market hour, timezones and country codes. """
    @staticmethod
    def Add(market: str, identifier: int) -> None:
        pass

    @staticmethod
    def Decode(code: int) -> str:
        pass

    @staticmethod
    def Encode(market: str) -> typing.Optional[int]:
        pass

    Binance: str
    Bitfinex: str
    Bithumb: str
    Bitstamp: str
    Bittrex: str
    CBOE: str
    CBOT: str
    CME: str
    Coinone: str
    COMEX: str
    Dukascopy: str
    FXCM: str
    GDAX: str
    Globex: str
    HitBTC: str
    HKFE: str
    ICE: str
    Kraken: str
    NSE: str
    NYMEX: str
    Oanda: str
    OkCoin: str
    Poloniex: str
    SGX: str
    USA: str
    __all__: list


class MarketCodes(System.object):
    """ Global Market Short Codes and their full versions: (used in tick objects) """
    Canada: Dictionary[str, str]
    US: Dictionary[str, str]
    __all__: list


class MarketDataType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Market data style: is the market data a summary (OHLC style) bar, or is it a time-price value.
    
    enum MarketDataType, values: Auxiliary (3), Base (0), FuturesChain (6), OptionChain (5), QuoteBar (4), Tick (2), TradeBar (1)
    """
    value__: int
    Auxiliary: MarketDataType
    Base: MarketDataType
    FuturesChain: MarketDataType
    OptionChain: MarketDataType
    QuoteBar: MarketDataType
    Tick: MarketDataType
    TradeBar: MarketDataType


class NewTradableDateEventArgs(System.EventArgs):
    """
    Event arguments for the NewTradableDate event
    
    NewTradableDateEventArgs(date: DateTime, lastBaseData: BaseData, symbol: Symbol)
    """
    @staticmethod # known case of __new__
    def __new__(self, date: datetime.datetime, lastBaseData: QuantConnect.Data.BaseData, symbol: QuantConnect.Symbol) -> None:
        pass

    Date: datetime.datetime

    LastBaseData: QuantConnect.Data.BaseData

    Symbol: QuantConnect.Symbol



class NumericalPrecisionLimitedEventArgs(System.EventArgs):
    """
    Event arguments for the QuantConnect.Interfaces.IDataProviderEvents.NumericalPrecisionLimited event
    
    NumericalPrecisionLimitedEventArgs(message: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, message: str) -> None:
        pass

    Message: str



class OptionRight(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Specifies the different types of options
    
    enum OptionRight, values: Call (0), Put (1)
    """
    value__: int

class OptionStyle(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Specifies the style of an option
    
    enum OptionStyle, values: American (0), European (1)
    """
    value__: int
    American: OptionStyle
    European: OptionStyle


class OS(System.object):
    """ Operating systems class for managing anything that is operation system specific. """
    @staticmethod
    def GetServerStatistics() -> System.Collections.Generic.Dictionary[str, str]:
        pass

    ApplicationMemoryUsed: Int64
    CpuUsage: Decimal
    DriveSpaceRemaining: Int64
    DriveSpaceUsed: Int64
    DriveTotalSpace: Int64
    IsLinux: bool
    IsWindows: bool
    PathSeparation: str
    TotalPhysicalMemoryUsed: Int64
    __all__: list


class Parse(System.object):
    """ Provides methods for parsing strings using System.Globalization.CultureInfo.InvariantCulture """
    @staticmethod
    def DateTime(value: str) -> datetime.datetime:
        pass

    @staticmethod
    @typing.overload
    def DateTimeExact(value: str, format: str) -> datetime.datetime:
        pass

    @staticmethod
    @typing.overload
    def DateTimeExact(value: str, format: str, dateTimeStyles: System.Globalization.DateTimeStyles) -> datetime.datetime:
        pass

    def DateTimeExact(self, *args) -> datetime.datetime:
        pass

    @staticmethod
    @typing.overload
    def Decimal(value: str) -> float:
        pass

    @staticmethod
    @typing.overload
    def Decimal(value: str, numberStyles: System.Globalization.NumberStyles) -> float:
        pass

    def Decimal(self, *args) -> float:
        pass

    @staticmethod
    def Double(value: str) -> float:
        pass

    @staticmethod
    def Int(value: str) -> int:
        pass

    @staticmethod
    @typing.overload
    def Long(value: str) -> int:
        pass

    @staticmethod
    @typing.overload
    def Long(value: str, numberStyles: System.Globalization.NumberStyles) -> int:
        pass

    def Long(self, *args) -> int:
        pass

    @staticmethod
    def TimeSpan(value: str) -> datetime.timedelta:
        pass

    @staticmethod
    @typing.overload
    def TryParse(input: str, value: System.TimeSpan) -> bool:
        pass

    @staticmethod
    @typing.overload
    def TryParse(input: str, dateTimeStyle: System.Globalization.DateTimeStyles, value: System.DateTime) -> bool:
        pass

    @staticmethod
    @typing.overload
    def TryParse(input: str, numberStyle: System.Globalization.NumberStyles, value: System.Double) -> bool:
        pass

    @staticmethod
    @typing.overload
    def TryParse(input: str, numberStyle: System.Globalization.NumberStyles, value: System.Decimal) -> bool:
        pass

    @staticmethod
    @typing.overload
    def TryParse(input: str, numberStyle: System.Globalization.NumberStyles, value: System.Int32) -> bool:
        pass

    @staticmethod
    @typing.overload
    def TryParse(input: str, numberStyle: System.Globalization.NumberStyles, value: System.Int64) -> bool:
        pass

    def TryParse(self, *args) -> bool:
        pass

    @staticmethod
    @typing.overload
    def TryParseExact(input: str, format: str, timeSpanStyle: System.Globalization.TimeSpanStyles, value: System.TimeSpan) -> bool:
        pass

    @staticmethod
    @typing.overload
    def TryParseExact(input: str, format: str, dateTimeStyle: System.Globalization.DateTimeStyles, value: System.DateTime) -> bool:
        pass

    def TryParseExact(self, *args) -> bool:
        pass

    __all__: list


class Period(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    enum Period - Enum of all the analysis periods, AS integers. Reference "Period" Array to access the values
    
    enum Period, values: FifteenMinutes (900), FiveMinutes (300), FourHours (14400), OneHour (3600), OneMinute (60), SixHours (21600), TenMinutes (600), TenSeconds (10), ThirtyMinutes (1800), ThirtySeconds (30), ThreeMinutes (180), TwentyMinutes (1200), TwoHours (7200), TwoMinutes (120)
    """
    value__: int
    FifteenMinutes: Period
    FiveMinutes: Period
    FourHours: Period
    OneHour: Period
    OneMinute: Period
    SixHours: Period
    TenMinutes: Period
    TenSeconds: Period
    ThirtyMinutes: Period
    ThirtySeconds: Period
    ThreeMinutes: Period
    TwentyMinutes: Period
    TwoHours: Period
    TwoMinutes: Period


class ReaderErrorDetectedEventArgs(System.EventArgs):
    """
    Event arguments for the QuantConnect.Interfaces.IDataProviderEvents.ReaderErrorDetected event
    
    ReaderErrorDetectedEventArgs(message: str, stackTrace: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, message: str, stackTrace: str) -> None:
        pass

    Message: str

    StackTrace: str



class RealTimeProvider(System.object, QuantConnect.ITimeProvider):
    """
    Provides an implementation of QuantConnect.ITimeProvider that
                uses System.DateTime.UtcNow to provide the current time
    
    RealTimeProvider()
    """
    def GetUtcNow(self) -> datetime.datetime:
        pass

    Instance: RealTimeProvider


class RealTimeSynchronizedTimer(System.object):
    """
    Real time timer class for precise callbacks on a millisecond resolution in a self managed thread.
    
    RealTimeSynchronizedTimer()
    RealTimeSynchronizedTimer(period: TimeSpan, callback: Action[DateTime])
    """
    def Pause(self) -> None:
        pass

    def Resume(self) -> None:
        pass

    def Scanner(self) -> None:
        pass

    def Start(self) -> None:
        pass

    def Stop(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, period: datetime.timedelta, callback: typing.Callable[[datetime.datetime], None]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass


class Resolution(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Resolution of data requested.
    
    enum Resolution, values: Daily (4), Hour (3), Minute (2), Second (1), Tick (0)
    """
    value__: int
    Daily: Resolution
    Hour: Resolution
    Minute: Resolution
    Second: Resolution
    Tick: Resolution


class Result(System.object):
    """
    Base class for backtesting and live results that packages result data.
                QuantConnect.Packets.LiveResultQuantConnect.Packets.BacktestResult
    
    Result()
    """
    AlphaRuntimeStatistics: QuantConnect.AlphaRuntimeStatistics
    Charts: System.Collections.Generic.IDictionary[str, QuantConnect.Chart]
    OrderEvents: typing.List[QuantConnect.Orders.OrderEvent]
    Orders: System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order]
    ProfitLoss: System.Collections.Generic.IDictionary[datetime.datetime, float]
    RuntimeStatistics: System.Collections.Generic.IDictionary[str, str]
    ServerStatistics: System.Collections.Generic.IDictionary[str, str]
    Statistics: System.Collections.Generic.IDictionary[str, str]

class ScatterMarkerSymbol(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Shape or symbol for the marker in a scatter plot
    
    enum ScatterMarkerSymbol, values: Circle (1), Diamond (3), None (0), Square (2), Triangle (4), TriangleDown (5)
    """
    value__: int
    Circle: ScatterMarkerSymbol
    Diamond: ScatterMarkerSymbol
    None: ScatterMarkerSymbol
    Square: ScatterMarkerSymbol
    Triangle: ScatterMarkerSymbol
    TriangleDown: ScatterMarkerSymbol


class SecurityIdentifier(System.object, System.IEquatable[SecurityIdentifier]):
    """
    Defines a unique identifier for securities
    
    SecurityIdentifier(symbol: str, properties: UInt64)
    SecurityIdentifier(symbol: str, properties: UInt64, underlying: SecurityIdentifier)
    """
    @typing.overload
    def Equals(self, other: QuantConnect.SecurityIdentifier) -> bool:
        pass

    @typing.overload
    def Equals(self, obj: object) -> bool:
        pass

    def Equals(self, *args) -> bool:
        pass

    @staticmethod
    def GenerateBase(dataType: type, symbol: str, market: str, mapSymbol: bool, date: typing.Optional[datetime.datetime]) -> QuantConnect.SecurityIdentifier:
        pass

    @staticmethod
    def GenerateBaseSymbol(dataType: type, symbol: str) -> str:
        pass

    @staticmethod
    def GenerateCfd(symbol: str, market: str) -> QuantConnect.SecurityIdentifier:
        pass

    @staticmethod
    def GenerateConstituentIdentifier(symbol: str, securityType: QuantConnect.SecurityType, market: str) -> QuantConnect.SecurityIdentifier:
        pass

    @staticmethod
    def GenerateCrypto(symbol: str, market: str) -> QuantConnect.SecurityIdentifier:
        pass

    @staticmethod
    @typing.overload
    def GenerateEquity(symbol: str, market: str, mapSymbol: bool, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, mappingResolveDate: typing.Optional[datetime.datetime]) -> QuantConnect.SecurityIdentifier:
        pass

    @staticmethod
    @typing.overload
    def GenerateEquity(date: datetime.datetime, symbol: str, market: str) -> QuantConnect.SecurityIdentifier:
        pass

    def GenerateEquity(self, *args) -> QuantConnect.SecurityIdentifier:
        pass

    @staticmethod
    def GenerateForex(symbol: str, market: str) -> QuantConnect.SecurityIdentifier:
        pass

    @staticmethod
    def GenerateFuture(expiry: datetime.datetime, symbol: str, market: str) -> QuantConnect.SecurityIdentifier:
        pass

    @staticmethod
    def GenerateOption(expiry: datetime.datetime, underlying: QuantConnect.SecurityIdentifier, market: str, strike: float, optionRight: QuantConnect.OptionRight, optionStyle: QuantConnect.OptionStyle) -> QuantConnect.SecurityIdentifier:
        pass

    def GetHashCode(self) -> int:
        pass

    @staticmethod
    def Parse(value: str) -> QuantConnect.SecurityIdentifier:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod
    def TryParse(value: str, identifier: QuantConnect.SecurityIdentifier) -> bool:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, symbol: str, properties: int) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: str, properties: int, underlying: QuantConnect.SecurityIdentifier) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Date: datetime.datetime

    HasUnderlying: bool

    Market: str

    OptionRight: QuantConnect.OptionRight

    OptionStyle: QuantConnect.OptionStyle

    SecurityType: QuantConnect.SecurityType

    StrikePrice: float

    Symbol: str

    Underlying: QuantConnect.SecurityIdentifier


    DefaultDate: DateTime
    Empty: SecurityIdentifier
    InvalidSymbolCharacters: HashSet[Char]
    None: SecurityIdentifier


class SecurityType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Type of tradable security / underlying asset
    
    enum SecurityType, values: Base (0), Cfd (6), Commodity (3), Crypto (7), Equity (1), Forex (4), Future (5), Option (2)
    """
    value__: int
    Base: SecurityType
    Cfd: SecurityType
    Commodity: SecurityType
    Crypto: SecurityType
    Equity: SecurityType
    Forex: SecurityType
    Future: SecurityType
    Option: SecurityType


class Series(System.object):
    """
    Chart Series Object - Series data and properties for a chart:
    
    Series()
    Series(name: str)
    Series(name: str, type: SeriesType)
    Series(name: str, type: SeriesType, index: int)
    Series(name: str, type: SeriesType, index: int, unit: str)
    Series(name: str, type: SeriesType, unit: str)
    Series(name: str, type: SeriesType, unit: str, color: Color)
    Series(name: str, type: SeriesType, unit: str, color: Color, symbol: ScatterMarkerSymbol)
    """
    @typing.overload
    def AddPoint(self, time: datetime.datetime, value: float) -> None:
        pass

    @typing.overload
    def AddPoint(self, chartPoint: QuantConnect.ChartPoint) -> None:
        pass

    def AddPoint(self, *args) -> None:
        pass

    def Clone(self) -> QuantConnect.Series:
        pass

    def ConsolidateChartPoints(self) -> QuantConnect.ChartPoint:
        pass

    def GetUpdates(self) -> QuantConnect.Series:
        pass

    def Purge(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, name: str) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, type: QuantConnect.SeriesType) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, type: QuantConnect.SeriesType, index: int) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, type: QuantConnect.SeriesType, index: int, unit: str) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, type: QuantConnect.SeriesType, unit: str) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, type: QuantConnect.SeriesType, unit: str, color: System.Drawing.Color) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, type: QuantConnect.SeriesType, unit: str, color: System.Drawing.Color, symbol: QuantConnect.ScatterMarkerSymbol) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Color: System.Drawing.Color
    Index: int
    Name: str
    ScatterMarkerSymbol: QuantConnect.ScatterMarkerSymbol
    SeriesType: QuantConnect.SeriesType
    Unit: str
    Values: typing.List[QuantConnect.ChartPoint]

class SeriesSampler(System.object):
    """
    A type capable of taking a chart and resampling using a linear interpolation strategy
    
    SeriesSampler(resolution: TimeSpan)
    """
    def Sample(self, series: QuantConnect.Series, start: datetime.datetime, stop: datetime.datetime) -> QuantConnect.Series:
        pass

    def SampleCharts(self, charts: System.Collections.Generic.IDictionary[str, QuantConnect.Chart], start: datetime.datetime, stop: datetime.datetime) -> System.Collections.Generic.Dictionary[str, QuantConnect.Chart]:
        pass

    @staticmethod # known case of __new__
    def __new__(self, resolution: datetime.timedelta) -> None:
        pass


class SeriesType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Available types of charts
    
    enum SeriesType, values: Bar (3), Candle (2), Flag (4), Line (0), Pie (6), Scatter (1), StackedArea (5), Treemap (7)
    """
    value__: int
    Bar: SeriesType
    Candle: SeriesType
    Flag: SeriesType
    Line: SeriesType
    Pie: SeriesType
    Scatter: SeriesType
    StackedArea: SeriesType
    Treemap: SeriesType


class ServerType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Live server types available through the web IDE. / QC deployment.
    
    enum ServerType, values: Server1024 (1), Server2048 (2), Server512 (0)
    """
    value__: int
    Server1024: ServerType
    Server2048: ServerType
    Server512: ServerType


class SettlementType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Specifies the type of settlement in derivative deals
    
    enum SettlementType, values: Cash (1), PhysicalDelivery (0)
    """
    value__: int
    Cash: SettlementType
    PhysicalDelivery: SettlementType


class SplitType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Specifies the type of QuantConnect.Data.Market.Split data
    
    enum SplitType, values: SplitOccurred (1), Warning (0)
    """
    value__: int
    SplitOccurred: SplitType
    Warning: SplitType


class StartDateLimitedEventArgs(System.EventArgs):
    """
    Event arguments for the QuantConnect.Interfaces.IDataProviderEvents.StartDateLimited event
    
    StartDateLimitedEventArgs(message: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, message: str) -> None:
        pass

    Message: str



class StoragePermissions(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Cloud storage permission options.
    
    enum StoragePermissions, values: Authenticated (1), Public (0)
    """
    value__: int
    Authenticated: StoragePermissions
    Public: StoragePermissions


class StringExtensions(System.object):
    """
    Provides extension methods for properly parsing and serializing values while properly using
                an IFormatProvider/CultureInfo when applicable
    """
    @staticmethod
    @typing.overload
    def ConvertInvariant(value: object) -> QuantConnect.T:
        pass

    @staticmethod
    @typing.overload
    def ConvertInvariant(value: object, conversionType: type) -> object:
        pass

    def ConvertInvariant(self, *args) -> object:
        pass

    @staticmethod
    def EndsWithInvariant(value: str, ending: str, ignoreCase: bool) -> bool:
        pass

    @staticmethod
    @typing.overload
    def IfNotNullOrEmpty(value: str, defaultValue: QuantConnect.T, func: typing.Callable[[str], QuantConnect.T]) -> QuantConnect.T:
        pass

    @staticmethod
    @typing.overload
    def IfNotNullOrEmpty(value: str, func: typing.Callable[[str], QuantConnect.T]) -> QuantConnect.T:
        pass

    def IfNotNullOrEmpty(self, *args) -> QuantConnect.T:
        pass

    @staticmethod
    @typing.overload
    def IndexOfInvariant(value: str, character: str) -> int:
        pass

    @staticmethod
    @typing.overload
    def IndexOfInvariant(value: str, substring: str, ignoreCase: bool) -> int:
        pass

    def IndexOfInvariant(self, *args) -> int:
        pass

    @staticmethod
    def Invariant(formattable: System.FormattableString) -> str:
        pass

    @staticmethod
    def LastIndexOfInvariant(value: str, substring: str, ignoreCase: bool) -> int:
        pass

    @staticmethod
    def SafeSubstring(value: str, startIndex: int, length: int) -> str:
        pass

    @staticmethod
    def StartsWithInvariant(value: str, beginning: str, ignoreCase: bool) -> bool:
        pass

    @staticmethod
    def ToIso8601Invariant(dateTime: datetime.datetime) -> str:
        pass

    @staticmethod
    @typing.overload
    def ToStringInvariant(convertible: System.IConvertible) -> str:
        pass

    @staticmethod
    @typing.overload
    def ToStringInvariant(formattable: System.IFormattable, format: str) -> str:
        pass

    def ToStringInvariant(self, *args) -> str:
        pass

    __all__: list


class SubscriptionTransportMedium(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Specifies where a subscription's data comes from
    
    enum SubscriptionTransportMedium, values: LocalFile (0), RemoteFile (1), Rest (2), Streaming (3)
    """
    value__: int
    LocalFile: SubscriptionTransportMedium
    RemoteFile: SubscriptionTransportMedium
    Rest: SubscriptionTransportMedium
    Streaming: SubscriptionTransportMedium


class Symbol(System.object, System.IEquatable[Symbol], System.IComparable):
    """
    Represents a unique security identifier. This is made of two components,
                the unique SID and the Value. The value is the current ticker symbol while
                the SID is constant over the life of a security
    
    Symbol(sid: SecurityIdentifier, value: str)
    """
    def CompareTo(self, obj: object) -> int:
        pass

    def Contains(self, value: str) -> bool:
        pass

    @staticmethod
    def Create(ticker: str, securityType: QuantConnect.SecurityType, market: str, alias: str, baseDataType: type) -> QuantConnect.Symbol:
        pass

    @staticmethod
    def CreateBase(baseType: type, underlying: QuantConnect.Symbol, market: str) -> QuantConnect.Symbol:
        pass

    @staticmethod
    def CreateFuture(ticker: str, market: str, expiry: datetime.datetime, alias: str) -> QuantConnect.Symbol:
        pass

    @staticmethod
    @typing.overload
    def CreateOption(underlying: str, market: str, style: QuantConnect.OptionStyle, right: QuantConnect.OptionRight, strike: float, expiry: datetime.datetime, alias: str, mapSymbol: bool) -> QuantConnect.Symbol:
        pass

    @staticmethod
    @typing.overload
    def CreateOption(underlyingSymbol: QuantConnect.Symbol, market: str, style: QuantConnect.OptionStyle, right: QuantConnect.OptionRight, strike: float, expiry: datetime.datetime, alias: str) -> QuantConnect.Symbol:
        pass

    def CreateOption(self, *args) -> QuantConnect.Symbol:
        pass

    def EndsWith(self, value: str) -> bool:
        pass

    @typing.overload
    def Equals(self, obj: object) -> bool:
        pass

    @typing.overload
    def Equals(self, other: QuantConnect.Symbol) -> bool:
        pass

    def Equals(self, *args) -> bool:
        pass

    def GetHashCode(self) -> int:
        pass

    def HasUnderlyingSymbol(self, symbol: QuantConnect.Symbol) -> bool:
        pass

    def IsCanonical(self) -> bool:
        pass

    def StartsWith(self, value: str) -> bool:
        pass

    def ToLower(self) -> str:
        pass

    def ToString(self) -> str:
        pass

    def ToUpper(self) -> str:
        pass

    def UpdateMappedSymbol(self, mappedSymbol: str) -> QuantConnect.Symbol:
        pass

    @staticmethod # known case of __new__
    def __new__(self, sid: QuantConnect.SecurityIdentifier, value: str) -> None:
        pass

    HasUnderlying: bool

    ID: QuantConnect.SecurityIdentifier

    SecurityType: QuantConnect.SecurityType

    Underlying: QuantConnect.Symbol

    Value: str


    Empty: Symbol
    None: Symbol


class SymbolCache(System.object):
    """
    Provides a string->Symbol mapping to allow for user defined strings to be lifted into a Symbol
                This is mainly used via the Symbol implicit operator, but also functions that create securities
                should also call Set to add new mappings
    """
    @staticmethod
    def Clear() -> None:
        pass

    @staticmethod
    def GetSymbol(ticker: str) -> QuantConnect.Symbol:
        pass

    @staticmethod
    def GetTicker(symbol: QuantConnect.Symbol) -> str:
        pass

    @staticmethod
    def Set(ticker: str, symbol: QuantConnect.Symbol) -> None:
        pass

    @staticmethod
    def TryGetSymbol(ticker: str, symbol: QuantConnect.Symbol) -> bool:
        pass

    @staticmethod
    def TryGetTicker(symbol: QuantConnect.Symbol, ticker: System.String) -> bool:
        pass

    @staticmethod
    @typing.overload
    def TryRemove(symbol: QuantConnect.Symbol) -> bool:
        pass

    @staticmethod
    @typing.overload
    def TryRemove(ticker: str) -> bool:
        pass

    def TryRemove(self, *args) -> bool:
        pass

    __all__: list


class SymbolJsonConverter(Newtonsoft.Json.JsonConverter):
    """
    Defines a Newtonsoft.Json.JsonConverter to be used when deserializing to
                the QuantConnect.Symbol class.
    
    SymbolJsonConverter()
    """
    def CanConvert(self, objectType: type) -> bool:
        pass

    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: type, existingValue: object, serializer: Newtonsoft.Json.JsonSerializer) -> object:
        pass

    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: object, serializer: Newtonsoft.Json.JsonSerializer) -> None:
        pass


class SymbolRepresentation(System.object):
    """ Public static helper class that does parsing/generation of symbol representations (options, futures) """
    @staticmethod
    def GenerateFutureTicker(underlying: str, expiration: datetime.datetime, doubleDigitsYear: bool) -> str:
        pass

    @staticmethod
    @typing.overload
    def GenerateOptionTickerOSI(symbol: QuantConnect.Symbol) -> str:
        pass

    @staticmethod
    @typing.overload
    def GenerateOptionTickerOSI(underlying: str, right: QuantConnect.OptionRight, strikePrice: float, expiration: datetime.datetime) -> str:
        pass

    def GenerateOptionTickerOSI(self, *args) -> str:
        pass

    @staticmethod
    def ParseFutureTicker(ticker: str) -> QuantConnect.FutureTickerProperties:
        pass

    @staticmethod
    def ParseOptionTickerIQFeed(ticker: str) -> QuantConnect.OptionTickerProperties:
        pass

    @staticmethod
    def ParseOptionTickerOSI(ticker: str) -> QuantConnect.Symbol:
        pass

    FutureTickerProperties: type
    OptionTickerProperties: type
    __all__: list


class SymbolValueJsonConverter(Newtonsoft.Json.JsonConverter):
    """
    Defines a Newtonsoft.Json.JsonConverter to be used when you only want to serialize
                the QuantConnect.Symbol.Value property instead of the full QuantConnect.Symbol
                instance
    
    SymbolValueJsonConverter()
    """
    def CanConvert(self, objectType: type) -> bool:
        pass

    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: type, existingValue: object, serializer: Newtonsoft.Json.JsonSerializer) -> object:
        pass

    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: object, serializer: Newtonsoft.Json.JsonSerializer) -> None:
        pass


class TickType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Types of tick data
    
    enum TickType, values: OpenInterest (2), Quote (1), Trade (0)
    """
    value__: int
    OpenInterest: TickType
    Quote: TickType
    Trade: TickType


class Time(System.object):
    """ Time helper class collection for working with trading dates """
    @staticmethod
    def Abs(timeSpan: datetime.timedelta) -> datetime.timedelta:
        pass

    @staticmethod
    def DateTimeToUnixTimeStamp(time: datetime.datetime) -> float:
        pass

    @staticmethod
    def EachDay(from_: datetime.datetime, thru: datetime.datetime) -> typing.List[datetime.datetime]:
        pass

    @staticmethod
    @typing.overload
    def EachTradeableDay(securities: typing.List[QuantConnect.Securities.Security], from_: datetime.datetime, thru: datetime.datetime) -> typing.List[datetime.datetime]:
        pass

    @staticmethod
    @typing.overload
    def EachTradeableDay(security: QuantConnect.Securities.Security, from_: datetime.datetime, thru: datetime.datetime) -> typing.List[datetime.datetime]:
        pass

    @staticmethod
    @typing.overload
    def EachTradeableDay(exchange: QuantConnect.Securities.SecurityExchangeHours, from_: datetime.datetime, thru: datetime.datetime) -> typing.List[datetime.datetime]:
        pass

    def EachTradeableDay(self, *args) -> typing.List[datetime.datetime]:
        pass

    @staticmethod
    def EachTradeableDayInTimeZone(exchange: QuantConnect.Securities.SecurityExchangeHours, from_: datetime.datetime, thru: datetime.datetime, timeZone: NodaTime.DateTimeZone, includeExtendedMarketHours: bool) -> typing.List[datetime.datetime]:
        pass

    @staticmethod
    def GetEndTimeForTradeBars(exchangeHours: QuantConnect.Securities.SecurityExchangeHours, start: datetime.datetime, barSize: datetime.timedelta, barCount: int, extendedMarketHours: bool) -> datetime.datetime:
        pass

    @staticmethod
    def GetNumberOfTradeBarsInInterval(exchangeHours: QuantConnect.Securities.SecurityExchangeHours, start: datetime.datetime, end: datetime.datetime, barSize: datetime.timedelta) -> int:
        pass

    @staticmethod
    def GetStartTimeForTradeBars(exchangeHours: QuantConnect.Securities.SecurityExchangeHours, end: datetime.datetime, barSize: datetime.timedelta, barCount: int, extendedMarketHours: bool) -> datetime.datetime:
        pass

    @staticmethod
    @typing.overload
    def Max(one: datetime.timedelta, two: datetime.timedelta) -> datetime.timedelta:
        pass

    @staticmethod
    @typing.overload
    def Max(one: datetime.datetime, two: datetime.datetime) -> datetime.datetime:
        pass

    def Max(self, *args) -> datetime.datetime:
        pass

    @staticmethod
    @typing.overload
    def Min(one: datetime.timedelta, two: datetime.timedelta) -> datetime.timedelta:
        pass

    @staticmethod
    @typing.overload
    def Min(one: datetime.datetime, two: datetime.datetime) -> datetime.datetime:
        pass

    def Min(self, *args) -> datetime.datetime:
        pass

    @staticmethod
    def Multiply(interval: datetime.timedelta, multiplier: float) -> datetime.timedelta:
        pass

    @staticmethod
    def NormalizeInstantWithinRange(start: datetime.datetime, current: datetime.datetime, period: datetime.timedelta) -> float:
        pass

    @staticmethod
    def NormalizeTimeStep(period: datetime.timedelta, stepSize: datetime.timedelta) -> float:
        pass

    @staticmethod
    def ParseDate(dateToParse: str) -> datetime.datetime:
        pass

    @staticmethod
    def TimeStamp() -> float:
        pass

    @staticmethod
    def TradableDate(securities: typing.List[QuantConnect.Securities.Security], day: datetime.datetime) -> bool:
        pass

    @staticmethod
    def TradeableDates(securities: typing.List[QuantConnect.Securities.Security], start: datetime.datetime, finish: datetime.datetime) -> int:
        pass

    @staticmethod
    def UnixMillisecondTimeStampToDateTime(unixTimeStamp: float) -> datetime.datetime:
        pass

    @staticmethod
    def UnixTimeStampToDateTime(unixTimeStamp: float) -> datetime.datetime:
        pass

    BeginningOfTime: DateTime
    DateTimeWithZone: type
    EndOfTime: DateTime
    EndOfTimeTimeSpan: TimeSpan
    MaxTimeSpan: TimeSpan
    OneDay: TimeSpan
    OneHour: TimeSpan
    OneMillisecond: TimeSpan
    OneMinute: TimeSpan
    OneSecond: TimeSpan
    OneYear: TimeSpan
    __all__: list


class TimeKeeper(System.object, QuantConnect.Interfaces.ITimeKeeper):
    """
    Provides a means of centralizing time for various time zones.
    
    TimeKeeper(utcDateTime: DateTime, *timeZones: Array[DateTimeZone])
    TimeKeeper(utcDateTime: DateTime, timeZones: IEnumerable[DateTimeZone])
    """
    def AddTimeZone(self, timeZone: NodaTime.DateTimeZone) -> None:
        pass

    def GetLocalTimeKeeper(self, timeZone: NodaTime.DateTimeZone) -> QuantConnect.LocalTimeKeeper:
        pass

    def GetTimeIn(self, timeZone: NodaTime.DateTimeZone) -> datetime.datetime:
        pass

    def SetUtcDateTime(self, utcDateTime: datetime.datetime) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, utcDateTime: datetime.datetime, timeZones: typing.List[NodaTime.DateTimeZone]) -> None:
        pass

    @typing.overload
    def __new__(self, utcDateTime: datetime.datetime, timeZones: typing.List[NodaTime.DateTimeZone]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    UtcTime: datetime.datetime



class TimeUpdatedEventArgs(System.EventArgs):
    """
    Event arguments class for the QuantConnect.LocalTimeKeeper.TimeUpdated event
    
    TimeUpdatedEventArgs(time: DateTime, timeZone: DateTimeZone)
    """
    @staticmethod # known case of __new__
    def __new__(self, time: datetime.datetime, timeZone: NodaTime.DateTimeZone) -> None:
        pass

    Time: datetime.datetime
    TimeZone: NodaTime.DateTimeZone

class TimeZoneOffsetProvider(System.object):
    """
    Represents the discontinuties in a single time zone and provides offsets to UTC.
                This type assumes that times will be asked in a forward marching manner.
                This type is not thread safe.
    
    TimeZoneOffsetProvider(timeZone: DateTimeZone, utcStartTime: DateTime, utcEndTime: DateTime)
    """
    def ConvertFromUtc(self, utcTime: datetime.datetime) -> datetime.datetime:
        pass

    def ConvertToUtc(self, localTime: datetime.datetime) -> datetime.datetime:
        pass

    def GetNextDiscontinuity(self) -> int:
        pass

    def GetOffsetTicks(self, utcTime: datetime.datetime) -> int:
        pass

    @staticmethod # known case of __new__
    def __new__(self, timeZone: NodaTime.DateTimeZone, utcStartTime: datetime.datetime, utcEndTime: datetime.datetime) -> None:
        pass

    TimeZone: NodaTime.DateTimeZone



class TimeZones(System.object):
    """ Provides access to common time zones """
    Amsterdam: CachedDateTimeZone
    Anchorage: CachedDateTimeZone
    Athens: CachedDateTimeZone
    Auckland: CachedDateTimeZone
    Berlin: CachedDateTimeZone
    Brisbane: CachedDateTimeZone
    Bucharest: CachedDateTimeZone
    BuenosAires: CachedDateTimeZone
    Cairo: CachedDateTimeZone
    Chicago: CachedDateTimeZone
    Denver: CachedDateTimeZone
    Detroit: CachedDateTimeZone
    Dublin: CachedDateTimeZone
    EasternStandard: FixedDateTimeZone
    Helsinki: CachedDateTimeZone
    HongKong: CachedDateTimeZone
    Honolulu: CachedDateTimeZone
    Istanbul: CachedDateTimeZone
    Jerusalem: CachedDateTimeZone
    Johannesburg: CachedDateTimeZone
    London: CachedDateTimeZone
    LosAngeles: CachedDateTimeZone
    Madrid: CachedDateTimeZone
    Melbourne: CachedDateTimeZone
    MexicoCity: CachedDateTimeZone
    Minsk: CachedDateTimeZone
    Moscow: CachedDateTimeZone
    NewYork: CachedDateTimeZone
    Paris: CachedDateTimeZone
    Phoenix: CachedDateTimeZone
    Rome: CachedDateTimeZone
    SaoPaulo: CachedDateTimeZone
    Shanghai: CachedDateTimeZone
    Sydney: CachedDateTimeZone
    Tokyo: CachedDateTimeZone
    Toronto: CachedDateTimeZone
    Utc: FixedDateTimeZone
    Vancouver: CachedDateTimeZone
    Zurich: CachedDateTimeZone
    __all__: list


class TradingCalendar(System.object):
    """
    Class represents trading calendar, populated with variety of events relevant to currently trading instruments
    
    TradingCalendar(securityManager: SecurityManager, marketHoursDatabase: MarketHoursDatabase)
    """
    def GetDaysByType(self, type: QuantConnect.TradingDayType, start: datetime.datetime, end: datetime.datetime) -> typing.List[QuantConnect.TradingDay]:
        pass

    @typing.overload
    def GetTradingDay(self) -> QuantConnect.TradingDay:
        pass

    @typing.overload
    def GetTradingDay(self, day: datetime.datetime) -> QuantConnect.TradingDay:
        pass

    def GetTradingDay(self, *args) -> QuantConnect.TradingDay:
        pass

    def GetTradingDays(self, start: datetime.datetime, end: datetime.datetime) -> typing.List[QuantConnect.TradingDay]:
        pass

    @staticmethod # known case of __new__
    def __new__(self, securityManager: QuantConnect.Securities.SecurityManager, marketHoursDatabase: QuantConnect.Securities.MarketHoursDatabase) -> None:
        pass


class TradingDay(System.object):
    """
    Class contains trading events associated with particular day in QuantConnect.TradingCalendar
    
    TradingDay()
    """
    BusinessDay: bool

    Date: datetime.datetime

    EquityDividends: typing.List[QuantConnect.Symbol]

    FutureExpirations: typing.List[QuantConnect.Symbol]

    FutureRolls: typing.List[QuantConnect.Symbol]

    OptionExpirations: typing.List[QuantConnect.Symbol]

    PublicHoliday: bool

    SymbolDelistings: typing.List[QuantConnect.Symbol]

    Weekend: bool



class TradingDayType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Enum lists available trading events
    
    enum TradingDayType, values: BusinessDay (0), EconomicEvent (8), EquityDividends (7), FutureExpiration (4), FutureRoll (5), OptionExpiration (3), PublicHoliday (1), SymbolDelisting (6), Weekend (2)
    """
    value__: int
    BusinessDay: TradingDayType
    EconomicEvent: TradingDayType
    EquityDividends: TradingDayType
    FutureExpiration: TradingDayType
    FutureRoll: TradingDayType
    OptionExpiration: TradingDayType
    PublicHoliday: TradingDayType
    SymbolDelisting: TradingDayType
    Weekend: TradingDayType


class UserPlan(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    User / Algorithm Job Subscription Level
    
    enum UserPlan, values: Free (0), Hobbyist (1), Professional (2)
    """
    value__: int
    Free: UserPlan
    Hobbyist: UserPlan
    Professional: UserPlan


class USHoliday(System.object):
    """ US Public Holidays - Not Tradeable: """
    Dates: HashSet[DateTime]
    __all__: list


# variables with complex values

