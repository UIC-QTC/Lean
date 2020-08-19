# encoding: utf-8
# module QuantConnect.Securities calls itself Securities
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import NodaTime
import Python.Runtime
import QuantConnect
import QuantConnect.Algorithm.Framework.Portfolio
import QuantConnect.Brokerages
import QuantConnect.Data
import QuantConnect.Data.Fundamental
import QuantConnect.Data.Market
import QuantConnect.Data.UniverseSelection
import QuantConnect.Indicators
import QuantConnect.Interfaces
import QuantConnect.Orders
import QuantConnect.Orders.Fees
import QuantConnect.Orders.Fills
import QuantConnect.Orders.Slippage
import QuantConnect.Securities
import QuantConnect.Securities.Interfaces
import System
import System.Collections
import System.Collections.Concurrent
import System.Collections.Generic
import System.Dynamic
import System.Linq.Expressions
import typing

# no functions
# classes

class AccountCurrencyImmediateSettlementModel(System.object, QuantConnect.Securities.ISettlementModel):
    """
    Represents the model responsible for applying cash settlement rules
    
    AccountCurrencyImmediateSettlementModel()
    """
    def ApplyFunds(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, applicationTimeUtc: datetime.datetime, currency: str, amount: float) -> None:
        pass


class AccountEvent(System.object):
    """
    Messaging class signifying a change in a user's account
    
    AccountEvent(currencySymbol: str, cashBalance: Decimal)
    """
    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    def __new__(self, currencySymbol: str, cashBalance: float) -> None:
        pass

    CashBalance: float

    CurrencySymbol: str



class AdjustedPriceVariationModel(System.object, QuantConnect.Securities.IPriceVariationModel):
    """
    Provides an implementation of QuantConnect.Securities.IPriceVariationModel
                for use when data is QuantConnect.DataNormalizationMode.Adjusted.
    
    AdjustedPriceVariationModel()
    """
    def GetMinimumPriceVariation(self, parameters: QuantConnect.Securities.GetMinimumPriceVariationParameters) -> float:
        pass


class BrokerageModelSecurityInitializer(System.object, QuantConnect.Securities.ISecurityInitializer):
    """
    Provides an implementation of QuantConnect.Securities.ISecurityInitializer that initializes a security
                by settings the QuantConnect.Securities.Security.FillModel, QuantConnect.Securities.Security.FeeModel,
                QuantConnect.Securities.Security.SlippageModel, and the QuantConnect.Securities.Security.SettlementModel properties
    
    BrokerageModelSecurityInitializer()
    BrokerageModelSecurityInitializer(brokerageModel: IBrokerageModel, securitySeeder: ISecuritySeeder)
    """
    def Initialize(self, security: QuantConnect.Securities.Security) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, brokerageModel: QuantConnect.Brokerages.IBrokerageModel, securitySeeder: QuantConnect.Securities.ISecuritySeeder) -> None:
        pass

    def __new__(self, *args) -> None:
        pass


class BuyingPower(System.object):
    """
    Defines the result for QuantConnect.Securities.IBuyingPowerModel.GetBuyingPower(QuantConnect.Securities.BuyingPowerParameters)
    
    BuyingPower(buyingPower: Decimal)
    """
    @staticmethod # known case of __new__
    def __new__(self, buyingPower: float) -> None:
        pass

    Value: float



class BuyingPowerModel(System.object, QuantConnect.Securities.IBuyingPowerModel):
    """
    Provides a base class for all buying power models
    
    BuyingPowerModel()
    BuyingPowerModel(initialMarginRequirement: Decimal, maintenanceMarginRequirement: Decimal, requiredFreeBuyingPowerPercent: Decimal)
    BuyingPowerModel(leverage: Decimal, requiredFreeBuyingPowerPercent: Decimal)
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
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, initialMarginRequirement: float, maintenanceMarginRequirement: float, requiredFreeBuyingPowerPercent: float) -> None:
        pass

    @typing.overload
    def __new__(self, leverage: float, requiredFreeBuyingPowerPercent: float) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    RequiredFreeBuyingPowerPercent: float

class BuyingPowerModelExtensions(System.object):
    """ Provides extension methods as backwards compatibility shims """
    @staticmethod
    def GetBuyingPower(model: QuantConnect.Securities.IBuyingPowerModel, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, direction: QuantConnect.Orders.OrderDirection) -> float:
        pass

    @staticmethod
    def GetMaximumOrderQuantityForTargetBuyingPower(model: QuantConnect.Securities.IBuyingPowerModel, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, target: float) -> QuantConnect.Securities.GetMaximumOrderQuantityResult:
        pass

    @staticmethod
    def GetReservedBuyingPowerForPosition(model: QuantConnect.Securities.IBuyingPowerModel, security: QuantConnect.Securities.Security) -> float:
        pass

    @staticmethod
    def HasSufficientBuyingPowerForOrder(model: QuantConnect.Securities.IBuyingPowerModel, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        pass

    __all__: list


class BuyingPowerParameters(System.object):
    """
    Defines the parameters for QuantConnect.Securities.IBuyingPowerModel.GetBuyingPower(QuantConnect.Securities.BuyingPowerParameters)
    
    BuyingPowerParameters(portfolio: SecurityPortfolioManager, security: Security, direction: OrderDirection)
    """
    def Result(self, buyingPower: float, currency: str) -> QuantConnect.Securities.BuyingPower:
        pass

    def ResultInAccountCurrency(self, buyingPower: float) -> QuantConnect.Securities.BuyingPower:
        pass

    @staticmethod # known case of __new__
    def __new__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, direction: QuantConnect.Orders.OrderDirection) -> None:
        pass

    Direction: QuantConnect.Orders.OrderDirection

    Portfolio: QuantConnect.Securities.SecurityPortfolioManager

    Security: QuantConnect.Securities.Security



class Cash(System.object):
    """
    Represents a holding of a currency in cash.
    
    Cash(symbol: str, amount: Decimal, conversionRate: Decimal)
    """
    def AddAmount(self, amount: float) -> float:
        pass

    def EnsureCurrencyDataFeed(self, securities: QuantConnect.Securities.SecurityManager, subscriptions: QuantConnect.Data.SubscriptionManager, marketMap: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str], changes: QuantConnect.Data.UniverseSelection.SecurityChanges, securityService: QuantConnect.Interfaces.ISecurityService, accountCurrency: str, defaultResolution: QuantConnect.Resolution) -> QuantConnect.Data.SubscriptionDataConfig:
        pass

    def SetAmount(self, amount: float) -> None:
        pass

    def ToString(self) -> str:
        pass

    def Update(self, data: QuantConnect.Data.BaseData) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, symbol: str, amount: float, conversionRate: float) -> None:
        pass

    Amount: float

    ConversionRate: float

    ConversionRateSecurity: QuantConnect.Securities.Security

    CurrencySymbol: str

    SecuritySymbol: QuantConnect.Symbol

    Symbol: str

    ValueInAccountCurrency: float


    Updated: BoundEvent


class CashAmount(System.object):
    """
    Represents a cash amount which can be converted to account currency using a currency converter
    
    CashAmount(amount: Decimal, currency: str)
    """
    def Equals(self, obj: object) -> bool:
        pass

    @staticmethod # known case of __new__
    def __new__(self, amount: float, currency: str) -> None:
        pass

    Amount: float

    Currency: str



class ICurrencyConverter:
    """ Provides the ability to convert cash amounts to the account currency """
    def ConvertToAccountCurrency(self, cashAmount: QuantConnect.Securities.CashAmount) -> QuantConnect.Securities.CashAmount:
        pass

    AccountCurrency: str



class CashBook(System.object, System.Collections.Generic.IDictionary[str, Cash], System.Collections.Generic.ICollection[KeyValuePair[str, Cash]], System.Collections.Generic.IEnumerable[KeyValuePair[str, Cash]], System.Collections.IEnumerable, QuantConnect.Securities.ICurrencyConverter):
    """
    Provides a means of keeping track of the different cash holdings of an algorithm
    
    CashBook()
    """
    @typing.overload
    def Add(self, symbol: str, quantity: float, conversionRate: float) -> None:
        pass

    @typing.overload
    def Add(self, item: System.Collections.Generic.KeyValuePair[str, QuantConnect.Securities.Cash]) -> None:
        pass

    @typing.overload
    def Add(self, symbol: str, value: QuantConnect.Securities.Cash) -> None:
        pass

    def Add(self, *args) -> None:
        pass

    def Clear(self) -> None:
        pass

    def Contains(self, item: System.Collections.Generic.KeyValuePair[str, QuantConnect.Securities.Cash]) -> bool:
        pass

    def ContainsKey(self, symbol: str) -> bool:
        pass

    def Convert(self, sourceQuantity: float, sourceCurrency: str, destinationCurrency: str) -> float:
        pass

    @typing.overload
    def ConvertToAccountCurrency(self, sourceQuantity: float, sourceCurrency: str) -> float:
        pass

    @typing.overload
    def ConvertToAccountCurrency(self, cashAmount: QuantConnect.Securities.CashAmount) -> QuantConnect.Securities.CashAmount:
        pass

    def ConvertToAccountCurrency(self, *args) -> QuantConnect.Securities.CashAmount:
        pass

    def CopyTo(self, array: typing.List[System.Collections.Generic.KeyValuePair], arrayIndex: int) -> None:
        pass

    def EnsureCurrencyDataFeeds(self, securities: QuantConnect.Securities.SecurityManager, subscriptions: QuantConnect.Data.SubscriptionManager, marketMap: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str], changes: QuantConnect.Data.UniverseSelection.SecurityChanges, securityService: QuantConnect.Interfaces.ISecurityService, defaultResolution: QuantConnect.Resolution) -> typing.List[QuantConnect.Data.SubscriptionDataConfig]:
        pass

    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[str, QuantConnect.Securities.Cash]]:
        pass

    @typing.overload
    def Remove(self, symbol: str) -> bool:
        pass

    @typing.overload
    def Remove(self, item: System.Collections.Generic.KeyValuePair[str, QuantConnect.Securities.Cash]) -> bool:
        pass

    def Remove(self, *args) -> bool:
        pass

    def ToString(self) -> str:
        pass

    def TryGetValue(self, symbol: str, value: QuantConnect.Securities.Cash) -> bool:
        pass

    AccountCurrency: str

    Count: int

    IsReadOnly: bool

    Keys: typing.List[str]

    TotalValueInAccountCurrency: float

    Values: typing.List[QuantConnect.Securities.Cash]


    Item: indexer#
    Updated: BoundEvent
    UpdateType: type


class CashBuyingPowerModel(QuantConnect.Securities.BuyingPowerModel, QuantConnect.Securities.IBuyingPowerModel):
    """
    Represents a buying power model for cash accounts
    
    CashBuyingPowerModel()
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

    RequiredFreeBuyingPowerPercent: float

