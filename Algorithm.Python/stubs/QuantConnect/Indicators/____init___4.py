from .____init___5 import *
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



class Identity(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicator[IndicatorDataPoint], System.IComparable[IIndicator[IndicatorDataPoint]], System.IComparable, QuantConnect.Indicators.IIndicator):
    """
    Represents an indicator that is a ready after ingesting a single sample and

                    always returns the same value as it is given.

    

    Identity(name: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, name: str) -> None:
        pass

    IsReady: bool



class IIndicatorWarmUpPeriodProvider:
    """ Represents an indicator with a warm up period provider. """
    WarmUpPeriod: int



class IndicatorBase(System.object, QuantConnect.Indicators.IIndicator[T], System.IComparable[IIndicator[T]], System.IComparable, QuantConnect.Indicators.IIndicator):
    # no doc
    @typing.overload
    def CompareTo(self, other: QuantConnect.Indicators.IIndicator[QuantConnect.Indicators.T]) -> int:
        pass

    @typing.overload
    def CompareTo(self, obj: object) -> int:
        pass

    def CompareTo(self, *args) -> int:
        pass

    def Equals(self, obj: object) -> bool:
        pass

    def Reset(self) -> None:
        pass

    def ToDetailedString(self) -> str:
        pass

    def ToString(self) -> str:
        pass

    @typing.overload
    def Update(self, input: QuantConnect.Data.IBaseData) -> bool:
        pass

    @typing.overload
    def Update(self, time: datetime.datetime, value: float) -> bool:
        pass

    def Update(self, *args) -> bool:
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        pass

    Current: QuantConnect.Indicators.IndicatorDataPoint

    IsReady: bool

    Name: str

    Samples: int


    Updated: BoundEvent


class IndicatorDataPoint(QuantConnect.Data.BaseData, QuantConnect.Data.IBaseData, System.IEquatable[IndicatorDataPoint], System.IComparable[IndicatorDataPoint], System.IComparable):
    """
    Represents a piece of data at a specific time

    

    IndicatorDataPoint()

    IndicatorDataPoint(time: DateTime, value: Decimal)

    IndicatorDataPoint(symbol: Symbol, time: DateTime, value: Decimal)
    """
    @typing.overload
    def CompareTo(self, other: QuantConnect.Indicators.IndicatorDataPoint) -> int:
        pass

    @typing.overload
    def CompareTo(self, obj: object) -> int:
        pass

    def CompareTo(self, *args) -> int:
        pass

    @typing.overload
    def Equals(self, other: QuantConnect.Indicators.IndicatorDataPoint) -> bool:
        pass

    @typing.overload
    def Equals(self, obj: object) -> bool:
        pass

    def Equals(self, *args) -> bool:
        pass

    def GetHashCode(self) -> int:
        pass

    @typing.overload
    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        pass

    @typing.overload
    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, datafeed: QuantConnect.DataFeedEndpoint) -> str:
        pass

    def GetSource(self, *args) -> str:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, stream: System.IO.StreamReader, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, datafeed: QuantConnect.DataFeedEndpoint) -> QuantConnect.Data.BaseData:
        pass

    def Reader(self, *args) -> QuantConnect.Data.BaseData:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, time: datetime.datetime, value: float) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, time: datetime.datetime, value: float) -> None:
        pass

    def __new__(self, *args) -> None:
        pass


class IndicatorExtensions(System.object):
    """ Provides extension methods for Indicator """
    @staticmethod
    @typing.overload
    def EMA(left: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], period: int, smoothingFactor: typing.Optional[float], waitForFirstToReady: bool) -> QuantConnect.Indicators.ExponentialMovingAverage:
        pass

    @staticmethod
    @typing.overload
    def EMA(left: Python.Runtime.PyObject, period: int, smoothingFactor: typing.Optional[float], waitForFirstToReady: bool) -> QuantConnect.Indicators.ExponentialMovingAverage:
        pass

    def EMA(self, *args) -> QuantConnect.Indicators.ExponentialMovingAverage:
        pass

    @staticmethod
    @typing.overload
    def MAX(left: QuantConnect.Indicators.IIndicator, period: int, waitForFirstToReady: bool) -> QuantConnect.Indicators.Maximum:
        pass

    @staticmethod
    @typing.overload
    def MAX(left: Python.Runtime.PyObject, period: int, waitForFirstToReady: bool) -> QuantConnect.Indicators.Maximum:
        pass

    def MAX(self, *args) -> QuantConnect.Indicators.Maximum:
        pass

    @staticmethod
    @typing.overload
    def MIN(left: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], period: int, waitForFirstToReady: bool) -> QuantConnect.Indicators.Minimum:
        pass

    @staticmethod
    @typing.overload
    def MIN(left: Python.Runtime.PyObject, period: int, waitForFirstToReady: bool) -> QuantConnect.Indicators.Minimum:
        pass

    def MIN(self, *args) -> QuantConnect.Indicators.Minimum:
        pass

    @staticmethod
    @typing.overload
    def Minus(left: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], constant: float) -> QuantConnect.Indicators.CompositeIndicator[QuantConnect.Indicators.T]:
        pass

    @staticmethod
    @typing.overload
    def Minus(left: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], right: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T]) -> QuantConnect.Indicators.CompositeIndicator[QuantConnect.Indicators.T]:
        pass

    @staticmethod
    @typing.overload
    def Minus(left: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], right: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], name: str) -> QuantConnect.Indicators.CompositeIndicator[QuantConnect.Indicators.T]:
        pass

    @staticmethod
    @typing.overload
    def Minus(left: Python.Runtime.PyObject, constant: float) -> object:
        pass

    @staticmethod
    @typing.overload
    def Minus(left: Python.Runtime.PyObject, right: Python.Runtime.PyObject, name: str) -> object:
        pass

    def Minus(self, *args) -> object:
        pass

    @staticmethod
    @typing.overload
    def Of(second: QuantConnect.Indicators.T, first: QuantConnect.Indicators.IIndicator, waitForFirstToReady: bool) -> QuantConnect.Indicators.T:
        pass

    @staticmethod
    @typing.overload
    def Of(second: Python.Runtime.PyObject, first: Python.Runtime.PyObject, waitForFirstToReady: bool) -> object:
        pass

    def Of(self, *args) -> object:
        pass

    @staticmethod
    @typing.overload
    def Over(left: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], constant: float) -> QuantConnect.Indicators.CompositeIndicator[QuantConnect.Indicators.T]:
        pass

    @staticmethod
    @typing.overload
    def Over(left: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], right: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T]) -> QuantConnect.Indicators.CompositeIndicator[QuantConnect.Indicators.T]:
        pass

    @staticmethod
    @typing.overload
    def Over(left: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], right: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], name: str) -> QuantConnect.Indicators.CompositeIndicator[QuantConnect.Indicators.T]:
        pass

    @staticmethod
    @typing.overload
    def Over(left: Python.Runtime.PyObject, constant: float) -> object:
        pass

    @staticmethod
    @typing.overload
    def Over(left: Python.Runtime.PyObject, right: Python.Runtime.PyObject, name: str) -> object:
        pass

    def Over(self, *args) -> object:
        pass

    @staticmethod
    @typing.overload
    def Plus(left: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], constant: float) -> QuantConnect.Indicators.CompositeIndicator[QuantConnect.Indicators.T]:
        pass

    @staticmethod
    @typing.overload
    def Plus(left: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], right: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T]) -> QuantConnect.Indicators.CompositeIndicator[QuantConnect.Indicators.T]:
        pass

    @staticmethod
    @typing.overload
    def Plus(left: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], right: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], name: str) -> QuantConnect.Indicators.CompositeIndicator[QuantConnect.Indicators.T]:
        pass

    @staticmethod
    @typing.overload
    def Plus(left: Python.Runtime.PyObject, constant: float) -> object:
        pass

    @staticmethod
    @typing.overload
    def Plus(left: Python.Runtime.PyObject, right: Python.Runtime.PyObject, name: str) -> object:
        pass

    def Plus(self, *args) -> object:
        pass

    @staticmethod
    @typing.overload
    def SMA(left: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], period: int, waitForFirstToReady: bool) -> QuantConnect.Indicators.SimpleMovingAverage:
        pass

    @staticmethod
    @typing.overload
    def SMA(left: Python.Runtime.PyObject, period: int, waitForFirstToReady: bool) -> QuantConnect.Indicators.SimpleMovingAverage:
        pass

    def SMA(self, *args) -> QuantConnect.Indicators.SimpleMovingAverage:
        pass

    @staticmethod
    @typing.overload
    def Times(left: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], constant: float) -> QuantConnect.Indicators.CompositeIndicator[QuantConnect.Indicators.T]:
        pass

    @staticmethod
    @typing.overload
    def Times(left: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], right: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T]) -> QuantConnect.Indicators.CompositeIndicator[QuantConnect.Indicators.T]:
        pass

    @staticmethod
    @typing.overload
    def Times(left: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], right: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], name: str) -> QuantConnect.Indicators.CompositeIndicator[QuantConnect.Indicators.T]:
        pass

    @staticmethod
    @typing.overload
    def Times(left: Python.Runtime.PyObject, constant: float) -> object:
        pass

    @staticmethod
    @typing.overload
    def Times(left: Python.Runtime.PyObject, right: Python.Runtime.PyObject, name: str) -> object:
        pass

    def Times(self, *args) -> object:
        pass

    @staticmethod
    def Update(indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], time: datetime.datetime, value: float) -> bool:
        pass

    @staticmethod
    @typing.overload
    def WeightedBy(value: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.T], weight: QuantConnect.Indicators.TWeight, period: int) -> QuantConnect.Indicators.CompositeIndicator[QuantConnect.Indicators.IndicatorDataPoint]:
        pass

    @staticmethod
    @typing.overload
    def WeightedBy(value: Python.Runtime.PyObject, weight: Python.Runtime.PyObject, period: int) -> QuantConnect.Indicators.CompositeIndicator[QuantConnect.Indicators.IndicatorDataPoint]:
        pass

    def WeightedBy(self, *args) -> QuantConnect.Indicators.CompositeIndicator[QuantConnect.Indicators.IndicatorDataPoint]:
        pass

    __all__: list
