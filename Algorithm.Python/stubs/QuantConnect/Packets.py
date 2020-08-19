# encoding: utf-8
# module QuantConnect.Packets calls itself Packets
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import QuantConnect
import QuantConnect.Orders
import QuantConnect.Packets
import QuantConnect.Securities
import QuantConnect.Statistics
import System
import System.Collections.Generic
import System.IO
import typing

# no functions
# classes

class Packet(System.object):
    """
    Base class for packet messaging system
    
    Packet(type: PacketType)
    """
    @staticmethod # known case of __new__
    def __new__(self, type: QuantConnect.Packets.PacketType) -> None:
        pass

    Channel: str

    Type: QuantConnect.Packets.PacketType



class AlgorithmNodePacket(QuantConnect.Packets.Packet):
    """
    Algorithm Node Packet is a work task for the Lean Engine
    
    AlgorithmNodePacket(type: PacketType)
    """
    def GetAlgorithmName(self) -> str:
        pass

    @staticmethod # known case of __new__
    def __new__(self, type: QuantConnect.Packets.PacketType) -> None:
        pass

    AlgorithmId: str

    RamAllocation: int

    Algorithm: typing.List[bytes]
    CompileId: str
    Controls: QuantConnect.Packets.Controls
    HistoryProvider: str
    Language: QuantConnect.Language
    Parameters: System.Collections.Generic.Dictionary[str, str]
    ProjectId: int
    Redelivered: bool
    RequestSource: str
    ServerType: QuantConnect.ServerType
    SessionId: str
    UserId: int
    UserPlan: QuantConnect.UserPlan
    UserToken: str
    Version: str


class AlgorithmStatusPacket(QuantConnect.Packets.Packet):
    """
    Algorithm status update information packet
    
    AlgorithmStatusPacket()
    AlgorithmStatusPacket(algorithmId: str, projectId: int, status: AlgorithmStatus, message: str)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, algorithmId: str, projectId: int, status: QuantConnect.AlgorithmStatus, message: str) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    AlgorithmId: str
    ChannelStatus: str
    ChartSubscription: str
    Message: str
    ProjectId: int
    Status: QuantConnect.AlgorithmStatus

class LiveNodePacket(QuantConnect.Packets.AlgorithmNodePacket):
    """
    Live job task packet: container for any live specific job variables
    
    LiveNodePacket()
    """
    Brokerage: str
    BrokerageData: System.Collections.Generic.Dictionary[str, str]
    DataChannelProvider: str
    DataQueueHandler: str
    DeployId: str
    DisableAcknowledgement: bool

class AlphaNodePacket(QuantConnect.Packets.LiveNodePacket):
    """
    Alpha job packet
    
    AlphaNodePacket()
    """
    AlphaId: str



class AlphaResultPacket(QuantConnect.Packets.Packet):
    """
    Provides a packet type for transmitting alpha insights data
    
    AlphaResultPacket()
    AlphaResultPacket(algorithmId: str, userId: int, insights: List[Insight], orderEvents: List[OrderEvent], orders: List[Order])
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, algorithmId: str, userId: int, insights: typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight], orderEvents: typing.List[QuantConnect.Orders.OrderEvent], orders: typing.List[QuantConnect.Orders.Order]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    AlgorithmId: str

    AlphaId: str

    Insights: typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight]

    OrderEvents: typing.List[QuantConnect.Orders.OrderEvent]

    Orders: typing.List[QuantConnect.Orders.Order]

    UserId: int



