from .____init___6 import *
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


class IndicatorResult(System.object):
    """
    Represents the result of an indicator's calculations

    

    IndicatorResult(value: Decimal, status: IndicatorStatus)
    """
    @staticmethod # known case of __new__
    def __new__(self, value: float, status: QuantConnect.Indicators.IndicatorStatus) -> None:
        pass

    Status: QuantConnect.Indicators.IndicatorStatus

    Value: float



class IndicatorStatus(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    The possible states returned by QuantConnect.Indicators.IndicatorBase

    

    enum IndicatorStatus, values: InvalidInput (1), MathError (2), Success (0), ValueNotReady (3)
    """
    value__: int
    InvalidInput: 'IndicatorStatus'
    MathError: 'IndicatorStatus'
    Success: 'IndicatorStatus'
    ValueNotReady: 'IndicatorStatus'


class IndicatorUpdatedHandler(System.MulticastDelegate, System.ICloneable, System.Runtime.Serialization.ISerializable):
    """
    Event handler type for the IndicatorBase.Updated event

    

    IndicatorUpdatedHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender: object, updated: QuantConnect.Indicators.IndicatorDataPoint, callback: System.AsyncCallback, object: object) -> System.IAsyncResult:
        pass

    def EndInvoke(self, result: System.IAsyncResult) -> None:
        pass

    def Invoke(self, sender: object, updated: QuantConnect.Indicators.IndicatorDataPoint) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, object: object, method: System.IntPtr) -> None:
        pass


class IntradayVwap(QuantConnect.Indicators.IndicatorBase[BaseData], QuantConnect.Indicators.IIndicator[BaseData], System.IComparable[IIndicator[BaseData]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Defines the canonical intraday VWAP indicator

    

    IntradayVwap(name: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, name: str) -> None:
        pass

    IsReady: bool



class IReadOnlyWindow(System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable):
    # no doc
    Count: int

    IsReady: bool

    MostRecentlyRemoved: QuantConnect.Indicators.T

    Samples: float

    Size: int


    Item: indexer#


class KaufmanAdaptiveMovingAverage(QuantConnect.Indicators.WindowIndicator[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Kaufman Adaptive Moving Average (KAMA).

                The Kaufman Adaptive Moving Average is calculated as explained here:

                http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:kaufman_s_adaptive_moving_average

    

    KaufmanAdaptiveMovingAverage(name: str, period: int, fastEmaPeriod: int, slowEmaPeriod: int)

    KaufmanAdaptiveMovingAverage(period: int, fastEmaPeriod: int, slowEmaPeriod: int)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, period: int, fastEmaPeriod: int, slowEmaPeriod: int) -> None:
        pass

    @typing.overload
    def __new__(self, period: int, fastEmaPeriod: int, slowEmaPeriod: int) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool

    WarmUpPeriod: int



class KeltnerChannels(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator creates a moving average (middle band) with an upper band and lower band

                fixed at k average true range multiples away from the middle band.

    

    KeltnerChannels(period: int, k: Decimal, movingAverageType: MovingAverageType)

    KeltnerChannels(name: str, period: int, k: Decimal, movingAverageType: MovingAverageType)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, period: int, k: float, movingAverageType: QuantConnect.Indicators.MovingAverageType) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, period: int, k: float, movingAverageType: QuantConnect.Indicators.MovingAverageType) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    AverageTrueRange: QuantConnect.Indicators.IndicatorBase[QuantConnect.Data.Market.IBaseDataBar]

    IsReady: bool

    LowerBand: QuantConnect.Indicators.IndicatorBase[QuantConnect.Data.Market.IBaseDataBar]

    MiddleBand: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    UpperBand: QuantConnect.Indicators.IndicatorBase[QuantConnect.Data.Market.IBaseDataBar]

    WarmUpPeriod: int



class LeastSquaresMovingAverage(QuantConnect.Indicators.WindowIndicator[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Least Squares Moving Average (LSMA) first calculates a least squares regression line

                over the preceding time periods, and then projects it forward to the current period. In

                essence, it calculates what the value would be if the regression line continued.

                Source: https://rtmath.net/helpFinAnalysis/html/b3fab79c-f4b2-40fb-8709-fdba43cdb363.htm

    

    LeastSquaresMovingAverage(name: str, period: int)

    LeastSquaresMovingAverage(period: int)
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

    Intercept: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    Slope: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    WarmUpPeriod: int



class LinearWeightedMovingAverage(QuantConnect.Indicators.WindowIndicator[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents the traditional Weighted Moving Average indicator. The weight are linearly

                 distributed according to the number of periods in the indicator.

                

                 For example, a 4 period indicator will have a numerator of (4 * window[0]) + (3 * window[1]) + (2 * window[2]) + window[3]

                 and a denominator of 4 + 3 + 2 + 1 = 10

                

                 During the warm up period, IsReady will return false, but the LWMA will still be computed correctly because

                 the denominator will be the minimum of Samples factorial or Size factorial and

                 the computation iterates over that minimum value.

                

                 The RollingWindow of inputs is created when the indicator is created.

                 A RollingWindow of LWMAs is not saved.  That is up to the caller.

    

    LinearWeightedMovingAverage(name: str, period: int)

    LinearWeightedMovingAverage(period: int)
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

    WarmUpPeriod: int



class LogReturn(QuantConnect.Indicators.WindowIndicator[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents the LogReturn indicator (LOGR)

                - log returns are useful for identifying price convergence/divergence in a given period

                - logr = log (current price / last price in period)

    

    LogReturn(name: str, period: int)

    LogReturn(period: int)
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

    WarmUpPeriod: int



class MassIndex(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicator[TradeBar], System.IComparable[IIndicator[TradeBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Mass Index uses the high-low range to identify trend reversals based on range expansions.

                In this sense, the Mass Index is a volatility indicator that does not have a directional

                bias. Instead, the Mass Index identifies range bulges that can foreshadow a reversal of the

                current trend. Developed by Donald Dorsey.

    

    MassIndex(name: str, emaPeriod: int, sumPeriod: int)

    MassIndex(emaPeriod: int, sumPeriod: int)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, emaPeriod: int, sumPeriod: int) -> None:
        pass

    @typing.overload
    def __new__(self, emaPeriod: int, sumPeriod: int) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool

    WarmUpPeriod: int
