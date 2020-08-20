from .__CandlestickPatterns_1 import *
import typing
import QuantConnect.Indicators.CandlestickPatterns
import datetime

# no functions
# classes

class CandlestickPattern(QuantConnect.Indicators.WindowIndicator[IBaseDataBar], QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """ Abstract base class for a candlestick pattern indicator """
    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        pass


class AbandonedBaby(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Abandoned Baby candlestick pattern

    

    AbandonedBaby(name: str, penetration: Decimal)

    AbandonedBaby(penetration: Decimal)

    AbandonedBaby()
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



class AdvanceBlock(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Advance Block candlestick pattern

    

    AdvanceBlock(name: str)

    AdvanceBlock()
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



class BeltHold(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Belt-hold candlestick pattern indicator

    

    BeltHold(name: str)

    BeltHold()
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



class Breakaway(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Breakaway candlestick pattern indicator

    

    Breakaway(name: str)

    Breakaway()
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



class CandleColor(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Colors of a candle

    

    enum CandleColor, values: Black (-1), White (1)
    """
    value__: int
    Black: 'CandleColor'
    White: 'CandleColor'


class CandleRangeType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Types of candlestick ranges

    

    enum CandleRangeType, values: HighLow (1), RealBody (0), Shadows (2)
    """
    value__: int
    HighLow: 'CandleRangeType'
    RealBody: 'CandleRangeType'
    Shadows: 'CandleRangeType'


class CandleSetting(System.object):
    """
    Represents a candle setting

    

    CandleSetting(rangeType: CandleRangeType, averagePeriod: int, factor: Decimal)
    """
    @staticmethod # known case of __new__
    def __new__(self, rangeType: QuantConnect.Indicators.CandlestickPatterns.CandleRangeType, averagePeriod: int, factor: float) -> None:
        pass

    AveragePeriod: int

    Factor: float

    RangeType: QuantConnect.Indicators.CandlestickPatterns.CandleRangeType



class CandleSettings(System.object):
    """ Candle settings for all candlestick patterns """
    @staticmethod
    def Get(type: QuantConnect.Indicators.CandlestickPatterns.CandleSettingType) -> QuantConnect.Indicators.CandlestickPatterns.CandleSetting:
        pass

    @staticmethod
    def Set(type: QuantConnect.Indicators.CandlestickPatterns.CandleSettingType, setting: QuantConnect.Indicators.CandlestickPatterns.CandleSetting) -> None:
        pass

    __all__: list


class CandleSettingType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Types of candlestick settings

    

    enum CandleSettingType, values: BodyDoji (3), BodyLong (0), BodyShort (2), BodyVeryLong (1), Equal (10), Far (9), Near (8), ShadowLong (4), ShadowShort (6), ShadowVeryLong (5), ShadowVeryShort (7)
    """
    value__: int
    BodyDoji: 'CandleSettingType'
    BodyLong: 'CandleSettingType'
    BodyShort: 'CandleSettingType'
    BodyVeryLong: 'CandleSettingType'
    Equal: 'CandleSettingType'
    Far: 'CandleSettingType'
    Near: 'CandleSettingType'
    ShadowLong: 'CandleSettingType'
    ShadowShort: 'CandleSettingType'
    ShadowVeryLong: 'CandleSettingType'
    ShadowVeryShort: 'CandleSettingType'


class ClosingMarubozu(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Closing Marubozu candlestick pattern indicator

    

    ClosingMarubozu(name: str)

    ClosingMarubozu()
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



class ConcealedBabySwallow(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Concealed Baby Swallow candlestick pattern

    

    ConcealedBabySwallow(name: str)

    ConcealedBabySwallow()
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



class Counterattack(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Counterattack candlestick pattern

    

    Counterattack(name: str)

    Counterattack()
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



class DarkCloudCover(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Dark Cloud Cover candlestick pattern

    

    DarkCloudCover(name: str, penetration: Decimal)

    DarkCloudCover(penetration: Decimal)

    DarkCloudCover()
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



class Doji(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Doji candlestick pattern indicator

    

    Doji(name: str)

    Doji()
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



class DojiStar(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Doji Star candlestick pattern indicator

    

    DojiStar(name: str)

    DojiStar()
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



class DragonflyDoji(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Dragonfly Doji candlestick pattern indicator

    

    DragonflyDoji(name: str)

    DragonflyDoji()
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
