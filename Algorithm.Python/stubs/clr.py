# encoding: utf-8
# module clr
# from (built-in)
# by generator 1.145
""" module() """

# imports
import datetime
import IronPython.Runtime
import System.Reflection
import System.Runtime.CompilerServices
import typing

# Variables with simple values

IsDebug = False
IsMacOS = False
IsMono = False
IsNetCoreApp = False

TargetFramework = '.NETFramework,Version=v4.5'

# functions

def accepts(*types, p_object=None): # real signature unknown; restored from __doc__
    """ accepts(*types: Array[object]) -> object """
    return object()

def AddReference(*args, **kwargs): # real signature unknown
    """
    Adds a reference to a .NET assembly.  Parameters can be an already loaded
    Assembly object, a full assembly name, or a partial assembly name. After the
    load the assemblies namespaces and top-level types will be available via 
    import Namespace.
    """
    pass

def AddReferenceByName(*args, **kwargs): # real signature unknown
    """
    Adds a reference to a .NET assembly.  Parameters are an assembly name. 
    After the load the assemblies namespaces and top-level types will be available via 
    import Namespace.
    """
    pass

def AddReferenceByPartialName(*args, **kwargs): # real signature unknown
    """
    Adds a reference to a .NET assembly.  Parameters are a partial assembly name. 
    After the load the assemblies namespaces and top-level types will be available via 
    import Namespace.
    """
    pass

def AddReferenceToFile(*args, **kwargs): # real signature unknown
    """
    Adds a reference to a .NET assembly.  One or more assembly names can
    be provided.  The assembly is searched for in the directories specified in 
    sys.path and dependencies will be loaded from sys.path as well.  The assembly 
    name should be the filename on disk without a directory specifier and 
    optionally including the .EXE or .DLL extension. After the load the assemblies 
    namespaces and top-level types will be available via import Namespace.
    """
    pass

def AddReferenceToFileAndPath(*args, **kwargs): # real signature unknown
    """
    Adds a reference to a .NET assembly.  One or more assembly names can
    be provided which are fully qualified names to the file on disk.  The 
    directory is added to sys.path and AddReferenceToFile is then called. After the 
    load the assemblies namespaces and top-level types will be available via 
    import Namespace.
    """
    pass

def AddReferenceToTypeLibrary(rcw): # real signature unknown; restored from __doc__
    """ AddReferenceToTypeLibrary(rcw: object)AddReferenceToTypeLibrary(typeLibGuid: Guid) """
    pass

def ClearProfilerData(): # real signature unknown; restored from __doc__
    """ ClearProfilerData() """
    pass

def CompileModules(assemblyName, **kwArgs, p_str=None, p_object=None, *args): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ CompileModules(assemblyName: str, **kwArgs: IDictionary[str, object], *filenames: Array[str]) """
    pass

def CompileSubclassTypes(assemblyName, *newTypes, p_object=None): # real signature unknown; restored from __doc__
    """ CompileSubclassTypes(assemblyName: str, *newTypes: Array[object]) """
    pass

def Convert(o, toType): # real signature unknown; restored from __doc__
    """ Convert(o: object, toType: Type) -> object """
    return object()

def Deserialize(serializationFormat, data): # real signature unknown; restored from __doc__
    """ Deserialize(serializationFormat: str, data: str) -> object """
    return object()

def Dir(o): # real signature unknown; restored from __doc__
    """ Dir(o: object) -> list """
    return []

def DirClr(o): # real signature unknown; restored from __doc__
    """ DirClr(o: object) -> list """
    return []

def EnableProfiler(enable): # real signature unknown; restored from __doc__
    """ EnableProfiler(enable: bool) """
    pass

def GetBytes(*args, **kwargs): # real signature unknown
    """ Converts a string to an array of bytesConverts maxCount of a string to an array of bytes """
    pass

def GetClrType(type): # real signature unknown; restored from __doc__
    """ GetClrType(type: Type) -> Type """
    pass

def GetCurrentRuntime(): # real signature unknown; restored from __doc__
    """ GetCurrentRuntime() -> ScriptDomainManager """
    pass

def GetDynamicType(t): # real signature unknown; restored from __doc__
    """ GetDynamicType(t: Type) -> type """
    return type(*(), **{})

def GetProfilerData(includeUnused): # real signature unknown; restored from __doc__
    """ GetProfilerData(includeUnused: bool) -> tuple """
    return ()

def GetPythonType(t): # real signature unknown; restored from __doc__
    """ GetPythonType(t: Type) -> type """
    return type(*(), **{})

def GetString(*args, **kwargs): # real signature unknown
    """ Converts an array of bytes to a string.Converts maxCount of an array of bytes to a string """
    pass

def GetSubclassedTypes(): # real signature unknown; restored from __doc__
    """ GetSubclassedTypes() -> tuple """
    return ()

def ImportExtensions(namespace, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ ImportExtensions(namespace: namespace#)ImportExtensions(type: type) """
    pass

