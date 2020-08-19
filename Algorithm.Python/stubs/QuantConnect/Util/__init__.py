# encoding: utf-8
# module QuantConnect.Util calls itself Util
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import Newtonsoft.Json
import NodaTime
import Python.Runtime
import QuantConnect
import QuantConnect.Data
import QuantConnect.Securities
import QuantConnect.Util
import System
import System.Collections.Generic
import System.IO
import System.Linq
import System.Linq.Expressions
import System.Text
import System.Threading
import System.Xml.Linq
import typing

# functions

def Ref(*args, **kwargs): # real signature unknown
    """ Provides some helper methods that leverage C# type inference """
    pass

# classes

class BusyBlockingCollection(System.object, QuantConnect.Interfaces.IBusyCollection[T], System.IDisposable):
    """
    BusyBlockingCollection[T]()
    BusyBlockingCollection[T](boundedCapacity: int)
    """
    @typing.overload
    def Add(self, item: QuantConnect.Util.T) -> None:
        pass

    @typing.overload
    def Add(self, item: QuantConnect.Util.T, cancellationToken: System.Threading.CancellationToken) -> None:
        pass

    def Add(self, *args) -> None:
        pass

    def CompleteAdding(self) -> None:
        pass

    def Dispose(self) -> None:
        pass

    @typing.overload
    def GetConsumingEnumerable(self) -> typing.List[QuantConnect.Util.T]:
        pass

    @typing.overload
    def GetConsumingEnumerable(self, cancellationToken: System.Threading.CancellationToken) -> typing.List[QuantConnect.Util.T]:
        pass

    def GetConsumingEnumerable(self, *args) -> typing.List[QuantConnect.Util.T]:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, boundedCapacity: int) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Count: int

    IsBusy: bool

    WaitHandle: System.Threading.WaitHandle



class BusyCollection(System.object, QuantConnect.Interfaces.IBusyCollection[T], System.IDisposable):
    """ BusyCollection[T]() """
    @typing.overload
    def Add(self, item: QuantConnect.Util.T) -> None:
        pass

    @typing.overload
    def Add(self, item: QuantConnect.Util.T, cancellationToken: System.Threading.CancellationToken) -> None:
        pass

    def Add(self, *args) -> None:
        pass

    def CompleteAdding(self) -> None:
        pass

    def Dispose(self) -> None:
        pass

    @typing.overload
    def GetConsumingEnumerable(self) -> typing.List[QuantConnect.Util.T]:
        pass

    @typing.overload
    def GetConsumingEnumerable(self, cancellationToken: System.Threading.CancellationToken) -> typing.List[QuantConnect.Util.T]:
        pass

    def GetConsumingEnumerable(self, *args) -> typing.List[QuantConnect.Util.T]:
        pass

    Count: int

    IsBusy: bool

    WaitHandle: System.Threading.WaitHandle



class CircularQueue(System.object):
    """
    CircularQueue[T](*items: Array[T])
    CircularQueue[T](items: IEnumerable[T])
    """
    def Dequeue(self) -> QuantConnect.Util.T:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, items: typing.List[QuantConnect.Util.T]) -> None:
        pass

    @typing.overload
    def __new__(self, items: typing.List[QuantConnect.Util.T]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    CircleCompleted: BoundEvent


class ColorJsonConverter(QuantConnect.Util.TypeChangeJsonConverter[Color, str]):
    """
    A Newtonsoft.Json.JsonConverter implementation that serializes a System.Drawing.Color as a string.
                If Color is empty, string is also empty and vice-versa. Meaning that color is autogen.
    
    ColorJsonConverter()
    """


class Composer(System.object):
    """
    Provides methods for obtaining exported MEF instances
    
    Composer()
    """
    def AddPart(self, instance: QuantConnect.Util.T) -> None:
        pass

    def GetExportedValueByTypeName(self, typeName: str) -> QuantConnect.Util.T:
        pass

    def GetExportedValues(self) -> typing.List[QuantConnect.Util.T]:
        pass

    def Reset(self) -> None:
        pass

    def Single(self, predicate: typing.Callable[[QuantConnect.Util.T], bool]) -> QuantConnect.Util.T:
        pass

    Instance: Composer


class ConcurrentSet(System.object, System.Collections.Generic.ISet[T], System.Collections.Generic.ICollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable):
    """ ConcurrentSet[T]() """
    def Add(self, item: QuantConnect.Util.T) -> None:
        pass

    def Clear(self) -> None:
        pass

    def Contains(self, item: QuantConnect.Util.T) -> bool:
        pass

    def CopyTo(self, array: typing.List[QuantConnect.Util.T], arrayIndex: int) -> None:
        pass

    def ExceptWith(self, other: typing.List[QuantConnect.Util.T]) -> None:
        pass

    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Util.T]:
        pass

    def IntersectWith(self, other: typing.List[QuantConnect.Util.T]) -> None:
        pass

    def IsProperSubsetOf(self, other: typing.List[QuantConnect.Util.T]) -> bool:
        pass

    def IsProperSupersetOf(self, other: typing.List[QuantConnect.Util.T]) -> bool:
        pass

    def IsSubsetOf(self, other: typing.List[QuantConnect.Util.T]) -> bool:
        pass

    def IsSupersetOf(self, other: typing.List[QuantConnect.Util.T]) -> bool:
        pass

    def Overlaps(self, other: typing.List[QuantConnect.Util.T]) -> bool:
        pass

    def Remove(self, item: QuantConnect.Util.T) -> bool:
        pass

    def SetEquals(self, other: typing.List[QuantConnect.Util.T]) -> bool:
        pass

    def SymmetricExceptWith(self, other: typing.List[QuantConnect.Util.T]) -> None:
        pass

    def UnionWith(self, other: typing.List[QuantConnect.Util.T]) -> None:
        pass

    Count: int

    IsReadOnly: bool



