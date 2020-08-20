from .____init___5 import *
import typing
import System.Linq.Expressions
import System.Dynamic
import System.Collections.Generic
import System.Collections.Concurrent
import System.Collections
import System
import QuantConnect.Securities.Interfaces
import QuantConnect.Securities
import QuantConnect.Orders.Slippage
import QuantConnect.Orders.Fills
import QuantConnect.Orders.Fees
import QuantConnect.Orders
import QuantConnect.Interfaces
import QuantConnect.Indicators
import QuantConnect.Data.UniverseSelection
import QuantConnect.Data.Market
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect.Brokerages
import QuantConnect.Algorithm.Framework.Portfolio
import QuantConnect
import Python.Runtime
import NodaTime
import datetime


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
    Closed: 'MarketHoursState'
    Market: 'MarketHoursState'
    PostMarket: 'MarketHoursState'
    PreMarket: 'MarketHoursState'


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

    def TryGetType(self, name: str, type: type) -> bool:
        pass

    def UnregisterType(self, type: type) -> bool:
        pass

    Null: 'RegisteredSecurityDataTypesProvider'


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