class BacktestNodePacket(QuantConnect.Packets.AlgorithmNodePacket):
    """
    Algorithm backtest task information packet.
    
    BacktestNodePacket()
    BacktestNodePacket(userId: int, projectId: int, sessionId: str, algorithmData: Array[Byte], startingCapital: Decimal, name: str, userPlan: UserPlan)
    BacktestNodePacket(userId: int, projectId: int, sessionId: str, algorithmData: Array[Byte], name: str, userPlan: UserPlan, startingCapital: Nullable[CashAmount])
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, userId: int, projectId: int, sessionId: str, algorithmData: typing.List[bytes], startingCapital: float, name: str, userPlan: QuantConnect.UserPlan) -> None:
        pass

    @typing.overload
    def __new__(self, userId: int, projectId: int, sessionId: str, algorithmData: typing.List[bytes], name: str, userPlan: QuantConnect.UserPlan, startingCapital: typing.Optional[QuantConnect.Securities.CashAmount]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsDebugging: bool

    BacktestId: str
    Breakpoints: typing.List[QuantConnect.Packets.Breakpoint]
    CashAmount: typing.Optional[QuantConnect.Securities.CashAmount]
    Name: str
    PeriodFinish: typing.Optional[datetime.datetime]
    PeriodStart: typing.Optional[datetime.datetime]
    TradeableDates: int
    Watchlist: typing.List[str]


class BacktestResult(QuantConnect.Result):
    """
    Backtest results object class - result specific items from the packet.
    
    BacktestResult()
    BacktestResult(parameters: BacktestResultParameters)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, parameters: QuantConnect.Packets.BacktestResultParameters) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    RollingWindow: System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]
    TotalPerformance: QuantConnect.Statistics.AlgorithmPerformance

class BacktestResultPacket(QuantConnect.Packets.Packet):
    """
    Backtest result packet: send backtest information to GUI for user consumption.
    
    BacktestResultPacket()
    BacktestResultPacket(json: str)
    BacktestResultPacket(job: BacktestNodePacket, results: BacktestResult, endDate: DateTime, startDate: DateTime, progress: Decimal)
    """
    @staticmethod
    def CreateEmpty(job: QuantConnect.Packets.BacktestNodePacket) -> QuantConnect.Packets.BacktestResultPacket:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, json: str) -> None:
        pass

    @typing.overload
    def __new__(self, job: QuantConnect.Packets.BacktestNodePacket, results: QuantConnect.Packets.BacktestResult, endDate: datetime.datetime, startDate: datetime.datetime, progress: float) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    BacktestId: str
    CompileId: str
    DateFinished: datetime.datetime
    DateRequested: datetime.datetime
    Name: str
    PeriodFinish: datetime.datetime
    PeriodStart: datetime.datetime
    ProcessingTime: float
    Progress: float
    ProjectId: int
    Results: QuantConnect.Packets.BacktestResult
    SessionId: str
    TradeableDates: int
    UserId: int

class BaseResultParameters(System.object):
    """
    Base parameters used by QuantConnect.Packets.LiveResultParameters and QuantConnect.Packets.BacktestResultParameters
    
    BaseResultParameters()
    """
    AlphaRuntimeStatistics: QuantConnect.AlphaRuntimeStatistics

    Charts: System.Collections.Generic.IDictionary[str, QuantConnect.Chart]

    OrderEvents: typing.List[QuantConnect.Orders.OrderEvent]

    Orders: System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order]

    ProfitLoss: System.Collections.Generic.IDictionary[datetime.datetime, float]

    RuntimeStatistics: System.Collections.Generic.IDictionary[str, str]

    Statistics: System.Collections.Generic.IDictionary[str, str]



class BacktestResultParameters(QuantConnect.Packets.BaseResultParameters):
    """
    Defines the parameters for QuantConnect.Packets.BacktestResult
    
    BacktestResultParameters(charts: IDictionary[str, Chart], orders: IDictionary[int, Order], profitLoss: IDictionary[DateTime, Decimal], statistics: IDictionary[str, str], runtimeStatistics: IDictionary[str, str], rollingWindow: Dictionary[str, AlgorithmPerformance], orderEvents: List[OrderEvent], totalPerformance: AlgorithmPerformance, alphaRuntimeStatistics: AlphaRuntimeStatistics)
    """
    @staticmethod # known case of __new__
    def __new__(self, charts: System.Collections.Generic.IDictionary[str, QuantConnect.Chart], orders: System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order], profitLoss: System.Collections.Generic.IDictionary[datetime.datetime, float], statistics: System.Collections.Generic.IDictionary[str, str], runtimeStatistics: System.Collections.Generic.IDictionary[str, str], rollingWindow: System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance], orderEvents: typing.List[QuantConnect.Orders.OrderEvent], totalPerformance: QuantConnect.Statistics.AlgorithmPerformance, alphaRuntimeStatistics: QuantConnect.AlphaRuntimeStatistics) -> None:
        pass

    RollingWindow: System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]

    TotalPerformance: QuantConnect.Statistics.AlgorithmPerformance



