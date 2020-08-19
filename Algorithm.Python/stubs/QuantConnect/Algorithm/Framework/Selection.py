# encoding: utf-8
# module QuantConnect.Algorithm.Framework.Selection calls itself Selection
# from QuantConnect.Algorithm, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import Python.Runtime
import QuantConnect
import QuantConnect.Algorithm
import QuantConnect.Algorithm.Framework.Selection
import QuantConnect.Data
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Securities
import System
import typing

# no functions
# classes

class UniverseSelectionModel(System.object, QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel):
    """
    Provides a base class for universe selection models.
    
    UniverseSelectionModel()
    """
    def CreateUniverses(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.List[QuantConnect.Data.UniverseSelection.Universe]:
        pass

    def GetNextRefreshTimeUtc(self) -> datetime.datetime:
        pass


class CompositeUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel, QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel that combines multiple universe
                selection models into a single model.
    
    CompositeUniverseSelectionModel(*universeSelectionModels: Array[IUniverseSelectionModel])
    CompositeUniverseSelectionModel(*universeSelectionModels: Array[PyObject])
    CompositeUniverseSelectionModel(universeSelectionModel: PyObject)
    """
    @typing.overload
    def AddUniverseSelection(self, universeSelectionModel: QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel) -> None:
        pass

    @typing.overload
    def AddUniverseSelection(self, pyUniverseSelectionModel: Python.Runtime.PyObject) -> None:
        pass

    def AddUniverseSelection(self, *args) -> None:
        pass

    def CreateUniverses(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.List[QuantConnect.Data.UniverseSelection.Universe]:
        pass

    def GetNextRefreshTimeUtc(self) -> datetime.datetime:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, universeSelectionModels: typing.List[QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel]) -> None:
        pass

    @typing.overload
    def __new__(self, universeSelectionModels: typing.List[Python.Runtime.PyObject]) -> None:
        pass

    @typing.overload
    def __new__(self, universeSelectionModel: Python.Runtime.PyObject) -> None:
        pass

    def __new__(self, *args) -> None:
        pass


class CustomUniverse(QuantConnect.Data.UniverseSelection.UserDefinedUniverse, System.IDisposable, System.Collections.Specialized.INotifyCollectionChanged, QuantConnect.Data.UniverseSelection.ITimeTriggeredUniverse):
    """
    Defines a universe as a set of dynamically set symbols.
    
    CustomUniverse(configuration: SubscriptionDataConfig, universeSettings: UniverseSettings, interval: TimeSpan, selector: Func[DateTime, IEnumerable[str]])
    """
    @typing.overload
    def GetSubscriptionRequests(self, security: QuantConnect.Securities.Security, currentTimeUtc: datetime.datetime, maximumEndTimeUtc: datetime.datetime, subscriptionService: QuantConnect.Interfaces.ISubscriptionDataConfigService) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    @typing.overload
    def GetSubscriptionRequests(self, security: QuantConnect.Securities.Security, currentTimeUtc: datetime.datetime, maximumEndTimeUtc: datetime.datetime) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    def GetSubscriptionRequests(self, *args) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    @staticmethod # known case of __new__
    def __new__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, interval: datetime.timedelta, selector: typing.Callable[[datetime.datetime], typing.List[str]]) -> None:
        pass


class CustomUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel, QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel that simply
                subscribes to the specified set of symbols
    
    CustomUniverseSelectionModel(name: str, selector: Func[DateTime, IEnumerable[str]])
    CustomUniverseSelectionModel(name: str, selector: PyObject)
    CustomUniverseSelectionModel(securityType: SecurityType, name: str, market: str, selector: Func[DateTime, IEnumerable[str]], universeSettings: UniverseSettings, interval: TimeSpan)
    CustomUniverseSelectionModel(securityType: SecurityType, name: str, market: str, selector: PyObject, universeSettings: UniverseSettings, interval: TimeSpan)
    """
    def CreateUniverses(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.List[QuantConnect.Data.UniverseSelection.Universe]:
        pass

    def Select(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, date: datetime.datetime) -> typing.List[str]:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, selector: typing.Callable[[datetime.datetime], typing.List[str]]) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, selector: Python.Runtime.PyObject) -> None:
        pass

    @typing.overload
    def __new__(self, securityType: QuantConnect.SecurityType, name: str, market: str, selector: typing.Callable[[datetime.datetime], typing.List[str]], universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, interval: datetime.timedelta) -> None:
        pass

    @typing.overload
    def __new__(self, securityType: QuantConnect.SecurityType, name: str, market: str, selector: Python.Runtime.PyObject, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, interval: datetime.timedelta) -> None:
        pass

    def __new__(self, *args) -> None:
        pass


