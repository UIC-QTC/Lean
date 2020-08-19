# encoding: utf-8
# module QuantConnect.Data.UniverseSelection calls itself UniverseSelection
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import NodaTime
import Python.Runtime
import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Scheduling
import QuantConnect.Securities
import QuantConnect.Securities.Future
import QuantConnect.Securities.Option
import System
import System.Collections.Concurrent
import System.Collections.Generic
import System.IO
import typing

# no functions
# classes

class BaseDataCollection(QuantConnect.Data.BaseData, QuantConnect.Data.IBaseData):
    """
    This type exists for transport of data as a single packet
    
    BaseDataCollection()
    BaseDataCollection(time: DateTime, symbol: Symbol, data: IEnumerable[BaseData])
    BaseDataCollection(time: DateTime, endTime: DateTime, symbol: Symbol, data: IEnumerable[BaseData])
    BaseDataCollection(time: DateTime, endTime: DateTime, symbol: Symbol, data: List[BaseData])
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
    def __new__(self, time: datetime.datetime, symbol: QuantConnect.Symbol, data: typing.List[QuantConnect.Data.BaseData]) -> None:
        pass

    @typing.overload
    def __new__(self, time: datetime.datetime, endTime: datetime.datetime, symbol: QuantConnect.Symbol, data: typing.List[QuantConnect.Data.BaseData]) -> None:
        pass

    @typing.overload
    def __new__(self, time: datetime.datetime, endTime: datetime.datetime, symbol: QuantConnect.Symbol, data: typing.List[QuantConnect.Data.BaseData]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Data: typing.List[QuantConnect.Data.BaseData]

    EndTime: datetime.datetime



class CoarseFundamental(QuantConnect.Data.BaseData, QuantConnect.Data.IBaseData):
    """
    Defines summary information about a single symbol for a given date
    
    CoarseFundamental()
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
    def CreateUniverseSymbol(market: str, addGuid: bool) -> QuantConnect.Symbol:
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

    AdjustedPrice: float

    DollarVolume: float

    EndTime: datetime.datetime

    HasFundamentalData: bool

    Market: str

    PriceFactor: float

    PriceScaleFactor: float

    SplitFactor: float

    Volume: int



