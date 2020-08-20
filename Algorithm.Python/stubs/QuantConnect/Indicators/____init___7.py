from .____init___8 import *
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



class MovingAverageType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Defines the different types of moving averages

    

    enum MovingAverageType, values: Alma (10), DoubleExponential (4), Exponential (1), Hull (9), Kama (8), LinearWeightedMovingAverage (3), Simple (0), T3 (7), Triangular (6), TripleExponential (5), Wilders (2)
    """
    value__: int
    Alma: 'MovingAverageType'
    DoubleExponential: 'MovingAverageType'
    Exponential: 'MovingAverageType'
    Hull: 'MovingAverageType'
    Kama: 'MovingAverageType'
    LinearWeightedMovingAverage: 'MovingAverageType'
    Simple: 'MovingAverageType'
    T3: 'MovingAverageType'
    Triangular: 'MovingAverageType'
    TripleExponential: 'MovingAverageType'
    Wilders: 'MovingAverageType'


class MovingAverageTypeExtensions(System.object):
    """ Provides extension methods for the MovingAverageType enumeration """
    @staticmethod
    @typing.overload
    def AsIndicator(movingAverageType: QuantConnect.Indicators.MovingAverageType, period: int) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        pass

    @staticmethod
    @typing.overload
    def AsIndicator(movingAverageType: QuantConnect.Indicators.MovingAverageType, name: str, period: int) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        pass

    def AsIndicator(self, *args) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        pass

    __all__: list


class NormalizedAverageTrueRange(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Normalized Average True Range (NATR).

                The Normalized Average True Range is calculated with the following formula:

                NATR = (ATR(period) / Close) * 100

    

    NormalizedAverageTrueRange(name: str, period: int)

    NormalizedAverageTrueRange(period: int)
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



class OnBalanceVolume(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicator[TradeBar], System.IComparable[IIndicator[TradeBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the On Balance Volume (OBV). 

                The On Balance Volume is calculated by determining the price of the current close price and previous close price.

                If the current close price is equivalent to the previous price the OBV remains the same,

                If the current close price is higher the volume of that day is added to the OBV, while a lower close price will

                result in negative value.

    

    OnBalanceVolume()

    OnBalanceVolume(name: str)
    """
    def Reset(self) -> None:
        pass

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



class ParabolicStopAndReverse(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Parabolic SAR Indicator 

                Based on TA-Lib implementation

    

    ParabolicStopAndReverse(name: str, afStart: Decimal, afIncrement: Decimal, afMax: Decimal)

    ParabolicStopAndReverse(afStart: Decimal, afIncrement: Decimal, afMax: Decimal)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, afStart: float, afIncrement: float, afMax: float) -> None:
        pass

    @typing.overload
    def __new__(self, afStart: float, afIncrement: float, afMax: float) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool

    WarmUpPeriod: int



class PercentagePriceOscillator(QuantConnect.Indicators.AbsolutePriceOscillator, QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Percentage Price Oscillator (PPO)

                The Percentage Price Oscillator is calculated using the following formula:

                PPO[i] = 100 * (FastMA[i] - SlowMA[i]) / SlowMA[i]

    

    PercentagePriceOscillator(name: str, fastPeriod: int, slowPeriod: int, movingAverageType: MovingAverageType)

    PercentagePriceOscillator(fastPeriod: int, slowPeriod: int, movingAverageType: MovingAverageType)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, fastPeriod: int, slowPeriod: int, movingAverageType: QuantConnect.Indicators.MovingAverageType) -> None:
        pass

    @typing.overload
    def __new__(self, fastPeriod: int, slowPeriod: int, movingAverageType: QuantConnect.Indicators.MovingAverageType) -> None:
        pass

    def __new__(self, *args) -> None:
        pass


class PythonIndicator(QuantConnect.Indicators.IndicatorBase[IBaseData], QuantConnect.Indicators.IIndicator[IBaseData], System.IComparable[IIndicator[IBaseData]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Provides a wrapper for QuantConnect.Indicators.IndicatorBase implementations written in python

    

    PythonIndicator()

    PythonIndicator(*args: Array[PyObject])

    PythonIndicator(indicator: PyObject)
    """
    def SetIndicator(self, indicator: Python.Runtime.PyObject) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, args: typing.List[Python.Runtime.PyObject]) -> None:
        pass

    @typing.overload
    def __new__(self, indicator: Python.Runtime.PyObject) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool



class RateOfChangeRatio(QuantConnect.Indicators.RateOfChange, QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Rate Of Change Ratio (ROCR). 

                The Rate Of Change Ratio is calculated with the following formula:

                ROCR = price / prevPrice

    

    RateOfChangeRatio(name: str, period: int)

    RateOfChangeRatio(period: int)
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


class RegressionChannel(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Regression Channel indicator extends the QuantConnect.Indicators.LeastSquaresMovingAverage

                with the inclusion of two (upper and lower) channel lines that are distanced from

                the linear regression line by a user defined number of standard deviations.

                Reference: http://www.onlinetradingconcepts.com/TechnicalAnalysis/LinRegChannel.html

    

    RegressionChannel(name: str, period: int, k: Decimal)

    RegressionChannel(period: int, k: Decimal)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, period: int, k: float) -> None:
        pass

    @typing.overload
    def __new__(self, period: int, k: float) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Intercept: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    IsReady: bool

    LinearRegression: QuantConnect.Indicators.LeastSquaresMovingAverage

    LowerChannel: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    Slope: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    UpperChannel: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    WarmUpPeriod: int



class RelativeStrengthIndex(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents the  Relative Strength Index (RSI) developed by K. Welles Wilder.

                You can optionally specified a different moving average type to be used in the computation

    

    RelativeStrengthIndex(period: int, movingAverageType: MovingAverageType)

    RelativeStrengthIndex(name: str, period: int, movingAverageType: MovingAverageType)
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

    AverageGain: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    AverageLoss: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    IsReady: bool

    MovingAverageType: QuantConnect.Indicators.MovingAverageType

    WarmUpPeriod: int