class CompositeSecurityInitializer(System.object, QuantConnect.Securities.ISecurityInitializer):
    """
    Provides an implementation of QuantConnect.Securities.ISecurityInitializer that executes
                each initializer in order
    
    CompositeSecurityInitializer(*initializers: Array[ISecurityInitializer])
    """
    def Initialize(self, security: QuantConnect.Securities.Security) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, initializers: typing.List[QuantConnect.Securities.ISecurityInitializer]) -> None:
        pass


class DefaultMarginCallModel(System.object, QuantConnect.Securities.IMarginCallModel):
    """
    Represents the model responsible for picking which orders should be executed during a margin call
    
    DefaultMarginCallModel(portfolio: SecurityPortfolioManager, defaultOrderProperties: IOrderProperties)
    """
    def ExecuteMarginCall(self, generatedMarginCallOrders: typing.List[QuantConnect.Orders.SubmitOrderRequest]) -> typing.List[QuantConnect.Orders.OrderTicket]:
        pass

    def GetMarginCallOrders(self, issueMarginCallWarning: System.Boolean) -> typing.List[QuantConnect.Orders.SubmitOrderRequest]:
        pass

    @staticmethod # known case of __new__
    def __new__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, defaultOrderProperties: QuantConnect.Interfaces.IOrderProperties) -> None:
        pass



class DelayedSettlementModel(System.object, QuantConnect.Securities.ISettlementModel):
    """
    Represents the model responsible for applying cash settlement rules
    
    DelayedSettlementModel(numberOfDays: int, timeOfDay: TimeSpan)
    """
    def ApplyFunds(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, applicationTimeUtc: datetime.datetime, currency: str, amount: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, numberOfDays: int, timeOfDay: datetime.timedelta) -> None:
        pass


class DynamicSecurityData(System.object, System.Dynamic.IDynamicMetaObjectProvider):
    """
    Provides access to a security's data via it's type. This implementation supports dynamic access
                by type name.
    
    DynamicSecurityData(registeredTypes: IRegisteredSecurityDataTypesProvider, cache: SecurityCache)
    """
    @typing.overload
    def Get(self) -> QuantConnect.Securities.T:
        pass

    @typing.overload
    def Get(self, type: type) -> Python.Runtime.PyObject:
        pass

    def Get(self, *args) -> Python.Runtime.PyObject:
        pass

    @typing.overload
    def GetAll(self) -> typing.List[QuantConnect.Securities.T]:
        pass

    @typing.overload
    def GetAll(self, type: type) -> System.Collections.IList:
        pass

    def GetAll(self, *args) -> System.Collections.IList:
        pass

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression) -> System.Dynamic.DynamicMetaObject:
        pass

    def GetProperty(self, name: str) -> object:
        pass

    def HasData(self) -> bool:
        pass

    def HasProperty(self, name: str) -> bool:
        pass

    def SetProperty(self, name: str, value: object) -> object:
        pass

    @staticmethod # known case of __new__
    def __new__(self, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, cache: QuantConnect.Securities.SecurityCache) -> None:
        pass


class SecurityPriceVariationModel(System.object, QuantConnect.Securities.IPriceVariationModel):
    """
    Provides default implementation of QuantConnect.Securities.IPriceVariationModel
                for use in defining the minimum price variation.
    
    SecurityPriceVariationModel()
    """
    def GetMinimumPriceVariation(self, parameters: QuantConnect.Securities.GetMinimumPriceVariationParameters) -> float:
        pass


class EquityPriceVariationModel(QuantConnect.Securities.SecurityPriceVariationModel, QuantConnect.Securities.IPriceVariationModel):
    """
    Provides an implementation of QuantConnect.Securities.IPriceVariationModel
                for use in defining the minimum price variation for a given equity
        
    EquityPriceVariationModel()
    """
    def GetMinimumPriceVariation(self, parameters: QuantConnect.Securities.GetMinimumPriceVariationParameters) -> float:
        pass


class ErrorCurrencyConverter(System.object, QuantConnect.Securities.ICurrencyConverter):
    """
    Provides an implementation of QuantConnect.Securities.ICurrencyConverter for use in
                tests that don't depend on this behavior.
    """
    def ConvertToAccountCurrency(self, cashAmount: QuantConnect.Securities.CashAmount) -> QuantConnect.Securities.CashAmount:
        pass

    AccountCurrency: str


    Instance: ErrorCurrencyConverter


class FuncSecurityDerivativeFilter(System.object, QuantConnect.Securities.IDerivativeSecurityFilter):
    """
    Provides a functional implementation of QuantConnect.Securities.IDerivativeSecurityFilter
    
    FuncSecurityDerivativeFilter(filter: Func[IDerivativeSecurityFilterUniverse, IDerivativeSecurityFilterUniverse])
    """
    def Filter(self, universe: QuantConnect.Securities.IDerivativeSecurityFilterUniverse) -> QuantConnect.Securities.IDerivativeSecurityFilterUniverse:
        pass

    @staticmethod # known case of __new__
    def __new__(self, filter: typing.Callable[[QuantConnect.Securities.IDerivativeSecurityFilterUniverse], QuantConnect.Securities.IDerivativeSecurityFilterUniverse]) -> None:
        pass


class FuncSecurityInitializer(System.object, QuantConnect.Securities.ISecurityInitializer):
    """
    Provides a functional implementation of QuantConnect.Securities.ISecurityInitializer
    
    FuncSecurityInitializer(initializer: Action[Security])
    """
    def Initialize(self, security: QuantConnect.Securities.Security) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, initializer: typing.Callable[[QuantConnect.Securities.Security], None]) -> None:
        pass


class FuncSecuritySeeder(System.object, QuantConnect.Securities.ISecuritySeeder):
    """
    Seed a security price from a history function
    
    FuncSecuritySeeder(seedFunction: Func[Security, BaseData])
    """
    def SeedSecurity(self, security: QuantConnect.Securities.Security) -> bool:
        pass

    @staticmethod # known case of __new__
    def __new__(self, seedFunction: typing.Callable[[QuantConnect.Securities.Security], QuantConnect.Data.BaseData]) -> None:
        pass


class FutureExpirationCycles(System.object):
    """ Static class contains definitions of popular futures expiration cycles """
    AllYear: Array[int]
    February: Array[int]
    FGHJKMNQUVXZ: Array[int]
    FHKNQUVZ: Array[int]
    FHKNQUX: Array[int]
    HKNUVZ: Array[int]
    HKNUZ: Array[int]
    HMUZ: Array[int]
    January: Array[int]
    March: Array[int]
    __all__: list


class IDerivativeSecurityFilterUniverse(System.Collections.Generic.IEnumerable[Symbol], System.Collections.IEnumerable):
    """ Represents derivative symbols universe used in filtering. """
    IsDynamic: bool

    Underlying: QuantConnect.Data.BaseData



class FutureFilterUniverse(System.object, QuantConnect.Securities.IDerivativeSecurityFilterUniverse, System.Collections.Generic.IEnumerable[Symbol], System.Collections.IEnumerable):
    """
    Represents futures symbols universe used in filtering.
    
    FutureFilterUniverse(allSymbols: IEnumerable[Symbol], underlying: BaseData)
    """
    def BackMonth(self) -> QuantConnect.Securities.FutureFilterUniverse:
        pass

    def BackMonths(self) -> QuantConnect.Securities.FutureFilterUniverse:
        pass

    @typing.overload
    def Contracts(self, contracts: typing.List[QuantConnect.Symbol]) -> QuantConnect.Securities.FutureFilterUniverse:
        pass

    @typing.overload
    def Contracts(self, contractSelector: typing.Callable[[typing.List[QuantConnect.Symbol]], typing.List[QuantConnect.Symbol]]) -> QuantConnect.Securities.FutureFilterUniverse:
        pass

    def Contracts(self, *args) -> QuantConnect.Securities.FutureFilterUniverse:
        pass

    @typing.overload
    def Expiration(self, minExpiry: datetime.timedelta, maxExpiry: datetime.timedelta) -> QuantConnect.Securities.FutureFilterUniverse:
        pass

    @typing.overload
    def Expiration(self, minExpiryDays: int, maxExpiryDays: int) -> QuantConnect.Securities.FutureFilterUniverse:
        pass

    def Expiration(self, *args) -> QuantConnect.Securities.FutureFilterUniverse:
        pass

    def ExpirationCycle(self, months: typing.List[int]) -> QuantConnect.Securities.FutureFilterUniverse:
        pass

    def FrontMonth(self) -> QuantConnect.Securities.FutureFilterUniverse:
        pass

    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Symbol]:
        pass

    def OnlyApplyFilterAtMarketOpen(self) -> QuantConnect.Securities.FutureFilterUniverse:
        pass

    @staticmethod # known case of __new__
    def __new__(self, allSymbols: typing.List[QuantConnect.Symbol], underlying: QuantConnect.Data.BaseData) -> None:
        pass

    IsDynamic: bool

    Underlying: QuantConnect.Data.BaseData



class FutureFilterUniverseEx(System.object):
    """ Extensions for Linq support """
    @staticmethod
    def Select(universe: QuantConnect.Securities.FutureFilterUniverse, mapFunc: typing.Callable[[QuantConnect.Symbol], QuantConnect.Symbol]) -> QuantConnect.Securities.FutureFilterUniverse:
        pass

    @staticmethod
    def SelectMany(universe: QuantConnect.Securities.FutureFilterUniverse, mapFunc: typing.Callable[[QuantConnect.Symbol], typing.List[QuantConnect.Symbol]]) -> QuantConnect.Securities.FutureFilterUniverse:
        pass

    @staticmethod
    def Where(universe: QuantConnect.Securities.FutureFilterUniverse, predicate: typing.Callable[[QuantConnect.Symbol], bool]) -> QuantConnect.Securities.FutureFilterUniverse:
        pass

    __all__: list


class Futures(System.object):
    """ Futures static class contains shortcut definitions of major futures contracts available for trading """
    Currencies: type
    Dairy: type
    Energies: type
    Financials: type
    Forestry: type
    Grains: type
    Indices: type
    Meats: type
    Metals: type
    Softs: type
    __all__: list


