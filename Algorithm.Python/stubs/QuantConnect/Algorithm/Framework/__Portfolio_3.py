import typing
import System.Collections.Generic
import System
import QuantConnect.Scheduling
import QuantConnect.Interfaces
import QuantConnect.Data.UniverseSelection
import QuantConnect.Algorithm.Framework.Portfolio
import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.Algorithm
import QuantConnect
import Python.Runtime
import datetime


class ReturnsSymbolData(System.object):
    """
    Contains returns specific to a symbol required for optimization model

    

    ReturnsSymbolData(symbol: Symbol, lookback: int, period: int)
    """
    def Add(self, time: datetime.datetime, value: float) -> None:
        pass

    def Reset(self) -> None:
        pass

    def Update(self, time: datetime.datetime, value: float) -> bool:
        pass

    @staticmethod # known case of __new__
    def __new__(self, symbol: QuantConnect.Symbol, lookback: int, period: int) -> None:
        pass

    Returns: System.Collections.Generic.Dictionary[datetime.datetime, float]



class ReturnsSymbolDataExtensions(System.object):
    """ Extension methods for QuantConnect.Algorithm.Framework.Portfolio.ReturnsSymbolData """
    @staticmethod
    def FormReturnsMatrix(symbolData: System.Collections.Generic.Dictionary[QuantConnect.Symbol, QuantConnect.Algorithm.Framework.Portfolio.ReturnsSymbolData], symbols: typing.List[QuantConnect.Symbol]) -> typing.List[typing.List[float]]:
        pass

    __all__: list


class SectorWeightingPortfolioConstructionModel(QuantConnect.Algorithm.Framework.Portfolio.EqualWeightingPortfolioConstructionModel, QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel that generates percent targets based on the

                QuantConnect.Data.Fundamental.CompanyReference.IndustryTemplateCode. 

                The target percent holdings of each sector is 1/S where S is the number of sectors and

                the target percent holdings of each security is 1/N where N is the number of securities of each sector.

                For insights of direction QuantConnect.Algorithm.Framework.Alphas.InsightDirection.Up, long targets are returned and for insights of direction

                QuantConnect.Algorithm.Framework.Alphas.InsightDirection.Down, short targets are returned.

                It will ignore QuantConnect.Algorithm.Framework.Alphas.Insight for symbols that have no QuantConnect.Data.Fundamental.CompanyReference.IndustryTemplateCode value.

    

    SectorWeightingPortfolioConstructionModel(rebalancingDateRules: IDateRule)

    SectorWeightingPortfolioConstructionModel(rebalancingFunc: Func[DateTime, Nullable[DateTime]])

    SectorWeightingPortfolioConstructionModel(rebalancingFunc: Func[DateTime, DateTime])

    SectorWeightingPortfolioConstructionModel(rebalance: PyObject)

    SectorWeightingPortfolioConstructionModel(timeSpan: TimeSpan)

    SectorWeightingPortfolioConstructionModel(resolution: Resolution)
    """
    def OnSecuritiesChanged(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, rebalancingDateRules: QuantConnect.Scheduling.IDateRule) -> None:
        pass

    @typing.overload
    def __new__(self, rebalancingFunc: typing.Callable[[datetime.datetime], typing.Optional[datetime.datetime]]) -> None:
        pass

    @typing.overload
    def __new__(self, rebalancingFunc: typing.Callable[[datetime.datetime], datetime.datetime]) -> None:
        pass

    @typing.overload
    def __new__(self, rebalance: Python.Runtime.PyObject) -> None:
        pass

    @typing.overload
    def __new__(self, timeSpan: datetime.timedelta) -> None:
        pass

    @typing.overload
    def __new__(self, resolution: QuantConnect.Resolution) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    PythonWrapper: QuantConnect.Algorithm.Framework.Portfolio.PortfolioConstructionModelPythonWrapper


class UnconstrainedMeanVariancePortfolioOptimizer(System.object, QuantConnect.Algorithm.Framework.Portfolio.IPortfolioOptimizer):
    """
    Provides an implementation of a portfolio optimizer with unconstrained mean variance.

    

    UnconstrainedMeanVariancePortfolioOptimizer()
    """
    def Optimize(self, historicalReturns: typing.List[typing.List[float]], expectedReturns: typing.List[float], covariance: typing.List[typing.List[float]]) -> typing.List[float]:
        pass

# no functions
# classes

class IPortfolioConstructionModel(QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """ Algorithm framework model that """
    def CreateTargets(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, insights: typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight]) -> typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        pass


class PortfolioConstructionModel(System.object, QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides a base class for portfolio construction models

    

    PortfolioConstructionModel(rebalancingFunc: Func[DateTime, Nullable[DateTime]])

    PortfolioConstructionModel(rebalancingFunc: Func[DateTime, DateTime])
    """
    def CreateTargets(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, insights: typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight]) -> typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        pass

    def OnSecuritiesChanged(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, rebalancingFunc: typing.Callable[[datetime.datetime], typing.Optional[datetime.datetime]]) -> None:
        pass

    @typing.overload
    def __new__(self, rebalancingFunc: typing.Callable[[datetime.datetime], datetime.datetime]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    RebalanceOnInsightChanges: bool

    RebalanceOnSecurityChanges: bool

    PythonWrapper: QuantConnect.Algorithm.Framework.Portfolio.PortfolioConstructionModelPythonWrapper


class MaximumSharpeRatioPortfolioOptimizer(System.object, QuantConnect.Algorithm.Framework.Portfolio.IPortfolioOptimizer):
    """
    Provides an implementation of a portfolio optimizer that maximizes the portfolio Sharpe Ratio.

                The interval of weights in optimization method can be changed based on the long-short algorithm.

                The default model uses flat risk free rate and weight for an individual security range from -1 to 1.

    

    MaximumSharpeRatioPortfolioOptimizer(lower: float, upper: float, riskFreeRate: float)
    """
    def Optimize(self, historicalReturns: typing.List[typing.List[float]], expectedReturns: typing.List[float], covariance: typing.List[typing.List[float]]) -> typing.List[float]:
        pass

    @staticmethod # known case of __new__
    def __new__(self, lower: float, upper: float, riskFreeRate: float) -> None:
        pass
