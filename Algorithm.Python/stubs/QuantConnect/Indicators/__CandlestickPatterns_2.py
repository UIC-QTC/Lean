from .__CandlestickPatterns_3 import *
import typing
import QuantConnect.Indicators.CandlestickPatterns
import datetime



class InvertedHammer(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Inverted Hammer candlestick pattern indicator

    

    InvertedHammer(name: str)

    InvertedHammer()
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

    IsReady: bool



class Kicking(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Kicking candlestick pattern

    

    Kicking(name: str)

    Kicking()
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

    IsReady: bool



class KickingByLength(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Kicking (bull/bear determined by the longer marubozu) candlestick pattern

    

    KickingByLength(name: str)

    KickingByLength()
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

    IsReady: bool



class LadderBottom(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Ladder Bottom candlestick pattern indicator

    

    LadderBottom(name: str)

    LadderBottom()
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

    IsReady: bool



class LongLeggedDoji(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Long Legged Doji candlestick pattern indicator

    

    LongLeggedDoji(name: str)

    LongLeggedDoji()
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

    IsReady: bool



class LongLineCandle(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Long Line Candle candlestick pattern indicator

    

    LongLineCandle(name: str)

    LongLineCandle()
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

    IsReady: bool



class Marubozu(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Marubozu candlestick pattern indicator

    

    Marubozu(name: str)

    Marubozu()
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

    IsReady: bool



class MatchingLow(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Matching Low candlestick pattern indicator

    

    MatchingLow(name: str)

    MatchingLow()
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

    IsReady: bool



class MatHold(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Mat Hold candlestick pattern

    

    MatHold(name: str, penetration: Decimal)

    MatHold(penetration: Decimal)

    MatHold()
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, penetration: float) -> None:
        pass

    @typing.overload
    def __new__(self, penetration: float) -> None:
        pass

    @typing.overload
    def __new__(self) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool



class MorningDojiStar(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Morning Doji Star candlestick pattern

    

    MorningDojiStar(name: str, penetration: Decimal)

    MorningDojiStar(penetration: Decimal)

    MorningDojiStar()
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, penetration: float) -> None:
        pass

    @typing.overload
    def __new__(self, penetration: float) -> None:
        pass

    @typing.overload
    def __new__(self) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool



class MorningStar(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Morning Star candlestick pattern

    

    MorningStar(name: str, penetration: Decimal)

    MorningStar(penetration: Decimal)

    MorningStar()
    """
    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, penetration: float) -> None:
        pass

    @typing.overload
    def __new__(self, penetration: float) -> None:
        pass

    @typing.overload
    def __new__(self) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    IsReady: bool



class OnNeck(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    On-Neck candlestick pattern indicator

    

    OnNeck(name: str)

    OnNeck()
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

    IsReady: bool



class Piercing(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Piercing candlestick pattern

    

    Piercing(name: str)

    Piercing()
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

    IsReady: bool



class RickshawMan(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Rickshaw Man candlestick pattern

    

    RickshawMan(name: str)

    RickshawMan()
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

    IsReady: bool



class RiseFallThreeMethods(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Rising/Falling Three Methods candlestick pattern

    

    RiseFallThreeMethods(name: str)

    RiseFallThreeMethods()
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

    IsReady: bool