class GetMaximumOrderQuantityForDeltaBuyingPowerParameters(System.object):
    """
    Defines the parameters for QuantConnect.Securities.IBuyingPowerModel.GetMaximumOrderQuantityForDeltaBuyingPower(QuantConnect.Securities.GetMaximumOrderQuantityForDeltaBuyingPowerParameters)
    
    GetMaximumOrderQuantityForDeltaBuyingPowerParameters(portfolio: SecurityPortfolioManager, security: Security, deltaBuyingPower: Decimal, silenceNonErrorReasons: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, deltaBuyingPower: float, silenceNonErrorReasons: bool) -> None:
        pass

    DeltaBuyingPower: float

    Portfolio: QuantConnect.Securities.SecurityPortfolioManager

    Security: QuantConnect.Securities.Security

    SilenceNonErrorReasons: bool



class GetMaximumOrderQuantityForTargetBuyingPowerParameters(System.object):
    """
    Defines the parameters for QuantConnect.Securities.IBuyingPowerModel.GetMaximumOrderQuantityForTargetBuyingPower(QuantConnect.Securities.GetMaximumOrderQuantityForTargetBuyingPowerParameters)
    
    GetMaximumOrderQuantityForTargetBuyingPowerParameters(portfolio: SecurityPortfolioManager, security: Security, targetBuyingPower: Decimal, silenceNonErrorReasons: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, targetBuyingPower: float, silenceNonErrorReasons: bool) -> None:
        pass

    Portfolio: QuantConnect.Securities.SecurityPortfolioManager

    Security: QuantConnect.Securities.Security

    SilenceNonErrorReasons: bool

    TargetBuyingPower: float



class GetMaximumOrderQuantityResult(System.object):
    """
    Contains the information returned by QuantConnect.Securities.IBuyingPowerModel.GetMaximumOrderQuantityForTargetBuyingPower(QuantConnect.Securities.GetMaximumOrderQuantityForTargetBuyingPowerParameters)
                and  QuantConnect.Securities.IBuyingPowerModel.GetMaximumOrderQuantityForDeltaBuyingPower(QuantConnect.Securities.GetMaximumOrderQuantityForDeltaBuyingPowerParameters)
    
    GetMaximumOrderQuantityResult(quantity: Decimal, reason: str)
    GetMaximumOrderQuantityResult(quantity: Decimal, reason: str, isError: bool)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, quantity: float, reason: str) -> None:
        pass

    @typing.overload
    def __new__(self, quantity: float, reason: str, isError: bool) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsError: bool

    Quantity: float

    Reason: str



class GetMinimumPriceVariationParameters(System.object):
    """
    Defines the parameters for QuantConnect.Securities.IPriceVariationModel.GetMinimumPriceVariation(QuantConnect.Securities.GetMinimumPriceVariationParameters)
    
    GetMinimumPriceVariationParameters(security: Security, referencePrice: Decimal)
    """
    @staticmethod # known case of __new__
    def __new__(self, security: QuantConnect.Securities.Security, referencePrice: float) -> None:
        pass

    ReferencePrice: float

    Security: QuantConnect.Securities.Security



class HasSufficientBuyingPowerForOrderParameters(System.object):
    """
    Defines the parameters for QuantConnect.Securities.IBuyingPowerModel.HasSufficientBuyingPowerForOrder(QuantConnect.Securities.HasSufficientBuyingPowerForOrderParameters)
    
    HasSufficientBuyingPowerForOrderParameters(portfolio: SecurityPortfolioManager, security: Security, order: Order)
    """
    @staticmethod # known case of __new__
    def __new__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> None:
        pass

    Order: QuantConnect.Orders.Order

    Portfolio: QuantConnect.Securities.SecurityPortfolioManager

    Security: QuantConnect.Securities.Security



class HasSufficientBuyingPowerForOrderResult(System.object):
    """
    Contains the information returned by QuantConnect.Securities.IBuyingPowerModel.HasSufficientBuyingPowerForOrder(QuantConnect.Securities.HasSufficientBuyingPowerForOrderParameters)
    
    HasSufficientBuyingPowerForOrderResult(isSufficient: bool, reason: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, isSufficient: bool, reason: str) -> None:
        pass

    IsSufficient: bool

    Reason: str



class IBaseCurrencySymbol:
    # no doc
    BaseCurrencySymbol: str



class IBuyingPowerModel:
    """ Represents a security's model of buying power """
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


class IdentityCurrencyConverter(System.object, QuantConnect.Securities.ICurrencyConverter):
    """
    Provides an implementation of QuantConnect.Securities.ICurrencyConverter that does NOT perform conversions.
                This implementation will throw if the specified cashAmount is not in units of account currency.
    
    IdentityCurrencyConverter(accountCurrency: str)
    """
    def ConvertToAccountCurrency(self, cashAmount: QuantConnect.Securities.CashAmount) -> QuantConnect.Securities.CashAmount:
        pass

    @staticmethod # known case of __new__
    def __new__(self, accountCurrency: str) -> None:
        pass

    AccountCurrency: str



class IDerivativeSecurity:
    """ Defines a security as a derivative of another security """
    Underlying: QuantConnect.Securities.Security



class IDerivativeSecurityFilter:
    """ Filters a set of derivative symbols using the underlying price data. """
    def Filter(self, universe: QuantConnect.Securities.IDerivativeSecurityFilterUniverse) -> QuantConnect.Securities.IDerivativeSecurityFilterUniverse:
        pass


class IMarginCallModel:
    """ Represents the model responsible for picking which orders should be executed during a margin call """
    def ExecuteMarginCall(self, generatedMarginCallOrders: typing.List[QuantConnect.Orders.SubmitOrderRequest]) -> typing.List[QuantConnect.Orders.OrderTicket]:
        pass

    def GetMarginCallOrders(self, issueMarginCallWarning: System.Boolean) -> typing.List[QuantConnect.Orders.SubmitOrderRequest]:
        pass


class ImmediateSettlementModel(System.object, QuantConnect.Securities.ISettlementModel):
    """
    Represents the model responsible for applying cash settlement rules
    
    ImmediateSettlementModel()
    """
    def ApplyFunds(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, applicationTimeUtc: datetime.datetime, currency: str, amount: float) -> None:
        pass