class Breakpoint(System.object):
    """
    A debugging breakpoint
    
    Breakpoint()
    """
    FileName: str

    LineNumber: int



class HistoryResult(System.object):
    """
    Provides a container for results from history requests. This contains
                the file path relative to the /Data folder where the data can be written
    """
    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        pass

    Type: QuantConnect.Packets.HistoryResultType



class CompletedHistoryResult(QuantConnect.Packets.HistoryResult):
    """
    Specifies the completed message from a history result
    
    CompletedHistoryResult()
    """

class Controls(System.object):
    """
    Specifies values used to control algorithm limits
    
    Controls()
    """
    def GetLimit(self, resolution: QuantConnect.Resolution) -> int:
        pass

    BacktestingMaxOrders: int

    BacktestingMaxInsights: int
    BacktestLogLimit: int
    CpuAllocation: float
    DailyLogLimit: int
    DataResolutionPermissions: System.Collections.Generic.HashSet[QuantConnect.Resolution]
    MaximumDataPointsPerChartSeries: int
    MinuteLimit: int
    PersistenceIntervalSeconds: int
    RamAllocation: int
    RemainingLogAllowance: int
    SecondLimit: int
    SecondTimeOut: int
    StorageFileCount: int
    StorageLimitMB: int
    StoragePermissions: System.IO.FileAccess
    StreamingDataPermissions: System.Collections.Generic.HashSet[str]
    TickLimit: int
    TrainingLimits: QuantConnect.Packets.LeakyBucketControlParameters


class DebugPacket(QuantConnect.Packets.Packet):
    """
    Send a simple debug message from the users algorithm to the console.
    
    DebugPacket()
    DebugPacket(projectId: int, algorithmId: str, compileId: str, message: str, toast: bool)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, projectId: int, algorithmId: str, compileId: str, message: str, toast: bool) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    AlgorithmId: str
    CompileId: str
    Message: str
    ProjectId: int
    Toast: bool

class ErrorHistoryResult(QuantConnect.Packets.HistoryResult):
    """
    Specfies an error message in a history result
    
    ErrorHistoryResult()
    ErrorHistoryResult(message: str)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, message: str) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Message: str

class FileHistoryResult(QuantConnect.Packets.HistoryResult):
    """
    Defines requested file data for a history request
    
    FileHistoryResult()
    FileHistoryResult(filepath: str, file: Array[Byte])
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, filepath: str, file: typing.List[bytes]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    File: typing.List[bytes]
    Filepath: str

class HandledErrorPacket(QuantConnect.Packets.Packet):
    """
    Algorithm runtime error packet from the lean engine. 
                This is a managed error which stops the algorithm execution.
    
    HandledErrorPacket()
    HandledErrorPacket(algorithmId: str, message: str, stacktrace: str)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, algorithmId: str, message: str, stacktrace: str) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    AlgorithmId: str
    Message: str
    StackTrace: str

class HistoryPacket(QuantConnect.Packets.Packet):
    """
    Packet for history jobs
    
    HistoryPacket()
    """
    QueueName: str
    Requests: typing.List[QuantConnect.Packets.HistoryRequest]

class HistoryRequest(System.object):
    """
    Specifies request parameters for a single historical request.
                A HistoryPacket is made of multiple requests for data. These
                are used to request data during live mode from a data server
    
    HistoryRequest()
    """
    EndTimeUtc: datetime.datetime
    Resolution: QuantConnect.Resolution
    StartTimeUtc: datetime.datetime
    Symbol: QuantConnect.Symbol
    TickType: QuantConnect.TickType

