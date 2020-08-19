# encoding: utf-8
# module QuantConnect.Securities.Future calls itself Future
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import Python.Runtime
import QuantConnect
import QuantConnect.Data
import QuantConnect.Securities
import System
import System.Collections.Concurrent
import typing

# no functions
# classes

class EmptyFutureChainProvider(System.object, QuantConnect.Interfaces.IFutureChainProvider):
    """
    An implementation of QuantConnect.Interfaces.IFutureChainProvider that always returns an empty list of contracts
    
    EmptyFutureChainProvider()
    """
    def GetFutureContractList(self, symbol: QuantConnect.Symbol, date: datetime.datetime) -> typing.List[QuantConnect.Symbol]:
        pass


class Future(QuantConnect.Securities.Security, QuantConnect.Interfaces.ISecurityPrice, QuantConnect.Securities.IDerivativeSecurity):
    """
    Futures Security Object Implementation for Futures Assets
    
    Future(exchangeHours: SecurityExchangeHours, config: SubscriptionDataConfig, quoteCurrency: Cash, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider)
    Future(symbol: Symbol, exchangeHours: SecurityExchangeHours, quoteCurrency: Cash, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider, securityCache: SecurityCache)
    """
    @typing.overload
    def SetFilter(self, minExpiry: datetime.timedelta, maxExpiry: datetime.timedelta) -> None:
        pass

    @typing.overload
    def SetFilter(self, minExpiryDays: int, maxExpiryDays: int) -> None:
        pass

    @typing.overload
    def SetFilter(self, universeFunc: typing.Callable[[QuantConnect.Securities.FutureFilterUniverse], QuantConnect.Securities.FutureFilterUniverse]) -> None:
        pass

    @typing.overload
    def SetFilter(self, universeFunc: Python.Runtime.PyObject) -> None:
        pass

    def SetFilter(self, *args) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, config: QuantConnect.Data.SubscriptionDataConfig, quoteCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.SymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, quoteCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.SymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, securityCache: QuantConnect.Securities.SecurityCache) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    ContractFilter: QuantConnect.Securities.IDerivativeSecurityFilter

    Expiry: datetime.datetime

    IsFutureChain: bool

    IsFutureContract: bool

    SettlementType: QuantConnect.SettlementType

    Underlying: QuantConnect.Securities.Security

    SubscriptionsBag: System.Collections.Concurrent.ConcurrentBag[QuantConnect.Data.SubscriptionDataConfig]

    DefaultSettlementDays: int
    DefaultSettlementTime: TimeSpan


class FutureCache(QuantConnect.Securities.SecurityCache):
    """
    Future specific caching support
    
    FutureCache()
    """

class FutureExchange(QuantConnect.Securities.SecurityExchange):
    """
    Future exchange class - information and helper tools for future exchange properties
    
    FutureExchange(exchangeHours: SecurityExchangeHours)
    """
    @staticmethod # known case of __new__
    def __new__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours) -> None:
        pass

    TradingDaysPerYear: int



class FutureHolding(QuantConnect.Securities.SecurityHolding):
    """
    Future holdings implementation of the base securities class
    
    FutureHolding(security: Security, currencyConverter: ICurrencyConverter)
    """
    @staticmethod # known case of __new__
    def __new__(self, security: QuantConnect.Securities.Security, currencyConverter: QuantConnect.Securities.ICurrencyConverter) -> None:
        pass



class FutureMarginModel(QuantConnect.Securities.SecurityMarginModel, QuantConnect.Securities.IBuyingPowerModel):
    """
    Represents a simple margin model for margin futures. Margin file contains Initial and Maintenance margins
    
    FutureMarginModel(requiredFreeBuyingPowerPercent: Decimal, security: Security)
    """
    def GetLeverage(self, security: QuantConnect.Securities.Security) -> float:
        pass

    def GetMaximumOrderQuantityForTargetBuyingPower(self, parameters: QuantConnect.Securities.GetMaximumOrderQuantityForTargetBuyingPowerParameters) -> QuantConnect.Securities.GetMaximumOrderQuantityResult:
        pass

    def SetLeverage(self, security: QuantConnect.Securities.Security, leverage: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, requiredFreeBuyingPowerPercent: float, security: QuantConnect.Securities.Security) -> None:
        pass

    EnableIntradayMargins: bool

    InitialIntradayMarginRequirement: float

    InitialOvernightMarginRequirement: float

    MaintenanceIntradayMarginRequirement: float

    MaintenanceOvernightMarginRequirement: float

    RequiredFreeBuyingPowerPercent: float


class FuturesExpiryFunctions(System.object):
    """
    Calculate the date of a futures expiry given an expiry month and year
    
    FuturesExpiryFunctions()
    """
    @staticmethod
    def FuturesExpiryFunction(symbol: QuantConnect.Symbol) -> typing.Callable[[datetime.datetime], datetime.datetime]:
        pass

    DairyReportDates: Dictionary[DateTime, DateTime]
    EnbridgeNoticeOfShipmentDates: Dictionary[DateTime, DateTime]
    FuturesExpiryDictionary: Dictionary[Symbol, Func[DateTime, DateTime]]


class FuturesExpiryUtilityFunctions(System.object):
    """ Class to implement common functions used in FuturesExpiryFunctions """
    @staticmethod
    def AddBusinessDays(time: datetime.datetime, n: int, useEquityHolidays: bool, holidayList: typing.List[datetime.datetime]) -> datetime.datetime:
        pass

    @staticmethod
    def DairyLastTradeDate(time: datetime.datetime, lastTradeTime: typing.Optional[datetime.timedelta]) -> datetime.datetime:
        pass

    @staticmethod
    def ExpiresInPreviousMonth(underlying: str) -> int:
        pass

    @staticmethod
    def LastThursday(time: datetime.datetime) -> datetime.datetime:
        pass

    @staticmethod
    def LastWeekday(time: datetime.datetime, dayofWeek: System.DayOfWeek) -> datetime.datetime:
        pass

    @staticmethod
    def NotHoliday(time: datetime.datetime) -> bool:
        pass

    @staticmethod
    def NotPrecededByHoliday(thursday: datetime.datetime) -> bool:
        pass

    @staticmethod
    def NthBusinessDay(time: datetime.datetime, nthBusinessDay: int, additionalHolidays: typing.List[datetime.datetime]) -> datetime.datetime:
        pass

    @staticmethod
    def NthFriday(time: datetime.datetime, n: int) -> datetime.datetime:
        pass

    @staticmethod
    def NthLastBusinessDay(time: datetime.datetime, n: int, holidayList: typing.List[datetime.datetime]) -> datetime.datetime:
        pass

    @staticmethod
    def NthWeekday(time: datetime.datetime, n: int, dayofWeek: System.DayOfWeek) -> datetime.datetime:
        pass

    @staticmethod
    def SecondFriday(time: datetime.datetime) -> datetime.datetime:
        pass

    @staticmethod
    def ThirdFriday(time: datetime.datetime) -> datetime.datetime:
        pass

    @staticmethod
    def ThirdWednesday(time: datetime.datetime) -> datetime.datetime:
        pass

    __all__: list


