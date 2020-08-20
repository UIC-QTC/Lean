from .__API_1 import *
import QuantConnect.API
import Newtonsoft.Json.Linq
import Newtonsoft.Json
import typing
import System
import QuantConnect.Packets
import QuantConnect.Api
import QuantConnect
import datetime

# no functions
# classes

class RestResponse(System.object):
    """
    Base API response class for the QuantConnect API.

    

    RestResponse()
    """
    Errors: typing.List[str]
    Success: bool

class AuthenticationResponse(QuantConnect.Api.RestResponse):
    """
    Verify if the credentials are OK.

    

    AuthenticationResponse()
    """

class Backtest(QuantConnect.Api.RestResponse):
    """
    Backtest response packet from the QuantConnect.com API.

    

    Backtest()
    """
    BacktestId: str
    Completed: bool
    Created: datetime.datetime
    Error: str
    Name: str
    Note: str
    Progress: float
    Result: QuantConnect.Packets.BacktestResult
    StackTrace: str

class BacktestList(QuantConnect.Api.RestResponse):
    """
    Collection container for a list of backtests for a project

    

    BacktestList()
    """
    Backtests: typing.List[QuantConnect.Api.Backtest]

class BacktestReport(QuantConnect.Api.RestResponse):
    """
    Backtest Report Response wrapper

    

    BacktestReport()
    """
    Report: str



class Compile(QuantConnect.Api.RestResponse):
    """
    Response from the compiler on a build event

    

    Compile()
    """
    CompileId: str
    Logs: typing.List[str]
    State: QuantConnect.Api.CompileState

class CompileState(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    State of the compilation request

    

    enum CompileState, values: BuildError (2), BuildSuccess (1), InQueue (0)
    """
    value__: int
    BuildError: 'CompileState'
    BuildSuccess: 'CompileState'
    InQueue: 'CompileState'


class Link(QuantConnect.Api.RestResponse):
    """
    Response from reading purchased data

    

    Link()
    """
    DataLink: str



class Project(QuantConnect.Api.RestResponse):
    """
    Response from reading a project by id.

    

    Project()
    """
    Created: datetime.datetime
    Language: QuantConnect.Language
    Modified: datetime.datetime
    Name: str
    ProjectId: int

class ProjectFile(System.object):
    """
    File for a project

    

    ProjectFile()
    """
    DateModified: datetime.datetime

    Code: str
    Name: str


class ProjectFilesResponse(QuantConnect.Api.RestResponse):
    """
    Response received when reading all files of a project

    

    ProjectFilesResponse()
    """
    Files: typing.List[QuantConnect.Api.ProjectFile]

class ProjectResponse(QuantConnect.Api.RestResponse):
    """
    Project list response

    

    ProjectResponse()
    """
    Projects: typing.List[QuantConnect.Api.Project]

# no functions
# classes

class BaseLiveAlgorithmSettings(System.object):
    """
    Base class for settings that must be configured per Brokerage to create new algorithms via the API.

    

    BaseLiveAlgorithmSettings(user: str, password: str, environment: BrokerageEnvironment, account: str)

    BaseLiveAlgorithmSettings(user: str, password: str)

    BaseLiveAlgorithmSettings(environment: BrokerageEnvironment, account: str)

    BaseLiveAlgorithmSettings(account: str)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, user: str, password: str, environment: QuantConnect.BrokerageEnvironment, account: str) -> None:
        pass

    @typing.overload
    def __new__(self, user: str, password: str) -> None:
        pass

    @typing.overload
    def __new__(self, environment: QuantConnect.BrokerageEnvironment, account: str) -> None:
        pass

    @typing.overload
    def __new__(self, account: str) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Account: str

    Environment: QuantConnect.BrokerageEnvironment

    Id: str

    Password: str

    User: str



class CreatedNode(QuantConnect.Api.RestResponse):
    """
    Rest api response wrapper for node/create, reads in the nodes information into a 

                node object

    

    CreatedNode()
    """
    Node: QuantConnect.API.Node



class DefaultLiveAlgorithmSettings(QuantConnect.API.BaseLiveAlgorithmSettings):
    """
    Default live algorithm settings

    

    DefaultLiveAlgorithmSettings(user: str, password: str, environment: BrokerageEnvironment, account: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, user: str, password: str, environment: QuantConnect.BrokerageEnvironment, account: str) -> None:
        pass


class Dividend(System.object):
    """
    Dividend returned from the api

    

    Dividend()
    """
    Date: datetime.datetime

    DividendPerShare: float

    ReferencePrice: float

    Symbol: QuantConnect.Symbol

    SymbolID: str



class DividendList(QuantConnect.Api.RestResponse):
    """
    Collection container for a list of dividend objects

    

    DividendList()
    """
    Dividends: typing.List[QuantConnect.API.Dividend]



class FXCMLiveAlgorithmSettings(QuantConnect.API.BaseLiveAlgorithmSettings):
    """
    Algorithm setting for trading with FXCM

    

    FXCMLiveAlgorithmSettings(user: str, password: str, environment: BrokerageEnvironment, account: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, user: str, password: str, environment: QuantConnect.BrokerageEnvironment, account: str) -> None:
        pass