class IndicatorVolatilityModel(System.object, QuantConnect.Securities.IVolatilityModel):
    """
    IndicatorVolatilityModel[T](indicator: IIndicator[T])
    IndicatorVolatilityModel[T](indicator: IIndicator[T], indicatorUpdate: Action[Security, BaseData, IIndicator[T]])
    """
    def GetHistoryRequirements(self, security: QuantConnect.Securities.Security, utcTime: datetime.datetime) -> typing.List[QuantConnect.Data.HistoryRequest]:
        pass

    def Update(self, security: QuantConnect.Securities.Security, data: QuantConnect.Data.BaseData) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, indicator: QuantConnect.Indicators.IIndicator[QuantConnect.Securities.T]) -> None:
        pass

    @typing.overload
    def __new__(self, indicator: QuantConnect.Indicators.IIndicator[QuantConnect.Securities.T], indicatorUpdate: typing.Callable[[QuantConnect.Securities.Security, QuantConnect.Data.BaseData, QuantConnect.Indicators.IIndicator[QuantConnect.Securities.T]], None]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Volatility: float



class InitialMarginRequiredForOrderParameters(System.object):
    """
    Defines the parameters for QuantConnect.Securities.BuyingPowerModel.GetInitialMarginRequiredForOrder(QuantConnect.Securities.InitialMarginRequiredForOrderParameters)
    
    InitialMarginRequiredForOrderParameters(currencyConverter: ICurrencyConverter, security: Security, order: Order)
    """
    @staticmethod # known case of __new__
    def __new__(self, currencyConverter: QuantConnect.Securities.ICurrencyConverter, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> None:
        pass

    CurrencyConverter: QuantConnect.Securities.ICurrencyConverter

    Order: QuantConnect.Orders.Order

    Security: QuantConnect.Securities.Security



class IOrderEventProvider:
    """ Represents a type with a new QuantConnect.Orders.OrderEvent event System.EventHandler. """
    NewOrderEvent: BoundEvent


class IOrderProvider:
    """ Represents a type capable of fetching Order instances by its QC order id or by a brokerage id """
    def GetOpenOrders(self, filter: typing.Callable[[QuantConnect.Orders.Order], bool]) -> typing.List[QuantConnect.Orders.Order]:
        pass

    def GetOpenOrderTickets(self, filter: typing.Callable[[QuantConnect.Orders.OrderTicket], bool]) -> typing.List[QuantConnect.Orders.OrderTicket]:
        pass

    def GetOrderByBrokerageId(self, brokerageId: str) -> QuantConnect.Orders.Order:
        pass

    def GetOrderById(self, orderId: int) -> QuantConnect.Orders.Order:
        pass

    def GetOrders(self, filter: typing.Callable[[QuantConnect.Orders.Order], bool]) -> typing.List[QuantConnect.Orders.Order]:
        pass

    def GetOrderTicket(self, orderId: int) -> QuantConnect.Orders.OrderTicket:
        pass

    def GetOrderTickets(self, filter: typing.Callable[[QuantConnect.Orders.OrderTicket], bool]) -> typing.List[QuantConnect.Orders.OrderTicket]:
        pass

    OrdersCount: int



class IOrderProcessor(QuantConnect.Securities.IOrderProvider):
    """ Represents a type capable of processing orders """
    def Process(self, request: QuantConnect.Orders.OrderRequest) -> QuantConnect.Orders.OrderTicket:
        pass


class IPriceVariationModel:
    """ Gets the minimum price variation of a given security """
    def GetMinimumPriceVariation(self, parameters: QuantConnect.Securities.GetMinimumPriceVariationParameters) -> float:
        pass


class IRegisteredSecurityDataTypesProvider:
    """ Provides the set of base data types registered in the algorithm """
    def RegisterType(self, type: type) -> bool:
        pass

    def TryGetType(self, name: str, type: System.Type) -> bool:
        pass

    def UnregisterType(self, type: type) -> bool:
        pass


class ISecurityInitializer:
    """ Represents a type capable of initializing a new security """
    def Initialize(self, security: QuantConnect.Securities.Security) -> None:
        pass


class ISecurityPortfolioModel:
    """ Performs order fill application to portfolio """
    def ProcessFill(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, fill: QuantConnect.Orders.OrderEvent) -> None:
        pass


class ISecurityProvider:
    """ Represents a type capable of fetching the holdings for the specified symbol """
    def GetSecurity(self, symbol: QuantConnect.Symbol) -> QuantConnect.Securities.Security:
        pass


class ISecuritySeeder:
    """ Used to seed the security with the correct price """
    def SeedSecurity(self, security: QuantConnect.Securities.Security) -> bool:
        pass


class ISettlementModel:
    """ Represents the model responsible for applying cash settlement rules """
    def ApplyFunds(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, applicationTimeUtc: datetime.datetime, currency: str, amount: float) -> None:
        pass


class IVolatilityModel:
    """ Represents a model that computes the volatility of a security """
    def GetHistoryRequirements(self, security: QuantConnect.Securities.Security, utcTime: datetime.datetime) -> typing.List[QuantConnect.Data.HistoryRequest]:
        pass

    def Update(self, security: QuantConnect.Securities.Security, data: QuantConnect.Data.BaseData) -> None:
        pass

    Volatility: float



class LocalMarketHours(System.object):
    """
    Represents the market hours under normal conditions for an exchange and a specific day of the week in terms of local time
    
    LocalMarketHours(day: DayOfWeek, *segments: Array[MarketHoursSegment])
    LocalMarketHours(day: DayOfWeek, segments: IEnumerable[MarketHoursSegment])
    LocalMarketHours(day: DayOfWeek, extendedMarketOpen: TimeSpan, marketOpen: TimeSpan, marketClose: TimeSpan, extendedMarketClose: TimeSpan)
    LocalMarketHours(day: DayOfWeek, marketOpen: TimeSpan, marketClose: TimeSpan)
    """
    @staticmethod
    def ClosedAllDay(dayOfWeek: System.DayOfWeek) -> QuantConnect.Securities.LocalMarketHours:
        pass

    def GetMarketClose(self, time: datetime.timedelta, extendedMarket: bool) -> typing.Optional[datetime.timedelta]:
        pass

    def GetMarketOpen(self, time: datetime.timedelta, extendedMarket: bool) -> typing.Optional[datetime.timedelta]:
        pass

    @typing.overload
    def IsOpen(self, time: datetime.timedelta, extendedMarket: bool) -> bool:
        pass

    @typing.overload
    def IsOpen(self, start: datetime.timedelta, end: datetime.timedelta, extendedMarket: bool) -> bool:
        pass

    def IsOpen(self, *args) -> bool:
        pass

    @staticmethod
    def OpenAllDay(dayOfWeek: System.DayOfWeek) -> QuantConnect.Securities.LocalMarketHours:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, day: System.DayOfWeek, segments: typing.List[QuantConnect.Securities.MarketHoursSegment]) -> None:
        pass

    @typing.overload
    def __new__(self, day: System.DayOfWeek, segments: typing.List[QuantConnect.Securities.MarketHoursSegment]) -> None:
        pass

    @typing.overload
    def __new__(self, day: System.DayOfWeek, extendedMarketOpen: datetime.timedelta, marketOpen: datetime.timedelta, marketClose: datetime.timedelta, extendedMarketClose: datetime.timedelta) -> None:
        pass

    @typing.overload
    def __new__(self, day: System.DayOfWeek, marketOpen: datetime.timedelta, marketClose: datetime.timedelta) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    DayOfWeek: System.DayOfWeek

    IsClosedAllDay: bool

    IsOpenAllDay: bool

    MarketDuration: datetime.timedelta

    Segments: typing.List[QuantConnect.Securities.MarketHoursSegment]



class MarginCallModel(System.object):
    """ Provides access to a null implementation for QuantConnect.Securities.IMarginCallModel """
    Null: NullMarginCallModel
    __all__: list


class MarketHoursDatabase(System.object):
    """
    Provides access to exchange hours and raw data times zones in various markets
    
    MarketHoursDatabase(exchangeHours: IReadOnlyDictionary[SecurityDatabaseKey, Entry])
    """
    @staticmethod
    @typing.overload
    def FromDataFolder() -> QuantConnect.Securities.MarketHoursDatabase:
        pass

    @staticmethod
    @typing.overload
    def FromDataFolder(dataFolder: str) -> QuantConnect.Securities.MarketHoursDatabase:
        pass

    def FromDataFolder(self, *args) -> QuantConnect.Securities.MarketHoursDatabase:
        pass

    @staticmethod
    def FromFile(path: str) -> QuantConnect.Securities.MarketHoursDatabase:
        pass

    @staticmethod
    def GetDatabaseSymbolKey(symbol: QuantConnect.Symbol) -> str:
        pass

    def GetDataTimeZone(self, market: str, symbol: QuantConnect.Symbol, securityType: QuantConnect.SecurityType) -> NodaTime.DateTimeZone:
        pass

    @typing.overload
    def GetEntry(self, market: str, symbol: str, securityType: QuantConnect.SecurityType) -> QuantConnect.Securities.Entry:
        pass

    @typing.overload
    def GetEntry(self, market: str, symbol: QuantConnect.Symbol, securityType: QuantConnect.SecurityType) -> QuantConnect.Securities.Entry:
        pass

    def GetEntry(self, *args) -> QuantConnect.Securities.Entry:
        pass

    @typing.overload
    def GetExchangeHours(self, configuration: QuantConnect.Data.SubscriptionDataConfig) -> QuantConnect.Securities.SecurityExchangeHours:
        pass

    @typing.overload
    def GetExchangeHours(self, market: str, symbol: QuantConnect.Symbol, securityType: QuantConnect.SecurityType) -> QuantConnect.Securities.SecurityExchangeHours:
        pass

    def GetExchangeHours(self, *args) -> QuantConnect.Securities.SecurityExchangeHours:
        pass

    @staticmethod
    def Reset() -> None:
        pass

    def SetEntry(self, market: str, symbol: str, securityType: QuantConnect.SecurityType, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, dataTimeZone: NodaTime.DateTimeZone) -> QuantConnect.Securities.Entry:
        pass

    def SetEntryAlwaysOpen(self, market: str, symbol: str, securityType: QuantConnect.SecurityType, timeZone: NodaTime.DateTimeZone) -> QuantConnect.Securities.Entry:
        pass

    @typing.overload
    def TryGetEntry(self, market: str, symbol: QuantConnect.Symbol, securityType: QuantConnect.SecurityType, entry: QuantConnect.Securities.Entry) -> bool:
        pass

    @typing.overload
    def TryGetEntry(self, market: str, symbol: str, securityType: QuantConnect.SecurityType, entry: QuantConnect.Securities.Entry) -> bool:
        pass

    def TryGetEntry(self, *args) -> bool:
        pass

    @staticmethod # known case of __new__
    def __new__(self, exchangeHours: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.Securities.SecurityDatabaseKey, QuantConnect.Securities.Entry]) -> None:
        pass

    ExchangeHoursListing: typing.List[System.Collections.Generic.KeyValuePair[QuantConnect.Securities.SecurityDatabaseKey, QuantConnect.Securities.Entry]]


    AlwaysOpen: AlwaysOpenMarketHoursDatabaseImpl
    Entry: type


class MarketHoursSegment(System.object):
    """
    Represents the state of an exchange during a specified time range
    
    MarketHoursSegment(state: MarketHoursState, start: TimeSpan, end: TimeSpan)
    """
    @staticmethod
    def ClosedAllDay() -> QuantConnect.Securities.MarketHoursSegment:
        pass

    def Contains(self, time: datetime.timedelta) -> bool:
        pass

    @staticmethod
    def GetMarketHoursSegments(extendedMarketOpen: datetime.timedelta, marketOpen: datetime.timedelta, marketClose: datetime.timedelta, extendedMarketClose: datetime.timedelta) -> typing.List[QuantConnect.Securities.MarketHoursSegment]:
        pass

    @staticmethod
    def OpenAllDay() -> QuantConnect.Securities.MarketHoursSegment:
        pass

    def Overlaps(self, start: datetime.timedelta, end: datetime.timedelta) -> bool:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    def __new__(self, state: QuantConnect.Securities.MarketHoursState, start: datetime.timedelta, end: datetime.timedelta) -> None:
        pass

    End: datetime.timedelta

    Start: datetime.timedelta

    State: QuantConnect.Securities.MarketHoursState