class Universe(System.object, System.IDisposable):
    """ Provides a base class for all universes to derive from. """
    def CanRemoveMember(self, utcTime: datetime.datetime, security: QuantConnect.Securities.Security) -> bool:
        pass

    def ContainsMember(self, symbol: QuantConnect.Symbol) -> bool:
        pass

    def CreateSecurity(self, symbol: QuantConnect.Symbol, algorithm: QuantConnect.Interfaces.IAlgorithm, marketHoursDatabase: QuantConnect.Securities.MarketHoursDatabase, symbolPropertiesDatabase: QuantConnect.Securities.SymbolPropertiesDatabase) -> QuantConnect.Securities.Security:
        pass

    def Dispose(self) -> None:
        pass

    @typing.overload
    def GetSubscriptionRequests(self, security: QuantConnect.Securities.Security, currentTimeUtc: datetime.datetime, maximumEndTimeUtc: datetime.datetime, subscriptionService: QuantConnect.Interfaces.ISubscriptionDataConfigService) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    @typing.overload
    def GetSubscriptionRequests(self, security: QuantConnect.Securities.Security, currentTimeUtc: datetime.datetime, maximumEndTimeUtc: datetime.datetime) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    def GetSubscriptionRequests(self, *args) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    def PerformSelection(self, utcTime: datetime.datetime, data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.List[QuantConnect.Symbol]:
        pass

    def SelectSymbols(self, utcTime: datetime.datetime, data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.List[QuantConnect.Symbol]:
        pass

    def SetSecurityInitializer(self, securityInitializer: QuantConnect.Securities.ISecurityInitializer) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        pass

    Configuration: QuantConnect.Data.SubscriptionDataConfig

    DisposeRequested: bool

    Market: str

    Members: System.Collections.Generic.Dictionary[QuantConnect.Symbol, QuantConnect.Securities.Security]

    Securities: System.Collections.Concurrent.ConcurrentDictionary[QuantConnect.Symbol, QuantConnect.Data.UniverseSelection.Member]

    SecurityInitializer: QuantConnect.Securities.ISecurityInitializer

    SecurityType: QuantConnect.SecurityType

    UniverseSettings: QuantConnect.Data.UniverseSelection.UniverseSettings


    Member: type
    Unchanged: UnchangedUniverse
    UnchangedUniverse: type


class CoarseFundamentalUniverse(QuantConnect.Data.UniverseSelection.Universe, System.IDisposable):
    """
    Defines a universe that reads coarse us equity data
    
    CoarseFundamentalUniverse(universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer, selector: Func[IEnumerable[CoarseFundamental], IEnumerable[Symbol]])
    CoarseFundamentalUniverse(universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer, selector: PyObject)
    CoarseFundamentalUniverse(symbol: Symbol, universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer, selector: Func[IEnumerable[CoarseFundamental], IEnumerable[Symbol]])
    CoarseFundamentalUniverse(symbol: Symbol, universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer, selector: PyObject)
    """
    @staticmethod
    def CreateConfiguration(symbol: QuantConnect.Symbol) -> QuantConnect.Data.SubscriptionDataConfig:
        pass

    def SelectSymbols(self, utcTime: datetime.datetime, data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.List[QuantConnect.Symbol]:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, securityInitializer: QuantConnect.Securities.ISecurityInitializer, selector: typing.Callable[[typing.List[QuantConnect.Data.UniverseSelection.CoarseFundamental]], typing.List[QuantConnect.Symbol]]) -> None:
        pass

    @typing.overload
    def __new__(self, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, securityInitializer: QuantConnect.Securities.ISecurityInitializer, selector: Python.Runtime.PyObject) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, securityInitializer: QuantConnect.Securities.ISecurityInitializer, selector: typing.Callable[[typing.List[QuantConnect.Data.UniverseSelection.CoarseFundamental]], typing.List[QuantConnect.Symbol]]) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, securityInitializer: QuantConnect.Securities.ISecurityInitializer, selector: Python.Runtime.PyObject) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    UniverseSettings: QuantConnect.Data.UniverseSelection.UniverseSettings



class FuncUniverse(QuantConnect.Data.UniverseSelection.Universe, System.IDisposable):
    """
    Provides a functional implementation of QuantConnect.Data.UniverseSelection.Universe
    
    FuncUniverse(configuration: SubscriptionDataConfig, universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer, universeSelector: Func[IEnumerable[BaseData], IEnumerable[Symbol]])
    FuncUniverse(configuration: SubscriptionDataConfig, universeSettings: UniverseSettings, universeSelector: Func[IEnumerable[BaseData], IEnumerable[Symbol]])
    """
    def SelectSymbols(self, utcTime: datetime.datetime, data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.List[QuantConnect.Symbol]:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, securityInitializer: QuantConnect.Securities.ISecurityInitializer, universeSelector: typing.Callable[[typing.List[QuantConnect.Data.BaseData]], typing.List[QuantConnect.Symbol]]) -> None:
        pass

    @typing.overload
    def __new__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, universeSelector: typing.Callable[[typing.List[QuantConnect.Data.BaseData]], typing.List[QuantConnect.Symbol]]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    UniverseSettings: QuantConnect.Data.UniverseSelection.UniverseSettings