class InteractiveBrokersLiveAlgorithmSettings(QuantConnect.API.BaseLiveAlgorithmSettings):
    """
    Live algorithm settings for trading with Interactive Brokers

    

    InteractiveBrokersLiveAlgorithmSettings(user: str, password: str, account: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, user: str, password: str, account: str) -> None:
        pass


class LiveAlgorithm(QuantConnect.Api.RestResponse):
    """
    Live algorithm instance result from the QuantConnect Rest API.

    

    LiveAlgorithm()
    """
    Brokerage: str
    DeployId: str
    Error: str
    Launched: datetime.datetime
    ProjectId: int
    Status: QuantConnect.AlgorithmStatus
    Stopped: typing.Optional[datetime.datetime]
    Subscription: str

class LiveAlgorithmApiSettingsWrapper(System.object):
    """
    Helper class to put BaseLiveAlgorithmSettings in proper format.

    

    LiveAlgorithmApiSettingsWrapper(projectId: int, compileId: str, serverType: str, settings: BaseLiveAlgorithmSettings, version: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, projectId: int, compileId: str, serverType: str, settings: QuantConnect.API.BaseLiveAlgorithmSettings, version: str) -> None:
        pass

    Brokerage: QuantConnect.API.BaseLiveAlgorithmSettings

    CompileId: str

    ProjectId: int

    ServerType: str

    VersionId: str



class LiveAlgorithmResults(QuantConnect.Api.RestResponse):
    """
    Details a live algorithm from the "live/read" Api endpoint

    

    LiveAlgorithmResults()
    """
    LiveResults: QuantConnect.API.LiveResultsData



class LiveAlgorithmResultsJsonConverter(Newtonsoft.Json.JsonConverter):
    """
    Custom JsonConverter for LiveResults data for live algorithms

    

    LiveAlgorithmResultsJsonConverter()
    """
    def CanConvert(self, objectType: type) -> bool:
        pass

    @staticmethod
    def CreateLiveResultsFromJObject(jObject: Newtonsoft.Json.Linq.JObject) -> QuantConnect.API.LiveAlgorithmResults:
        pass

    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: type, existingValue: object, serializer: Newtonsoft.Json.JsonSerializer) -> object:
        pass

    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: object, serializer: Newtonsoft.Json.JsonSerializer) -> None:
        pass

    CanWrite: bool



class LiveList(QuantConnect.Api.RestResponse):
    """
    List of the live algorithms running which match the requested status

    

    LiveList()
    """
    Algorithms: typing.List[QuantConnect.API.LiveAlgorithm]

class LiveLog(QuantConnect.Api.RestResponse):
    """
    Logs from a live algorithm

    

    LiveLog()
    """
    Logs: typing.List[str]



class LiveResultsData(System.object):
    """
    Holds information about the state and operation of the live running algorithm

    

    LiveResultsData()
    """
    Resolution: QuantConnect.Resolution

    Results: QuantConnect.Packets.LiveResult

    Version: int



class Node(System.object):
    """
    Node class built for API endpoints nodes/read and nodes/create.

                Converts JSON properties from API response into data members for the class.

                Contains all relevant information on a Node to interact through API endpoints.

    

    Node()
    """
    Busy: bool

    CpuCount: int

    Description: str

    Id: str

    Name: str

    Prices: QuantConnect.API.NodePrices

    ProjectName: str

    Ram: float

    SKU: str

    Speed: float

    UsedBy: str



class NodeList(QuantConnect.Api.RestResponse):
    """
    Rest api response wrapper for node/read, contains sets of node lists for each

                target environment. List are composed of QuantConnect.API.Node objects.

    

    NodeList()
    """
    BacktestNodes: typing.List[QuantConnect.API.Node]
    LiveNodes: typing.List[QuantConnect.API.Node]
    ResearchNodes: typing.List[QuantConnect.API.Node]

class NodePrices(System.object):
    """
    Class for deserializing node prices from node object

    

    NodePrices()
    """
    Monthly: int

    Yearly: int



class NodeType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    NodeTypes enum for all possible options of target environments

                Used in conjuction with SKU class as a NodeType is a required parameter for SKU

    

    enum NodeType, values: Backtest (0), Live (2), Research (1)
    """
    value__: int
    Backtest: 'NodeType'
    Live: 'NodeType'
    Research: 'NodeType'


class OandaLiveAlgorithmSettings(QuantConnect.API.BaseLiveAlgorithmSettings):
    """
    Live algorithm settings for trading with Oanda

    

    OandaLiveAlgorithmSettings(accessToken: str, environment: BrokerageEnvironment, account: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, accessToken: str, environment: QuantConnect.BrokerageEnvironment, account: str) -> None:
        pass

    AccessToken: str

    DateIssued: str