class IUniverseSelectionModel:
    """ Algorithm framework model that defines the universes to be used by an algorithm """
    def CreateUniverses(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.List[QuantConnect.Data.UniverseSelection.Universe]:
        pass

    def GetNextRefreshTimeUtc(self) -> datetime.datetime:
        pass


class ManualUniverse(QuantConnect.Data.UniverseSelection.UserDefinedUniverse, System.IDisposable, System.Collections.Specialized.INotifyCollectionChanged, QuantConnect.Data.UniverseSelection.ITimeTriggeredUniverse):
    """
    Defines a universe as a set of manually set symbols. This differs from QuantConnect.Data.UniverseSelection.UserDefinedUniverse
                in that these securities were not added via AddSecurity.
    
    ManualUniverse(configuration: SubscriptionDataConfig, universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer, symbols: IEnumerable[Symbol])
    ManualUniverse(configuration: SubscriptionDataConfig, universeSettings: UniverseSettings, symbols: IEnumerable[Symbol])
    ManualUniverse(configuration: SubscriptionDataConfig, universeSettings: UniverseSettings, symbols: Array[Symbol])
    """
    @typing.overload
    def GetSubscriptionRequests(self, security: QuantConnect.Securities.Security, currentTimeUtc: datetime.datetime, maximumEndTimeUtc: datetime.datetime, subscriptionService: QuantConnect.Interfaces.ISubscriptionDataConfigService) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    @typing.overload
    def GetSubscriptionRequests(self, security: QuantConnect.Securities.Security, currentTimeUtc: datetime.datetime, maximumEndTimeUtc: datetime.datetime) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    def GetSubscriptionRequests(self, *args) -> typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, securityInitializer: QuantConnect.Securities.ISecurityInitializer, symbols: typing.List[QuantConnect.Symbol]) -> None:
        pass

    @typing.overload
    def __new__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, symbols: typing.List[QuantConnect.Symbol]) -> None:
        pass

    @typing.overload
    def __new__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, symbols: typing.List[QuantConnect.Symbol]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass


class ManualUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel, QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel that simply
                subscribes to the specified set of symbols
    
    ManualUniverseSelectionModel()
    ManualUniverseSelectionModel(symbols: IEnumerable[Symbol])
    ManualUniverseSelectionModel(*symbols: Array[Symbol])
    ManualUniverseSelectionModel(symbols: IEnumerable[Symbol], universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)
    """
    def CreateUniverses(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.List[QuantConnect.Data.UniverseSelection.Universe]:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, symbols: typing.List[QuantConnect.Symbol]) -> None:
        pass

    @typing.overload
    def __new__(self, symbols: typing.List[QuantConnect.Symbol]) -> None:
        pass

    @typing.overload
    def __new__(self, symbols: typing.List[QuantConnect.Symbol], universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, securityInitializer: QuantConnect.Securities.ISecurityInitializer) -> None:
        pass

    def __new__(self, *args) -> None:
        pass


class NullUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel, QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel):
    """
    Provides a null implementation of QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel
    
    NullUniverseSelectionModel()
    """
    def CreateUniverses(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.List[QuantConnect.Data.UniverseSelection.Universe]:
        pass


class UniverseSelectionModelPythonWrapper(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel, QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel that wraps a Python.Runtime.PyObject object
    
    UniverseSelectionModelPythonWrapper(model: PyObject)
    """
    def CreateUniverses(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.List[QuantConnect.Data.UniverseSelection.Universe]:
        pass

    def GetNextRefreshTimeUtc(self) -> datetime.datetime:
        pass

    @staticmethod # known case of __new__
    def __new__(self, model: Python.Runtime.PyObject) -> None:
        pass


