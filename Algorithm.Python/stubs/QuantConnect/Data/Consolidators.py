from .__Consolidators_1 import *
import typing
import System
import QuantConnect.Data.Market
import QuantConnect.Data.Consolidators
import QuantConnect.Data
import QuantConnect
import Python.Runtime
import datetime

# functions

def FilteredIdentityDataConsolidator(*args, **kwargs): # real signature unknown
    """ Provides factory methods for creating instances of QuantConnect.Data.Consolidators.FilteredIdentityDataConsolidator """
    pass

def RenkoConsolidator(barSize, type): # real signature unknown; restored from __doc__
    """
    This consolidator can transform a stream of QuantConnect.Data.BaseData instances into a stream of QuantConnect.Data.Market.RenkoBar

    

    RenkoConsolidator(barSize: Decimal, type: RenkoType)

    RenkoConsolidator(barSize: Decimal, evenBars: bool)

    RenkoConsolidator(barSize: Decimal, selector: Func[IBaseData, Decimal], volumeSelector: Func[IBaseData, Decimal], evenBars: bool)

    RenkoConsolidator(barSize: Decimal, selector: PyObject, volumeSelector: PyObject, evenBars: bool)
    """
    pass

# classes

class BaseDataConsolidator(QuantConnect.Data.Consolidators.TradeBarConsolidatorBase[BaseData], QuantConnect.Data.Consolidators.IDataConsolidator, System.IDisposable):
    """
    Type capable of consolidating trade bars from any base data instance

    

    BaseDataConsolidator(period: TimeSpan)

    BaseDataConsolidator(maxCount: int)

    BaseDataConsolidator(maxCount: int, period: TimeSpan)

    BaseDataConsolidator(func: Func[DateTime, CalendarInfo])

    BaseDataConsolidator(pyfuncobj: PyObject)
    """
    @staticmethod
    def FromResolution(resolution: QuantConnect.Resolution) -> QuantConnect.Data.Consolidators.BaseDataConsolidator:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, period: datetime.timedelta) -> None:
        pass

    @typing.overload
    def __new__(self, maxCount: int) -> None:
        pass

    @typing.overload
    def __new__(self, maxCount: int, period: datetime.timedelta) -> None:
        pass

    @typing.overload
    def __new__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        pass

    @typing.overload
    def __new__(self, pyfuncobj: Python.Runtime.PyObject) -> None:
        pass

    def __new__(self, *args) -> None:
        pass



class Calendar(System.object):
    """ Helper class that provides System.Func used to define consolidation calendar """
    __all__: list


class CalendarInfo(System.object):
    """ CalendarInfo(start: DateTime, period: TimeSpan) """
    @staticmethod # known case of __new__
    def __new__(self, start: datetime.datetime, period: datetime.timedelta) -> None:
        pass

    Period: datetime.timedelta
    Start: datetime.datetime

class CalendarType(System.object):
    # no doc
    __all__: list


class DataConsolidatedHandler(System.MulticastDelegate, System.ICloneable, System.Runtime.Serialization.ISerializable):
    """
    Event handler type for the IDataConsolidator.DataConsolidated event

    

    DataConsolidatedHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender: object, consolidated: QuantConnect.Data.IBaseData, callback: System.AsyncCallback, object: object) -> System.IAsyncResult:
        pass

    def EndInvoke(self, result: System.IAsyncResult) -> None:
        pass

    def Invoke(self, sender: object, consolidated: QuantConnect.Data.IBaseData) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, object: object, method: System.IntPtr) -> None:
        pass


class DataConsolidator(System.object, QuantConnect.Data.Consolidators.IDataConsolidator, System.IDisposable):
    # no doc
    def Dispose(self) -> None:
        pass

    def Scan(self, currentLocalTime: datetime.datetime) -> None:
        pass

    @typing.overload
    def Update(self, data: QuantConnect.Data.IBaseData) -> None:
        pass

    @typing.overload
    def Update(self, data: QuantConnect.Data.Consolidators.TInput) -> None:
        pass

    def Update(self, *args) -> None:
        pass

    Consolidated: QuantConnect.Data.IBaseData

    InputType: type

    OutputType: type

    WorkingData: QuantConnect.Data.IBaseData


    DataConsolidated: BoundEvent


class DynamicDataConsolidator(QuantConnect.Data.Consolidators.TradeBarConsolidatorBase[DynamicData], QuantConnect.Data.Consolidators.IDataConsolidator, System.IDisposable):
    """
    A data csolidator that can make trade bars from DynamicData derived types. This is useful for

                aggregating Quandl and other highly flexible dynamic custom data types.

    

    DynamicDataConsolidator(period: TimeSpan)

    DynamicDataConsolidator(maxCount: int)

    DynamicDataConsolidator(maxCount: int, period: TimeSpan)

    DynamicDataConsolidator(func: Func[DateTime, CalendarInfo])
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, period: datetime.timedelta) -> None:
        pass

    @typing.overload
    def __new__(self, maxCount: int) -> None:
        pass

    @typing.overload
    def __new__(self, maxCount: int, period: datetime.timedelta) -> None:
        pass

    @typing.overload
    def __new__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass



