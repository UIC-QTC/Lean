from .__Packets_1 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Statistics
import QuantConnect.Securities
import QuantConnect.Packets
import QuantConnect.Orders
import QuantConnect
import datetime

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