def LoadAssemblyByName(*args, **kwargs): # real signature unknown
    """
    Loads an assembly from the specified assembly name and returns the assembly
    object.  Namespaces or types in the assembly can be accessed directly from 
    the assembly object.
    """
    pass

def LoadAssemblyByPartialName(*args, **kwargs): # real signature unknown
    """
    Loads an assembly from the specified partial assembly name and returns the 
    assembly object.  Namespaces or types in the assembly can be accessed directly 
    from the assembly object.
    """
    pass

def LoadAssemblyFromFile(*args, **kwargs): # real signature unknown
    """
    Loads an assembly from the specified filename and returns the assembly
    object.  Namespaces or types in the assembly can be accessed directly from 
    the assembly object.
    """
    pass

def LoadAssemblyFromFileWithPath(*args, **kwargs): # real signature unknown
    """
    Adds a reference to a .NET assembly.  Parameters are a full path to an. 
    assembly on disk. After the load the assemblies namespaces and top-level types 
    will be available via import Namespace.
    """
    pass

def LoadTypeLibrary(rcw): # real signature unknown; restored from __doc__
    """
    LoadTypeLibrary(rcw: object) -> ComTypeLibInfo
    LoadTypeLibrary(typeLibGuid: Guid) -> ComTypeLibInfo
    """
    pass

def returns(type): # real signature unknown; restored from __doc__
    """ returns(type: object) -> object """
    return object()

def Self(): # real signature unknown; restored from __doc__
    """ Self() -> object """
    return object()

def Serialize(self): # real signature unknown; restored from __doc__
    """ Serialize(self: object) -> tuple """
    return ()

def SetCommandDispatcher(dispatcher, Action=None): # real signature unknown; restored from __doc__
    """ SetCommandDispatcher(dispatcher: Action[Action]) -> Action[Action] """
    pass

def Use(name): # real signature unknown; restored from __doc__
    """
    Use(name: str) -> object
    Use(path: str, language: str) -> object
    """
    return object()

# classes

class ArgChecker(System.object):
    """ ArgChecker(prms: Array[object]) """
    @staticmethod # known case of __new__
    def __new__(self, prms: typing.List[object]) -> None:
        pass

    def __init__(self, *args):
        pass

class StrongBox(System.object, System.Runtime.CompilerServices.IStrongBox):
    """
    StrongBox[T]()
    StrongBox[T](value: T)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, value: System.Runtime.CompilerServices.T) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    def __init__(self, *args):
        self.Value: System.Runtime.CompilerServices.T

Reference = StrongBox


class ReferencesList(System.Collections.Generic.List[Assembly], System.Collections.Generic.IList[Assembly], System.Collections.Generic.ICollection[Assembly], System.Collections.Generic.IEnumerable[Assembly], System.Collections.IEnumerable, System.Collections.IList, System.Collections.ICollection, System.Collections.Generic.IReadOnlyList[Assembly], System.Collections.Generic.IReadOnlyCollection[Assembly], IronPython.Runtime.ICodeFormattable):
    """ ReferencesList() """
    @typing.overload
    def Add(self, other: System.Reflection.Assembly) -> None:
        pass

    @typing.overload
    def Add(self, other: object) -> IronPython.Runtime.ReferencesList:
        pass

    @typing.overload
    def Add(self, item: System.Reflection.Assembly) -> None:
        pass

    def Add(self, *args) -> None:
        pass

    def __repr__(self, context: IronPython.Runtime.CodeContext) -> str:
        pass

    def __init__(self, *args):
        pass

class ReturnChecker(System.object):
    """ ReturnChecker(returnType: object) """
    @staticmethod # known case of __new__
    def __new__(self, returnType: object) -> None:
        pass

    def __init__(self, *args):
        self.retType: object

class RuntimeArgChecker(IronPython.Runtime.Types.PythonTypeSlot):
    """
    RuntimeArgChecker(function: object, expectedArgs: Array[object])
    RuntimeArgChecker(instance: object, function: object, expectedArgs: Array[object])
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, function: object, expectedArgs: typing.List[object]) -> None:
        pass

    @typing.overload
    def __new__(self, instance: object, function: object, expectedArgs: typing.List[object]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    def __init__(self, *args):
        pass

class RuntimeReturnChecker(IronPython.Runtime.Types.PythonTypeSlot):
    """
    RuntimeReturnChecker(function: object, expectedReturn: object)
    RuntimeReturnChecker(instance: object, function: object, expectedReturn: object)
    """
    def GetAttribute(self, instance: object, owner: object) -> object:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, function: object, expectedReturn: object) -> None:
        pass

    @typing.overload
    def __new__(self, instance: object, function: object, expectedReturn: object) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    def __init__(self, *args):
        pass

# variables with complex values

References = None

