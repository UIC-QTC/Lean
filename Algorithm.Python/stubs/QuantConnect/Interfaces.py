# encoding: utf-8
# module QuantConnect.Interfaces calls itself Interfaces
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import NodaTime
import Python.Runtime
import QuantConnect
import QuantConnect.API
import QuantConnect.Api
import QuantConnect.Benchmarks
import QuantConnect.Brokerages
import QuantConnect.Data
import QuantConnect.Data.Auxiliary
import QuantConnect.Data.Market
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Notifications
import QuantConnect.Orders
import QuantConnect.Packets
import QuantConnect.Scheduling
import QuantConnect.Securities
import QuantConnect.Securities.Future
import QuantConnect.Securities.Option
import QuantConnect.Storage
import System
import System.Collections.Concurrent
import System.Collections.Generic
import System.IO
import System.Threading
import typing

# no functions
# classes

class AlgorithmEvent(System.MulticastDelegate, System.ICloneable, System.Runtime.Serialization.ISerializable):
    """ AlgorithmEvent[T](object: object, method: IntPtr) """
    def BeginInvoke(self, algorithm: QuantConnect.Interfaces.IAlgorithm, eventData: QuantConnect.Interfaces.T, callback: System.AsyncCallback, object: object) -> System.IAsyncResult:
        pass

    def EndInvoke(self, result: System.IAsyncResult) -> None:
        pass

    def Invoke(self, algorithm: QuantConnect.Interfaces.IAlgorithm, eventData: QuantConnect.Interfaces.T) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, object: object, method: System.IntPtr) -> None:
        pass


class IAccountCurrencyProvider:
    """ A reduced interface for an account currency provider """
    AccountCurrency: str



class ISecurityInitializerProvider:
    """ Reduced interface which provides an instance which implements QuantConnect.Securities.ISecurityInitializer """
    SecurityInitializer: QuantConnect.Securities.ISecurityInitializer