class IDataConsolidator(System.IDisposable):
    """
    Represents a type capable of taking BaseData updates and firing events containing new

                'consolidated' data. These types can be used to produce larger bars, or even be used to

                transform the data before being sent to another component. The most common usage of these

                types is with indicators.
    """
    def Scan(self, currentLocalTime: datetime.datetime) -> None:
        pass

    def Update(self, data: QuantConnect.Data.IBaseData) -> None:
        pass

    Consolidated: QuantConnect.Data.IBaseData

    InputType: type

    OutputType: type

    WorkingData: QuantConnect.Data.IBaseData


    DataConsolidated: BoundEvent


class IdentityDataConsolidator(QuantConnect.Data.Consolidators.DataConsolidator[T], QuantConnect.Data.Consolidators.IDataConsolidator, System.IDisposable):
    """ IdentityDataConsolidator[T]() """
    def Scan(self, currentLocalTime: datetime.datetime) -> None:
        pass

    @typing.overload
    def Update(self, data: QuantConnect.Data.Consolidators.T) -> None:
        pass

    @typing.overload
    def Update(self, data: QuantConnect.Data.IBaseData) -> None:
        pass

    def Update(self, *args) -> None:
        pass

    OutputType: type

    WorkingData: QuantConnect.Data.IBaseData



class OpenInterestConsolidator(QuantConnect.Data.Consolidators.PeriodCountConsolidatorBase[Tick, OpenInterest], QuantConnect.Data.Consolidators.IDataConsolidator, System.IDisposable):
    """
    Type capable of consolidating open interest

    

    OpenInterestConsolidator(period: TimeSpan)

    OpenInterestConsolidator(maxCount: int)

    OpenInterestConsolidator(maxCount: int, period: TimeSpan)

    OpenInterestConsolidator(func: Func[DateTime, CalendarInfo])

    OpenInterestConsolidator(pyfuncobj: PyObject)
    """
    @staticmethod
    def FromResolution(resolution: QuantConnect.Resolution) -> QuantConnect.Data.Consolidators.OpenInterestConsolidator:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, period: datetime.timedelta) -> None:
        pass

    @typing.overload
    def __new__(self, maxCount: int) -> None:
        pass

    @typing.overload
    def __new__(self, maxCount: int, period: datetime.timedelta) -> None:
        pass

    @typing.overload
    def __new__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        pass

    @typing.overload
    def __new__(self, pyfuncobj: Python.Runtime.PyObject) -> None:
        pass

    def __new__(self, *args) -> None:
        pass



class PeriodCountConsolidatorBase(QuantConnect.Data.Consolidators.DataConsolidator[T], QuantConnect.Data.Consolidators.IDataConsolidator, System.IDisposable):
    # no doc
    def Scan(self, currentLocalTime: datetime.datetime) -> None:
        pass

    @typing.overload
    def Update(self, data: QuantConnect.Data.Consolidators.T) -> None:
        pass

    @typing.overload
    def Update(self, data: QuantConnect.Data.IBaseData) -> None:
        pass

    def Update(self, *args) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        pass

    OutputType: type

    WorkingData: QuantConnect.Data.IBaseData


    DataConsolidated: BoundEvent


class QuoteBarConsolidator(QuantConnect.Data.Consolidators.PeriodCountConsolidatorBase[QuoteBar, QuoteBar], QuantConnect.Data.Consolidators.IDataConsolidator, System.IDisposable):
    """
    Consolidates QuoteBars into larger QuoteBars

    

    QuoteBarConsolidator(period: TimeSpan)

    QuoteBarConsolidator(maxCount: int)

    QuoteBarConsolidator(maxCount: int, period: TimeSpan)

    QuoteBarConsolidator(func: Func[DateTime, CalendarInfo])

    QuoteBarConsolidator(pyfuncobj: PyObject)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, period: datetime.timedelta) -> None:
        pass

    @typing.overload
    def __new__(self, maxCount: int) -> None:
        pass

    @typing.overload
    def __new__(self, maxCount: int, period: datetime.timedelta) -> None:
        pass

    @typing.overload
    def __new__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        pass

    @typing.overload
    def __new__(self, pyfuncobj: Python.Runtime.PyObject) -> None:
        pass

    def __new__(self, *args) -> None:
        pass



class SequentialConsolidator(System.object, QuantConnect.Data.Consolidators.IDataConsolidator, System.IDisposable):
    """
    This consolidator wires up the events on its First and Second consolidators

                such that data flows from the First to Second consolidator. It's output comes

                from the Second.

    

    SequentialConsolidator(first: IDataConsolidator, second: IDataConsolidator)
    """
    def Dispose(self) -> None:
        pass

    def Scan(self, currentLocalTime: datetime.datetime) -> None:
        pass

    def Update(self, data: QuantConnect.Data.IBaseData) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, first: QuantConnect.Data.Consolidators.IDataConsolidator, second: QuantConnect.Data.Consolidators.IDataConsolidator) -> None:
        pass

    Consolidated: QuantConnect.Data.IBaseData

    First: QuantConnect.Data.Consolidators.IDataConsolidator

    InputType: type

    OutputType: type

    Second: QuantConnect.Data.Consolidators.IDataConsolidator

    WorkingData: QuantConnect.Data.IBaseData


    DataConsolidated: BoundEvent
