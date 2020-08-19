# encoding: utf-8
# module QuantConnect.Python calls itself Python
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import Python.Runtime
import QuantConnect
import QuantConnect.Brokerages
import QuantConnect.Data
import QuantConnect.Data.Market
import QuantConnect.Interfaces
import QuantConnect.Orders
import QuantConnect.Orders.Fees
import QuantConnect.Orders.Fills
import QuantConnect.Orders.Slippage
import QuantConnect.Python
import QuantConnect.Securities
import System
import System.Collections.Generic
import System.IO
import typing

# no functions
# classes

class BrokerageMessageHandlerPythonWrapper(System.object, QuantConnect.Brokerages.IBrokerageMessageHandler):
    """
    Provides a wrapper for QuantConnect.Brokerages.IBrokerageMessageHandler implementations written in python
    
    BrokerageMessageHandlerPythonWrapper(model: PyObject)
    """
    def Handle(self, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, model: Python.Runtime.PyObject) -> None:
        pass


class BrokerageModelPythonWrapper(System.object, QuantConnect.Brokerages.IBrokerageModel):
    """
    Provides an implementation of QuantConnect.Brokerages.IBrokerageModel that wraps a Python.Runtime.PyObject object
    
    BrokerageModelPythonWrapper(model: PyObject)
    """
    def ApplySplit(self, tickets: typing.List[QuantConnect.Orders.OrderTicket], split: QuantConnect.Data.Market.Split) -> None:
        pass

    def CanExecuteOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> bool:
        pass

    def CanSubmitOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> bool:
        pass

    def CanUpdateOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> bool:
        pass

    @typing.overload
    def GetBuyingPowerModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.IBuyingPowerModel:
        pass

    @typing.overload
    def GetBuyingPowerModel(self, security: QuantConnect.Securities.Security, accountType: QuantConnect.AccountType) -> QuantConnect.Securities.IBuyingPowerModel:
        pass

    def GetBuyingPowerModel(self, *args) -> QuantConnect.Securities.IBuyingPowerModel:
        pass

    def GetFeeModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        pass

    def GetFillModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fills.IFillModel:
        pass

    def GetLeverage(self, security: QuantConnect.Securities.Security) -> float:
        pass

    @typing.overload
    def GetSettlementModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.ISettlementModel:
        pass

    @typing.overload
    def GetSettlementModel(self, security: QuantConnect.Securities.Security, accountType: QuantConnect.AccountType) -> QuantConnect.Securities.ISettlementModel:
        pass

    def GetSettlementModel(self, *args) -> QuantConnect.Securities.ISettlementModel:
        pass

    def GetSlippageModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Slippage.ISlippageModel:
        pass

    @staticmethod # known case of __new__
    def __new__(self, model: Python.Runtime.PyObject) -> None:
        pass

    AccountType: QuantConnect.AccountType

    DefaultMarkets: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]

    RequiredFreeBuyingPowerPercent: float



class BuyingPowerModelPythonWrapper(System.object, QuantConnect.Securities.IBuyingPowerModel):
    """
    Wraps a Python.Runtime.PyObject object that represents a security's model of buying power
    
    BuyingPowerModelPythonWrapper(model: PyObject)
    """
    def GetBuyingPower(self, parameters: QuantConnect.Securities.BuyingPowerParameters) -> QuantConnect.Securities.BuyingPower:
        pass

    def GetLeverage(self, security: QuantConnect.Securities.Security) -> float:
        pass

    def GetMaximumOrderQuantityForDeltaBuyingPower(self, parameters: QuantConnect.Securities.GetMaximumOrderQuantityForDeltaBuyingPowerParameters) -> QuantConnect.Securities.GetMaximumOrderQuantityResult:
        pass

    def GetMaximumOrderQuantityForTargetBuyingPower(self, parameters: QuantConnect.Securities.GetMaximumOrderQuantityForTargetBuyingPowerParameters) -> QuantConnect.Securities.GetMaximumOrderQuantityResult:
        pass

    def GetReservedBuyingPowerForPosition(self, parameters: QuantConnect.Securities.ReservedBuyingPowerForPositionParameters) -> QuantConnect.Securities.ReservedBuyingPowerForPosition:
        pass

    def HasSufficientBuyingPowerForOrder(self, parameters: QuantConnect.Securities.HasSufficientBuyingPowerForOrderParameters) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        pass

    def SetLeverage(self, security: QuantConnect.Securities.Security, leverage: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, model: Python.Runtime.PyObject) -> None:
        pass


class FeeModelPythonWrapper(QuantConnect.Orders.Fees.FeeModel, QuantConnect.Orders.Fees.IFeeModel):
    """
    Provides an order fee model that wraps a Python.Runtime.PyObject object that represents a model that simulates order fees
    
    FeeModelPythonWrapper(model: PyObject)
    """
    def GetOrderFee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        pass

    @staticmethod # known case of __new__
    def __new__(self, model: Python.Runtime.PyObject) -> None:
        pass