class DateTimeJsonConverter(Newtonsoft.Json.Converters.IsoDateTimeConverter):
    """
    Provides a json converter that allows defining the date time format used
    
    DateTimeJsonConverter(format: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, format: str) -> None:
        pass


class DisposableExtensions(System.object):
    """ Provides extensions methods for System.IDisposable """
    @staticmethod
    @typing.overload
    def DisposeSafely(disposable: System.IDisposable) -> bool:
        pass

    @staticmethod
    @typing.overload
    def DisposeSafely(disposable: System.IDisposable, errorHandler: typing.Callable[[System.Exception], None]) -> bool:
        pass

    def DisposeSafely(self, *args) -> bool:
        pass

    __all__: list


class DoubleUnixSecondsDateTimeJsonConverter(QuantConnect.Util.TypeChangeJsonConverter[Nullable[DateTime], Nullable[float]]):
    """
    Defines a Newtonsoft.Json.JsonConverter that serializes System.DateTime use the number of whole and fractional seconds since unix epoch
    
    DoubleUnixSecondsDateTimeJsonConverter()
    """
    def CanConvert(self, objectType: type) -> bool:
        pass



class EnumeratorExtensions(System.object):
    """ Provides convenience of linq extension methods for System.Collections.Generic.IEnumerator types """
    @staticmethod
    def Select(enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Util.T], selector: typing.Callable[[QuantConnect.Util.T], QuantConnect.Util.TResult]) -> System.Collections.Generic.IEnumerator[QuantConnect.Util.TResult]:
        pass

    @staticmethod
    def SelectMany(enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Util.T], selector: typing.Callable[[QuantConnect.Util.T], System.Collections.Generic.IEnumerator[QuantConnect.Util.TResult]]) -> System.Collections.Generic.IEnumerator[QuantConnect.Util.TResult]:
        pass

    @staticmethod
    def Where(enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Util.T], predicate: typing.Callable[[QuantConnect.Util.T], bool]) -> System.Collections.Generic.IEnumerator[QuantConnect.Util.T]:
        pass

    __all__: list


class ExpressionBuilder(System.object):
    """ Provides methods for constructing expressions at runtime """
    @staticmethod
    def AsEnumerable(expression: System.Linq.Expressions.Expression) -> typing.List[System.Linq.Expressions.Expression]:
        pass

    @staticmethod
    @typing.overload
    def MakePropertyOrFieldSelector(type: type, propertyOrField: str) -> System.Linq.Expressions.LambdaExpression:
        pass

    @staticmethod
    @typing.overload
    def MakePropertyOrFieldSelector(propertyOrField: str) -> System.Linq.Expressions.Expression[typing.Callable[[QuantConnect.Util.T], QuantConnect.Util.TProperty]]:
        pass

    def MakePropertyOrFieldSelector(self, *args) -> System.Linq.Expressions.Expression[typing.Callable[[QuantConnect.Util.T], QuantConnect.Util.TProperty]]:
        pass

    @staticmethod
    def OfType(expression: System.Linq.Expressions.Expression) -> typing.List[QuantConnect.Util.T]:
        pass

    __all__: list


class FixedSizeHashQueue(System.object, System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable):
    """ FixedSizeHashQueue[T](size: int) """
    def Add(self, item: QuantConnect.Util.T) -> bool:
        pass

    def Contains(self, item: QuantConnect.Util.T) -> bool:
        pass

    def Dequeue(self) -> QuantConnect.Util.T:
        pass

    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Util.T]:
        pass

    def TryPeek(self, item: QuantConnect.Util.T) -> bool:
        pass

    @staticmethod # known case of __new__
    def __new__(self, size: int) -> None:
        pass


class FixedSizeQueue(System.Collections.Generic.Queue[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[T]):
    """ FixedSizeQueue[T](limit: int) """
    @typing.overload
    def Enqueue(self, item: QuantConnect.Util.T) -> None:
        pass

    @typing.overload
    def Enqueue(self, item: QuantConnect.Util.T) -> None:
        pass

    def Enqueue(self, *args) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, limit: int) -> None:
        pass

    Limit: int



class FuncTextWriter(System.IO.TextWriter, System.IDisposable):
    """
    Provides an implementation of System.IO.TextWriter that redirects Write(string) and WriteLine(string)
    
    FuncTextWriter(writer: Action[str])
    """
    def Dispose(self) -> None:
        pass

    @typing.overload
    def Write(self, value: str) -> None:
        pass

    @typing.overload
    def Write(self, value: str) -> None:
        pass

    @typing.overload
    def Write(self, buffer: typing.List[str]) -> None:
        pass

    @typing.overload
    def Write(self, buffer: typing.List[str], index: int, count: int) -> None:
        pass

    @typing.overload
    def Write(self, value: int) -> None:
        pass

    @typing.overload
    def Write(self, value: int) -> None:
        pass

    @typing.overload
    def Write(self, value: int) -> None:
        pass

    @typing.overload
    def Write(self, value: int) -> None:
        pass

    @typing.overload
    def Write(self, value: float) -> None:
        pass

    @typing.overload
    def Write(self, value: float) -> None:
        pass

    @typing.overload
    def Write(self, value: float) -> None:
        pass

    @typing.overload
    def Write(self, value: object) -> None:
        pass

    @typing.overload
    def Write(self, format: str, arg0: object) -> None:
        pass

    @typing.overload
    def Write(self, format: str, arg0: object, arg1: object) -> None:
        pass

    @typing.overload
    def Write(self, format: str, arg0: object, arg1: object, arg2: object) -> None:
        pass

    @typing.overload
    def Write(self, format: str, arg: typing.List[object]) -> None:
        pass

    @typing.overload
    def Write(self, value: bool) -> None:
        pass

    def Write(self, *args) -> None:
        pass

    @typing.overload
    def WriteLine(self, value: str) -> None:
        pass

    @typing.overload
    def WriteLine(self) -> None:
        pass

    @typing.overload
    def WriteLine(self, value: str) -> None:
        pass

    @typing.overload
    def WriteLine(self, buffer: typing.List[str]) -> None:
        pass

    @typing.overload
    def WriteLine(self, buffer: typing.List[str], index: int, count: int) -> None:
        pass

    @typing.overload
    def WriteLine(self, value: bool) -> None:
        pass

    @typing.overload
    def WriteLine(self, value: int) -> None:
        pass

    @typing.overload
    def WriteLine(self, value: int) -> None:
        pass

    @typing.overload
    def WriteLine(self, value: int) -> None:
        pass

    @typing.overload
    def WriteLine(self, value: int) -> None:
        pass

    @typing.overload
    def WriteLine(self, value: float) -> None:
        pass

    @typing.overload
    def WriteLine(self, value: float) -> None:
        pass

    @typing.overload
    def WriteLine(self, value: float) -> None:
        pass

    @typing.overload
    def WriteLine(self, value: object) -> None:
        pass

    @typing.overload
    def WriteLine(self, format: str, arg0: object) -> None:
        pass

    @typing.overload
    def WriteLine(self, format: str, arg0: object, arg1: object) -> None:
        pass

    @typing.overload
    def WriteLine(self, format: str, arg0: object, arg1: object, arg2: object) -> None:
        pass

    @typing.overload
    def WriteLine(self, format: str, arg: typing.List[object]) -> None:
        pass

    def WriteLine(self, *args) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, writer: typing.Callable[[str], None]) -> None:
        pass

    Encoding: System.Text.Encoding

    CoreNewLine: typing.List[str]


class IReadOnlyRef:
    # no doc
    Value: QuantConnect.Util.T



class JsonRoundingConverter(Newtonsoft.Json.JsonConverter):
    """
    Helper Newtonsoft.Json.JsonConverter that will round decimal and double types,
                to QuantConnect.Util.JsonRoundingConverter.FractionalDigits fractional digits
    
    JsonRoundingConverter()
    """
    def CanConvert(self, objectType: type) -> bool:
        pass

    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: type, existingValue: object, serializer: Newtonsoft.Json.JsonSerializer) -> object:
        pass

    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: object, serializer: Newtonsoft.Json.JsonSerializer) -> None:
        pass

    CanRead: bool


    FractionalDigits: int


class LeanData(System.object):
    """ Provides methods for generating lean data file content """
    @staticmethod
    @typing.overload
    def GenerateLine(data: QuantConnect.Data.IBaseData, resolution: QuantConnect.Resolution, exchangeTimeZone: NodaTime.DateTimeZone, dataTimeZone: NodaTime.DateTimeZone) -> str:
        pass

    @staticmethod
    @typing.overload
    def GenerateLine(data: QuantConnect.Data.IBaseData, securityType: QuantConnect.SecurityType, resolution: QuantConnect.Resolution) -> str:
        pass

    def GenerateLine(self, *args) -> str:
        pass

    @staticmethod
    def GenerateRelativeFactorFilePath(symbol: QuantConnect.Symbol) -> str:
        pass

    @staticmethod
    def GenerateRelativeZipFileDirectory(symbol: QuantConnect.Symbol, resolution: QuantConnect.Resolution) -> str:
        pass

    @staticmethod
    @typing.overload
    def GenerateRelativeZipFilePath(symbol: QuantConnect.Symbol, date: datetime.datetime, resolution: QuantConnect.Resolution, tickType: QuantConnect.TickType) -> str:
        pass

    @staticmethod
    @typing.overload
    def GenerateRelativeZipFilePath(symbol: str, securityType: QuantConnect.SecurityType, market: str, date: datetime.datetime, resolution: QuantConnect.Resolution) -> str:
        pass

    def GenerateRelativeZipFilePath(self, *args) -> str:
        pass

    @staticmethod
    def GenerateZipEntryName(symbol: QuantConnect.Symbol, date: datetime.datetime, resolution: QuantConnect.Resolution, tickType: QuantConnect.TickType) -> str:
        pass

    @staticmethod
    @typing.overload
    def GenerateZipFileName(symbol: QuantConnect.Symbol, date: datetime.datetime, resolution: QuantConnect.Resolution, tickType: QuantConnect.TickType) -> str:
        pass

    @staticmethod
    @typing.overload
    def GenerateZipFileName(symbol: str, securityType: QuantConnect.SecurityType, date: datetime.datetime, resolution: QuantConnect.Resolution, tickType: typing.Optional[QuantConnect.TickType]) -> str:
        pass

    def GenerateZipFileName(self, *args) -> str:
        pass

    @staticmethod
    @typing.overload
    def GenerateZipFilePath(dataDirectory: str, symbol: QuantConnect.Symbol, date: datetime.datetime, resolution: QuantConnect.Resolution, tickType: QuantConnect.TickType) -> str:
        pass

    @staticmethod
    @typing.overload
    def GenerateZipFilePath(dataDirectory: str, symbol: str, securityType: QuantConnect.SecurityType, market: str, date: datetime.datetime, resolution: QuantConnect.Resolution) -> str:
        pass

    def GenerateZipFilePath(self, *args) -> str:
        pass

    @staticmethod
    def GetCommonTickType(securityType: QuantConnect.SecurityType) -> QuantConnect.TickType:
        pass

    @staticmethod
    def GetCommonTickTypeForCommonDataTypes(type: type, securityType: QuantConnect.SecurityType) -> QuantConnect.TickType:
        pass

    @staticmethod
    def GetDataType(resolution: QuantConnect.Resolution, tickType: QuantConnect.TickType) -> type:
        pass

    @staticmethod
    def IsCommonLeanDataType(baseDataType: type) -> bool:
        pass

    @staticmethod
    def ParseDataSecurityType(securityType: str) -> QuantConnect.SecurityType:
        pass

    @staticmethod
    def ReadSymbolFromZipEntry(symbol: QuantConnect.Symbol, resolution: QuantConnect.Resolution, zipEntryName: str) -> QuantConnect.Symbol:
        pass

    @staticmethod
    def TryParsePath(fileName: str, symbol: QuantConnect.Symbol, date: System.DateTime, resolution: QuantConnect.Resolution) -> bool:
        pass

    SecurityTypeAsDataPath: List[str]
    __all__: list


class LeanDataPathComponents(System.object):
    """
    Type representing the various pieces of information emebedded into a lean data file path
    
    LeanDataPathComponents(securityType: SecurityType, market: str, resolution: Resolution, symbol: Symbol, filename: str, date: DateTime, tickType: TickType)
    """
    @staticmethod
    def Parse(path: str) -> QuantConnect.Util.LeanDataPathComponents:
        pass

    @staticmethod # known case of __new__
    def __new__(self, securityType: QuantConnect.SecurityType, market: str, resolution: QuantConnect.Resolution, symbol: QuantConnect.Symbol, filename: str, date: datetime.datetime, tickType: QuantConnect.TickType) -> None:
        pass

    Date: datetime.datetime

    Filename: str

    Market: str

    Resolution: QuantConnect.Resolution

    SecurityType: QuantConnect.SecurityType

    Symbol: QuantConnect.Symbol

    TickType: QuantConnect.TickType



class LinqExtensions(System.object):
    """ Provides more extension methods for the enumerable types """
    @staticmethod
    def AreDifferent(left: System.Collections.Generic.ISet[QuantConnect.Util.T], right: System.Collections.Generic.ISet[QuantConnect.Util.T]) -> bool:
        pass

    @staticmethod
    def AsEnumerable(enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Util.T]) -> typing.List[QuantConnect.Util.T]:
        pass

    @staticmethod
    @typing.overload
    def BinarySearch(list: typing.List[QuantConnect.Util.TItem], value: QuantConnect.Util.TSearch, comparer: typing.Callable[[QuantConnect.Util.TSearch, QuantConnect.Util.TItem], int]) -> int:
        pass

    @staticmethod
    @typing.overload
    def BinarySearch(list: typing.List[QuantConnect.Util.TItem], value: QuantConnect.Util.TItem) -> int:
        pass

    @staticmethod
    @typing.overload
    def BinarySearch(list: typing.List[QuantConnect.Util.TItem], value: QuantConnect.Util.TItem, comparer: System.Collections.Generic.IComparer[QuantConnect.Util.TItem]) -> int:
        pass

    def BinarySearch(self, *args) -> int:
        pass

    @staticmethod
    def DefaultIfEmpty(enumerable: typing.List[QuantConnect.Util.T], selector: typing.Callable[[QuantConnect.Util.T], QuantConnect.Util.TResult], defaultValue: QuantConnect.Util.TResult) -> typing.List[QuantConnect.Util.TResult]:
        pass

    @staticmethod
    def DistinctBy(enumerable: typing.List[QuantConnect.Util.T], selector: typing.Callable[[QuantConnect.Util.T], QuantConnect.Util.TPropery]) -> typing.List[QuantConnect.Util.T]:
        pass

    @staticmethod
    def Except(enumerable: typing.List[QuantConnect.Util.T], set: System.Collections.Generic.ISet[QuantConnect.Util.T]) -> typing.List[QuantConnect.Util.T]:
        pass

    @staticmethod
    def GetValueOrDefault(dictionary: System.Collections.Generic.IDictionary[QuantConnect.Util.K, QuantConnect.Util.V], key: QuantConnect.Util.K, defaultValue: QuantConnect.Util.V) -> QuantConnect.Util.V:
        pass

    @staticmethod
    def GroupAdjacentBy(enumerable: typing.List[QuantConnect.Util.T], grouper: typing.Callable[[QuantConnect.Util.T, QuantConnect.Util.T], bool]) -> typing.List[typing.List[QuantConnect.Util.T]]:
        pass

    @staticmethod
    def IsNullOrEmpty(enumerable: typing.List[QuantConnect.Util.T]) -> bool:
        pass

    @staticmethod
    @typing.overload
    def Median(enumerable: typing.List[QuantConnect.Util.T]) -> QuantConnect.Util.T:
        pass

    @staticmethod
    @typing.overload
    def Median(collection: typing.List[QuantConnect.Util.T], selector: typing.Callable[[QuantConnect.Util.T], QuantConnect.Util.TProperty]) -> QuantConnect.Util.TProperty:
        pass

    def Median(self, *args) -> QuantConnect.Util.TProperty:
        pass

    @staticmethod
    def Memoize(enumerable: typing.List[QuantConnect.Util.T]) -> typing.List[QuantConnect.Util.T]:
        pass

    @staticmethod
    def Range(start: QuantConnect.Util.T, end: QuantConnect.Util.T, incrementer: typing.Callable[[QuantConnect.Util.T], QuantConnect.Util.T], includeEndPoint: bool) -> typing.List[QuantConnect.Util.T]:
        pass

    @staticmethod
    @typing.overload
    def ToDictionary(lookup: System.Linq.ILookup[QuantConnect.Util.K, QuantConnect.Util.V]) -> System.Collections.Generic.Dictionary[QuantConnect.Util.K, typing.List[QuantConnect.Util.V]]:
        pass

    @staticmethod
    @typing.overload
    def ToDictionary(enumerable: typing.List[System.Collections.Generic.KeyValuePair[QuantConnect.Util.K, QuantConnect.Util.V]]) -> System.Collections.Generic.Dictionary[QuantConnect.Util.K, QuantConnect.Util.V]:
        pass

    def ToDictionary(self, *args) -> System.Collections.Generic.Dictionary[QuantConnect.Util.K, QuantConnect.Util.V]:
        pass

    @staticmethod
    @typing.overload
    def ToHashSet(enumerable: typing.List[QuantConnect.Util.T]) -> System.Collections.Generic.HashSet[QuantConnect.Util.T]:
        pass

    @staticmethod
    @typing.overload
    def ToHashSet(enumerable: typing.List[QuantConnect.Util.T], selector: typing.Callable[[QuantConnect.Util.T], QuantConnect.Util.TResult]) -> System.Collections.Generic.HashSet[QuantConnect.Util.TResult]:
        pass

    def ToHashSet(self, *args) -> System.Collections.Generic.HashSet[QuantConnect.Util.TResult]:
        pass

    @staticmethod
    def ToList(enumerable: typing.List[QuantConnect.Util.T], selector: typing.Callable[[QuantConnect.Util.T], QuantConnect.Util.TResult]) -> typing.List[QuantConnect.Util.TResult]:
        pass

    @staticmethod
    def ToReadOnlyDictionary(enumerable: typing.List[System.Collections.Generic.KeyValuePair[QuantConnect.Util.K, QuantConnect.Util.V]]) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.Util.K, QuantConnect.Util.V]:
        pass

    __all__: list


class ListComparer(System.object, System.Collections.Generic.IEqualityComparer[List[T]]):
    """ ListComparer[T]() """
    @typing.overload
    def Equals(self, x: typing.List[QuantConnect.Util.T], y: typing.List[QuantConnect.Util.T]) -> bool:
        pass

    @typing.overload
    def Equals(self, obj: object) -> bool:
        pass

    def Equals(self, *args) -> bool:
        pass

    @typing.overload
    def GetHashCode(self, obj: typing.List[QuantConnect.Util.T]) -> int:
        pass

    @typing.overload
    def GetHashCode(self) -> int:
        pass

    def GetHashCode(self, *args) -> int:
        pass


class MarketHoursDatabaseJsonConverter(QuantConnect.Util.TypeChangeJsonConverter[MarketHoursDatabase, MarketHoursDatabaseJson]):
    """
    Provides json conversion for the QuantConnect.Securities.MarketHoursDatabase class
    
    MarketHoursDatabaseJsonConverter()
    """

    MarketHoursDatabaseEntryJson: type
    MarketHoursDatabaseJson: type


class MemoizingEnumerable(System.object, System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable):
    """
    MemoizingEnumerable[T](enumerable: IEnumerable[T])
    MemoizingEnumerable[T](enumerator: IEnumerator[T])
    """
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Util.T]:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, enumerable: typing.List[QuantConnect.Util.T]) -> None:
        pass

    @typing.overload
    def __new__(self, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Util.T]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass


class NullStringValueConverter(Newtonsoft.Json.JsonConverter):
    """ NullStringValueConverter[T]() """
    def CanConvert(self, objectType: type) -> bool:
        pass

    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: type, existingValue: object, serializer: Newtonsoft.Json.JsonSerializer) -> object:
        pass

    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: object, serializer: Newtonsoft.Json.JsonSerializer) -> None:
        pass


class ObjectActivator(System.object):
    """ Provides methods for creating new instances of objects """
    @staticmethod
    def AddActivator(key: type, value: typing.Callable[[typing.List[object]], object]) -> None:
        pass

    @staticmethod
    @typing.overload
    def Clone(instanceToClone: object) -> object:
        pass

    @staticmethod
    @typing.overload
    def Clone(instanceToClone: QuantConnect.Util.T) -> QuantConnect.Util.T:
        pass

    def Clone(self, *args) -> QuantConnect.Util.T:
        pass

    @staticmethod
    def GetActivator(dataType: type) -> typing.Callable[[typing.List[object]], object]:
        pass

    @staticmethod
    def ResetActivators() -> None:
        pass

    __all__: list


class PythonUtil(System.object):
    """
    Collection of utils for python objects processing
    
    PythonUtil()
    """
    @staticmethod
    def PythonExceptionStackParser(value: str) -> str:
        pass

    @staticmethod
    @typing.overload
    def ToAction(pyObject: Python.Runtime.PyObject) -> typing.Callable[[QuantConnect.Util.T1], None]:
        pass

    @staticmethod
    @typing.overload
    def ToAction(pyObject: Python.Runtime.PyObject) -> typing.Callable[[QuantConnect.Util.T1, QuantConnect.Util.T2], None]:
        pass

    def ToAction(self, *args) -> typing.Callable[[QuantConnect.Util.T1, QuantConnect.Util.T2], None]:
        pass

    @staticmethod
    def ToCoarseFundamentalSelector(pyObject: Python.Runtime.PyObject) -> typing.Callable[[typing.List[QuantConnect.Data.UniverseSelection.CoarseFundamental]], typing.List[QuantConnect.Symbol]]:
        pass

    @staticmethod
    def ToFineFundamentalSelector(pyObject: Python.Runtime.PyObject) -> typing.Callable[[typing.List[QuantConnect.Data.Fundamental.FineFundamental]], typing.List[QuantConnect.Symbol]]:
        pass

    @staticmethod
    def ToFunc(pyObject: Python.Runtime.PyObject) -> typing.Callable[[QuantConnect.Util.T1], QuantConnect.Util.T2]:
        pass


class RateGate(System.object, System.IDisposable):
    """
    Used to control the rate of some occurrence per unit of time.
    
    RateGate(occurrences: int, timeUnit: TimeSpan)
    """
    def Dispose(self) -> None:
        pass

    @typing.overload
    def WaitToProceed(self, millisecondsTimeout: int) -> bool:
        pass

    @typing.overload
    def WaitToProceed(self, timeout: datetime.timedelta) -> bool:
        pass

    @typing.overload
    def WaitToProceed(self) -> None:
        pass

    def WaitToProceed(self, *args) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, occurrences: int, timeUnit: datetime.timedelta) -> None:
        pass

    IsRateLimited: bool

    Occurrences: int

    TimeUnitMilliseconds: int



class ReaderWriterLockSlimExtensions(System.object):
    """ Provides extension methods to make working with the System.Threading.ReaderWriterLockSlim class easier """
    @staticmethod
    def Read(readerWriterLockSlim: System.Threading.ReaderWriterLockSlim) -> System.IDisposable:
        pass

    @staticmethod
    def Write(readerWriterLockSlim: System.Threading.ReaderWriterLockSlim) -> System.IDisposable:
        pass

    __all__: list


class ReferenceWrapper(System.object):
    """ ReferenceWrapper[T](value: T) """
    @staticmethod # known case of __new__
    def __new__(self, value: QuantConnect.Util.T) -> None:
        pass

    Value: QuantConnect.Util.T

class SecurityExtensions(System.object):
    """
    Provides useful infrastructure methods to the QuantConnect.Securities.Security class.
                These are added in this way to avoid mudding the class's public API
    """
    @staticmethod
    def IsInternalFeed(security: QuantConnect.Securities.Security) -> bool:
        pass

    __all__: list


class SecurityIdentifierJsonConverter(QuantConnect.Util.TypeChangeJsonConverter[SecurityIdentifier, str]):
    """
    A Newtonsoft.Json.JsonConverter implementation that serializes a QuantConnect.SecurityIdentifier as a string
    
    SecurityIdentifierJsonConverter()
    """


class SeriesJsonConverter(Newtonsoft.Json.JsonConverter):
    """
    Json Converter for Series which handles special Pie Series serialization case
    
    SeriesJsonConverter()
    """
    def CanConvert(self, objectType: type) -> bool:
        pass

    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: type, existingValue: object, serializer: Newtonsoft.Json.JsonSerializer) -> object:
        pass

    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: object, serializer: Newtonsoft.Json.JsonSerializer) -> None:
        pass

    CanRead: bool



class SingleValueListConverter(Newtonsoft.Json.JsonConverter):
    """ SingleValueListConverter[T]() """
    def CanConvert(self, objectType: type) -> bool:
        pass

    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: type, existingValue: object, serializer: Newtonsoft.Json.JsonSerializer) -> object:
        pass

    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: object, serializer: Newtonsoft.Json.JsonSerializer) -> None:
        pass


class StreamReaderEnumerable(System.object, System.Collections.Generic.IEnumerable[str], System.Collections.IEnumerable, System.IDisposable):
    """
    Converts a System.IO.StreamReader into an enumerable of string
    
    StreamReaderEnumerable(stream: Stream, *disposables: Array[IDisposable])
    StreamReaderEnumerable(reader: StreamReader, *disposables: Array[IDisposable])
    """
    def Dispose(self) -> None:
        pass

    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[str]:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, stream: System.IO.Stream, disposables: typing.List[System.IDisposable]) -> None:
        pass

    @typing.overload
    def __new__(self, reader: System.IO.StreamReader, disposables: typing.List[System.IDisposable]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass


class StreamReaderExtensions(System.object):
    """ Extension methods to fetch data from a System.IO.StreamReader instance """
    @staticmethod
    def GetDateTime(stream: System.IO.StreamReader, format: str, delimiter: str) -> datetime.datetime:
        pass

    @staticmethod
    @typing.overload
    def GetDecimal(stream: System.IO.StreamReader, delimiter: str) -> float:
        pass

    @staticmethod
    @typing.overload
    def GetDecimal(stream: System.IO.StreamReader, pastEndLine: System.Boolean, delimiter: str) -> float:
        pass

    def GetDecimal(self, *args) -> float:
        pass

    @staticmethod
    def GetInt32(stream: System.IO.StreamReader, delimiter: str) -> int:
        pass

    @staticmethod
    def GetString(stream: System.IO.StreamReader, delimiter: str) -> str:
        pass

    __all__: list


class TypeChangeJsonConverter(Newtonsoft.Json.JsonConverter):
    # no doc
    def CanConvert(self, objectType: type) -> bool:
        pass

    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: type, existingValue: object, serializer: Newtonsoft.Json.JsonSerializer) -> object:
        pass

    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: object, serializer: Newtonsoft.Json.JsonSerializer) -> None:
        pass



class Validate(System.object):
    """ Provides methods for validating strings following a certain format, such as an email address """
    @staticmethod
    def EmailAddress(emailAddress: str) -> bool:
        pass

    RegularExpression: type
    __all__: list


class VersionHelper(System.object):
    """ Provides methods for dealing with lean assembly versions """
    @staticmethod
    def CompareVersions(left: str, right: str) -> int:
        pass

    @staticmethod
    def IsEqualVersion(version: str) -> bool:
        pass

    @staticmethod
    def IsNewerVersion(version: str) -> bool:
        pass

    @staticmethod
    def IsNotEqualVersion(version: str) -> bool:
        pass

    @staticmethod
    def IsOlderVersion(version: str) -> bool:
        pass

    __all__: list


class WorkerThread(System.object, System.IDisposable):
    """
    This worker tread is required to guarantee all python operations are
                executed by the same thread, to enable complete debugging functionality.
                We don't use the main thread, to avoid any chance of blocking the process
    """
    def Add(self, action: System.Action) -> None:
        pass

    def Dispose(self) -> None:
        pass

    FinishedWorkItem: System.Threading.AutoResetEvent


    Instance: WorkerThread


class XElementExtensions(System.object):
    """ Provides extension methods for the XML to LINQ types """
    @staticmethod
    def Get(element: System.Xml.Linq.XElement, name: str) -> QuantConnect.Util.T:
        pass

    __all__: list


# variables with complex values

