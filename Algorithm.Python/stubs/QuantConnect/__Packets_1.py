from .__Packets_2 import *
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
    Completed: 'HistoryResultType'
    Error: 'HistoryResultType'
    File: 'HistoryResultType'
    Status: 'HistoryResultType'


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
    AlgorithmNode: 'PacketType'
    AlgorithmStatus: 'PacketType'
    AlphaHeartbeat: 'PacketType'
    AlphaNode: 'PacketType'
    AlphaResult: 'PacketType'
    AlphaWork: 'PacketType'
    AutocompleteResult: 'PacketType'
    AutocompleteWork: 'PacketType'
    BacktestError: 'PacketType'
    BacktestNode: 'PacketType'
    BacktestResult: 'PacketType'
    BacktestWork: 'PacketType'
    BuildError: 'PacketType'
    BuildSuccess: 'PacketType'
    BuildWork: 'PacketType'
    CommandResult: 'PacketType'
    Debug: 'PacketType'
    DebuggingStatus: 'PacketType'
    Documentation: 'PacketType'
    DocumentationResult: 'PacketType'
    GitHubHook: 'PacketType'
    HandledError: 'PacketType'
    History: 'PacketType'
    LiveNode: 'PacketType'
    LiveResult: 'PacketType'
    LiveWork: 'PacketType'
    Log: 'PacketType'
    OrderEvent: 'PacketType'
    RegressionAlgorithm: 'PacketType'
    RuntimeError: 'PacketType'
    SecurityTypes: 'PacketType'
    Success: 'PacketType'
    SystemDebug: 'PacketType'
    None_: 'PacketType'
