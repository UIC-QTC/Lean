# encoding: utf-8
# module QuantConnect.Parameters calls itself Parameters
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import System.Collections.Generic
import System.Reflection
import typing

# no functions
# classes

class ParameterAttribute(System.Attribute, System.Runtime.InteropServices._Attribute):
    """
    Specifies a field or property is a parameter that can be set
                from an QuantConnect.Packets.AlgorithmNodePacket.Parameters dictionary
    
    ParameterAttribute(name: str)
    """
    @staticmethod
    def ApplyAttributes(parameters: System.Collections.Generic.Dictionary[str, str], instance: object) -> None:
        pass

    @staticmethod
    def GetParametersFromAssembly(assembly: System.Reflection.Assembly) -> System.Collections.Generic.Dictionary[str, str]:
        pass

    @staticmethod
    def GetParametersFromType(type: type) -> typing.List[System.Collections.Generic.KeyValuePair[str, str]]:
        pass

    @staticmethod # known case of __new__
    def __new__(self, name: str) -> None:
        pass

    Name: str


    BindingFlags: BindingFlags


