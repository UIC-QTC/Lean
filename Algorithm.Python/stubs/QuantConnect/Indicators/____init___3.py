from .____init___4 import *
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



class ExponentialMovingAverage(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents the traditional exponential moving average indicator (EMA)

    

    ExponentialMovingAverage(name: str, period: int)

    ExponentialMovingAverage(name: str, period: int, smoothingFactor: Decimal)

    ExponentialMovingAverage(period: int)

    ExponentialMovingAverage(period: int, smoothingFactor: Decimal)
    """
    @staticmethod
    def SmoothingFactorDefault(period: int) -> float:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, period: int) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, period: int, smoothingFactor: float) -> None:
        pass

    @typing.overload
    def __new__(self, period: int) -> None:
        pass

    @typing.overload
    def __new__(self, period: int, smoothingFactor: float) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool

    WarmUpPeriod: int



class FilteredIdentity(QuantConnect.Indicators.IndicatorBase[IBaseData], QuantConnect.Indicators.IIndicator[IBaseData], System.IComparable[IIndicator[IBaseData]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Represents an indicator that is a ready after ingesting a single sample and

                always returns the same value as it is given if it passes a filter condition

    

    FilteredIdentity(name: str, filter: Func[IBaseData, bool])
    """
    @staticmethod # known case of __new__
    def __new__(self, name: str, filter: typing.Callable[[QuantConnect.Data.IBaseData], bool]) -> None:
        pass

    IsReady: bool



class FisherTransform(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Fisher transform is a mathematical process which is used to convert any data set to a modified

                 data set whose Probability Distribution Function is approximately Gaussian. Once the Fisher transform

                 is computed, the transformed data can then be analyzed in terms of it's deviation from the mean.

                

                 The equation is y = .5 * ln [ 1 + x / 1 - x ] where

                 x is the input

                 y is the output

                 ln is the natural logarithm

                

                 The Fisher transform has much sharper turning points than other indicators such as MACD

                

                 For more info, read chapter 1 of Cybernetic Analysis for Stocks and Futures by John F. Ehlers

                

                 We are implementing the latest version of this indicator found at Fig. 4 of

                 http://www.mesasoftware.com/papers/UsingTheFisherTransform.pdf

    

    FisherTransform(period: int)

    FisherTransform(name: str, period: int)
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



class FractalAdaptiveMovingAverage(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Fractal Adaptive Moving Average (FRAMA) by John Ehlers

    

    FractalAdaptiveMovingAverage(name: str, n: int, longPeriod: int)

    FractalAdaptiveMovingAverage(n: int, longPeriod: int)

    FractalAdaptiveMovingAverage(n: int)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, n: int, longPeriod: int) -> None:
        pass

    @typing.overload
    def __new__(self, n: int, longPeriod: int) -> None:
        pass

    @typing.overload
    def __new__(self, n: int) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool

    WarmUpPeriod: int



class FunctionalIndicator(QuantConnect.Indicators.IndicatorBase[T], QuantConnect.Indicators.IIndicator[T], System.IComparable[IIndicator[T]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    FunctionalIndicator[T](name: str, computeNextValue: Func[T, Decimal], isReady: Func[IndicatorBase[T], bool])

    FunctionalIndicator[T](name: str, computeNextValue: Func[T, Decimal], isReady: Func[IndicatorBase[T], bool], reset: Action)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, computeNextValue: typing.Callable[[QuantConnect.Indicators.T], float], isReady: typing.Callable[[QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T]], bool]) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, computeNextValue: typing.Callable[[QuantConnect.Indicators.T], float], isReady: typing.Callable[[QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T]], bool], reset: System.Action) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool



class HeikinAshi(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Heikin-Ashi bar (HA)

                The Heikin-Ashi bar is calculated using the following formulas:

                HA_Close[0] = (Open[0] + High[0] + Low[0] + Close[0]) / 4

                HA_Open[0] = (HA_Open[1] + HA_Close[1]) / 2

                HA_High[0] = MAX(High[0], HA_Open[0], HA_Close[0])

                HA_Low[0] = MIN(Low[0], HA_Open[0], HA_Close[0])

    

    HeikinAshi(name: str)

    HeikinAshi()
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str) -> None:
        pass

    @typing.overload
    def __new__(self) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Close: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    High: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    IsReady: bool

    Low: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    Open: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    Volume: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    WarmUpPeriod: int



class HullMovingAverage(QuantConnect.Indicators.IndicatorBase[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Produces a Hull Moving Average as explained at http://www.alanhull.com/hull-moving-average/

                and derived from the instructions for the Excel VBA code at http://finance4traders.blogspot.com/2009/06/how-to-calculate-hull-moving-average.html

    

    HullMovingAverage(name: str, period: int)

    HullMovingAverage(period: int)
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



class IchimokuKinkoHyo(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Ichimoku Kinko Hyo indicator. It consists of the following main indicators:

                Tenkan-sen: (Highest High + Lowest Low) / 2 for the specific period (normally 9)

                Kijun-sen: (Highest High + Lowest Low) / 2 for the specific period (normally 26)

                Senkou A Span: (Tenkan-sen + Kijun-sen )/ 2 from a specific number of periods ago (normally 26)

                Senkou B Span: (Highest High + Lowest Low) / 2 for the specific period (normally 52), from a specific number of periods ago (normally 26)

    

    IchimokuKinkoHyo(tenkanPeriod: int, kijunPeriod: int, senkouAPeriod: int, senkouBPeriod: int, senkouADelayPeriod: int, senkouBDelayPeriod: int)

    IchimokuKinkoHyo(name: str, tenkanPeriod: int, kijunPeriod: int, senkouAPeriod: int, senkouBPeriod: int, senkouADelayPeriod: int, senkouBDelayPeriod: int)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, tenkanPeriod: int, kijunPeriod: int, senkouAPeriod: int, senkouBPeriod: int, senkouADelayPeriod: int, senkouBDelayPeriod: int) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, tenkanPeriod: int, kijunPeriod: int, senkouAPeriod: int, senkouBPeriod: int, senkouADelayPeriod: int, senkouBDelayPeriod: int) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Chikou: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    DelayedKijunSenkouA: QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint]

    DelayedMaximumSenkouB: QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint]

    DelayedMinimumSenkouB: QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint]

    DelayedTenkanSenkouA: QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint]

    IsReady: bool

    Kijun: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    KijunMaximum: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    KijunMinimum: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    SenkouA: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    SenkouB: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    SenkouBMaximum: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    SenkouBMinimum: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    Tenkan: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    TenkanMaximum: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    TenkanMinimum: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    WarmUpPeriod: int