class FillModelPythonWrapper(QuantConnect.Orders.Fills.FillModel, QuantConnect.Orders.Fills.IFillModel):
    """
    Wraps a Python.Runtime.PyObject object that represents a model that simulates order fill events
    
    FillModelPythonWrapper(model: PyObject)
    """
    def Fill(self, parameters: QuantConnect.Orders.Fills.FillModelParameters) -> QuantConnect.Orders.Fills.Fill:
        pass

    def LimitFill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.LimitOrder) -> QuantConnect.Orders.OrderEvent:
        pass

    def MarketFill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.MarketOrder) -> QuantConnect.Orders.OrderEvent:
        pass

    def MarketOnCloseFill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.MarketOnCloseOrder) -> QuantConnect.Orders.OrderEvent:
        pass

    def MarketOnOpenFill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.MarketOnOpenOrder) -> QuantConnect.Orders.OrderEvent:
        pass

    def StopLimitFill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.StopLimitOrder) -> QuantConnect.Orders.OrderEvent:
        pass

    def StopMarketFill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.StopMarketOrder) -> QuantConnect.Orders.OrderEvent:
        pass

    @staticmethod # known case of __new__
    def __new__(self, model: Python.Runtime.PyObject) -> None:
        pass

    PythonWrapper: QuantConnect.Python.FillModelPythonWrapper


class MarginCallModelPythonWrapper(System.object, QuantConnect.Securities.IMarginCallModel):
    """
    Provides a margin call model that wraps a Python.Runtime.PyObject object that represents the model responsible for picking which orders should be executed during a margin call
    
    MarginCallModelPythonWrapper(model: PyObject)
    """
    def ExecuteMarginCall(self, generatedMarginCallOrders: typing.List[QuantConnect.Orders.SubmitOrderRequest]) -> typing.List[QuantConnect.Orders.OrderTicket]:
        pass

    def GetMarginCallOrders(self, issueMarginCallWarning: System.Boolean) -> typing.List[QuantConnect.Orders.SubmitOrderRequest]:
        pass

    @staticmethod # known case of __new__
    def __new__(self, model: Python.Runtime.PyObject) -> None:
        pass


class PandasConverter(System.object):
    """
    Collection of methods that converts lists of objects in pandas.DataFrame
    
    PandasConverter()
    """
    @typing.overload
    def GetDataFrame(self, data: typing.List[QuantConnect.Data.Slice]) -> Python.Runtime.PyObject:
        pass

    @typing.overload
    def GetDataFrame(self, data: typing.List[QuantConnect.Python.T]) -> Python.Runtime.PyObject:
        pass

    def GetDataFrame(self, *args) -> Python.Runtime.PyObject:
        pass

    def GetIndicatorDataFrame(self, data: System.Collections.Generic.IDictionary[str, typing.List[QuantConnect.Indicators.IndicatorDataPoint]]) -> Python.Runtime.PyObject:
        pass

    def ToString(self) -> str:
        pass


class PandasData(System.object):
    """
    Organizes a list of data to create pandas.DataFrames
    
    PandasData(data: object)
    """
    @typing.overload
    def Add(self, baseData: object) -> None:
        pass

    @typing.overload
    def Add(self, ticks: typing.List[QuantConnect.Data.Market.Tick], tradeBar: QuantConnect.Data.Market.TradeBar, quoteBar: QuantConnect.Data.Market.QuoteBar) -> None:
        pass

    def Add(self, *args) -> None:
        pass

    def ToPandasDataFrame(self, levels: int) -> Python.Runtime.PyObject:
        pass

    @staticmethod # known case of __new__
    def __new__(self, data: object) -> None:
        pass

    IsCustomData: bool

    Levels: int



class PythonActivator(System.object):
    """
    Provides methods for creating new instances of python custom data objects
    
    PythonActivator(type: Type, value: PyObject)
    """
    @staticmethod # known case of __new__
    def __new__(self, type: type, value: Python.Runtime.PyObject) -> None:
        pass

    Factory: typing.Callable[[typing.List[object]], object]

    Type: type



class PythonData(QuantConnect.Data.DynamicData, QuantConnect.Data.IBaseData, System.Dynamic.IDynamicMetaObjectProvider):
    """
    Dynamic data class for Python algorithms.
                Stores properties of python instances in DynamicData dictionary
    
    PythonData()
    PythonData(pythonData: PyObject)
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

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, pythonData: Python.Runtime.PyObject) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Item: indexer#


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

    def TryGetValue(self, symbol: QuantConnect.Symbol, data: System.Object) -> bool:
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


