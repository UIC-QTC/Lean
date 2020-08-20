import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Securities
import QuantConnect.Python
import QuantConnect.Orders.Slippage
import QuantConnect.Orders.Fills
import QuantConnect.Orders.Fees
import QuantConnect.Orders
import QuantConnect.Interfaces
import QuantConnect.Data.Market
import QuantConnect.Data
import QuantConnect.Brokerages
import QuantConnect
import Python.Runtime
import datetime


class PythonInitializer(System.object):
    """ Helper class for Python initialization """
    @staticmethod
    def AddPythonPaths(paths: typing.List[str]) -> None:
        pass

    @staticmethod
    def Initialize() -> None:
        pass

    @staticmethod
    def SetPythonPathEnvironmentVariable(extraDirectories: typing.List[str]) -> None:
        pass

    __all__: list


class PythonQuandl(QuantConnect.Data.Custom.Quandl, QuantConnect.Data.IBaseData, System.Dynamic.IDynamicMetaObjectProvider):
    """
    Dynamic data class for Python algorithms.

    

    PythonQuandl()

    PythonQuandl(valueColumnName: str)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, valueColumnName: str) -> None:
        pass

    def __new__(self, *args) -> None:
        pass


class PythonSlice(QuantConnect.Data.Slice, QuantConnect.Interfaces.IExtendedDictionary[Symbol, object], System.Collections.Generic.IEnumerable[KeyValuePair[Symbol, BaseData]], System.Collections.IEnumerable):
    """
    Provides a data structure for all of an algorithm's data at a single time step

    

    PythonSlice(slice: Slice)
    """
    def ContainsKey(self, symbol: QuantConnect.Symbol) -> bool:
        pass

    @typing.overload
    def Get(self, type: Python.Runtime.PyObject, symbol: QuantConnect.Symbol) -> object:
        pass

    @typing.overload
    def Get(self, type: Python.Runtime.PyObject) -> Python.Runtime.PyObject:
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

    def TryGetValue(self, symbol: QuantConnect.Symbol, data: object) -> bool:
        pass

    @staticmethod # known case of __new__
    def __new__(self, slice: QuantConnect.Data.Slice) -> None:
        pass

    Count: int

    Keys: typing.List[QuantConnect.Symbol]

    Values: typing.List[QuantConnect.Data.BaseData]


    Item: indexer#


class PythonWrapper(System.object):
    """ Provides extension methods for managing python wrapper classes """
    @staticmethod
    def ValidateImplementationOf(model: Python.Runtime.PyObject) -> None:
        pass

    __all__: list


class SecurityInitializerPythonWrapper(System.object, QuantConnect.Securities.ISecurityInitializer):
    """
    Wraps a Python.Runtime.PyObject object that represents a type capable of initializing a new security

    

    SecurityInitializerPythonWrapper(model: PyObject)
    """
    def Initialize(self, security: QuantConnect.Securities.Security) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, model: Python.Runtime.PyObject) -> None:
        pass


class SlippageModelPythonWrapper(System.object, QuantConnect.Orders.Slippage.ISlippageModel):
    """
    Wraps a Python.Runtime.PyObject object that represents a model that simulates market order slippage

    

    SlippageModelPythonWrapper(model: PyObject)
    """
    def GetSlippageApproximation(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> float:
        pass

    @staticmethod # known case of __new__
    def __new__(self, model: Python.Runtime.PyObject) -> None:
        pass


class VolatilityModelPythonWrapper(QuantConnect.Securities.Volatility.BaseVolatilityModel, QuantConnect.Securities.IVolatilityModel):
    """
    Provides a volatility model that wraps a Python.Runtime.PyObject object that represents a model that computes the volatility of a security

    

    VolatilityModelPythonWrapper(model: PyObject)
    """
    def GetHistoryRequirements(self, security: QuantConnect.Securities.Security, utcTime: datetime.datetime) -> typing.List[QuantConnect.Data.HistoryRequest]:
        pass

    def SetSubscriptionDataConfigProvider(self, subscriptionDataConfigProvider: QuantConnect.Interfaces.ISubscriptionDataConfigProvider) -> None:
        pass

    def Update(self, security: QuantConnect.Securities.Security, data: QuantConnect.Data.BaseData) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, model: Python.Runtime.PyObject) -> None:
        pass

    Volatility: float

    SubscriptionDataConfigProvider: QuantConnect.Interfaces.ISubscriptionDataConfigProvider
