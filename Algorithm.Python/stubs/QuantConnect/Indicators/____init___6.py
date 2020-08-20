from .____init___7 import *
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



class Maximum(QuantConnect.Indicators.WindowIndicator[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents an indicator capable of tracking the maximum value and how many periods ago it occurred

    

    Maximum(period: int)

    Maximum(name: str, period: int)
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

    PeriodsSinceMaximum: int

    WarmUpPeriod: int



class MeanAbsoluteDeviation(QuantConnect.Indicators.WindowIndicator[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period mean absolute deviation.

    

    MeanAbsoluteDeviation(period: int)

    MeanAbsoluteDeviation(name: str, period: int)
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

    Mean: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    WarmUpPeriod: int



class MidPoint(QuantConnect.Indicators.IndicatorBase[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the MidPoint (MIDPOINT)

                The MidPoint is calculated using the following formula:

                MIDPOINT = (Highest Value + Lowest Value) / 2

    

    MidPoint(name: str, period: int)

    MidPoint(period: int)
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



class MidPrice(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the MidPrice (MIDPRICE).

                The MidPrice is calculated using the following formula:

                MIDPRICE = (Highest High + Lowest Low) / 2

    

    MidPrice(name: str, period: int)

    MidPrice(period: int)
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

    WarmUpPeriod: int



class Minimum(QuantConnect.Indicators.WindowIndicator[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents an indicator capable of tracking the minimum value and how many periods ago it occurred

    

    Minimum(period: int)

    Minimum(name: str, period: int)
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

    PeriodsSinceMinimum: int

    WarmUpPeriod: int



class Momentum(QuantConnect.Indicators.WindowIndicator[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period change in a value using the following:

                value_0 - value_n

    

    Momentum(period: int)

    Momentum(name: str, period: int)
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

    WarmUpPeriod: int



class RateOfChange(QuantConnect.Indicators.WindowIndicator[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period rate of change in a value using the following:

                (value_0 - value_n) / value_n

    

    RateOfChange(period: int)

    RateOfChange(name: str, period: int)
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

    WarmUpPeriod: int



class RateOfChangePercent(QuantConnect.Indicators.RateOfChange, QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period percentage rate of change in a value using the following:

                100 * (value_0 - value_n) / value_n

    

    RateOfChangePercent(period: int)

    RateOfChangePercent(name: str, period: int)
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


class MomentumPercent(QuantConnect.Indicators.RateOfChangePercent, QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period percentage rate of change in a value using the following:

                 100 * (value_0 - value_n) / value_n

                

                 This indicator yields the same results of RateOfChangePercent

    

    MomentumPercent(period: int)

    MomentumPercent(name: str, period: int)
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


class MomersionIndicator(QuantConnect.Indicators.WindowIndicator[IndicatorDataPoint], QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Oscillator indicator that measures momentum and mean-reversion over a specified

                period n.

                Source: Harris, Michael. "Momersion Indicator." Price Action Lab.,

                            13 Aug. 2015. Web. http://www.priceactionlab.com/Blog/2015/08/momersion-indicator/.

    

    MomersionIndicator(name: str, minPeriod: Nullable[int], fullPeriod: int)

    MomersionIndicator(minPeriod: Nullable[int], fullPeriod: int)

    MomersionIndicator(fullPeriod: int)
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, minPeriod: typing.Optional[int], fullPeriod: int) -> None:
        pass

    @typing.overload
    def __new__(self, minPeriod: typing.Optional[int], fullPeriod: int) -> None:
        pass

    @typing.overload
    def __new__(self, fullPeriod: int) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool

    WarmUpPeriod: int



class MoneyFlowIndex(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicator[TradeBar], System.IComparable[IIndicator[TradeBar]], System.IComparable, QuantConnect.Indicators.IIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Money Flow Index (MFI) is an oscillator that uses both price and volume to

                 measure buying and selling pressure

                

                 Typical Price = (High + Low + Close)/3

                 Money Flow = Typical Price x Volume

                 Positive Money Flow = Sum of the money flows of all days where the typical

                     price is greater than the previous day's typical price

                 Negative Money Flow = Sum of the money flows of all days where the typical

                     price is less than the previous day's typical price

                 Money Flow Ratio = (14-period Positive Money Flow)/(14-period Negative Money Flow)

                

                 Money Flow Index = 100 x  Positive Money Flow / ( Positive Money Flow + Negative Money Flow)

    

    MoneyFlowIndex(period: int)

    MoneyFlowIndex(name: str, period: int)
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

    NegativeMoneyFlow: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    PositiveMoneyFlow: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]

    PreviousTypicalPrice: float

    WarmUpPeriod: int