class IAlgorithm(QuantConnect.Interfaces.ISecurityInitializerProvider, QuantConnect.Interfaces.IAccountCurrencyProvider):
    """
    Interface for QuantConnect algorithm implementations. All algorithms must implement these
                basic members to allow interaction with the Lean Backtesting Engine.
    """
    def AddChart(self, chart: QuantConnect.Chart) -> None:
        pass

    def AddFutureContract(self, symbol: QuantConnect.Symbol, resolution: typing.Optional[QuantConnect.Resolution], fillDataForward: bool, leverage: float) -> QuantConnect.Securities.Future.Future:
        pass

    def AddOptionContract(self, symbol: QuantConnect.Symbol, resolution: typing.Optional[QuantConnect.Resolution], fillDataForward: bool, leverage: float) -> QuantConnect.Securities.Option.Option:
        pass

    def AddSecurity(self, securityType: QuantConnect.SecurityType, symbol: str, resolution: typing.Optional[QuantConnect.Resolution], market: str, fillDataForward: bool, leverage: float, extendedMarketHours: bool) -> QuantConnect.Securities.Security:
        pass

    def Debug(self, message: str) -> None:
        pass

    def Error(self, message: str) -> None:
        pass

    def GetChartUpdates(self, clearChartData: bool) -> typing.List[QuantConnect.Chart]:
        pass

    def GetLocked(self) -> bool:
        pass

    def GetParameter(self, name: str) -> str:
        pass

    def GetWarmupHistoryRequests(self) -> typing.List[QuantConnect.Data.HistoryRequest]:
        pass

    def Initialize(self) -> None:
        pass

    def Liquidate(self, symbolToLiquidate: QuantConnect.Symbol, tag: str) -> typing.List[int]:
        pass

    def Log(self, message: str) -> None:
        pass

    def OnAssignmentOrderEvent(self, assignmentEvent: QuantConnect.Orders.OrderEvent) -> None:
        pass

    def OnBrokerageDisconnect(self) -> None:
        pass

    def OnBrokerageMessage(self, messageEvent: QuantConnect.Brokerages.BrokerageMessageEvent) -> None:
        pass

    def OnBrokerageReconnect(self) -> None:
        pass

    def OnData(self, slice: QuantConnect.Data.Slice) -> None:
        pass

    def OnEndOfAlgorithm(self) -> None:
        pass

    @typing.overload
    def OnEndOfDay(self) -> None:
        pass

    @typing.overload
    def OnEndOfDay(self, symbol: QuantConnect.Symbol) -> None:
        pass

    def OnEndOfDay(self, *args) -> None:
        pass

    def OnEndOfTimeStep(self) -> None:
        pass

    def OnFrameworkData(self, slice: QuantConnect.Data.Slice) -> None:
        pass

    def OnFrameworkSecuritiesChanged(self, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        pass

    def OnMarginCall(self, requests: typing.List[QuantConnect.Orders.SubmitOrderRequest]) -> None:
        pass

    def OnMarginCallWarning(self) -> None:
        pass

    def OnOrderEvent(self, newEvent: QuantConnect.Orders.OrderEvent) -> None:
        pass

    def OnSecuritiesChanged(self, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        pass

    def OnWarmupFinished(self) -> None:
        pass

    def PostInitialize(self) -> None:
        pass

    def RemoveSecurity(self, symbol: QuantConnect.Symbol) -> bool:
        pass

    def SetAccountCurrency(self, accountCurrency: str) -> None:
        pass

    def SetAlgorithmId(self, algorithmId: str) -> None:
        pass

    def SetApi(self, api: QuantConnect.Interfaces.IApi) -> None:
        pass

    def SetAvailableDataTypes(self, availableDataTypes: System.Collections.Generic.Dictionary[QuantConnect.SecurityType, typing.List[QuantConnect.TickType]]) -> None:
        pass

    def SetBrokerageMessageHandler(self, handler: QuantConnect.Brokerages.IBrokerageMessageHandler) -> None:
        pass

    def SetBrokerageModel(self, brokerageModel: QuantConnect.Brokerages.IBrokerageModel) -> None:
        pass

    @typing.overload
    def SetCash(self, startingCash: float) -> None:
        pass

    @typing.overload
    def SetCash(self, symbol: str, startingCash: float, conversionRate: float) -> None:
        pass

    def SetCash(self, *args) -> None:
        pass

    def SetCurrentSlice(self, slice: QuantConnect.Data.Slice) -> None:
        pass

    def SetDateTime(self, time: datetime.datetime) -> None:
        pass

    def SetEndDate(self, end: datetime.datetime) -> None:
        pass

    def SetFinishedWarmingUp(self) -> None:
        pass

    def SetFutureChainProvider(self, futureChainProvider: QuantConnect.Interfaces.IFutureChainProvider) -> None:
        pass

    def SetHistoryProvider(self, historyProvider: QuantConnect.Interfaces.IHistoryProvider) -> None:
        pass

    def SetLiveMode(self, live: bool) -> None:
        pass

    def SetLocked(self) -> None:
        pass

    def SetMaximumOrders(self, max: int) -> None:
        pass

    def SetObjectStore(self, objectStore: QuantConnect.Interfaces.IObjectStore) -> None:
        pass

    def SetOptionChainProvider(self, optionChainProvider: QuantConnect.Interfaces.IOptionChainProvider) -> None:
        pass

    def SetParameters(self, parameters: System.Collections.Generic.Dictionary[str, str]) -> None:
        pass

    def SetRunTimeError(self, exception: System.Exception) -> None:
        pass

    def SetStartDate(self, start: datetime.datetime) -> None:
        pass

    def SetStatus(self, status: QuantConnect.AlgorithmStatus) -> None:
        pass

    AlgorithmId: str

    Benchmark: QuantConnect.Benchmarks.IBenchmark

    BrokerageMessageHandler: QuantConnect.Brokerages.IBrokerageMessageHandler

    BrokerageModel: QuantConnect.Brokerages.IBrokerageModel

    CurrentSlice: QuantConnect.Data.Slice

    DebugMessages: System.Collections.Concurrent.ConcurrentQueue[str]

    EndDate: datetime.datetime

    ErrorMessages: System.Collections.Concurrent.ConcurrentQueue[str]

    FutureChainProvider: QuantConnect.Interfaces.IFutureChainProvider

    HistoryProvider: QuantConnect.Interfaces.IHistoryProvider

    IsWarmingUp: bool

    LiveMode: bool

    LogMessages: System.Collections.Concurrent.ConcurrentQueue[str]

    Name: str

    Notify: QuantConnect.Notifications.NotificationManager

    ObjectStore: QuantConnect.Storage.ObjectStore

    OptionChainProvider: QuantConnect.Interfaces.IOptionChainProvider

    Portfolio: QuantConnect.Securities.SecurityPortfolioManager

    RunTimeError: System.Exception

    RuntimeStatistics: System.Collections.Concurrent.ConcurrentDictionary[str, str]

    Schedule: QuantConnect.Scheduling.ScheduleManager

    Securities: QuantConnect.Securities.SecurityManager

    Settings: QuantConnect.Interfaces.IAlgorithmSettings

    StartDate: datetime.datetime

    Status: QuantConnect.AlgorithmStatus

    SubscriptionManager: QuantConnect.Data.SubscriptionManager

    Time: datetime.datetime

    TimeKeeper: QuantConnect.Interfaces.ITimeKeeper

    TimeZone: NodaTime.DateTimeZone

    TradeBuilder: QuantConnect.Interfaces.ITradeBuilder

    Transactions: QuantConnect.Securities.SecurityTransactionManager

    UniverseManager: QuantConnect.Securities.UniverseManager

    UniverseSettings: QuantConnect.Data.UniverseSelection.UniverseSettings

    UtcTime: datetime.datetime


    InsightsGenerated: BoundEvent


class IAlgorithmSettings:
    """ User settings for the algorithm which can be changed in the QuantConnect.Interfaces.IAlgorithm.Initialize method """
    DataSubscriptionLimit: int

    FreePortfolioValue: float

    FreePortfolioValuePercentage: float

    LiquidateEnabled: bool

    MaxAbsolutePortfolioTargetPercentage: float

    MinAbsolutePortfolioTargetPercentage: float

    RebalancePortfolioOnInsightChanges: typing.Optional[bool]

    RebalancePortfolioOnSecurityChanges: typing.Optional[bool]

    StalePriceTimeSpan: datetime.timedelta



class ISubscriptionDataConfigProvider:
    """ Reduced interface which provides access to registered QuantConnect.Data.SubscriptionDataConfig """
    def GetSubscriptionDataConfigs(self, symbol: QuantConnect.Symbol, includeInternalConfigs: bool) -> typing.List[QuantConnect.Data.SubscriptionDataConfig]:
        pass


class ISubscriptionDataConfigService(QuantConnect.Interfaces.ISubscriptionDataConfigProvider):
    """
    This interface exposes methods for creating a list of QuantConnect.Data.SubscriptionDataConfig for a given
                configuration
    """
    @typing.overload
    def Add(self, dataType: type, symbol: QuantConnect.Symbol, resolution: typing.Optional[QuantConnect.Resolution], fillForward: bool, extendedMarketHours: bool, isFilteredSubscription: bool, isInternalFeed: bool, isCustomData: bool, dataNormalizationMode: QuantConnect.DataNormalizationMode) -> QuantConnect.Data.SubscriptionDataConfig:
        pass

    @typing.overload
    def Add(self, symbol: QuantConnect.Symbol, resolution: typing.Optional[QuantConnect.Resolution], fillForward: bool, extendedMarketHours: bool, isFilteredSubscription: bool, isInternalFeed: bool, isCustomData: bool, subscriptionDataTypes: typing.List[System.Tuple[type, QuantConnect.TickType]], dataNormalizationMode: QuantConnect.DataNormalizationMode) -> typing.List[QuantConnect.Data.SubscriptionDataConfig]:
        pass

    def Add(self, *args) -> typing.List[QuantConnect.Data.SubscriptionDataConfig]:
        pass

    def LookupSubscriptionConfigDataTypes(self, symbolSecurityType: QuantConnect.SecurityType, resolution: QuantConnect.Resolution, isCanonical: bool) -> typing.List[System.Tuple[type, QuantConnect.TickType]]:
        pass

    AvailableDataTypes: System.Collections.Generic.Dictionary[QuantConnect.SecurityType, typing.List[QuantConnect.TickType]]



class IAlgorithmSubscriptionManager(QuantConnect.Interfaces.ISubscriptionDataConfigService, QuantConnect.Interfaces.ISubscriptionDataConfigProvider):
    """ AlgorithmSubscriptionManager interface will manage the subscriptions for the SubscriptionManager """
    def SubscriptionManagerCount(self) -> int:
        pass

    SubscriptionManagerSubscriptions: typing.List[QuantConnect.Data.SubscriptionDataConfig]



class IApi(System.IDisposable):
    """ API for QuantConnect.com """
    def AddProjectFile(self, projectId: int, name: str, content: str) -> QuantConnect.Api.ProjectFilesResponse:
        pass

    def CreateBacktest(self, projectId: int, compileId: str, backtestName: str) -> QuantConnect.Api.Backtest:
        pass

    def CreateCompile(self, projectId: int) -> QuantConnect.Api.Compile:
        pass

    def CreateLiveAlgorithm(self, projectId: int, compileId: str, serverType: str, baseLiveAlgorithmSettings: QuantConnect.API.BaseLiveAlgorithmSettings, versionId: str) -> QuantConnect.API.LiveAlgorithm:
        pass

    def CreateProject(self, name: str, language: QuantConnect.Language) -> QuantConnect.Api.ProjectResponse:
        pass

    def DeleteBacktest(self, projectId: int, backtestId: str) -> QuantConnect.Api.RestResponse:
        pass

    def DeleteProject(self, projectId: int) -> QuantConnect.Api.RestResponse:
        pass

    def DeleteProjectFile(self, projectId: int, name: str) -> QuantConnect.Api.RestResponse:
        pass

    def Download(self, address: str, headers: typing.List[System.Collections.Generic.KeyValuePair[str, str]], userName: str, password: str) -> str:
        pass

    def DownloadData(self, symbol: QuantConnect.Symbol, resolution: QuantConnect.Resolution, date: datetime.datetime) -> bool:
        pass

    def GetAlgorithmStatus(self, algorithmId: str) -> QuantConnect.AlgorithmControl:
        pass

    def GetDividends(self, from_: datetime.datetime, to: datetime.datetime) -> typing.List[QuantConnect.Data.Market.Dividend]:
        pass

    def GetSplits(self, from_: datetime.datetime, to: datetime.datetime) -> typing.List[QuantConnect.Data.Market.Split]:
        pass

    def Initialize(self, userId: int, token: str, dataFolder: str) -> None:
        pass

    def LiquidateLiveAlgorithm(self, projectId: int) -> QuantConnect.Api.RestResponse:
        pass

    def ListBacktests(self, projectId: int) -> QuantConnect.Api.BacktestList:
        pass

    def ListLiveAlgorithms(self, status: typing.Optional[QuantConnect.AlgorithmStatus], startTime: typing.Optional[datetime.datetime], endTime: typing.Optional[datetime.datetime]) -> QuantConnect.API.LiveList:
        pass

    def ListProjects(self) -> QuantConnect.Api.ProjectResponse:
        pass

    def ReadBacktest(self, projectId: int, backtestId: str) -> QuantConnect.Api.Backtest:
        pass

    def ReadCompile(self, projectId: int, compileId: str) -> QuantConnect.Api.Compile:
        pass

    def ReadDataLink(self, symbol: QuantConnect.Symbol, resolution: QuantConnect.Resolution, date: datetime.datetime) -> QuantConnect.Api.Link:
        pass

    def ReadLiveAlgorithm(self, projectId: int, deployId: str) -> QuantConnect.API.LiveAlgorithmResults:
        pass

    def ReadLiveLogs(self, projectId: int, algorithmId: str, startTime: typing.Optional[datetime.datetime], endTime: typing.Optional[datetime.datetime]) -> QuantConnect.API.LiveLog:
        pass

    def ReadPrices(self, symbols: typing.List[QuantConnect.Symbol]) -> QuantConnect.API.PricesList:
        pass

    def ReadProject(self, projectId: int) -> QuantConnect.Api.ProjectResponse:
        pass

    def ReadProjectFile(self, projectId: int, fileName: str) -> QuantConnect.Api.ProjectFilesResponse:
        pass

    def ReadProjectFiles(self, projectId: int) -> QuantConnect.Api.ProjectFilesResponse:
        pass

    def SendStatistics(self, algorithmId: str, unrealized: float, fees: float, netProfit: float, holdings: float, equity: float, netReturn: float, volume: float, trades: int, sharpe: float) -> None:
        pass

    def SendUserEmail(self, algorithmId: str, subject: str, body: str) -> None:
        pass

    def SetAlgorithmStatus(self, algorithmId: str, status: QuantConnect.AlgorithmStatus, message: str) -> None:
        pass

    def StopLiveAlgorithm(self, projectId: int) -> QuantConnect.Api.RestResponse:
        pass

    def UpdateBacktest(self, projectId: int, backtestId: str, backtestName: str, backtestNote: str) -> QuantConnect.Api.RestResponse:
        pass

    def UpdateProjectFileContent(self, projectId: int, fileName: str, newFileContents: str) -> QuantConnect.Api.RestResponse:
        pass

    def UpdateProjectFileName(self, projectId: int, oldFileName: str, newFileName: str) -> QuantConnect.Api.RestResponse:
        pass


class IBrokerageCashSynchronizer:
    """ Defines live brokerage cash synchronization operations. """
    def PerformCashSync(self, algorithm: QuantConnect.Interfaces.IAlgorithm, currentTimeUtc: datetime.datetime, getTimeSinceLastFill: typing.Callable[[], datetime.timedelta]) -> bool:
        pass

    def ShouldPerformCashSync(self, currentTimeUtc: datetime.datetime) -> bool:
        pass

    LastSyncDateTimeUtc: datetime.datetime



class IBrokerage(QuantConnect.Interfaces.IBrokerageCashSynchronizer, System.IDisposable):
    """
    Brokerage interface that defines the operations all brokerages must implement. The IBrokerage implementation
                must have a matching IBrokerageFactory implementation.
    """
    def CancelOrder(self, order: QuantConnect.Orders.Order) -> bool:
        pass

    def Connect(self) -> None:
        pass

    def Disconnect(self) -> None:
        pass

    def GetAccountHoldings(self) -> typing.List[QuantConnect.Holding]:
        pass

    def GetCashBalance(self) -> typing.List[QuantConnect.Securities.CashAmount]:
        pass

    def GetHistory(self, request: QuantConnect.Data.HistoryRequest) -> typing.List[QuantConnect.Data.BaseData]:
        pass

    def GetOpenOrders(self) -> typing.List[QuantConnect.Orders.Order]:
        pass

    def PlaceOrder(self, order: QuantConnect.Orders.Order) -> bool:
        pass

    def UpdateOrder(self, order: QuantConnect.Orders.Order) -> bool:
        pass

    AccountInstantlyUpdated: bool

    IsConnected: bool

    Name: str


    AccountChanged: BoundEvent
    Message: BoundEvent
    OptionPositionAssigned: BoundEvent
    OrderStatusChanged: BoundEvent


class IBrokerageFactory(System.IDisposable):
    """ Defines factory types for brokerages. Every IBrokerage is expected to also implement an IBrokerageFactory. """
    def CreateBrokerage(self, job: QuantConnect.Packets.LiveNodePacket, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Interfaces.IBrokerage:
        pass

    def CreateBrokerageMessageHandler(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, api: QuantConnect.Interfaces.IApi) -> QuantConnect.Brokerages.IBrokerageMessageHandler:
        pass

    def GetBrokerageModel(self, orderProvider: QuantConnect.Securities.IOrderProvider) -> QuantConnect.Brokerages.IBrokerageModel:
        pass

    BrokerageData: System.Collections.Generic.Dictionary[str, str]

    BrokerageType: type



class IBusyCollection(System.IDisposable):
    # no doc
    @typing.overload
    def Add(self, item: QuantConnect.Interfaces.T) -> None:
        pass

    @typing.overload
    def Add(self, item: QuantConnect.Interfaces.T, cancellationToken: System.Threading.CancellationToken) -> None:
        pass

    def Add(self, *args) -> None:
        pass

    def CompleteAdding(self) -> None:
        pass

    @typing.overload
    def GetConsumingEnumerable(self) -> typing.List[QuantConnect.Interfaces.T]:
        pass

    @typing.overload
    def GetConsumingEnumerable(self, cancellationToken: System.Threading.CancellationToken) -> typing.List[QuantConnect.Interfaces.T]:
        pass

    def GetConsumingEnumerable(self, *args) -> typing.List[QuantConnect.Interfaces.T]:
        pass

    Count: int

    IsBusy: bool

    WaitHandle: System.Threading.WaitHandle



class IDataCacheProvider(System.IDisposable):
    """ Defines a cache for data """
    def Fetch(self, key: str) -> System.IO.Stream:
        pass

    def Store(self, key: str, data: typing.List[bytes]) -> None:
        pass

    IsDataEphemeral: bool



class IDataChannelProvider:
    """ Specifies data channel settings """
    def ShouldStreamSubscription(self, job: QuantConnect.Packets.LiveNodePacket, config: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        pass


class IDataPermissionManager:
    """ Entity in charge of handling data permissions """
    def AssertConfiguration(self, subscriptionDataConfig: QuantConnect.Data.SubscriptionDataConfig) -> None:
        pass

    def GetResolution(self, preferredResolution: QuantConnect.Resolution) -> QuantConnect.Resolution:
        pass

    def Initialize(self, job: QuantConnect.Packets.AlgorithmNodePacket) -> None:
        pass

    DataChannelProvider: QuantConnect.Interfaces.IDataChannelProvider



class IDataProvider:
    """
    Fetches a remote file for a security.
                Must save the file to Globals.DataFolder.
    """
    def Fetch(self, key: str) -> System.IO.Stream:
        pass


class IDataProviderEvents:
    """ Events related to data providers """
    DownloadFailed: BoundEvent
    InvalidConfigurationDetected: BoundEvent
    NumericalPrecisionLimited: BoundEvent
    ReaderErrorDetected: BoundEvent
    StartDateLimited: BoundEvent


class IDataQueueHandler(System.IDisposable):
    """ Task requestor interface with cloud system """
    def GetNextTicks(self) -> typing.List[QuantConnect.Data.BaseData]:
        pass

    def Subscribe(self, job: QuantConnect.Packets.LiveNodePacket, symbols: typing.List[QuantConnect.Symbol]) -> None:
        pass

    def Unsubscribe(self, job: QuantConnect.Packets.LiveNodePacket, symbols: typing.List[QuantConnect.Symbol]) -> None:
        pass

    IsConnected: bool



class IDataQueueUniverseProvider:
    """
    This interface allows interested parties to lookup or enumerate the available symbols. Data source exposes it if this feature is available.
                Availability of a symbol doesn't imply that it is possible to trade it. This is a data source specific interface, not broker specific.
    """
    def CanAdvanceTime(self, securityType: QuantConnect.SecurityType) -> bool:
        pass

    def LookupSymbols(self, lookupName: str, securityType: QuantConnect.SecurityType, includeExpired: bool, securityCurrency: str, securityExchange: str) -> typing.List[QuantConnect.Symbol]:
        pass


class IDownloadProvider:
    """ Wrapper on the API for downloading data for an algorithm. """
    def Download(self, address: str, headers: typing.List[System.Collections.Generic.KeyValuePair[str, str]], userName: str, password: str) -> str:
        pass


class IExtendedDictionary:
    # no doc
    def clear(self) -> None:
        pass

    def copy(self) -> Python.Runtime.PyDict:
        pass

    @typing.overload
    def fromkeys(self, sequence: typing.List[QuantConnect.Interfaces.TKey]) -> Python.Runtime.PyDict:
        pass

    @typing.overload
    def fromkeys(self, sequence: typing.List[QuantConnect.Interfaces.TKey], value: QuantConnect.Interfaces.TValue) -> Python.Runtime.PyDict:
        pass

    def fromkeys(self, *args) -> Python.Runtime.PyDict:
        pass

    @typing.overload
    def get(self, key: QuantConnect.Interfaces.TKey) -> QuantConnect.Interfaces.TValue:
        pass

    @typing.overload
    def get(self, key: QuantConnect.Interfaces.TKey, value: QuantConnect.Interfaces.TValue) -> QuantConnect.Interfaces.TValue:
        pass

    def get(self, *args) -> QuantConnect.Interfaces.TValue:
        pass

    def items(self) -> Python.Runtime.PyList:
        pass

    def keys(self) -> Python.Runtime.PyList:
        pass

    @typing.overload
    def pop(self, key: QuantConnect.Interfaces.TKey) -> QuantConnect.Interfaces.TValue:
        pass

    @typing.overload
    def pop(self, key: QuantConnect.Interfaces.TKey, default_value: QuantConnect.Interfaces.TValue) -> QuantConnect.Interfaces.TValue:
        pass

    def pop(self, *args) -> QuantConnect.Interfaces.TValue:
        pass

    def popitem(self) -> Python.Runtime.PyTuple:
        pass

    @typing.overload
    def setdefault(self, key: QuantConnect.Interfaces.TKey) -> QuantConnect.Interfaces.TValue:
        pass

    @typing.overload
    def setdefault(self, key: QuantConnect.Interfaces.TKey, default_value: QuantConnect.Interfaces.TValue) -> QuantConnect.Interfaces.TValue:
        pass

    def setdefault(self, *args) -> QuantConnect.Interfaces.TValue:
        pass

    def update(self, other: Python.Runtime.PyObject) -> None:
        pass

    def values(self) -> Python.Runtime.PyList:
        pass


class IFactorFileProvider:
    """ Provides instances of QuantConnect.Data.Auxiliary.FactorFile at run time """
    def Get(self, symbol: QuantConnect.Symbol) -> QuantConnect.Data.Auxiliary.FactorFile:
        pass


class IFutureChainProvider:
    """ Provides the full future chain for a given underlying. """
    def GetFutureContractList(self, symbol: QuantConnect.Symbol, date: datetime.datetime) -> typing.List[QuantConnect.Symbol]:
        pass


class IHistoryProvider(QuantConnect.Interfaces.IDataProviderEvents):
    """ Provides historical data to an algorithm at runtime """
    def GetHistory(self, requests: typing.List[QuantConnect.Data.HistoryRequest], sliceTimeZone: NodaTime.DateTimeZone) -> typing.List[QuantConnect.Data.Slice]:
        pass

    def Initialize(self, parameters: QuantConnect.Data.HistoryProviderInitializeParameters) -> None:
        pass

    DataPointCount: int



class IJobQueueHandler:
    """ Task requestor interface with cloud system """
    def AcknowledgeJob(self, job: QuantConnect.Packets.AlgorithmNodePacket) -> None:
        pass

    def Initialize(self, api: QuantConnect.Interfaces.IApi) -> None:
        pass

    def NextJob(self, algorithmPath: System.String) -> QuantConnect.Packets.AlgorithmNodePacket:
        pass


class IMapFileProvider:
    """ Provides instances of QuantConnect.Data.Auxiliary.MapFileResolver at run time """
    def Get(self, market: str) -> QuantConnect.Data.Auxiliary.MapFileResolver:
        pass


class IMessagingHandler(System.IDisposable):
    """
    Messaging System Plugin Interface. 
                Provides a common messaging pattern between desktop and cloud implementations of QuantConnect.
    """
    def Initialize(self) -> None:
        pass

    def Send(self, packet: QuantConnect.Packets.Packet) -> None:
        pass

    def SendNotification(self, notification: QuantConnect.Notifications.Notification) -> None:
        pass

    def SetAuthentication(self, job: QuantConnect.Packets.AlgorithmNodePacket) -> None:
        pass

    HasSubscribers: bool



class IObjectStore(System.IDisposable, System.Collections.Generic.IEnumerable[KeyValuePair[str, Array[Byte]]], System.Collections.IEnumerable):
    """ Provides object storage for data persistence. """
    def ContainsKey(self, key: str) -> bool:
        pass

    def Delete(self, key: str) -> bool:
        pass

    def GetFilePath(self, key: str) -> str:
        pass

    def Initialize(self, algorithmName: str, userId: int, projectId: int, userToken: str, controls: QuantConnect.Packets.Controls) -> None:
        pass

    def ReadBytes(self, key: str) -> typing.List[bytes]:
        pass

    def SaveBytes(self, key: str, contents: typing.List[bytes]) -> bool:
        pass

    ErrorRaised: BoundEvent


class IOptionChainProvider:
    """ Provides the full option chain for a given underlying. """
    def GetOptionContractList(self, symbol: QuantConnect.Symbol, date: datetime.datetime) -> typing.List[QuantConnect.Symbol]:
        pass


class ISecurityPrice:
    """
    Reduced interface which allows setting and accessing
                price properties for a QuantConnect.Securities.Security
    """
    def GetLastData(self) -> QuantConnect.Data.BaseData:
        pass

    def SetMarketPrice(self, data: QuantConnect.Data.BaseData) -> None:
        pass

    def Update(self, data: typing.List[QuantConnect.Data.BaseData], dataType: type, containsFillForwardData: typing.Optional[bool]) -> None:
        pass

    AskPrice: float

    AskSize: float

    BidPrice: float

    BidSize: float

    Close: float

    OpenInterest: int

    Price: float

    Symbol: QuantConnect.Symbol

    Volume: float



class IOptionPrice(QuantConnect.Interfaces.ISecurityPrice):
    """
    Reduced interface for accessing QuantConnect.Securities.Option.Option
                specific price properties and methods
    """
    def EvaluatePriceModel(self, slice: QuantConnect.Data.Slice, contract: QuantConnect.Data.Market.OptionContract) -> QuantConnect.Securities.Option.OptionPriceModelResult:
        pass

    Underlying: QuantConnect.Interfaces.ISecurityPrice



class IOrderProperties:
    """ Contains additional properties and settings for an order """
    def Clone(self) -> QuantConnect.Interfaces.IOrderProperties:
        pass

    TimeInForce: QuantConnect.Orders.TimeInForce



class IPriceProvider:
    """ Provides access to price data for a given asset """
    def GetLastPrice(self, symbol: QuantConnect.Symbol) -> float:
        pass


class IRegressionAlgorithmDefinition:
    """
    Defines a C# algorithm as a regression algorithm to be run as part of the test suite.
                This interface also allows the algorithm to declare that it has versions in other languages
                that should yield identical results.
    """
    CanRunLocally: bool

    ExpectedStatistics: System.Collections.Generic.Dictionary[str, str]

    Languages: typing.List[QuantConnect.Language]



class ISecurityService:
    """ This interface exposes methods for creating a new QuantConnect.Securities.Security """
    @typing.overload
    def CreateSecurity(self, symbol: QuantConnect.Symbol, subscriptionDataConfigList: typing.List[QuantConnect.Data.SubscriptionDataConfig], leverage: float, addToSymbolCache: bool) -> QuantConnect.Securities.Security:
        pass

    @typing.overload
    def CreateSecurity(self, symbol: QuantConnect.Symbol, subscriptionDataConfig: QuantConnect.Data.SubscriptionDataConfig, leverage: float, addToSymbolCache: bool) -> QuantConnect.Securities.Security:
        pass

    def CreateSecurity(self, *args) -> QuantConnect.Securities.Security:
        pass


class IStreamReader(System.IDisposable):
    """ Defines a transport mechanism for data from its source into various reader methods """
    def ReadLine(self) -> str:
        pass

    EndOfStream: bool

    ShouldBeRateLimited: bool

    StreamReader: System.IO.StreamReader

    TransportMedium: QuantConnect.SubscriptionTransportMedium



class ITimeInForceHandler:
    """ Handles the time in force for an order """
    def IsFillValid(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, fill: QuantConnect.Orders.OrderEvent) -> bool:
        pass

    def IsOrderExpired(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> bool:
        pass


class ITimeKeeper:
    """ Interface implemented by QuantConnect.TimeKeeper """
    def AddTimeZone(self, timeZone: NodaTime.DateTimeZone) -> None:
        pass

    def GetLocalTimeKeeper(self, timeZone: NodaTime.DateTimeZone) -> QuantConnect.LocalTimeKeeper:
        pass

    UtcTime: datetime.datetime



class ITradeBuilder:
    """ Generates trades from executions and market price updates """
    def HasOpenPosition(self, symbol: QuantConnect.Symbol) -> bool:
        pass

    def ProcessFill(self, fill: QuantConnect.Orders.OrderEvent, securityConversionRate: float, feeInAccountCurrency: float, multiplier: float) -> None:
        pass

    def SetLiveMode(self, live: bool) -> None:
        pass

    def SetMarketPrice(self, symbol: QuantConnect.Symbol, price: float) -> None:
        pass

    ClosedTrades: typing.List[QuantConnect.Statistics.Trade]



class ObjectStoreErrorRaisedEventArgs(System.EventArgs):
    """
    Event arguments for the QuantConnect.Interfaces.IObjectStore.ErrorRaised event
    
    ObjectStoreErrorRaisedEventArgs(error: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, error: System.Exception) -> None:
        pass

    Error: System.Exception



