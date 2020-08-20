from .____init___10 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Indicators
import QuantConnect.Data.Market
import QuantConnect.Data
import QuantConnect
import Python.Runtime
import datetime



class TripleExponentialMovingAverage(QuantConnect.Indicators.IndicatorBase[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Triple Exponential Moving Average (TEMA). 

                The Triple Exponential Moving Average is calculated with the following formula:

                EMA1 = EMA(t,period)

                EMA2 = EMA(EMA(t,period),period)

                EMA3 = EMA(EMA(EMA(t,period),period),period)

                TEMA = 3 * EMA1 - 3 * EMA2 + EMA3

    

    TripleExponentialMovingAverage(name: str, period: int)

    TripleExponentialMovingAverage(period: int)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, period: int) -> None:
        pass

    @typing.overload
    def __new__(self, period: int) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool

    WarmUpPeriod: int



class Trix(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the TRIX (1-period ROC of a Triple EMA)

                The TRIX is calculated as explained here:

                http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:trix

    

    Trix(name: str, period: int)

    Trix(period: int)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, period: int) -> None:
        pass

    @typing.overload
    def __new__(self, period: int) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool

    WarmUpPeriod: int



class TrueRange(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the True Range (TR).

                The True Range is the greatest of the following values:

                value1 = distance from today's high to today's low.

                value2 = distance from yesterday's close to today's high.

                value3 = distance from yesterday's close to today's low.

    

    TrueRange()

    TrueRange(name: str)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, name: str) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool

    WarmUpPeriod: int



class UltimateOscillator(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Ultimate Oscillator (ULTOSC)

                The Ultimate Oscillator is calculated as explained here:

                http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:ultimate_oscillator

    

    UltimateOscillator(period1: int, period2: int, period3: int)

    UltimateOscillator(name: str, period1: int, period2: int, period3: int)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, period1: int, period2: int, period3: int) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, period1: int, period2: int, period3: int) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool

    WarmUpPeriod: int



class VolumeWeightedAveragePriceIndicator(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicator[TradeBar], System.IComparable[IIndicator[TradeBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Volume Weighted Average Price (VWAP) Indicator:

                It is calculated by adding up the dollars traded for every transaction (price multiplied

                by number of shares traded) and then dividing by the total shares traded for the day.

    

    VolumeWeightedAveragePriceIndicator(period: int)

    VolumeWeightedAveragePriceIndicator(name: str, period: int)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, period: int) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, period: int) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool

    WarmUpPeriod: int



class WilderMovingAverage(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents the moving average indicator defined by Welles Wilder in his book:

                New Concepts in Technical Trading Systems.

    

    WilderMovingAverage(name: str, period: int)

    WilderMovingAverage(period: int)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, period: int) -> None:
        pass

    @typing.overload
    def __new__(self, period: int) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool

    WarmUpPeriod: int



class WilliamsPercentR(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Williams %R, or just %R, is the current closing price in relation to the high and low of

                the past N days (for a given N). The value of this indicator fluctuates between -100 and 0.

                The symbol is said to be oversold when the oscillator is below -80%,

                and overbought when the oscillator is above -20%.

    

    WilliamsPercentR(period: int)

    WilliamsPercentR(name: str, period: int)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, period: int) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, period: int) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool

    Maximum: QuantConnect.Indicators.Maximum

    Minimum: QuantConnect.Indicators.Minimum

    WarmUpPeriod: int



class WindowIdentity(QuantConnect.Indicators.WindowIndicator[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Represents an indicator that is a ready after ingesting enough samples (# samples > period) 

                and always returns the same value as it is given.

    

    WindowIdentity(name: str, period: int)

    WindowIdentity(period: int)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, period: int) -> None:
        pass

    @typing.overload
    def __new__(self, period: int) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool



class WindowIndicator(QuantConnect.Indicators.IndicatorBase[T], QuantConnect.Indicators.IIndicator[T], System.IComparable[IIndicator[T]], System.IComparable, QuantConnect.Indicators.IIndicator):
    # no doc
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        pass

    IsReady: bool

    Period: int

# classes

class IIndicatorWarmUpPeriodProvider:
    """ Represents an indicator with a warm up period provider. """
    WarmUpPeriod: int



class IndicatorDataPoint(QuantConnect.Data.BaseData, QuantConnect.Data.IBaseData, System.IEquatable[IndicatorDataPoint], System.IComparable[IndicatorDataPoint], System.IComparable):
    """
    Represents a piece of data at a specific time

    

    IndicatorDataPoint()

    IndicatorDataPoint(time: DateTime, value: Decimal)

    IndicatorDataPoint(symbol: Symbol, time: DateTime, value: Decimal)
    """
    @typing.overload
    def CompareTo(self, other: QuantConnect.Indicators.IndicatorDataPoint) -> int:
        pass

    @typing.overload
    def CompareTo(self, obj: object) -> int:
        pass

    def CompareTo(self, *args) -> int:
        pass

    @typing.overload
    def Equals(self, other: QuantConnect.Indicators.IndicatorDataPoint) -> bool:
        pass

    @typing.overload
    def Equals(self, obj: object) -> bool:
        pass

    def Equals(self, *args) -> bool:
        pass

    def GetHashCode(self) -> int:
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

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, time: datetime.datetime, value: float) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, time: datetime.datetime, value: float) -> None:
        pass

    def __new__(self, *args) -> None:
        pass
