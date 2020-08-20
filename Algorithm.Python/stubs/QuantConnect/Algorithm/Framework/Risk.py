import typing
import QuantConnect.Data.UniverseSelection
import QuantConnect.Algorithm.Framework.Risk
import QuantConnect.Algorithm.Framework.Portfolio
import QuantConnect.Algorithm
import Python.Runtime
import datetime

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


class MaximumDrawdownPercentPerSecurity(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel, QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel that limits the drawdown

                per holding to the specified percentage

    

    MaximumDrawdownPercentPerSecurity(maximumDrawdownPercent: Decimal)
    """
    def ManageRisk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        pass

    @staticmethod # known case of __new__
    def __new__(self, maximumDrawdownPercent: float) -> None:
        pass


class MaximumDrawdownPercentPortfolio(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel, QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel that limits the drawdown of the portfolio

                to the specified percentage. Once this is triggered the algorithm will need to be manually restarted.

    

    MaximumDrawdownPercentPortfolio(maximumDrawdownPercent: Decimal, isTrailing: bool)
    """
    def ManageRisk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        pass

    @staticmethod # known case of __new__
    def __new__(self, maximumDrawdownPercent: float, isTrailing: bool) -> None:
        pass


class MaximumSectorExposureRiskManagementModel(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel, QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel that limits

                the sector exposure to the specified percentage

    

    MaximumSectorExposureRiskManagementModel(maximumSectorExposure: Decimal)
    """
    def ManageRisk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        pass

    def OnSecuritiesChanged(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, maximumSectorExposure: float) -> None:
        pass


class MaximumUnrealizedProfitPercentPerSecurity(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel, QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel that limits the unrealized profit

                per holding to the specified percentage

    

    MaximumUnrealizedProfitPercentPerSecurity(maximumUnrealizedProfitPercent: Decimal)
    """
    def ManageRisk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        pass

    @staticmethod # known case of __new__
    def __new__(self, maximumUnrealizedProfitPercent: float) -> None:
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


class TrailingStopRiskManagementModel(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel, QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel that limits the maximum possible loss

                measured from the highest unrealized profit

    

    TrailingStopRiskManagementModel(maximumDrawdownPercent: Decimal)
    """
    def ManageRisk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        pass

    @staticmethod # known case of __new__
    def __new__(self, maximumDrawdownPercent: float) -> None:
        pass
