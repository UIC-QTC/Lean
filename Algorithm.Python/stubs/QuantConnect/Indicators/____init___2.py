from .____init___3 import *
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



class ChandeMomentumOscillator(QuantConnect.Indicators.WindowIndicator[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Chande Momentum Oscillator (CMO).

                CMO calculation is mostly identical to RSI.

                The only difference is in the last step of calculation:

                RSI = gain / (gain+loss)

                CMO = (gain-loss) / (gain+loss)

    

    ChandeMomentumOscillator(period: int)

    ChandeMomentumOscillator(name: str, period: int)
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



class CommodityChannelIndex(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents the traditional commodity channel index (CCI)

                

                 CCI = (Typical Price - 20-period SMA of TP) / (.015 * Mean Deviation)

                 Typical Price (TP) = (High + Low + Close)/3

                 Constant = 0.015

                

                 There are four steps to calculating the Mean Deviation, first, subtract

                 the most recent 20-period average of the typical price from each period's

                 typical price. Second, take the absolute values of these numbers. Third,

                 sum the absolute values. Fourth, divide by the total number of periods (20).

    

    CommodityChannelIndex(period: int, movingAverageType: MovingAverageType)

    CommodityChannelIndex(name: str, period: int, movingAverageType: MovingAverageType)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, period: int, movingAverageType: QuantConnect.Indicators.MovingAverageType) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, period: int, movingAverageType: QuantConnect.Indicators.MovingAverageType) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool

    MovingAverageType: QuantConnect.Indicators.MovingAverageType

    TypicalPriceAverage: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    TypicalPriceMeanDeviation: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    WarmUpPeriod: int



class CompositeIndicator(QuantConnect.Indicators.IndicatorBase[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    CompositeIndicator[T](name: str, left: IndicatorBase[T], right: IndicatorBase[T], composer: IndicatorComposer)

    CompositeIndicator[T](left: IndicatorBase[T], right: IndicatorBase[T], composer: IndicatorComposer)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, left: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], right: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], composer: QuantConnect.Indicators.IndicatorComposer[QuantConnect.Indicators.T]) -> None:
        pass

    @typing.overload
    def __new__(self, left: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], right: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], composer: QuantConnect.Indicators.IndicatorComposer[QuantConnect.Indicators.T]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool

    Left: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T]

    Right: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T]


    IndicatorComposer: type


class ConstantIndicator(QuantConnect.Indicators.IndicatorBase[T], QuantConnect.Indicators.IIndicator[T], System.IComparable[IIndicator[T]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """ ConstantIndicator[T](name: str, value: Decimal) """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, name: str, value: float) -> None:
        pass

    IsReady: bool



class CoppockCurve(QuantConnect.Indicators.IndicatorBase[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    A momentum indicator developed by Edwin “Sedge” Coppock in October 1965.

                The goal of this indicator is to identify long-term buying opportunities in the S&P500 and Dow Industrials.

                Source: http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:coppock_curve

    

    CoppockCurve()

    CoppockCurve(shortRocPeriod: int, longRocPeriod: int, lwmaPeriod: int)

    CoppockCurve(name: str, shortRocPeriod: int, longRocPeriod: int, lwmaPeriod: int)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, shortRocPeriod: int, longRocPeriod: int, lwmaPeriod: int) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, shortRocPeriod: int, longRocPeriod: int, lwmaPeriod: int) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool

    WarmUpPeriod: int



class Delay(QuantConnect.Indicators.WindowIndicator[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    An indicator that delays its input for a certain period

    

    Delay(period: int)

    Delay(name: str, period: int)
    """
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



class DetrendedPriceOscillator(QuantConnect.Indicators.IndicatorBase[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Detrended Price Oscillator is an indicator designed to remove trend from price

                and make it easier to identify cycles.

                DPO does not extend to the last date because it is based on a displaced moving average.

                Is estimated as Price {X/2 + 1} periods ago less the X-period simple moving average.

                E.g.DPO(20) equals price 11 days ago less the 20-day SMA.

    

    DetrendedPriceOscillator(name: str, period: int)

    DetrendedPriceOscillator(period: int)
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



class DonchianChannel(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the upper and lower band of the Donchian Channel.

                The upper band is computed by finding the highest high over the given period.

                The lower band is computed by finding the lowest low over the given period.

                The primary output value of the indicator is the mean of the upper and lower band for 

                the given timeframe.

    

    DonchianChannel(period: int)

    DonchianChannel(upperPeriod: int, lowerPeriod: int)

    DonchianChannel(name: str, period: int)

    DonchianChannel(name: str, upperPeriod: int, lowerPeriod: int)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, period: int) -> None:
        pass

    @typing.overload
    def __new__(self, upperPeriod: int, lowerPeriod: int) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, period: int) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, upperPeriod: int, lowerPeriod: int) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool

    LowerBand: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    UpperBand: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    WarmUpPeriod: int



class DoubleExponentialMovingAverage(QuantConnect.Indicators.IndicatorBase[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Double Exponential Moving Average (DEMA).

                The Double Exponential Moving Average is calculated with the following formula:

                EMA2 = EMA(EMA(t,period),period)

                DEMA = 2 * EMA(t,period) - EMA2

                The Generalized DEMA (GD) is calculated with the following formula:

                GD = (volumeFactor+1) * EMA(t,period) - volumeFactor * EMA2

    

    DoubleExponentialMovingAverage(name: str, period: int, volumeFactor: Decimal)

    DoubleExponentialMovingAverage(period: int, volumeFactor: Decimal)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, period: int, volumeFactor: float) -> None:
        pass

    @typing.overload
    def __new__(self, period: int, volumeFactor: float) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool

    WarmUpPeriod: int