class MarketHoursState(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Specifies the open/close state for a QuantConnect.Securities.MarketHoursSegment
    
    enum MarketHoursState, values: Closed (0), Market (2), PostMarket (3), PreMarket (1)
    """
    value__: int
    Closed: MarketHoursState
    Market: MarketHoursState
    PostMarket: MarketHoursState
    PreMarket: MarketHoursState


class OptionFilterUniverse(System.object, QuantConnect.Securities.IDerivativeSecurityFilterUniverse, System.Collections.Generic.IEnumerable[Symbol], System.Collections.IEnumerable):
    """
    Represents options symbols universe used in filtering.
    
    OptionFilterUniverse()
    OptionFilterUniverse(allSymbols: IEnumerable[Symbol], underlying: BaseData)
    """
    def BackMonth(self) -> QuantConnect.Securities.OptionFilterUniverse:
        pass

    def BackMonths(self) -> QuantConnect.Securities.OptionFilterUniverse:
        pass

    def CallsOnly(self) -> QuantConnect.Securities.OptionFilterUniverse:
        pass

    @typing.overload
    def Contracts(self, contracts: typing.List[QuantConnect.Symbol]) -> QuantConnect.Securities.OptionFilterUniverse:
        pass

    @typing.overload
    def Contracts(self, contractSelector: typing.Callable[[typing.List[QuantConnect.Symbol]], typing.List[QuantConnect.Symbol]]) -> QuantConnect.Securities.OptionFilterUniverse:
        pass

    def Contracts(self, *args) -> QuantConnect.Securities.OptionFilterUniverse:
        pass

    @typing.overload
    def Expiration(self, minExpiry: datetime.timedelta, maxExpiry: datetime.timedelta) -> QuantConnect.Securities.OptionFilterUniverse:
        pass

    @typing.overload
    def Expiration(self, minExpiryDays: int, maxExpiryDays: int) -> QuantConnect.Securities.OptionFilterUniverse:
        pass

    def Expiration(self, *args) -> QuantConnect.Securities.OptionFilterUniverse:
        pass

    def FrontMonth(self) -> QuantConnect.Securities.OptionFilterUniverse:
        pass

    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Symbol]:
        pass

    def IncludeWeeklys(self) -> QuantConnect.Securities.OptionFilterUniverse:
        pass

    def OnlyApplyFilterAtMarketOpen(self) -> QuantConnect.Securities.OptionFilterUniverse:
        pass

    def PutsOnly(self) -> QuantConnect.Securities.OptionFilterUniverse:
        pass

    def Refresh(self, allSymbols: typing.List[QuantConnect.Symbol], underlying: QuantConnect.Data.BaseData, exchangeDateChange: bool) -> None:
        pass

    def Strikes(self, minStrike: int, maxStrike: int) -> QuantConnect.Securities.OptionFilterUniverse:
        pass

    def WeeklysOnly(self) -> QuantConnect.Securities.OptionFilterUniverse:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, allSymbols: typing.List[QuantConnect.Symbol], underlying: QuantConnect.Data.BaseData) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsDynamic: bool

    Underlying: QuantConnect.Data.BaseData


    Type: type


class OptionFilterUniverseEx(System.object):
    """ Extensions for Linq support """
    @staticmethod
    def Select(universe: QuantConnect.Securities.OptionFilterUniverse, mapFunc: typing.Callable[[QuantConnect.Symbol], QuantConnect.Symbol]) -> QuantConnect.Securities.OptionFilterUniverse:
        pass

    @staticmethod
    def SelectMany(universe: QuantConnect.Securities.OptionFilterUniverse, mapFunc: typing.Callable[[QuantConnect.Symbol], typing.List[QuantConnect.Symbol]]) -> QuantConnect.Securities.OptionFilterUniverse:
        pass

    @staticmethod
    def Where(universe: QuantConnect.Securities.OptionFilterUniverse, predicate: typing.Callable[[QuantConnect.Symbol], bool]) -> QuantConnect.Securities.OptionFilterUniverse:
        pass

    __all__: list


class OrderProviderExtensions(System.object):
    """ Provides extension methods for the QuantConnect.Securities.IOrderProvider interface """
    @staticmethod
    @typing.overload
    def GetOrderByBrokerageId(orderProvider: QuantConnect.Securities.IOrderProvider, brokerageId: int) -> QuantConnect.Orders.Order:
        pass

    @staticmethod
    @typing.overload
    def GetOrderByBrokerageId(orderProvider: QuantConnect.Securities.IOrderProvider, brokerageId: int) -> QuantConnect.Orders.Order:
        pass

    def GetOrderByBrokerageId(self, *args) -> QuantConnect.Orders.Order:
        pass

    __all__: list


class SecurityMarginModel(QuantConnect.Securities.BuyingPowerModel, QuantConnect.Securities.IBuyingPowerModel):
    """
    Represents a simple, constant margin model by specifying the percentages of required margin.
    
    SecurityMarginModel()
    SecurityMarginModel(initialMarginRequirement: Decimal, maintenanceMarginRequirement: Decimal, requiredFreeBuyingPowerPercent: Decimal)
    SecurityMarginModel(leverage: Decimal, requiredFreeBuyingPowerPercent: Decimal)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, initialMarginRequirement: float, maintenanceMarginRequirement: float, requiredFreeBuyingPowerPercent: float) -> None:
        pass

    @typing.overload
    def __new__(self, leverage: float, requiredFreeBuyingPowerPercent: float) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    RequiredFreeBuyingPowerPercent: float

class PatternDayTradingMarginModel(QuantConnect.Securities.SecurityMarginModel, QuantConnect.Securities.IBuyingPowerModel):
    """
    Represents a simple margining model where margin/leverage depends on market state (open or close).
                During regular market hours, leverage is 4x, otherwise 2x
    
    PatternDayTradingMarginModel()
    PatternDayTradingMarginModel(closedMarketLeverage: Decimal, openMarketLeverage: Decimal)
    """
    def GetLeverage(self, security: QuantConnect.Securities.Security) -> float:
        pass

    def SetLeverage(self, security: QuantConnect.Securities.Security, leverage: float) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, closedMarketLeverage: float, openMarketLeverage: float) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    RequiredFreeBuyingPowerPercent: float

class RegisteredSecurityDataTypesProvider(System.object, QuantConnect.Securities.IRegisteredSecurityDataTypesProvider):
    """
    Provides an implementation of QuantConnect.Securities.IRegisteredSecurityDataTypesProvider that permits the
                consumer to modify the expected types
    
    RegisteredSecurityDataTypesProvider()
    """
    def RegisterType(self, type: type) -> bool:
        pass

    def TryGetType(self, name: str, type: System.Type) -> bool:
        pass

    def UnregisterType(self, type: type) -> bool:
        pass

    Null: RegisteredSecurityDataTypesProvider


class RelativeStandardDeviationVolatilityModel(QuantConnect.Securities.Volatility.BaseVolatilityModel, QuantConnect.Securities.IVolatilityModel):
    """
    Provides an implementation of QuantConnect.Securities.IVolatilityModel that computes the
                relative standard deviation as the volatility of the security
    
    RelativeStandardDeviationVolatilityModel(periodSpan: TimeSpan, periods: int)
    """
    def GetHistoryRequirements(self, security: QuantConnect.Securities.Security, utcTime: datetime.datetime) -> typing.List[QuantConnect.Data.HistoryRequest]:
        pass

    def Update(self, security: QuantConnect.Securities.Security, data: QuantConnect.Data.BaseData) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, periodSpan: datetime.timedelta, periods: int) -> None:
        pass

    Volatility: float

    SubscriptionDataConfigProvider: QuantConnect.Interfaces.ISubscriptionDataConfigProvider


class ReservedBuyingPowerForPosition(System.object):
    """
    Defines the result for QuantConnect.Securities.IBuyingPowerModel.GetReservedBuyingPowerForPosition(QuantConnect.Securities.ReservedBuyingPowerForPositionParameters)
    
    ReservedBuyingPowerForPosition(reservedBuyingPowerForPosition: Decimal)
    """
    @staticmethod # known case of __new__
    def __new__(self, reservedBuyingPowerForPosition: float) -> None:
        pass

    AbsoluteUsedBuyingPower: float



class ReservedBuyingPowerForPositionParameters(System.object):
    """
    Defines the parameters for QuantConnect.Securities.IBuyingPowerModel.GetReservedBuyingPowerForPosition(QuantConnect.Securities.ReservedBuyingPowerForPositionParameters)
    
    ReservedBuyingPowerForPositionParameters(security: Security)
    """
    def ResultInAccountCurrency(self, reservedBuyingPower: float) -> QuantConnect.Securities.ReservedBuyingPowerForPosition:
        pass

    @staticmethod # known case of __new__
    def __new__(self, security: QuantConnect.Securities.Security) -> None:
        pass

    Security: QuantConnect.Securities.Security



class Security(System.object, QuantConnect.Interfaces.ISecurityPrice):
    """
    A base vehicle properties class for providing a common interface to all assets in QuantConnect.
    
    Security(exchangeHours: SecurityExchangeHours, config: SubscriptionDataConfig, quoteCurrency: Cash, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypesProvider: IRegisteredSecurityDataTypesProvider, cache: SecurityCache)
    Security(symbol: Symbol, exchangeHours: SecurityExchangeHours, quoteCurrency: Cash, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypesProvider: IRegisteredSecurityDataTypesProvider, cache: SecurityCache)
    """
    def GetLastData(self) -> QuantConnect.Data.BaseData:
        pass

    def IsCustomData(self) -> bool:
        pass

    def RefreshDataNormalizationModeProperty(self) -> None:
        pass

    @typing.overload
    def SetBuyingPowerModel(self, buyingPowerModel: QuantConnect.Securities.IBuyingPowerModel) -> None:
        pass

    @typing.overload
    def SetBuyingPowerModel(self, pyObject: Python.Runtime.PyObject) -> None:
        pass

    def SetBuyingPowerModel(self, *args) -> None:
        pass

    def SetDataNormalizationMode(self, mode: QuantConnect.DataNormalizationMode) -> None:
        pass

    @typing.overload
    def SetFeeModel(self, feelModel: QuantConnect.Orders.Fees.IFeeModel) -> None:
        pass

    @typing.overload
    def SetFeeModel(self, feelModel: Python.Runtime.PyObject) -> None:
        pass

    def SetFeeModel(self, *args) -> None:
        pass

    @typing.overload
    def SetFillModel(self, fillModel: QuantConnect.Orders.Fills.IFillModel) -> None:
        pass

    @typing.overload
    def SetFillModel(self, fillModel: Python.Runtime.PyObject) -> None:
        pass

    def SetFillModel(self, *args) -> None:
        pass

    def SetLeverage(self, leverage: float) -> None:
        pass

    def SetLocalTimeKeeper(self, localTimeKeeper: QuantConnect.LocalTimeKeeper) -> None:
        pass

    @typing.overload
    def SetMarginModel(self, marginModel: QuantConnect.Securities.IBuyingPowerModel) -> None:
        pass

    @typing.overload
    def SetMarginModel(self, pyObject: Python.Runtime.PyObject) -> None:
        pass

    def SetMarginModel(self, *args) -> None:
        pass

    def SetMarketPrice(self, data: QuantConnect.Data.BaseData) -> None:
        pass

    def SetRealTimePrice(self, data: QuantConnect.Data.BaseData) -> None:
        pass

    @typing.overload
    def SetSlippageModel(self, slippageModel: QuantConnect.Orders.Slippage.ISlippageModel) -> None:
        pass

    @typing.overload
    def SetSlippageModel(self, slippageModel: Python.Runtime.PyObject) -> None:
        pass

    def SetSlippageModel(self, *args) -> None:
        pass

    @typing.overload
    def SetVolatilityModel(self, volatilityModel: QuantConnect.Securities.IVolatilityModel) -> None:
        pass

    @typing.overload
    def SetVolatilityModel(self, volatilityModel: Python.Runtime.PyObject) -> None:
        pass

    def SetVolatilityModel(self, *args) -> None:
        pass

    def ToString(self) -> str:
        pass

    def Update(self, data: typing.List[QuantConnect.Data.BaseData], dataType: type, containsFillForwardData: typing.Optional[bool]) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, config: QuantConnect.Data.SubscriptionDataConfig, quoteCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.SymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypesProvider: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, cache: QuantConnect.Securities.SecurityCache) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, quoteCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.SymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypesProvider: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, cache: QuantConnect.Securities.SecurityCache) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    AskPrice: float

    AskSize: float

    BidPrice: float

    BidSize: float

    BuyingPowerModel: QuantConnect.Securities.IBuyingPowerModel

    Cache: QuantConnect.Securities.SecurityCache

    Close: float

    Data: object

    DataFilter: QuantConnect.Securities.Interfaces.ISecurityDataFilter

    DataNormalizationMode: QuantConnect.DataNormalizationMode

    Exchange: QuantConnect.Securities.SecurityExchange

    FeeModel: QuantConnect.Orders.Fees.IFeeModel

    FillModel: QuantConnect.Orders.Fills.IFillModel

    Fundamentals: QuantConnect.Data.Fundamental.Fundamentals

    HasData: bool

    High: float

    Holdings: QuantConnect.Securities.SecurityHolding

    HoldStock: bool

    Invested: bool

    IsDelisted: bool

    IsExtendedMarketHours: bool

    IsFillDataForward: bool

    IsTradable: bool

    Leverage: float

    LocalTime: datetime.datetime

    Low: float

    MarginModel: QuantConnect.Securities.IBuyingPowerModel

    Open: float

    OpenInterest: int

    PortfolioModel: QuantConnect.Securities.ISecurityPortfolioModel

    Price: float

    PriceVariationModel: QuantConnect.Securities.IPriceVariationModel

    QuoteCurrency: QuantConnect.Securities.Cash

    Resolution: QuantConnect.Resolution

    SettlementModel: QuantConnect.Securities.ISettlementModel

    SlippageModel: QuantConnect.Orders.Slippage.ISlippageModel

    SubscriptionDataConfig: QuantConnect.Data.SubscriptionDataConfig

    Subscriptions: typing.List[QuantConnect.Data.SubscriptionDataConfig]

    Symbol: QuantConnect.Symbol

    SymbolProperties: QuantConnect.Securities.SymbolProperties

    Type: QuantConnect.SecurityType

    VolatilityModel: QuantConnect.Securities.IVolatilityModel

    Volume: float

    SubscriptionsBag: System.Collections.Concurrent.ConcurrentBag[QuantConnect.Data.SubscriptionDataConfig]

    NullLeverage: Decimal


