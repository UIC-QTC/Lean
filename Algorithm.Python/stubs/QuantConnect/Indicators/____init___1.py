from .____init___2 import *
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


class ArmsIndex(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicator[TradeBar], System.IComparable[IIndicator[TradeBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Arms Index, also called the Short-Term Trading Index (TRIN) 

                is a technical analysis indicator that compares the number of advancing 

                and declining stocks (AD Ratio) to advancing and declining volume (AD volume).

    

    ArmsIndex(name: str)
    """
    def AddStock(self, symbol: QuantConnect.Symbol) -> None:
        pass

    def RemoveStock(self, symbol: QuantConnect.Symbol) -> None:
        pass

    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, name: str) -> None:
        pass

    ADRatio: QuantConnect.Indicators.AdvanceDeclineRatio

    ADVRatio: QuantConnect.Indicators.AdvanceDeclineVolumeRatio

    IsReady: bool

    WarmUpPeriod: int



class ArnaudLegouxMovingAverage(QuantConnect.Indicators.WindowIndicator[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Smooth and high sensitive moving Average. This moving average reduce lag of the information

                but still being smooth to reduce noises.

                Is a weighted moving average, which weights have a Normal shape;

                the parameters Sigma and Offset affect the kurtosis and skewness of the weights respectively.

                Source: http://www.arnaudlegoux.com/index.html

    

    ArnaudLegouxMovingAverage(name: str, period: int, sigma: int, offset: Decimal)

    ArnaudLegouxMovingAverage(name: str, period: int)

    ArnaudLegouxMovingAverage(period: int, sigma: int, offset: Decimal)

    ArnaudLegouxMovingAverage(period: int)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, period: int, sigma: int, offset: float) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, period: int) -> None:
        pass

    @typing.overload
    def __new__(self, period: int, sigma: int, offset: float) -> None:
        pass

    @typing.overload
    def __new__(self, period: int) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    WarmUpPeriod: int



class BarIndicator(QuantConnect.Indicators.IndicatorBase[IBaseDataBar], QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    The BarIndicator is an indicator that accepts IBaseDataBar data as its input.

                

                This type is more of a shim/typedef to reduce the need to refer to things as IndicatorBase<IBaseDataBar>
    """
    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        pass


class AroonOscillator(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Aroon Oscillator is the difference between AroonUp and AroonDown. The value of this

                indicator fluctuates between -100 and +100. An upward trend bias is present when the oscillator

                is positive, and a negative trend bias is present when the oscillator is negative. AroonUp/Down

                values over 75 identify strong trends in their respective direction.

    

    AroonOscillator(upPeriod: int, downPeriod: int)

    AroonOscillator(name: str, upPeriod: int, downPeriod: int)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, upPeriod: int, downPeriod: int) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, upPeriod: int, downPeriod: int) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    AroonDown: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    AroonUp: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    IsReady: bool

    WarmUpPeriod: int



class AverageDirectionalIndex(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes Average Directional Index which measures trend strength without regard to trend direction.

                Firstly, it calculates the Directional Movement and the True Range value, and then the values are accumulated and smoothed

                using a custom smoothing method proposed by Wilder. For an n period smoothing, 1/n of each period's value is added to the total period.

                From these accumulated values we are therefore able to derived the 'Positive Directional Index' (+DI) and 'Negative Directional Index' (-DI)

                which is used to calculate the Average Directional Index.

                Computation source:

                https://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:average_directional_index_adx

    

    AverageDirectionalIndex(period: int)

    AverageDirectionalIndex(name: str, period: int)
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

    NegativeDirectionalIndex: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    PositiveDirectionalIndex: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    WarmUpPeriod: int



class AverageDirectionalMovementIndexRating(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Average Directional Movement Index Rating (ADXR). 

                The Average Directional Movement Index Rating is calculated with the following formula:

                ADXR[i] = (ADX[i] + ADX[i - period + 1]) / 2

    

    AverageDirectionalMovementIndexRating(name: str, period: int)

    AverageDirectionalMovementIndexRating(period: int)
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

    ADX: QuantConnect.Indicators.AverageDirectionalIndex

    IsReady: bool

    WarmUpPeriod: int



class AverageTrueRange(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The AverageTrueRange indicator is a measure of volatility introduced by Welles Wilder in his

                 book: New Concepts in Technical Trading Systems. This indicator computes the TrueRange and then

                 smoothes the TrueRange over a given period.

                

                 TrueRange is defined as the maximum of the following:

                   High - Low

                   ABS(High - PreviousClose)

                   ABS(Low - PreviousClose)

    

    AverageTrueRange(name: str, period: int, movingAverageType: MovingAverageType)

    AverageTrueRange(period: int, movingAverageType: MovingAverageType)
    """
    @staticmethod
    def ComputeTrueRange(previous: QuantConnect.Data.Market.IBaseDataBar, current: QuantConnect.Data.Market.IBaseDataBar) -> float:
        pass

    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, period: int, movingAverageType: QuantConnect.Indicators.MovingAverageType) -> None:
        pass

    @typing.overload
    def __new__(self, period: int, movingAverageType: QuantConnect.Indicators.MovingAverageType) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool

    TrueRange: QuantConnect.Indicators.IndicatorBase[QuantConnect.Data.Market.IBaseDataBar]

    WarmUpPeriod: int



class BalanceOfPower(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Balance Of Power (BOP).

                The Balance Of Power is calculated with the following formula:

                BOP = (Close - Open) / (High - Low)

    

    BalanceOfPower()

    BalanceOfPower(name: str)
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



class BollingerBands(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator creates a moving average (middle band) with an upper band and lower band

                fixed at k standard deviations above and below the moving average.

    

    BollingerBands(period: int, k: Decimal, movingAverageType: MovingAverageType)

    BollingerBands(name: str, period: int, k: Decimal, movingAverageType: MovingAverageType)
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

    BandWidth: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    IsReady: bool

    LowerBand: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    MiddleBand: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    MovingAverageType: QuantConnect.Indicators.MovingAverageType

    PercentB: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    Price: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    StandardDeviation: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    UpperBand: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    WarmUpPeriod: int
