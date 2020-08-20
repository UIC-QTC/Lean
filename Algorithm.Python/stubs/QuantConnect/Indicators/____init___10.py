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