class SecurityCache(System.object):
    """
    Base class caching caching spot for security data and any other temporary properties.
    
    SecurityCache()
    """
    def AddData(self, data: QuantConnect.Data.BaseData) -> None:
        pass

    def AddDataList(self, data: typing.List[QuantConnect.Data.BaseData], dataType: type, containsFillForwardData: typing.Optional[bool]) -> None:
        pass

    def GetAll(self) -> typing.List[QuantConnect.Securities.T]:
        pass

    @typing.overload
    def GetData(self) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def GetData(self) -> QuantConnect.Securities.T:
        pass

    def GetData(self, *args) -> QuantConnect.Securities.T:
        pass

    def HasData(self, type: type) -> bool:
        pass

    def Reset(self) -> None:
        pass

    @staticmethod
    def ShareTypeCacheInstance(sourceToShare: QuantConnect.Securities.SecurityCache, targetToModify: QuantConnect.Securities.SecurityCache) -> None:
        pass

    def StoreData(self, data: typing.List[QuantConnect.Data.BaseData], dataType: type) -> None:
        pass

    def TryGetValue(self, type: type, data: typing.List) -> bool:
        pass

    AskPrice: float

    AskSize: float

    BidPrice: float

    BidSize: float

    Close: float

    High: float

    Low: float

    Open: float

    OpenInterest: int

    Price: float

    Volume: float



class SecurityCacheDataStoredEventArgs(System.EventArgs):
    """
    Event args for SecurityCache.DataStored event
    
    SecurityCacheDataStoredEventArgs(dataType: Type, data: IReadOnlyList[BaseData])
    """
    @staticmethod # known case of __new__
    def __new__(self, dataType: type, data: typing.List[QuantConnect.Data.BaseData]) -> None:
        pass

    Data: typing.List[QuantConnect.Data.BaseData]

    DataType: type



class SecurityCacheProvider(System.object):
    """
    A helper class that will provide QuantConnect.Securities.SecurityCache instances
    
    SecurityCacheProvider(securityProvider: ISecurityProvider)
    """
    def GetSecurityCache(self, symbol: QuantConnect.Symbol) -> QuantConnect.Securities.SecurityCache:
        pass

    @staticmethod # known case of __new__
    def __new__(self, securityProvider: QuantConnect.Securities.ISecurityProvider) -> None:
        pass


class SecurityDatabaseKey(System.object, System.IEquatable[SecurityDatabaseKey]):
    """
    Represents the key to a single entry in the QuantConnect.Securities.MarketHoursDatabase or the QuantConnect.Securities.SymbolPropertiesDatabase
    
    SecurityDatabaseKey(market: str, symbol: str, securityType: SecurityType)
    """
    @typing.overload
    def Equals(self, other: QuantConnect.Securities.SecurityDatabaseKey) -> bool:
        pass

    @typing.overload
    def Equals(self, obj: object) -> bool:
        pass

    def Equals(self, *args) -> bool:
        pass

    def GetHashCode(self) -> int:
        pass

    @staticmethod
    def Parse(key: str) -> QuantConnect.Securities.SecurityDatabaseKey:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    def __new__(self, market: str, symbol: str, securityType: QuantConnect.SecurityType) -> None:
        pass

    Market: str
    SecurityType: QuantConnect.SecurityType
    Symbol: str
    Wildcard: str


class SecurityDataFilter(System.object, QuantConnect.Securities.Interfaces.ISecurityDataFilter):
    """
    Base class implementation for packet by packet data filtering mechanism to dynamically detect bad ticks.
    
    SecurityDataFilter()
    """
    def Filter(self, vehicle: QuantConnect.Securities.Security, data: QuantConnect.Data.BaseData) -> bool:
        pass


class SecurityExchange(System.object):
    """
    Base exchange class providing information and helper tools for reading the current exchange situation
    
    SecurityExchange(exchangeHours: SecurityExchangeHours)
    """
    def DateIsOpen(self, dateToCheck: datetime.datetime) -> bool:
        pass

    def DateTimeIsOpen(self, dateTime: datetime.datetime) -> bool:
        pass

    def IsClosingSoon(self, minutesToClose: int) -> bool:
        pass

    def IsOpenDuringBar(self, barStartTime: datetime.datetime, barEndTime: datetime.datetime, isExtendedMarketHours: bool) -> bool:
        pass

    def SetLocalDateTimeFrontier(self, newLocalTime: datetime.datetime) -> None:
        pass

    def SetMarketHours(self, marketHoursSegments: typing.List[QuantConnect.Securities.MarketHoursSegment], days: typing.List[System.DayOfWeek]) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours) -> None:
        pass

    ClosingSoon: bool

    ExchangeOpen: bool

    Hours: QuantConnect.Securities.SecurityExchangeHours

    LocalTime: datetime.datetime

    TimeZone: NodaTime.DateTimeZone

    TradingDaysPerYear: int



class SecurityExchangeHours(System.object):
    """
    Represents the schedule of a security exchange. This includes daily regular and extended market hours
                as well as holidays, early closes and late opens.
    
    SecurityExchangeHours(timeZone: DateTimeZone, holidayDates: IEnumerable[DateTime], marketHoursForEachDayOfWeek: IReadOnlyDictionary[DayOfWeek, LocalMarketHours], earlyCloses: IReadOnlyDictionary[DateTime, TimeSpan], lateOpens: IReadOnlyDictionary[DateTime, TimeSpan])
    """
    @staticmethod
    def AlwaysOpen(timeZone: NodaTime.DateTimeZone) -> QuantConnect.Securities.SecurityExchangeHours:
        pass

    def GetMarketHours(self, localDateTime: datetime.datetime) -> QuantConnect.Securities.LocalMarketHours:
        pass

    def GetNextMarketClose(self, localDateTime: datetime.datetime, extendedMarket: bool) -> datetime.datetime:
        pass

    def GetNextMarketOpen(self, localDateTime: datetime.datetime, extendedMarket: bool) -> datetime.datetime:
        pass

    def GetNextTradingDay(self, date: datetime.datetime) -> datetime.datetime:
        pass

    def GetPreviousTradingDay(self, localDate: datetime.datetime) -> datetime.datetime:
        pass

    def IsDateOpen(self, localDateTime: datetime.datetime) -> bool:
        pass

    @typing.overload
    def IsOpen(self, localDateTime: datetime.datetime, extendedMarket: bool) -> bool:
        pass

    @typing.overload
    def IsOpen(self, startLocalDateTime: datetime.datetime, endLocalDateTime: datetime.datetime, extendedMarket: bool) -> bool:
        pass

    def IsOpen(self, *args) -> bool:
        pass

    @staticmethod # known case of __new__
    def __new__(self, timeZone: NodaTime.DateTimeZone, holidayDates: typing.List[datetime.datetime], marketHoursForEachDayOfWeek: System.Collections.Generic.IReadOnlyDictionary[System.DayOfWeek, QuantConnect.Securities.LocalMarketHours], earlyCloses: System.Collections.Generic.IReadOnlyDictionary[datetime.datetime, datetime.timedelta], lateOpens: System.Collections.Generic.IReadOnlyDictionary[datetime.datetime, datetime.timedelta]) -> None:
        pass

    EarlyCloses: System.Collections.Generic.IReadOnlyDictionary[datetime.datetime, datetime.timedelta]

    Holidays: System.Collections.Generic.HashSet[datetime.datetime]

    LateOpens: System.Collections.Generic.IReadOnlyDictionary[datetime.datetime, datetime.timedelta]

    MarketHours: System.Collections.Generic.IReadOnlyDictionary[System.DayOfWeek, QuantConnect.Securities.LocalMarketHours]

    RegularMarketDuration: datetime.timedelta

    TimeZone: NodaTime.DateTimeZone



class SecurityHolding(System.object):
    """
    SecurityHolding is a base class for purchasing and holding a market item which manages the asset portfolio
    
    SecurityHolding(security: Security, currencyConverter: ICurrencyConverter)
    """
    def AddNewFee(self, newFee: float) -> None:
        pass

    def AddNewProfit(self, profitLoss: float) -> None:
        pass

    def AddNewSale(self, saleValue: float) -> None:
        pass

    @typing.overload
    def SetHoldings(self, averagePrice: float, quantity: int) -> None:
        pass

    @typing.overload
    def SetHoldings(self, averagePrice: float, quantity: float) -> None:
        pass

    def SetHoldings(self, *args) -> None:
        pass

    def SetLastTradeProfit(self, lastTradeProfit: float) -> None:
        pass

    def TotalCloseProfit(self) -> float:
        pass

    def UpdateMarketPrice(self, closingPrice: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, security: QuantConnect.Securities.Security, currencyConverter: QuantConnect.Securities.ICurrencyConverter) -> None:
        pass

    AbsoluteHoldingsCost: float

    AbsoluteHoldingsValue: float

    AbsoluteQuantity: float

    AveragePrice: float

    HoldingsCost: float

    HoldingsValue: float

    HoldStock: bool

    Invested: bool

    IsLong: bool

    IsShort: bool

    LastTradeProfit: float

    Leverage: float

    NetProfit: float

    Price: float

    Profit: float

    Quantity: float

    Symbol: QuantConnect.Symbol

    Target: QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget

    TotalFees: float

    TotalSaleVolume: float

    Type: QuantConnect.SecurityType

    UnleveredAbsoluteHoldingsCost: float

    UnleveredHoldingsCost: float

    UnrealizedProfit: float

    UnrealizedProfitPercent: float



