# encoding: utf-8
# module QuantConnect.Algorithm.Framework.Risk calls itself Risk
# from QuantConnect.Algorithm, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import Python.Runtime
import QuantConnect.Algorithm
import QuantConnect.Algorithm.Framework.Portfolio
import QuantConnect.Algorithm.Framework.Risk
import QuantConnect.Data.UniverseSelection
import typing

# no functions
# classes

class RiskManagementModel(System.object, QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides a base class for risk management models
    
    RiskManagementModel()
    """
    def ManageRisk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        pass

    def OnSecuritiesChanged(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        pass


class CompositeRiskManagementModel(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel, QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel that combines multiple risk
                models into a single risk management model and properly sets each insights 'SourceModel' property.
    
    CompositeRiskManagementModel(*riskManagementModels: Array[IRiskManagementModel])
    CompositeRiskManagementModel(riskManagementModels: IEnumerable[IRiskManagementModel])
    CompositeRiskManagementModel(*riskManagementModels: Array[PyObject])
    CompositeRiskManagementModel(riskManagementModel: PyObject)
    """
    @typing.overload
    def AddRiskManagement(self, riskManagementModel: QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel) -> None:
        pass

    @typing.overload
    def AddRiskManagement(self, pyRiskManagementModel: Python.Runtime.PyObject) -> None:
        pass

    def AddRiskManagement(self, *args) -> None:
        pass

    def ManageRisk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        pass

    def OnSecuritiesChanged(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, riskManagementModels: typing.List[QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel]) -> None:
        pass

    @typing.overload
    def __new__(self, riskManagementModels: typing.List[QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel]) -> None:
        pass

    @typing.overload
    def __new__(self, riskManagementModels: typing.List[Python.Runtime.PyObject]) -> None:
        pass

    @typing.overload
    def __new__(self, riskManagementModel: Python.Runtime.PyObject) -> None:
        pass

    def __new__(self, *args) -> None:
        pass


class IRiskManagementModel(QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """ Algorithm framework model that manages an algorithm's risk/downside """
    def ManageRisk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        pass


class NullRiskManagementModel(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel, QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel that does nothing
    
    NullRiskManagementModel()
    """
    def ManageRisk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        pass


class RiskManagementModelPythonWrapper(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel, QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel that wraps a Python.Runtime.PyObject object
    
    RiskManagementModelPythonWrapper(model: PyObject)
    """
    def ManageRisk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        pass

    def OnSecuritiesChanged(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, model: Python.Runtime.PyObject) -> None:
        pass


