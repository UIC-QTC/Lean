# encoding: utf-8
# module QuantConnect.Scheduling calls itself Scheduling
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import NodaTime
import Python.Runtime
import QuantConnect
import QuantConnect.Scheduling
import QuantConnect.Securities
import System
import System.Collections.Generic
import typing

# no functions
# classes

class CompositeTimeRule(System.object, QuantConnect.Scheduling.ITimeRule):
    """
    Combines multiple time rules into a single rule that emits for each rule
    
    CompositeTimeRule(*timeRules: Array[ITimeRule])
    CompositeTimeRule(timeRules: IEnumerable[ITimeRule])
    """
    def CreateUtcEventTimes(self, dates: typing.List[datetime.datetime]) -> typing.List[datetime.datetime]:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, timeRules: typing.List[QuantConnect.Scheduling.ITimeRule]) -> None:
        pass

    @typing.overload
    def __new__(self, timeRules: typing.List[QuantConnect.Scheduling.ITimeRule]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Name: str

    Rules: typing.List[QuantConnect.Scheduling.ITimeRule]


class DateRules(System.object):
    """
    Helper class used to provide better syntax when defining date rules
    
    DateRules(securities: SecurityManager, timeZone: DateTimeZone)
    """
    @typing.overload
    def Every(self, day: System.DayOfWeek) -> QuantConnect.Scheduling.IDateRule:
        pass

    @typing.overload
    def Every(self, days: typing.List[System.DayOfWeek]) -> QuantConnect.Scheduling.IDateRule:
        pass

    def Every(self, *args) -> QuantConnect.Scheduling.IDateRule:
        pass

    @typing.overload
    def EveryDay(self) -> QuantConnect.Scheduling.IDateRule:
        pass

    @typing.overload
    def EveryDay(self, symbol: QuantConnect.Symbol) -> QuantConnect.Scheduling.IDateRule:
        pass

    def EveryDay(self, *args) -> QuantConnect.Scheduling.IDateRule:
        pass

    @typing.overload
    def MonthEnd(self) -> QuantConnect.Scheduling.IDateRule:
        pass

    @typing.overload
    def MonthEnd(self, symbol: QuantConnect.Symbol) -> QuantConnect.Scheduling.IDateRule:
        pass

    def MonthEnd(self, *args) -> QuantConnect.Scheduling.IDateRule:
        pass

    @typing.overload
    def MonthStart(self) -> QuantConnect.Scheduling.IDateRule:
        pass

    @typing.overload
    def MonthStart(self, symbol: QuantConnect.Symbol) -> QuantConnect.Scheduling.IDateRule:
        pass

    def MonthStart(self, *args) -> QuantConnect.Scheduling.IDateRule:
        pass

    @typing.overload
    def On(self, year: int, month: int, day: int) -> QuantConnect.Scheduling.IDateRule:
        pass

    @typing.overload
    def On(self, dates: typing.List[datetime.datetime]) -> QuantConnect.Scheduling.IDateRule:
        pass

    def On(self, *args) -> QuantConnect.Scheduling.IDateRule:
        pass

    @typing.overload
    def WeekEnd(self) -> QuantConnect.Scheduling.IDateRule:
        pass

    @typing.overload
    def WeekEnd(self, symbol: QuantConnect.Symbol) -> QuantConnect.Scheduling.IDateRule:
        pass

    def WeekEnd(self, *args) -> QuantConnect.Scheduling.IDateRule:
        pass

    @typing.overload
    def WeekStart(self) -> QuantConnect.Scheduling.IDateRule:
        pass

    @typing.overload
    def WeekStart(self, symbol: QuantConnect.Symbol) -> QuantConnect.Scheduling.IDateRule:
        pass

    def WeekStart(self, *args) -> QuantConnect.Scheduling.IDateRule:
        pass

    @staticmethod # known case of __new__
    def __new__(self, securities: QuantConnect.Securities.SecurityManager, timeZone: NodaTime.DateTimeZone) -> None:
        pass

    Today: QuantConnect.Scheduling.IDateRule

    Tomorrow: QuantConnect.Scheduling.IDateRule



class FluentScheduledEventBuilder(System.object, QuantConnect.Scheduling.IFluentSchedulingDateSpecifier, QuantConnect.Scheduling.IFluentSchedulingRunnable, QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier):
    """
    Provides a builder class to allow for fluent syntax when constructing new events
    
    FluentScheduledEventBuilder(schedule: ScheduleManager, securities: SecurityManager, name: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, schedule: QuantConnect.Scheduling.ScheduleManager, securities: QuantConnect.Securities.SecurityManager, name: str) -> None:
        pass


class FuncDateRule(System.object, QuantConnect.Scheduling.IDateRule):
    """
    Uses a function to define an enumerable of dates over a requested start/end period
    
    FuncDateRule(name: str, getDatesFunction: Func[DateTime, DateTime, IEnumerable[DateTime]])
    """
    def GetDates(self, start: datetime.datetime, end: datetime.datetime) -> typing.List[datetime.datetime]:
        pass

    @staticmethod # known case of __new__
    def __new__(self, name: str, getDatesFunction: typing.Callable[[datetime.datetime, datetime.datetime], typing.List[datetime.datetime]]) -> None:
        pass

    Name: str



class FuncTimeRule(System.object, QuantConnect.Scheduling.ITimeRule):
    """
    Uses a function to define a time rule as a projection of date times to date times
    
    FuncTimeRule(name: str, createUtcEventTimesFunction: Func[IEnumerable[DateTime], IEnumerable[DateTime]])
    """
    def CreateUtcEventTimes(self, dates: typing.List[datetime.datetime]) -> typing.List[datetime.datetime]:
        pass

    @staticmethod # known case of __new__
    def __new__(self, name: str, createUtcEventTimesFunction: typing.Callable[[typing.List[datetime.datetime]], typing.List[datetime.datetime]]) -> None:
        pass

    Name: str



class IDateRule:
    """ Specifies dates that events should be fired, used in conjunction with the QuantConnect.Scheduling.ITimeRule """
    def GetDates(self, start: datetime.datetime, end: datetime.datetime) -> typing.List[datetime.datetime]:
        pass

    Name: str



class IEventSchedule:
    """ Provides the ability to add/remove scheduled events from the real time handler """
    def Add(self, scheduledEvent: QuantConnect.Scheduling.ScheduledEvent) -> None:
        pass

    def Remove(self, scheduledEvent: QuantConnect.Scheduling.ScheduledEvent) -> None:
        pass


class IFluentSchedulingDateSpecifier:
    """ Specifies the date rule component of a scheduled event """
    def Every(self, days: typing.List[System.DayOfWeek]) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        pass

    @typing.overload
    def EveryDay(self) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        pass

    @typing.overload
    def EveryDay(self, symbol: QuantConnect.Symbol) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        pass

    def EveryDay(self, *args) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        pass

    @typing.overload
    def MonthStart(self) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        pass

    @typing.overload
    def MonthStart(self, symbol: QuantConnect.Symbol) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        pass

    def MonthStart(self, *args) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        pass

    @typing.overload
    def On(self, year: int, month: int, day: int) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        pass

    @typing.overload
    def On(self, dates: typing.List[datetime.datetime]) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        pass

    def On(self, *args) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        pass

    def Where(self, predicate: typing.Callable[[datetime.datetime], bool]) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        pass


class IFluentSchedulingTimeSpecifier:
    """ Specifies the time rule component of a scheduled event """
    def AfterMarketOpen(self, symbol: QuantConnect.Symbol, minutesAfterOpen: float, extendedMarketOpen: bool) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        pass

    @typing.overload
    def At(self, hour: int, minute: int, second: int) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        pass

    @typing.overload
    def At(self, hour: int, minute: int, timeZone: NodaTime.DateTimeZone) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        pass

    @typing.overload
    def At(self, hour: int, minute: int, second: int, timeZone: NodaTime.DateTimeZone) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        pass

    @typing.overload
    def At(self, timeOfDay: datetime.timedelta, timeZone: NodaTime.DateTimeZone) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        pass

    @typing.overload
    def At(self, timeOfDay: datetime.timedelta) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        pass

    def At(self, *args) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        pass

    def BeforeMarketClose(self, symbol: QuantConnect.Symbol, minuteBeforeClose: float, extendedMarketClose: bool) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        pass

    def Every(self, interval: datetime.timedelta) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        pass

    def Where(self, predicate: typing.Callable[[datetime.datetime], bool]) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        pass


class IFluentSchedulingRunnable(QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier):
    """ Specifies the callback component of a scheduled event, as well as final filters """
    def DuringMarketHours(self, symbol: QuantConnect.Symbol, extendedMarket: bool) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        pass

    @typing.overload
    def Run(self, callback: System.Action) -> QuantConnect.Scheduling.ScheduledEvent:
        pass

    @typing.overload
    def Run(self, callback: typing.Callable[[datetime.datetime], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        pass

    @typing.overload
    def Run(self, callback: typing.Callable[[str, datetime.datetime], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        pass

    def Run(self, *args) -> QuantConnect.Scheduling.ScheduledEvent:
        pass

    def Where(self, predicate: typing.Callable[[datetime.datetime], bool]) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        pass


class ITimeRule:
    """ Specifies times times on dates for events, used in conjunction with QuantConnect.Scheduling.IDateRule """
    def CreateUtcEventTimes(self, dates: typing.List[datetime.datetime]) -> typing.List[datetime.datetime]:
        pass

    Name: str



class ScheduledEvent(System.object, System.IDisposable):
    """
    Real time self scheduling event
    
    ScheduledEvent(name: str, eventUtcTime: DateTime, callback: Action[str, DateTime])
    ScheduledEvent(name: str, orderedEventUtcTimes: IEnumerable[DateTime], callback: Action[str, DateTime])
    ScheduledEvent(name: str, orderedEventUtcTimes: IEnumerator[DateTime], callback: Action[str, DateTime])
    """
    def Equals(self, obj: object) -> bool:
        pass

    def GetHashCode(self) -> int:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, name: str, eventUtcTime: datetime.datetime, callback: typing.Callable[[str, datetime.datetime], None]) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, orderedEventUtcTimes: typing.List[datetime.datetime], callback: typing.Callable[[str, datetime.datetime], None]) -> None:
        pass

    @typing.overload
    def __new__(self, name: str, orderedEventUtcTimes: System.Collections.Generic.IEnumerator[datetime.datetime], callback: typing.Callable[[str, datetime.datetime], None]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Enabled: bool

    Name: str

    NextEventUtcTime: datetime.datetime


    AlgorithmEndOfDayDelta: TimeSpan
    EventFired: BoundEvent
    SecurityEndOfDayDelta: TimeSpan


class ScheduledEventException(System.Exception, System.Runtime.Serialization.ISerializable, System.Runtime.InteropServices._Exception):
    """
    Throw this if there is an exception in the callback function of the scheduled event
    
    ScheduledEventException(name: str, message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, name: str, message: str, innerException: System.Exception) -> None:
        pass

    ScheduledEventName: str


    SerializeObjectState: BoundEvent


class ScheduleManager(System.object, QuantConnect.Scheduling.IEventSchedule):
    """
    Provides access to the real time handler's event scheduling feature
    
    ScheduleManager(securities: SecurityManager, timeZone: DateTimeZone)
    """
    def Add(self, scheduledEvent: QuantConnect.Scheduling.ScheduledEvent) -> None:
        pass

    @typing.overload
    def Event(self) -> QuantConnect.Scheduling.IFluentSchedulingDateSpecifier:
        pass

    @typing.overload
    def Event(self, name: str) -> QuantConnect.Scheduling.IFluentSchedulingDateSpecifier:
        pass

    def Event(self, *args) -> QuantConnect.Scheduling.IFluentSchedulingDateSpecifier:
        pass

    @typing.overload
    def On(self, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, callback: System.Action) -> QuantConnect.Scheduling.ScheduledEvent:
        pass

    @typing.overload
    def On(self, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, callback: Python.Runtime.PyObject) -> QuantConnect.Scheduling.ScheduledEvent:
        pass

    @typing.overload
    def On(self, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, callback: typing.Callable[[str, datetime.datetime], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        pass

    @typing.overload
    def On(self, name: str, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, callback: System.Action) -> QuantConnect.Scheduling.ScheduledEvent:
        pass

    @typing.overload
    def On(self, name: str, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, callback: Python.Runtime.PyObject) -> QuantConnect.Scheduling.ScheduledEvent:
        pass

    @typing.overload
    def On(self, name: str, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, callback: typing.Callable[[str, datetime.datetime], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        pass

    def On(self, *args) -> QuantConnect.Scheduling.ScheduledEvent:
        pass

    def Remove(self, scheduledEvent: QuantConnect.Scheduling.ScheduledEvent) -> None:
        pass

    @typing.overload
    def Training(self, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, trainingCode: System.Action) -> QuantConnect.Scheduling.ScheduledEvent:
        pass

    @typing.overload
    def Training(self, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, trainingCode: Python.Runtime.PyObject) -> QuantConnect.Scheduling.ScheduledEvent:
        pass

    @typing.overload
    def Training(self, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, trainingCode: typing.Callable[[datetime.datetime], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        pass

    def Training(self, *args) -> QuantConnect.Scheduling.ScheduledEvent:
        pass

    @typing.overload
    def TrainingNow(self, trainingCode: System.Action) -> QuantConnect.Scheduling.ScheduledEvent:
        pass

    @typing.overload
    def TrainingNow(self, trainingCode: Python.Runtime.PyObject) -> QuantConnect.Scheduling.ScheduledEvent:
        pass

    def TrainingNow(self, *args) -> QuantConnect.Scheduling.ScheduledEvent:
        pass

    @staticmethod # known case of __new__
    def __new__(self, securities: QuantConnect.Securities.SecurityManager, timeZone: NodaTime.DateTimeZone) -> None:
        pass

    DateRules: QuantConnect.Scheduling.DateRules

    TimeRules: QuantConnect.Scheduling.TimeRules



class TimeConsumer(System.object):
    """
    Represents a timer consumer instance
    
    TimeConsumer()
    """
    Finished: bool

    IsolatorLimitProvider: QuantConnect.IIsolatorLimitResultProvider

    NextTimeRequest: typing.Optional[datetime.datetime]

    TimeProvider: QuantConnect.ITimeProvider



class TimeMonitor(System.object, System.IDisposable):
    """
    Helper class that will monitor timer consumers and request more time if required.
                Used by QuantConnect.IsolatorLimitResultProvider
    
    TimeMonitor(monitorIntervalMs: int)
    """
    def Add(self, consumer: QuantConnect.Scheduling.TimeConsumer) -> None:
        pass

    def Dispose(self) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, monitorIntervalMs: int) -> None:
        pass

    Count: int



class TimeRules(System.object):
    """
    Helper class used to provide better syntax when defining time rules
    
    TimeRules(securities: SecurityManager, timeZone: DateTimeZone)
    """
    def AfterMarketOpen(self, symbol: QuantConnect.Symbol, minutesAfterOpen: float, extendedMarketOpen: bool) -> QuantConnect.Scheduling.ITimeRule:
        pass

    @typing.overload
    def At(self, timeOfDay: datetime.timedelta) -> QuantConnect.Scheduling.ITimeRule:
        pass

    @typing.overload
    def At(self, hour: int, minute: int, second: int) -> QuantConnect.Scheduling.ITimeRule:
        pass

    @typing.overload
    def At(self, hour: int, minute: int, timeZone: NodaTime.DateTimeZone) -> QuantConnect.Scheduling.ITimeRule:
        pass

    @typing.overload
    def At(self, hour: int, minute: int, second: int, timeZone: NodaTime.DateTimeZone) -> QuantConnect.Scheduling.ITimeRule:
        pass

    @typing.overload
    def At(self, timeOfDay: datetime.timedelta, timeZone: NodaTime.DateTimeZone) -> QuantConnect.Scheduling.ITimeRule:
        pass

    def At(self, *args) -> QuantConnect.Scheduling.ITimeRule:
        pass

    def BeforeMarketClose(self, symbol: QuantConnect.Symbol, minutesBeforeClose: float, extendedMarketClose: bool) -> QuantConnect.Scheduling.ITimeRule:
        pass

    def Every(self, interval: datetime.timedelta) -> QuantConnect.Scheduling.ITimeRule:
        pass

    def SetDefaultTimeZone(self, timeZone: NodaTime.DateTimeZone) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, securities: QuantConnect.Securities.SecurityManager, timeZone: NodaTime.DateTimeZone) -> None:
        pass

    Midnight: QuantConnect.Scheduling.ITimeRule

    Noon: QuantConnect.Scheduling.ITimeRule

    Now: QuantConnect.Scheduling.ITimeRule