class SecurityInitializer(System.object):
    """ Provides static access to the QuantConnect.Securities.SecurityInitializer.Null security initializer """
    Null: NullSecurityInitializer
    __all__: list


class SecurityManager(QuantConnect.ExtendedDictionary[Security], QuantConnect.Interfaces.IExtendedDictionary[Symbol, Security], System.Collections.Generic.IDictionary[Symbol, Security], System.Collections.Generic.ICollection[KeyValuePair[Symbol, Security]], System.Collections.Generic.IEnumerable[KeyValuePair[Symbol, Security]], System.Collections.IEnumerable, System.Collections.Specialized.INotifyCollectionChanged):
    """
    Enumerable security management class for grouping security objects into an array and providing any common properties.
    
    SecurityManager(timeKeeper: ITimeKeeper)
    """
    @typing.overload
    def Add(self, symbol: QuantConnect.Symbol, security: QuantConnect.Securities.Security) -> None:
        pass

    @typing.overload
    def Add(self, security: QuantConnect.Securities.Security) -> None:
        pass

    @typing.overload
    def Add(self, pair: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Securities.Security]) -> None:
        pass

    def Add(self, *args) -> None:
        pass

    def Clear(self) -> None:
        pass

    def Contains(self, pair: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Securities.Security]) -> bool:
        pass

    def ContainsKey(self, symbol: QuantConnect.Symbol) -> bool:
        pass

    def CopyTo(self, array: typing.List[System.Collections.Generic.KeyValuePair], number: int) -> None:
        pass

    @typing.overload
    def CreateSecurity(self, symbol: QuantConnect.Symbol, subscriptionDataConfigList: typing.List[QuantConnect.Data.SubscriptionDataConfig], leverage: float, addToSymbolCache: bool) -> QuantConnect.Securities.Security:
        pass

    @typing.overload
    def CreateSecurity(self, symbol: QuantConnect.Symbol, subscriptionDataConfig: QuantConnect.Data.SubscriptionDataConfig, leverage: float, addToSymbolCache: bool) -> QuantConnect.Securities.Security:
        pass

    def CreateSecurity(self, *args) -> QuantConnect.Securities.Security:
        pass

    @typing.overload
    def Remove(self, pair: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Securities.Security]) -> bool:
        pass

    @typing.overload
    def Remove(self, symbol: QuantConnect.Symbol) -> bool:
        pass

    def Remove(self, *args) -> bool:
        pass

    def SetLiveMode(self, isLiveMode: bool) -> None:
        pass

    def SetSecurityService(self, securityService: QuantConnect.Securities.SecurityService) -> None:
        pass

    def TryGetValue(self, symbol: QuantConnect.Symbol, security: QuantConnect.Securities.Security) -> bool:
        pass

    @staticmethod # known case of __new__
    def __new__(self, timeKeeper: QuantConnect.Interfaces.ITimeKeeper) -> None:
        pass

    Count: int

    IsReadOnly: bool

    Keys: typing.List[QuantConnect.Symbol]

    UtcTime: datetime.datetime

    Values: typing.List[QuantConnect.Securities.Security]


    CollectionChanged: BoundEvent
    Item: indexer#


class SecurityPortfolioManager(QuantConnect.ExtendedDictionary[SecurityHolding], QuantConnect.Interfaces.IExtendedDictionary[Symbol, SecurityHolding], System.Collections.Generic.IDictionary[Symbol, SecurityHolding], System.Collections.Generic.ICollection[KeyValuePair[Symbol, SecurityHolding]], System.Collections.Generic.IEnumerable[KeyValuePair[Symbol, SecurityHolding]], System.Collections.IEnumerable, QuantConnect.Securities.ISecurityProvider):
    """
    Portfolio manager class groups popular properties and makes them accessible through one interface.
                It also provide indexing by the vehicle symbol to get the Security.Holding objects.
    
    SecurityPortfolioManager(securityManager: SecurityManager, transactions: SecurityTransactionManager, defaultOrderProperties: IOrderProperties)
    """
    @typing.overload
    def Add(self, symbol: QuantConnect.Symbol, holding: QuantConnect.Securities.SecurityHolding) -> None:
        pass

    @typing.overload
    def Add(self, pair: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Securities.SecurityHolding]) -> None:
        pass

    def Add(self, *args) -> None:
        pass

    def AddTransactionRecord(self, time: datetime.datetime, transactionProfitLoss: float) -> None:
        pass

    def AddUnsettledCashAmount(self, item: QuantConnect.Securities.UnsettledCashAmount) -> None:
        pass

    def ApplyDividend(self, dividend: QuantConnect.Data.Market.Dividend, liveMode: bool, mode: QuantConnect.DataNormalizationMode) -> None:
        pass

    def ApplySplit(self, split: QuantConnect.Data.Market.Split, liveMode: bool, mode: QuantConnect.DataNormalizationMode) -> None:
        pass

    def Clear(self) -> None:
        pass

    def Contains(self, pair: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Securities.SecurityHolding]) -> bool:
        pass

    def ContainsKey(self, symbol: QuantConnect.Symbol) -> bool:
        pass

    def CopyTo(self, array: typing.List[System.Collections.Generic.KeyValuePair], index: int) -> None:
        pass

    def GetBuyingPower(self, symbol: QuantConnect.Symbol, direction: QuantConnect.Orders.OrderDirection) -> float:
        pass

    @typing.overload
    def GetMarginRemaining(self, totalPortfolioValue: float) -> float:
        pass

    @typing.overload
    def GetMarginRemaining(self, symbol: QuantConnect.Symbol, direction: QuantConnect.Orders.OrderDirection) -> float:
        pass

    def GetMarginRemaining(self, *args) -> float:
        pass

    def InvalidateTotalPortfolioValue(self) -> None:
        pass

    def LogMarginInformation(self, orderRequest: QuantConnect.Orders.OrderRequest) -> None:
        pass

    def ProcessFill(self, fill: QuantConnect.Orders.OrderEvent) -> None:
        pass

    @typing.overload
    def Remove(self, pair: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Securities.SecurityHolding]) -> bool:
        pass

    @typing.overload
    def Remove(self, symbol: QuantConnect.Symbol) -> bool:
        pass

    def Remove(self, *args) -> bool:
        pass

    def ScanForCashSettlement(self, timeUtc: datetime.datetime) -> None:
        pass

    def SetAccountCurrency(self, accountCurrency: str) -> None:
        pass

    @typing.overload
    def SetCash(self, cash: float) -> None:
        pass

    @typing.overload
    def SetCash(self, symbol: str, cash: float, conversionRate: float) -> None:
        pass

    def SetCash(self, *args) -> None:
        pass

    @typing.overload
    def SetMarginCallModel(self, marginCallModel: QuantConnect.Securities.IMarginCallModel) -> None:
        pass

    @typing.overload
    def SetMarginCallModel(self, pyObject: Python.Runtime.PyObject) -> None:
        pass

    def SetMarginCallModel(self, *args) -> None:
        pass

    def TryGetValue(self, symbol: QuantConnect.Symbol, holding: QuantConnect.Securities.SecurityHolding) -> bool:
        pass

    @staticmethod # known case of __new__
    def __new__(self, securityManager: QuantConnect.Securities.SecurityManager, transactions: QuantConnect.Securities.SecurityTransactionManager, defaultOrderProperties: QuantConnect.Interfaces.IOrderProperties) -> None:
        pass

    Cash: float

    CashBook: QuantConnect.Securities.CashBook

    Count: int

    HoldStock: bool

    Invested: bool

    IsReadOnly: bool

    Keys: typing.List[QuantConnect.Symbol]

    MarginCallModel: QuantConnect.Securities.IMarginCallModel

    MarginRemaining: float

    TotalAbsoluteHoldingsCost: float

    TotalFees: float

    TotalHoldingsValue: float

    TotalMarginUsed: float

    TotalPortfolioValue: float

    TotalProfit: float

    TotalSaleVolume: float

    TotalUnleveredAbsoluteHoldingsCost: float

    TotalUnrealisedProfit: float

    TotalUnrealizedProfit: float

    UnsettledCash: float

    UnsettledCashBook: QuantConnect.Securities.CashBook

    Values: typing.List[QuantConnect.Securities.SecurityHolding]

    Securities: QuantConnect.Securities.SecurityManager
    Transactions: QuantConnect.Securities.SecurityTransactionManager

    Item: indexer#


class SecurityPortfolioModel(System.object, QuantConnect.Securities.ISecurityPortfolioModel):
    """
    Provides a default implementation of QuantConnect.Securities.ISecurityPortfolioModel that simply
                applies the fills to the algorithm's portfolio. This implementation is intended to
                handle all security types.
    
    SecurityPortfolioModel()
    """
    def ProcessFill(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, fill: QuantConnect.Orders.OrderEvent) -> None:
        pass


class SecurityProviderExtensions(System.object):
    """ Provides extension methods for the QuantConnect.Securities.ISecurityProvider interface. """
    @staticmethod
    def GetHoldingsQuantity(provider: QuantConnect.Securities.ISecurityProvider, symbol: QuantConnect.Symbol) -> float:
        pass

    __all__: list


class SecuritySeeder(System.object):
    """ Provides access to a null implementation for QuantConnect.Securities.ISecuritySeeder """
    Null: NullSecuritySeeder
    __all__: list


