# encoding: utf-8
# module QuantConnect.Indicators calls itself Indicators
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import QuantConnect
import QuantConnect.Data
import QuantConnect.Indicators
import System
import System.Collections.Generic
import System.IO
import typing

# functions

def IIndicator(*args, **kwargs): # real signature unknown
    """
    Represents an indicator that can receive data updates and emit events when the value of
                the indicator has changed.
    """
    pass

# classes

class IIndicatorWarmUpPeriodProvider:
    """ Represents an indicator with a warm up period provider. """
    WarmUpPeriod: int



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


class IndicatorUpdatedHandler(System.MulticastDelegate, System.ICloneable, System.Runtime.Serialization.ISerializable):
    """
    Event handler type for the IndicatorBase.Updated event
    
    IndicatorUpdatedHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender: object, updated: QuantConnect.Indicators.IndicatorDataPoint, callback: System.AsyncCallback, object: object) -> System.IAsyncResult:
        pass

    def EndInvoke(self, result: System.IAsyncResult) -> None:
        pass

    def Invoke(self, sender: object, updated: QuantConnect.Indicators.IndicatorDataPoint) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, object: object, method: System.IntPtr) -> None:
        pass


class IReadOnlyWindow(System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable):
    # no doc
    Count: int

    IsReady: bool

    MostRecentlyRemoved: QuantConnect.Indicators.T

    Samples: float

    Size: int


    Item: indexer#


class RollingWindow(System.object, QuantConnect.Indicators.IReadOnlyWindow[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable):
    """ RollingWindow[T](size: int) """
    def Add(self, item: QuantConnect.Indicators.T) -> None:
        pass

    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Indicators.T]:
        pass

    def Reset(self) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, size: int) -> None:
        pass

    Count: int

    IsReady: bool

    MostRecentlyRemoved: QuantConnect.Indicators.T

    Samples: float

    Size: int


    Item: indexer#