class HistoryResultType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Specifies various types of history results
    
    enum HistoryResultType, values: Completed (2), Error (3), File (0), Status (1)
    """
    value__: int
    Completed: HistoryResultType
    Error: HistoryResultType
    File: HistoryResultType
    Status: HistoryResultType


class LeakyBucketControlParameters(System.object):
    """
    Provides parameters that control the behavior of a leaky bucket rate limiting algorithm. The
                parameter names below are phrased in the positive, such that the bucket is filled up over time
                vs leaking out over time.
    
    LeakyBucketControlParameters()
    LeakyBucketControlParameters(capacity: int, refillAmount: int, timeIntervalMinutes: int)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, capacity: int, refillAmount: int, timeIntervalMinutes: int) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Capacity: int
    RefillAmount: int
    TimeIntervalMinutes: int
    DefaultCapacity: int
    DefaultRefillAmount: int
    DefaultTimeInterval: int


class LiveResult(QuantConnect.Result):
    """
    Live results object class for packaging live result data.
    
    LiveResult()
    LiveResult(parameters: LiveResultParameters)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, parameters: QuantConnect.Packets.LiveResultParameters) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Cash: QuantConnect.Securities.CashBook
    Holdings: System.Collections.Generic.IDictionary[str, QuantConnect.Holding]

class LiveResultPacket(QuantConnect.Packets.Packet):
    """
    Live result packet from a lean engine algorithm.
    
    LiveResultPacket()
    LiveResultPacket(json: str)
    LiveResultPacket(job: LiveNodePacket, results: LiveResult)
    """
    @staticmethod
    def CreateEmpty(job: QuantConnect.Packets.LiveNodePacket) -> QuantConnect.Packets.LiveResultPacket:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, json: str) -> None:
        pass

    @typing.overload
    def __new__(self, job: QuantConnect.Packets.LiveNodePacket, results: QuantConnect.Packets.LiveResult) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    CompileId: str
    DeployId: str
    ProcessingTime: float
    ProjectId: int
    Results: QuantConnect.Packets.LiveResult
    SessionId: str
    UserId: int

class LiveResultParameters(QuantConnect.Packets.BaseResultParameters):
    """
    Defines the parameters for QuantConnect.Packets.LiveResult
    
    LiveResultParameters(charts: IDictionary[str, Chart], orders: IDictionary[int, Order], profitLoss: IDictionary[DateTime, Decimal], holdings: IDictionary[str, Holding], cashBook: CashBook, statistics: IDictionary[str, str], runtimeStatistics: IDictionary[str, str], orderEvents: List[OrderEvent], serverStatistics: IDictionary[str, str], alphaRuntimeStatistics: AlphaRuntimeStatistics)
    """
    @staticmethod # known case of __new__
    def __new__(self, charts: System.Collections.Generic.IDictionary[str, QuantConnect.Chart], orders: System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order], profitLoss: System.Collections.Generic.IDictionary[datetime.datetime, float], holdings: System.Collections.Generic.IDictionary[str, QuantConnect.Holding], cashBook: QuantConnect.Securities.CashBook, statistics: System.Collections.Generic.IDictionary[str, str], runtimeStatistics: System.Collections.Generic.IDictionary[str, str], orderEvents: typing.List[QuantConnect.Orders.OrderEvent], serverStatistics: System.Collections.Generic.IDictionary[str, str], alphaRuntimeStatistics: QuantConnect.AlphaRuntimeStatistics) -> None:
        pass

    CashBook: QuantConnect.Securities.CashBook

    Holdings: System.Collections.Generic.IDictionary[str, QuantConnect.Holding]

    ServerStatistics: System.Collections.Generic.IDictionary[str, str]



class LogPacket(QuantConnect.Packets.Packet):
    """
    Simple log message instruction from the lean engine.
    
    LogPacket()
    LogPacket(algorithmId: str, message: str)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, algorithmId: str, message: str) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    AlgorithmId: str
    Message: str

class MarketHours(System.object):
    """
    Market open hours model for pre, normal and post market hour definitions.
    
    MarketHours(referenceDate: DateTime, defaultStart: float, defaultEnd: float)
    """
    @staticmethod # known case of __new__
    def __new__(self, referenceDate: datetime.datetime, defaultStart: float, defaultEnd: float) -> None:
        pass

    End: datetime.datetime
    Start: datetime.datetime

