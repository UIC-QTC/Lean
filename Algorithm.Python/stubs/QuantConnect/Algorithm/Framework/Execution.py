# encoding: utf-8
# module QuantConnect.Algorithm.Framework.Execution calls itself Execution
# from QuantConnect.Algorithm, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import Python.Runtime
import QuantConnect.Algorithm
import QuantConnect.Algorithm.Framework.Portfolio
import QuantConnect.Data.UniverseSelection
import typing

# no functions
# classes

class ExecutionModel(System.object, QuantConnect.Algorithm.Framework.Execution.IExecutionModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides a base class for execution models
    
    ExecutionModel()
    """
    def Execute(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> None:
        pass

    def OnSecuritiesChanged(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        pass


class ExecutionModelPythonWrapper(QuantConnect.Algorithm.Framework.Execution.ExecutionModel, QuantConnect.Algorithm.Framework.Execution.IExecutionModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Execution.IExecutionModel that wraps a Python.Runtime.PyObject object
    
    ExecutionModelPythonWrapper(model: PyObject)
    """
    def Execute(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> None:
        pass

    def OnSecuritiesChanged(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, model: Python.Runtime.PyObject) -> None:
        pass


class IExecutionModel(QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """ Algorithm framework model that executes portfolio targets """
    def Execute(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> None:
        pass


class ImmediateExecutionModel(QuantConnect.Algorithm.Framework.Execution.ExecutionModel, QuantConnect.Algorithm.Framework.Execution.IExecutionModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Execution.IExecutionModel that immediately submits
                market orders to achieve the desired portfolio targets
    
    ImmediateExecutionModel()
    """
    def Execute(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> None:
        pass

    def OnSecuritiesChanged(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        pass


class NullExecutionModel(QuantConnect.Algorithm.Framework.Execution.ExecutionModel, QuantConnect.Algorithm.Framework.Execution.IExecutionModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Execution.IExecutionModel that does nothing
    
    NullExecutionModel()
    """
    def Execute(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> None:
        pass