class ConstituentsUniverse(QuantConnect.Data.UniverseSelection.FuncUniverse, System.IDisposable):
    """
    ConstituentsUniverse allows to perform universe selection based on an
                already preselected set of QuantConnect.Symbol.
    
    ConstituentsUniverse(symbol: Symbol, universeSettings: UniverseSettings, type: Type)
    ConstituentsUniverse(subscriptionDataConfig: SubscriptionDataConfig, universeSettings: UniverseSettings)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, type: type) -> None:
        pass

    @typing.overload
    def __new__(self, subscriptionDataConfig: QuantConnect.Data.SubscriptionDataConfig, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        pass

    def __new__(self, *args) -> None:
        pass


class ConstituentsUniverseData(QuantConnect.Data.BaseData, QuantConnect.Data.IBaseData):
    """
    Custom base data class used for QuantConnect.Data.UniverseSelection.ConstituentsUniverse
    
    ConstituentsUniverseData()
    """
    def DefaultResolution(self) -> QuantConnect.Resolution:
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

    EndTime: datetime.datetime



class UniverseDecorator(QuantConnect.Data.UniverseSelection.Universe, System.IDisposable):
    """
    Provides an implementation of QuantConnect.Data.UniverseSelection.Universe that redirects all calls to a
                wrapped (or decorated) universe. This provides scaffolding for other decorators who
                only need to override one or two methods.
    """
    def CanRemoveMember(self, utcTime: datetime.datetime, security: QuantConnect.Securities.Security) -> bool:
        pass

    def CreateSecurity(self, symbol: QuantConnect.Symbol, algorithm: QuantConnect.Interfaces.IAlgorithm, marketHoursDatabase: QuantConnect.Securities.MarketHoursDatabase, symbolPropertiesDatabase: QuantConnect.Securities.SymbolPropertiesDatabase) -> QuantConnect.Securities.Security:
        pass

    @typing.overload
    def GetSubscriptionRequests(self, security: QuantConnect.Securities.Security, currentTimeUtc: datetime.datetime, maximumEndTimeUtc: datetime.datetime) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    @typing.overload
    def GetSubscriptionRequests(self, security: QuantConnect.Securities.Security, currentTimeUtc: datetime.datetime, maximumEndTimeUtc: datetime.datetime, subscriptionService: QuantConnect.Interfaces.ISubscriptionDataConfigService) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    def GetSubscriptionRequests(self, *args) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    def SelectSymbols(self, utcTime: datetime.datetime, data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.List[QuantConnect.Symbol]:
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        pass

    Securities: System.Collections.Concurrent.ConcurrentDictionary[QuantConnect.Symbol, QuantConnect.Data.UniverseSelection.Member]

    UniverseSettings: QuantConnect.Data.UniverseSelection.UniverseSettings

    Universe: QuantConnect.Data.UniverseSelection.Universe


class SelectSymbolsUniverseDecorator(QuantConnect.Data.UniverseSelection.UniverseDecorator, System.IDisposable):
    """
    Provides a univese decoration that replaces the implementation of QuantConnect.Data.UniverseSelection.SelectSymbolsUniverseDecorator.SelectSymbols(System.DateTime,QuantConnect.Data.UniverseSelection.BaseDataCollection)
    
    SelectSymbolsUniverseDecorator(universe: Universe, selectSymbols: SelectSymbolsDelegate)
    """
    def SelectSymbols(self, utcTime: datetime.datetime, data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.List[QuantConnect.Symbol]:
        pass

    @staticmethod # known case of __new__
    def __new__(self, universe: QuantConnect.Data.UniverseSelection.Universe, selectSymbols: QuantConnect.Data.UniverseSelection.SelectSymbolsDelegate) -> None:
        pass

    Universe: QuantConnect.Data.UniverseSelection.Universe
    SelectSymbolsDelegate: type


class FineFundamentalFilteredUniverse(QuantConnect.Data.UniverseSelection.SelectSymbolsUniverseDecorator, System.IDisposable):
    """
    Provides a universe that can be filtered with a QuantConnect.Data.Fundamental.FineFundamental selection function
    
    FineFundamentalFilteredUniverse(universe: Universe, fineSelector: Func[IEnumerable[FineFundamental], IEnumerable[Symbol]])
    FineFundamentalFilteredUniverse(universe: Universe, fineSelector: PyObject)
    """
    def SetSecurityInitializer(self, securityInitializer: QuantConnect.Securities.ISecurityInitializer) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, universe: QuantConnect.Data.UniverseSelection.Universe, fineSelector: typing.Callable[[typing.List[QuantConnect.Data.Fundamental.FineFundamental]], typing.List[QuantConnect.Symbol]]) -> None:
        pass

    @typing.overload
    def __new__(self, universe: QuantConnect.Data.UniverseSelection.Universe, fineSelector: Python.Runtime.PyObject) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    FineFundamentalUniverse: QuantConnect.Data.UniverseSelection.FineFundamentalUniverse

    Universe: QuantConnect.Data.UniverseSelection.Universe


class FineFundamentalUniverse(QuantConnect.Data.UniverseSelection.Universe, System.IDisposable):
    """
    Defines a universe that reads fine us equity data
    
    FineFundamentalUniverse(universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer, selector: Func[IEnumerable[FineFundamental], IEnumerable[Symbol]])
    FineFundamentalUniverse(symbol: Symbol, universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer, selector: Func[IEnumerable[FineFundamental], IEnumerable[Symbol]])
    """
    @staticmethod
    def CreateConfiguration(symbol: QuantConnect.Symbol) -> QuantConnect.Data.SubscriptionDataConfig:
        pass

    def SelectSymbols(self, utcTime: datetime.datetime, data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.List[QuantConnect.Symbol]:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, securityInitializer: QuantConnect.Securities.ISecurityInitializer, selector: typing.Callable[[typing.List[QuantConnect.Data.Fundamental.FineFundamental]], typing.List[QuantConnect.Symbol]]) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, securityInitializer: QuantConnect.Securities.ISecurityInitializer, selector: typing.Callable[[typing.List[QuantConnect.Data.Fundamental.FineFundamental]], typing.List[QuantConnect.Symbol]]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    UniverseSettings: QuantConnect.Data.UniverseSelection.UniverseSettings



class FuturesChainUniverse(QuantConnect.Data.UniverseSelection.Universe, System.IDisposable):
    """
    Defines a universe for a single futures chain
    
    FuturesChainUniverse(future: Future, universeSettings: UniverseSettings)
    FuturesChainUniverse(future: Future, universeSettings: UniverseSettings, subscriptionManager: SubscriptionManager, securityInitializer: ISecurityInitializer)
    """
    def CanRemoveMember(self, utcTime: datetime.datetime, security: QuantConnect.Securities.Security) -> bool:
        pass

    def SelectSymbols(self, utcTime: datetime.datetime, data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.List[QuantConnect.Symbol]:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, future: QuantConnect.Securities.Future.Future, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        pass

    @typing.overload
    def __new__(self, future: QuantConnect.Securities.Future.Future, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, subscriptionManager: QuantConnect.Data.SubscriptionManager, securityInitializer: QuantConnect.Securities.ISecurityInitializer) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Future: QuantConnect.Securities.Future.Future

    UniverseSettings: QuantConnect.Data.UniverseSelection.UniverseSettings



class FuturesChainUniverseDataCollection(QuantConnect.Data.UniverseSelection.BaseDataCollection, QuantConnect.Data.IBaseData):
    """
    Defines the universe selection data type for QuantConnect.Data.UniverseSelection.FuturesChainUniverse
    
    FuturesChainUniverseDataCollection()
    FuturesChainUniverseDataCollection(time: DateTime, symbol: Symbol, data: List[BaseData])
    FuturesChainUniverseDataCollection(time: DateTime, endTime: DateTime, symbol: Symbol, data: List[BaseData])
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
    def __new__(self, time: datetime.datetime, symbol: QuantConnect.Symbol, data: typing.List[QuantConnect.Data.BaseData]) -> None:
        pass

    @typing.overload
    def __new__(self, time: datetime.datetime, endTime: datetime.datetime, symbol: QuantConnect.Symbol, data: typing.List[QuantConnect.Data.BaseData]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    FilteredContracts: System.Collections.Generic.HashSet[QuantConnect.Symbol]



class GetSubscriptionRequestsUniverseDecorator(QuantConnect.Data.UniverseSelection.UniverseDecorator, System.IDisposable):
    """
    Provides a universe decoration that replaces the implementation of QuantConnect.Data.UniverseSelection.GetSubscriptionRequestsUniverseDecorator.GetSubscriptionRequests(QuantConnect.Securities.Security,System.DateTime,System.DateTime)
    
    GetSubscriptionRequestsUniverseDecorator(universe: Universe, getRequests: GetSubscriptionRequestsDelegate)
    """
    @typing.overload
    def GetSubscriptionRequests(self, security: QuantConnect.Securities.Security, currentTimeUtc: datetime.datetime, maximumEndTimeUtc: datetime.datetime) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    @typing.overload
    def GetSubscriptionRequests(self, security: QuantConnect.Securities.Security, currentTimeUtc: datetime.datetime, maximumEndTimeUtc: datetime.datetime, subscriptionService: QuantConnect.Interfaces.ISubscriptionDataConfigService) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    def GetSubscriptionRequests(self, *args) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    @staticmethod # known case of __new__
    def __new__(self, universe: QuantConnect.Data.UniverseSelection.Universe, getRequests: QuantConnect.Data.UniverseSelection.GetSubscriptionRequestsDelegate) -> None:
        pass

    Universe: QuantConnect.Data.UniverseSelection.Universe
    GetSubscriptionRequestsDelegate: type


class ITimeTriggeredUniverse:
    """
    A universe implementing this interface will NOT use it's SubscriptionDataConfig to generate data
                that is used to 'pulse' the universe selection function -- instead, the times output by
                GetTriggerTimes are used to 'pulse' the universe selection function WITHOUT data.
    """
    def GetTriggerTimes(self, startTimeUtc: datetime.datetime, endTimeUtc: datetime.datetime, marketHoursDatabase: QuantConnect.Securities.MarketHoursDatabase) -> typing.List[datetime.datetime]:
        pass


class OptionChainUniverse(QuantConnect.Data.UniverseSelection.Universe, System.IDisposable):
    """
    Defines a universe for a single option chain
    
    OptionChainUniverse(option: Option, universeSettings: UniverseSettings, liveMode: bool)
    OptionChainUniverse(option: Option, universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer, liveMode: bool)
    """
    def CanRemoveMember(self, utcTime: datetime.datetime, security: QuantConnect.Securities.Security) -> bool:
        pass

    @typing.overload
    def GetSubscriptionRequests(self, security: QuantConnect.Securities.Security, currentTimeUtc: datetime.datetime, maximumEndTimeUtc: datetime.datetime, subscriptionService: QuantConnect.Interfaces.ISubscriptionDataConfigService) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    @typing.overload
    def GetSubscriptionRequests(self, security: QuantConnect.Securities.Security, currentTimeUtc: datetime.datetime, maximumEndTimeUtc: datetime.datetime) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    def GetSubscriptionRequests(self, *args) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    def SelectSymbols(self, utcTime: datetime.datetime, data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.List[QuantConnect.Symbol]:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, option: QuantConnect.Securities.Option.Option, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, liveMode: bool) -> None:
        pass

    @typing.overload
    def __new__(self, option: QuantConnect.Securities.Option.Option, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, securityInitializer: QuantConnect.Securities.ISecurityInitializer, liveMode: bool) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Option: QuantConnect.Securities.Option.Option

    UniverseSettings: QuantConnect.Data.UniverseSelection.UniverseSettings



class OptionChainUniverseDataCollection(QuantConnect.Data.UniverseSelection.BaseDataCollection, QuantConnect.Data.IBaseData):
    """
    Defines the universe selection data type for QuantConnect.Data.UniverseSelection.OptionChainUniverse
    
    OptionChainUniverseDataCollection()
    OptionChainUniverseDataCollection(time: DateTime, symbol: Symbol, data: List[BaseData], underlying: BaseData)
    OptionChainUniverseDataCollection(time: DateTime, endTime: DateTime, symbol: Symbol, data: List[BaseData], underlying: BaseData)
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
    def __new__(self, time: datetime.datetime, symbol: QuantConnect.Symbol, data: typing.List[QuantConnect.Data.BaseData], underlying: QuantConnect.Data.BaseData) -> None:
        pass

    @typing.overload
    def __new__(self, time: datetime.datetime, endTime: datetime.datetime, symbol: QuantConnect.Symbol, data: typing.List[QuantConnect.Data.BaseData], underlying: QuantConnect.Data.BaseData) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    FilteredContracts: System.Collections.Generic.HashSet[QuantConnect.Symbol]

    Underlying: QuantConnect.Data.BaseData



class ScheduledUniverse(QuantConnect.Data.UniverseSelection.Universe, System.IDisposable, QuantConnect.Data.UniverseSelection.ITimeTriggeredUniverse):
    """
    Defines a user that is fired based on a specified QuantConnect.Scheduling.IDateRule and QuantConnect.Scheduling.ITimeRule
    
    ScheduledUniverse(timeZone: DateTimeZone, dateRule: IDateRule, timeRule: ITimeRule, selector: Func[DateTime, IEnumerable[Symbol]], settings: UniverseSettings, securityInitializer: ISecurityInitializer)
    ScheduledUniverse(dateRule: IDateRule, timeRule: ITimeRule, selector: Func[DateTime, IEnumerable[Symbol]], settings: UniverseSettings, securityInitializer: ISecurityInitializer)
    ScheduledUniverse(timeZone: DateTimeZone, dateRule: IDateRule, timeRule: ITimeRule, selector: PyObject, settings: UniverseSettings, securityInitializer: ISecurityInitializer)
    ScheduledUniverse(dateRule: IDateRule, timeRule: ITimeRule, selector: PyObject, settings: UniverseSettings, securityInitializer: ISecurityInitializer)
    """
    def GetTriggerTimes(self, startTimeUtc: datetime.datetime, endTimeUtc: datetime.datetime, marketHoursDatabase: QuantConnect.Securities.MarketHoursDatabase) -> typing.List[datetime.datetime]:
        pass

    def SelectSymbols(self, utcTime: datetime.datetime, data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.List[QuantConnect.Symbol]:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, timeZone: NodaTime.DateTimeZone, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, selector: typing.Callable[[datetime.datetime], typing.List[QuantConnect.Symbol]], settings: QuantConnect.Data.UniverseSelection.UniverseSettings, securityInitializer: QuantConnect.Securities.ISecurityInitializer) -> None:
        pass

    @typing.overload
    def __new__(self, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, selector: typing.Callable[[datetime.datetime], typing.List[QuantConnect.Symbol]], settings: QuantConnect.Data.UniverseSelection.UniverseSettings, securityInitializer: QuantConnect.Securities.ISecurityInitializer) -> None:
        pass

    @typing.overload
    def __new__(self, timeZone: NodaTime.DateTimeZone, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, selector: Python.Runtime.PyObject, settings: QuantConnect.Data.UniverseSelection.UniverseSettings, securityInitializer: QuantConnect.Securities.ISecurityInitializer) -> None:
        pass

    @typing.overload
    def __new__(self, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, selector: Python.Runtime.PyObject, settings: QuantConnect.Data.UniverseSelection.UniverseSettings, securityInitializer: QuantConnect.Securities.ISecurityInitializer) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    UniverseSettings: QuantConnect.Data.UniverseSelection.UniverseSettings



class SecurityChanges(System.object):
    """
    Defines the additions and subtractions to the algorithm's security subscriptions
    
    SecurityChanges(addedSecurities: IEnumerable[Security], removedSecurities: IEnumerable[Security])
    SecurityChanges(changes: SecurityChanges)
    """
    @staticmethod
    def Added(securities: typing.List[QuantConnect.Securities.Security]) -> QuantConnect.Data.UniverseSelection.SecurityChanges:
        pass

    @staticmethod
    def Removed(securities: typing.List[QuantConnect.Securities.Security]) -> QuantConnect.Data.UniverseSelection.SecurityChanges:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, addedSecurities: typing.List[QuantConnect.Securities.Security], removedSecurities: typing.List[QuantConnect.Securities.Security]) -> None:
        pass

    @typing.overload
    def __new__(self, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    AddedSecurities: typing.List[QuantConnect.Securities.Security]

    Count: int

    FilterCustomSecurities: bool

    RemovedSecurities: typing.List[QuantConnect.Securities.Security]


    None: SecurityChanges


class SubscriptionRequest(System.object):
    """
    Defines the parameters required to add a subscription to a data feed.
    
    SubscriptionRequest(isUniverseSubscription: bool, universe: Universe, security: Security, configuration: SubscriptionDataConfig, startTimeUtc: DateTime, endTimeUtc: DateTime)
    SubscriptionRequest(template: SubscriptionRequest, isUniverseSubscription: Nullable[bool], universe: Universe, security: Security, configuration: SubscriptionDataConfig, startTimeUtc: Nullable[DateTime], endTimeUtc: Nullable[DateTime])
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, isUniverseSubscription: bool, universe: QuantConnect.Data.UniverseSelection.Universe, security: QuantConnect.Securities.Security, configuration: QuantConnect.Data.SubscriptionDataConfig, startTimeUtc: datetime.datetime, endTimeUtc: datetime.datetime) -> None:
        pass

    @typing.overload
    def __new__(self, template: QuantConnect.Data.UniverseSelection.SubscriptionRequest, isUniverseSubscription: typing.Optional[bool], universe: QuantConnect.Data.UniverseSelection.Universe, security: QuantConnect.Securities.Security, configuration: QuantConnect.Data.SubscriptionDataConfig, startTimeUtc: typing.Optional[datetime.datetime], endTimeUtc: typing.Optional[datetime.datetime]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Configuration: QuantConnect.Data.SubscriptionDataConfig

    EndTimeLocal: datetime.datetime

    EndTimeUtc: datetime.datetime

    IsUniverseSubscription: bool

    Security: QuantConnect.Securities.Security

    StartTimeLocal: datetime.datetime

    StartTimeUtc: datetime.datetime

    TradableDays: typing.List[datetime.datetime]

    Universe: QuantConnect.Data.UniverseSelection.Universe



class UniverseExtensions(System.object):
    """ Provides extension methods for the QuantConnect.Data.UniverseSelection.Universe class """
    @staticmethod
    def ChainedTo(first: QuantConnect.Data.UniverseSelection.Universe, second: QuantConnect.Data.UniverseSelection.Universe, configurationPerSymbol: bool) -> QuantConnect.Data.UniverseSelection.Universe:
        pass

    @staticmethod
    def PrefilterUsing(second: QuantConnect.Data.UniverseSelection.Universe, first: QuantConnect.Data.UniverseSelection.Universe) -> QuantConnect.Data.UniverseSelection.Universe:
        pass

    __all__: list


class UniversePythonWrapper(QuantConnect.Data.UniverseSelection.Universe, System.IDisposable):
    """
    Provides an implementation of QuantConnect.Data.UniverseSelection.Universe that wraps a Python.Runtime.PyObject object
    
    UniversePythonWrapper(universe: PyObject)
    """
    @typing.overload
    def GetSubscriptionRequests(self, security: QuantConnect.Securities.Security, currentTimeUtc: datetime.datetime, maximumEndTimeUtc: datetime.datetime, subscriptionService: QuantConnect.Interfaces.ISubscriptionDataConfigService) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    @typing.overload
    def GetSubscriptionRequests(self, security: QuantConnect.Securities.Security, currentTimeUtc: datetime.datetime, maximumEndTimeUtc: datetime.datetime) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    def GetSubscriptionRequests(self, *args) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    def SelectSymbols(self, utcTime: datetime.datetime, data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.List[QuantConnect.Symbol]:
        pass

    @staticmethod # known case of __new__
    def __new__(self, universe: Python.Runtime.PyObject) -> None:
        pass

    Configuration: QuantConnect.Data.SubscriptionDataConfig

    DisposeRequested: bool

    Securities: System.Collections.Concurrent.ConcurrentDictionary[QuantConnect.Symbol, QuantConnect.Data.UniverseSelection.Member]

    UniverseSettings: QuantConnect.Data.UniverseSelection.UniverseSettings



class UniverseSettings(System.object):
    """
    Defines settings required when adding a subscription
    
    UniverseSettings(resolution: Resolution, leverage: Decimal, fillForward: bool, extendedMarketHours: bool, minimumTimeInUniverse: TimeSpan, dataNormalizationMode: DataNormalizationMode)
    """
    @staticmethod # known case of __new__
    def __new__(self, resolution: QuantConnect.Resolution, leverage: float, fillForward: bool, extendedMarketHours: bool, minimumTimeInUniverse: datetime.timedelta, dataNormalizationMode: QuantConnect.DataNormalizationMode) -> None:
        pass

    DataNormalizationMode: QuantConnect.DataNormalizationMode
    ExtendedMarketHours: bool
    FillForward: bool
    Leverage: float
    MinimumTimeInUniverse: datetime.timedelta
    Resolution: QuantConnect.Resolution

class UserDefinedUniverse(QuantConnect.Data.UniverseSelection.Universe, System.IDisposable, System.Collections.Specialized.INotifyCollectionChanged, QuantConnect.Data.UniverseSelection.ITimeTriggeredUniverse):
    """
    Represents the universe defined by the user's algorithm. This is
                the default universe where manually added securities live by
                market/security type. They can also be manually generated and
                can be configured to fire on certain interval and will always
                return the internal list of symbols.
    
    UserDefinedUniverse(configuration: SubscriptionDataConfig, universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer, interval: TimeSpan, symbols: IEnumerable[Symbol])
    UserDefinedUniverse(configuration: SubscriptionDataConfig, universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer, interval: TimeSpan, selector: Func[DateTime, IEnumerable[str]])
    UserDefinedUniverse(configuration: SubscriptionDataConfig, universeSettings: UniverseSettings, interval: TimeSpan, symbols: IEnumerable[Symbol])
    UserDefinedUniverse(configuration: SubscriptionDataConfig, universeSettings: UniverseSettings, interval: TimeSpan, selector: Func[DateTime, IEnumerable[str]])
    """
    @typing.overload
    def Add(self, symbol: QuantConnect.Symbol) -> bool:
        pass

    @typing.overload
    def Add(self, subscriptionDataConfig: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        pass

    def Add(self, *args) -> bool:
        pass

    @staticmethod
    def CreateSymbol(securityType: QuantConnect.SecurityType, market: str) -> QuantConnect.Symbol:
        pass

    @typing.overload
    def GetSubscriptionRequests(self, security: QuantConnect.Securities.Security, currentTimeUtc: datetime.datetime, maximumEndTimeUtc: datetime.datetime, subscriptionService: QuantConnect.Interfaces.ISubscriptionDataConfigService) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    @typing.overload
    def GetSubscriptionRequests(self, security: QuantConnect.Securities.Security, currentTimeUtc: datetime.datetime, maximumEndTimeUtc: datetime.datetime) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    def GetSubscriptionRequests(self, *args) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    def GetTriggerTimes(self, startTimeUtc: datetime.datetime, endTimeUtc: datetime.datetime, marketHoursDatabase: QuantConnect.Securities.MarketHoursDatabase) -> typing.List[datetime.datetime]:
        pass

    def Remove(self, symbol: QuantConnect.Symbol) -> bool:
        pass

    def SelectSymbols(self, utcTime: datetime.datetime, data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.List[QuantConnect.Symbol]:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, securityInitializer: QuantConnect.Securities.ISecurityInitializer, interval: datetime.timedelta, symbols: typing.List[QuantConnect.Symbol]) -> None:
        pass

    @typing.overload
    def __new__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, securityInitializer: QuantConnect.Securities.ISecurityInitializer, interval: datetime.timedelta, selector: typing.Callable[[datetime.datetime], typing.List[str]]) -> None:
        pass

    @typing.overload
    def __new__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, interval: datetime.timedelta, symbols: typing.List[QuantConnect.Symbol]) -> None:
        pass

    @typing.overload
    def __new__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, interval: datetime.timedelta, selector: typing.Callable[[datetime.datetime], typing.List[str]]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Interval: datetime.timedelta

    UniverseSettings: QuantConnect.Data.UniverseSelection.UniverseSettings


    CollectionChanged: BoundEvent