class MarketToday(System.object):
    """
    Market today information class
    
    MarketToday()
    """
    Date: datetime.datetime

    Open: QuantConnect.Packets.MarketHours
    PostMarket: QuantConnect.Packets.MarketHours
    PreMarket: QuantConnect.Packets.MarketHours
    Status: str


class OrderEventPacket(QuantConnect.Packets.Packet):
    """
    Order event packet for passing updates on the state of an order to the portfolio.
    
    OrderEventPacket()
    OrderEventPacket(algorithmId: str, eventOrder: OrderEvent)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, algorithmId: str, eventOrder: QuantConnect.Orders.OrderEvent) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    AlgorithmId: str
    Event: QuantConnect.Orders.OrderEvent

class PacketType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Classifications of internal packet system
    
    enum PacketType, values: AlgorithmNode (1), AlgorithmStatus (12), AlphaHeartbeat (32), AlphaNode (30), AlphaResult (28), AlphaWork (29), AutocompleteResult (3), AutocompleteWork (2), BacktestError (11), BacktestNode (4), BacktestResult (5), BacktestWork (6), BuildError (15), BuildSuccess (14), BuildWork (13), CommandResult (23), Debug (19), DebuggingStatus (33), Documentation (26), DocumentationResult (25), GitHubHook (24), HandledError (17), History (22), LiveNode (7), LiveResult (8), LiveWork (9), Log (18), None (0), OrderEvent (20), RegressionAlgorithm (31), RuntimeError (16), SecurityTypes (10), Success (21), SystemDebug (27)
    """
    value__: int
    AlgorithmNode: PacketType
    AlgorithmStatus: PacketType
    AlphaHeartbeat: PacketType
    AlphaNode: PacketType
    AlphaResult: PacketType
    AlphaWork: PacketType
    AutocompleteResult: PacketType
    AutocompleteWork: PacketType
    BacktestError: PacketType
    BacktestNode: PacketType
    BacktestResult: PacketType
    BacktestWork: PacketType
    BuildError: PacketType
    BuildSuccess: PacketType
    BuildWork: PacketType
    CommandResult: PacketType
    Debug: PacketType
    DebuggingStatus: PacketType
    Documentation: PacketType
    DocumentationResult: PacketType
    GitHubHook: PacketType
    HandledError: PacketType
    History: PacketType
    LiveNode: PacketType
    LiveResult: PacketType
    LiveWork: PacketType
    Log: PacketType
    None: PacketType
    OrderEvent: PacketType
    RegressionAlgorithm: PacketType
    RuntimeError: PacketType
    SecurityTypes: PacketType
    Success: PacketType
    SystemDebug: PacketType


class RuntimeErrorPacket(QuantConnect.Packets.Packet):
    """
    Algorithm runtime error packet from the lean engine. 
                This is a managed error which stops the algorithm execution.
    
    RuntimeErrorPacket()
    RuntimeErrorPacket(userId: int, algorithmId: str, message: str, stacktrace: str)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, userId: int, algorithmId: str, message: str, stacktrace: str) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    AlgorithmId: str
    Message: str
    StackTrace: str
    UserId: int

class SecurityTypesPacket(QuantConnect.Packets.Packet):
    """
    Security types packet contains information on the markets the user data has requested.
    
    SecurityTypesPacket()
    """
    TypesCSV: str

    Types: typing.List[QuantConnect.SecurityType]


class StatusHistoryResult(QuantConnect.Packets.HistoryResult):
    """
    Specifies the progress of a request
    
    StatusHistoryResult()
    StatusHistoryResult(progress: int)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, progress: int) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Progress: int

class SystemDebugPacket(QuantConnect.Packets.DebugPacket):
    """
    Debug packets generated by Lean
    
    SystemDebugPacket()
    SystemDebugPacket(projectId: int, algorithmId: str, compileId: str, message: str, toast: bool)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, projectId: int, algorithmId: str, compileId: str, message: str, toast: bool) -> None:
        pass

    def __new__(self, *args) -> None:
        pass