class SecurityService(System.object, QuantConnect.Interfaces.ISecurityService):
    """
    This class implements interface QuantConnect.Interfaces.ISecurityService providing methods for creating new QuantConnect.Securities.Security
    
    SecurityService(cashBook: CashBook, marketHoursDatabase: MarketHoursDatabase, symbolPropertiesDatabase: SymbolPropertiesDatabase, securityInitializerProvider: ISecurityInitializerProvider, registeredTypes: IRegisteredSecurityDataTypesProvider, cacheProvider: SecurityCacheProvider)
    """
    @typing.overload
    def CreateSecurity(self, symbol: QuantConnect.Symbol, subscriptionDataConfigList: typing.List[QuantConnect.Data.SubscriptionDataConfig], leverage: float, addToSymbolCache: bool) -> QuantConnect.Securities.Security:
        pass

    @typing.overload
    def CreateSecurity(self, symbol: QuantConnect.Symbol, subscriptionDataConfig: QuantConnect.Data.SubscriptionDataConfig, leverage: float, addToSymbolCache: bool) -> QuantConnect.Securities.Security:
        pass

    def CreateSecurity(self, *args) -> QuantConnect.Securities.Security:
        pass

    def SetLiveMode(self, isLiveMode: bool) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, cashBook: QuantConnect.Securities.CashBook, marketHoursDatabase: QuantConnect.Securities.MarketHoursDatabase, symbolPropertiesDatabase: QuantConnect.Securities.SymbolPropertiesDatabase, securityInitializerProvider: QuantConnect.Interfaces.ISecurityInitializerProvider, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, cacheProvider: QuantConnect.Securities.SecurityCacheProvider) -> None:
        pass


class SecurityTransactionManager(System.object, QuantConnect.Securities.IOrderProvider):
    """
    Algorithm Transactions Manager - Recording Transactions
    
    SecurityTransactionManager(algorithm: IAlgorithm, security: SecurityManager)
    """
    def AddOrder(self, request: QuantConnect.Orders.SubmitOrderRequest) -> QuantConnect.Orders.OrderTicket:
        pass

    def AddTransactionRecord(self, time: datetime.datetime, transactionProfitLoss: float) -> None:
        pass

    @typing.overload
    def CancelOpenOrders(self) -> typing.List[QuantConnect.Orders.OrderTicket]:
        pass

    @typing.overload
    def CancelOpenOrders(self, symbol: QuantConnect.Symbol, tag: str) -> typing.List[QuantConnect.Orders.OrderTicket]:
        pass

    def CancelOpenOrders(self, *args) -> typing.List[QuantConnect.Orders.OrderTicket]:
        pass

    def CancelOrder(self, orderId: int, orderTag: str) -> QuantConnect.Orders.OrderTicket:
        pass

    def GetIncrementOrderId(self) -> int:
        pass

    @typing.overload
    def GetOpenOrders(self, symbol: QuantConnect.Symbol) -> typing.List[QuantConnect.Orders.Order]:
        pass

    @typing.overload
    def GetOpenOrders(self, filter: typing.Callable[[QuantConnect.Orders.Order], bool]) -> typing.List[QuantConnect.Orders.Order]:
        pass

    def GetOpenOrders(self, *args) -> typing.List[QuantConnect.Orders.Order]:
        pass

    @typing.overload
    def GetOpenOrderTickets(self, symbol: QuantConnect.Symbol) -> typing.List[QuantConnect.Orders.OrderTicket]:
        pass

    @typing.overload
    def GetOpenOrderTickets(self, filter: typing.Callable[[QuantConnect.Orders.OrderTicket], bool]) -> typing.List[QuantConnect.Orders.OrderTicket]:
        pass

    def GetOpenOrderTickets(self, *args) -> typing.List[QuantConnect.Orders.OrderTicket]:
        pass

    def GetOrderByBrokerageId(self, brokerageId: str) -> QuantConnect.Orders.Order:
        pass

    def GetOrderById(self, orderId: int) -> QuantConnect.Orders.Order:
        pass

    def GetOrders(self, filter: typing.Callable[[QuantConnect.Orders.Order], bool]) -> typing.List[QuantConnect.Orders.Order]:
        pass

    def GetOrderTicket(self, orderId: int) -> QuantConnect.Orders.OrderTicket:
        pass

    def GetOrderTickets(self, filter: typing.Callable[[QuantConnect.Orders.OrderTicket], bool]) -> typing.List[QuantConnect.Orders.OrderTicket]:
        pass

    def ProcessRequest(self, request: QuantConnect.Orders.OrderRequest) -> QuantConnect.Orders.OrderTicket:
        pass

    def RemoveOrder(self, orderId: int, tag: str) -> QuantConnect.Orders.OrderTicket:
        pass

    def SetOrderProcessor(self, orderProvider: QuantConnect.Securities.IOrderProcessor) -> None:
        pass

    def UpdateOrder(self, request: QuantConnect.Orders.UpdateOrderRequest) -> QuantConnect.Orders.OrderTicket:
        pass

    def WaitForOrder(self, orderId: int) -> bool:
        pass

    @staticmethod # known case of __new__
    def __new__(self, algorithm: QuantConnect.Interfaces.IAlgorithm, security: QuantConnect.Securities.SecurityManager) -> None:
        pass

    LastOrderId: int

    MarketOrderFillTimeout: datetime.timedelta

    MinimumOrderQuantity: int

    MinimumOrderSize: float

    OrdersCount: int

    TransactionRecord: System.Collections.Generic.Dictionary[datetime.datetime, float]

    UtcTime: datetime.datetime



class StandardDeviationOfReturnsVolatilityModel(QuantConnect.Securities.Volatility.BaseVolatilityModel, QuantConnect.Securities.IVolatilityModel):
    """
    Provides an implementation of QuantConnect.Securities.IVolatilityModel that computes the
                annualized sample standard deviation of daily returns as the volatility of the security
    
    StandardDeviationOfReturnsVolatilityModel(periods: int)
    """
    def GetHistoryRequirements(self, security: QuantConnect.Securities.Security, utcTime: datetime.datetime) -> typing.List[QuantConnect.Data.HistoryRequest]:
        pass

    def Update(self, security: QuantConnect.Securities.Security, data: QuantConnect.Data.BaseData) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, periods: int) -> None:
        pass

    Volatility: float

    SubscriptionDataConfigProvider: QuantConnect.Interfaces.ISubscriptionDataConfigProvider


class SymbolProperties(System.object):
    """
    Represents common properties for a specific security, uniquely identified by market, symbol and security type
    
    SymbolProperties(description: str, quoteCurrency: str, contractMultiplier: Decimal, minimumPriceVariation: Decimal, lotSize: Decimal)
    """
    @staticmethod
    def GetDefault(quoteCurrency: str) -> QuantConnect.Securities.SymbolProperties:
        pass

    @staticmethod # known case of __new__
    def __new__(self, description: str, quoteCurrency: str, contractMultiplier: float, minimumPriceVariation: float, lotSize: float) -> None:
        pass

    ContractMultiplier: float

    Description: str

    LotSize: float

    MinimumPriceVariation: float

    QuoteCurrency: str



class SymbolPropertiesDatabase(System.object):
    """ Provides access to specific properties for various symbols """
    @typing.overload
    def ContainsKey(self, market: str, symbol: str, securityType: QuantConnect.SecurityType) -> bool:
        pass

    @typing.overload
    def ContainsKey(self, market: str, symbol: QuantConnect.Symbol, securityType: QuantConnect.SecurityType) -> bool:
        pass

    def ContainsKey(self, *args) -> bool:
        pass

    @staticmethod
    def FromDataFolder() -> QuantConnect.Securities.SymbolPropertiesDatabase:
        pass

    @typing.overload
    def GetSymbolProperties(self, market: str, symbol: str, securityType: QuantConnect.SecurityType, defaultQuoteCurrency: str) -> QuantConnect.Securities.SymbolProperties:
        pass

    @typing.overload
    def GetSymbolProperties(self, market: str, symbol: QuantConnect.Symbol, securityType: QuantConnect.SecurityType, defaultQuoteCurrency: str) -> QuantConnect.Securities.SymbolProperties:
        pass

    def GetSymbolProperties(self, *args) -> QuantConnect.Securities.SymbolProperties:
        pass

    def TryGetMarket(self, symbol: str, securityType: QuantConnect.SecurityType, market: System.String) -> bool:
        pass


class UniverseManager(System.object, System.Collections.Generic.IDictionary[Symbol, Universe], System.Collections.Generic.ICollection[KeyValuePair[Symbol, Universe]], System.Collections.Generic.IEnumerable[KeyValuePair[Symbol, Universe]], System.Collections.IEnumerable, System.Collections.Specialized.INotifyCollectionChanged):
    """
    Manages the algorithm's collection of universes
    
    UniverseManager()
    """
    @typing.overload
    def Add(self, item: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Data.UniverseSelection.Universe]) -> None:
        pass

    @typing.overload
    def Add(self, key: QuantConnect.Symbol, universe: QuantConnect.Data.UniverseSelection.Universe) -> None:
        pass

    def Add(self, *args) -> None:
        pass

    def Clear(self) -> None:
        pass

    def Contains(self, item: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Data.UniverseSelection.Universe]) -> bool:
        pass

    def ContainsKey(self, key: QuantConnect.Symbol) -> bool:
        pass

    def CopyTo(self, array: typing.List[System.Collections.Generic.KeyValuePair], arrayIndex: int) -> None:
        pass

    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Data.UniverseSelection.Universe]]:
        pass

    @typing.overload
    def Remove(self, item: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Data.UniverseSelection.Universe]) -> bool:
        pass

    @typing.overload
    def Remove(self, key: QuantConnect.Symbol) -> bool:
        pass

    def Remove(self, *args) -> bool:
        pass

    def TryGetValue(self, key: QuantConnect.Symbol, value: QuantConnect.Data.UniverseSelection.Universe) -> bool:
        pass

    ActiveSecurities: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.Symbol, QuantConnect.Securities.Security]

    Count: int

    IsReadOnly: bool

    Keys: typing.List[QuantConnect.Symbol]

    Values: typing.List[QuantConnect.Data.UniverseSelection.Universe]


    CollectionChanged: BoundEvent
    Item: indexer#


class UnsettledCashAmount(System.object):
    """
    Represents a pending cash amount waiting for settlement time
    
    UnsettledCashAmount(settlementTimeUtc: DateTime, currency: str, amount: Decimal)
    """
    @staticmethod # known case of __new__
    def __new__(self, settlementTimeUtc: datetime.datetime, currency: str, amount: float) -> None:
        pass

    Amount: float

    Currency: str

    SettlementTimeUtc: datetime.datetime



class VolatilityModel(System.object):
    """ Provides access to a null implementation for QuantConnect.Securities.IVolatilityModel """
    Null: NullVolatilityModel
    __all__: list


# variables with complex values

