import typing
import System
import QuantConnect.Data.Market
import QuantConnect.Data.Consolidators
import QuantConnect.Data
import QuantConnect
import Python.Runtime
import datetime


class TickConsolidator(QuantConnect.Data.Consolidators.TradeBarConsolidatorBase[Tick], QuantConnect.Data.Consolidators.IDataConsolidator, System.IDisposable):
    """
    A data consolidator that can make bigger bars from ticks over a given

                time span or a count of pieces of data.

    

    TickConsolidator(period: TimeSpan)

    TickConsolidator(maxCount: int)

    TickConsolidator(maxCount: int, period: TimeSpan)

    TickConsolidator(func: Func[DateTime, CalendarInfo])

    TickConsolidator(pyfuncobj: PyObject)
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



class TickQuoteBarConsolidator(QuantConnect.Data.Consolidators.PeriodCountConsolidatorBase[Tick, QuoteBar], QuantConnect.Data.Consolidators.IDataConsolidator, System.IDisposable):
    """
    Consolidates ticks into quote bars. This consolidator ignores trade ticks

    

    TickQuoteBarConsolidator(period: TimeSpan)

    TickQuoteBarConsolidator(maxCount: int)

    TickQuoteBarConsolidator(maxCount: int, period: TimeSpan)

    TickQuoteBarConsolidator(func: Func[DateTime, CalendarInfo])

    TickQuoteBarConsolidator(pyfuncobj: PyObject)
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



class TradeBarConsolidator(QuantConnect.Data.Consolidators.TradeBarConsolidatorBase[TradeBar], QuantConnect.Data.Consolidators.IDataConsolidator, System.IDisposable):
    """
    A data consolidator that can make bigger bars from smaller ones over a given

                 time span or a count of pieces of data.

                

                 Use this consolidator to turn data of a lower resolution into data of a higher resolution,

                 for example, if you subscribe to minute data but want to have a 15 minute bar.

    

    TradeBarConsolidator(period: TimeSpan)

    TradeBarConsolidator(maxCount: int)

    TradeBarConsolidator(maxCount: int, period: TimeSpan)

    TradeBarConsolidator(func: Func[DateTime, CalendarInfo])

    TradeBarConsolidator(pyfuncobj: PyObject)
    """
    @staticmethod
    def FromResolution(resolution: QuantConnect.Resolution) -> QuantConnect.Data.Consolidators.TradeBarConsolidator:
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



class TradeBarConsolidatorBase(QuantConnect.Data.Consolidators.PeriodCountConsolidatorBase[T, TradeBar], QuantConnect.Data.Consolidators.IDataConsolidator, System.IDisposable):
    # no doc
    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        pass

    WorkingBar: QuantConnect.Data.Market.TradeBar
