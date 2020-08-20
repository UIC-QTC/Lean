from .__CandlestickPatterns_2 import *
import typing
import QuantConnect.Indicators.CandlestickPatterns
import datetime



class Engulfing(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Engulfing candlestick pattern

    

    Engulfing(name: str)

    Engulfing()
    """
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



class EveningDojiStar(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Evening Doji Star candlestick pattern

    

    EveningDojiStar(name: str, penetration: Decimal)

    EveningDojiStar(penetration: Decimal)

    EveningDojiStar()
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



class EveningStar(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Evening Star candlestick pattern

    

    EveningStar(name: str, penetration: Decimal)

    EveningStar(penetration: Decimal)

    EveningStar()
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



class GapSideBySideWhite(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Up/Down-gap side-by-side white lines candlestick pattern

    

    GapSideBySideWhite(name: str)

    GapSideBySideWhite()
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



class GravestoneDoji(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Gravestone Doji candlestick pattern indicator

    

    GravestoneDoji(name: str)

    GravestoneDoji()
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



class Hammer(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Hammer candlestick pattern indicator

    

    Hammer(name: str)

    Hammer()
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



class HangingMan(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Hanging Man candlestick pattern indicator

    

    HangingMan(name: str)

    HangingMan()
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



class Harami(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Harami candlestick pattern indicator

    

    Harami(name: str)

    Harami()
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



class HaramiCross(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Harami Cross candlestick pattern indicator

    

    HaramiCross(name: str)

    HaramiCross()
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



class HighWaveCandle(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    High-Wave Candle candlestick pattern indicator

    

    HighWaveCandle(name: str)

    HighWaveCandle()
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



class Hikkake(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Hikkake candlestick pattern

    

    Hikkake(name: str)

    Hikkake()
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



class HikkakeModified(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Hikkake Modified candlestick pattern

    

    HikkakeModified(name: str)

    HikkakeModified()
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



class HomingPigeon(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Homing Pigeon candlestick pattern indicator

    

    HomingPigeon(name: str)

    HomingPigeon()
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



class IdenticalThreeCrows(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Identical Three Crows candlestick pattern

    

    IdenticalThreeCrows(name: str)

    IdenticalThreeCrows()
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



class InNeck(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    In-Neck candlestick pattern indicator

    

    InNeck(name: str)

    InNeck()
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
