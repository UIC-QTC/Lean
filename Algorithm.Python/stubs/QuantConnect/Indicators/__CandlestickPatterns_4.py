import typing
import QuantConnect.Indicators.CandlestickPatterns
import datetime



class TwoCrows(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Two Crows candlestick pattern indicator

    

    TwoCrows(name: str)

    TwoCrows()
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



class UniqueThreeRiver(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Unique Three River candlestick pattern

    

    UniqueThreeRiver(name: str)

    UniqueThreeRiver()
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



class UpDownGapThreeMethods(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Up/Down Gap Three Methods candlestick pattern

    

    UpDownGapThreeMethods(name: str)

    UpDownGapThreeMethods()
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



class UpsideGapTwoCrows(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern, QuantConnect.Indicators.IIndicator[IBaseDataBar], System.IComparable[IIndicator[IBaseDataBar]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Upside Gap Two Crows candlestick pattern

    

    UpsideGapTwoCrows(name: str)

    UpsideGapTwoCrows()
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
