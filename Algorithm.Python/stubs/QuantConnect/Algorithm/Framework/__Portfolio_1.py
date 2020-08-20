from .__Portfolio_2 import *
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


class EqualWeightingPortfolioConstructionModel(QuantConnect.Algorithm.Framework.Portfolio.PortfolioConstructionModel, QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel that gives equal weighting to all

                securities. The target percent holdings of each security is 1/N where N is the number of securities. For

                insights of direction QuantConnect.Algorithm.Framework.Alphas.InsightDirection.Up, long targets are returned and for insights of direction

                QuantConnect.Algorithm.Framework.Alphas.InsightDirection.Down, short targets are returned.

    

    EqualWeightingPortfolioConstructionModel(rebalancingDateRules: IDateRule, portfolioBias: PortfolioBias)

    EqualWeightingPortfolioConstructionModel(rebalancingFunc: Func[DateTime, Nullable[DateTime]], portfolioBias: PortfolioBias)

    EqualWeightingPortfolioConstructionModel(rebalancingFunc: Func[DateTime, DateTime], portfolioBias: PortfolioBias)

    EqualWeightingPortfolioConstructionModel(rebalance: PyObject, portfolioBias: PortfolioBias)

    EqualWeightingPortfolioConstructionModel(timeSpan: TimeSpan, portfolioBias: PortfolioBias)

    EqualWeightingPortfolioConstructionModel(resolution: Resolution, portfolioBias: PortfolioBias)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, rebalancingDateRules: QuantConnect.Scheduling.IDateRule, portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias) -> None:
        pass

    @typing.overload
    def __new__(self, rebalancingFunc: typing.Callable[[datetime.datetime], typing.Optional[datetime.datetime]], portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias) -> None:
        pass

    @typing.overload
    def __new__(self, rebalancingFunc: typing.Callable[[datetime.datetime], datetime.datetime], portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias) -> None:
        pass

    @typing.overload
    def __new__(self, rebalance: Python.Runtime.PyObject, portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias) -> None:
        pass

    @typing.overload
    def __new__(self, timeSpan: datetime.timedelta, portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias) -> None:
        pass

    @typing.overload
    def __new__(self, resolution: QuantConnect.Resolution, portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    PythonWrapper: QuantConnect.Algorithm.Framework.Portfolio.PortfolioConstructionModelPythonWrapper


class InsightWeightingPortfolioConstructionModel(QuantConnect.Algorithm.Framework.Portfolio.EqualWeightingPortfolioConstructionModel, QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel that generates percent targets based on the

                QuantConnect.Algorithm.Framework.Alphas.Insight.Weight. The target percent holdings of each Symbol is given by the QuantConnect.Algorithm.Framework.Alphas.Insight.Weight

                from the last active QuantConnect.Algorithm.Framework.Alphas.Insight for that symbol.

                For insights of direction QuantConnect.Algorithm.Framework.Alphas.InsightDirection.Up, long targets are returned and for insights of direction

                QuantConnect.Algorithm.Framework.Alphas.InsightDirection.Down, short targets are returned.

                If the sum of all the last active QuantConnect.Algorithm.Framework.Alphas.Insight per symbol is bigger than 1, it will factor down each target

                percent holdings proportionally so the sum is 1.

                It will ignore QuantConnect.Algorithm.Framework.Alphas.Insight that have no QuantConnect.Algorithm.Framework.Alphas.Insight.Weight value.

    

    InsightWeightingPortfolioConstructionModel(rebalancingDateRules: IDateRule, portfolioBias: PortfolioBias)

    InsightWeightingPortfolioConstructionModel(rebalance: PyObject, portfolioBias: PortfolioBias)

    InsightWeightingPortfolioConstructionModel(rebalancingFunc: Func[DateTime, Nullable[DateTime]], portfolioBias: PortfolioBias)

    InsightWeightingPortfolioConstructionModel(rebalancingFunc: Func[DateTime, DateTime], portfolioBias: PortfolioBias)

    InsightWeightingPortfolioConstructionModel(timeSpan: TimeSpan, portfolioBias: PortfolioBias)

    InsightWeightingPortfolioConstructionModel(resolution: Resolution, portfolioBias: PortfolioBias)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, rebalancingDateRules: QuantConnect.Scheduling.IDateRule, portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias) -> None:
        pass

    @typing.overload
    def __new__(self, rebalance: Python.Runtime.PyObject, portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias) -> None:
        pass

    @typing.overload
    def __new__(self, rebalancingFunc: typing.Callable[[datetime.datetime], typing.Optional[datetime.datetime]], portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias) -> None:
        pass

    @typing.overload
    def __new__(self, rebalancingFunc: typing.Callable[[datetime.datetime], datetime.datetime], portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias) -> None:
        pass

    @typing.overload
    def __new__(self, timeSpan: datetime.timedelta, portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias) -> None:
        pass

    @typing.overload
    def __new__(self, resolution: QuantConnect.Resolution, portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    PythonWrapper: QuantConnect.Algorithm.Framework.Portfolio.PortfolioConstructionModelPythonWrapper


class ConfidenceWeightedPortfolioConstructionModel(QuantConnect.Algorithm.Framework.Portfolio.InsightWeightingPortfolioConstructionModel, QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel that generates percent targets based on the

                QuantConnect.Algorithm.Framework.Alphas.Insight.Confidence. The target percent holdings of each Symbol is given by the QuantConnect.Algorithm.Framework.Alphas.Insight.Confidence

                from the last active QuantConnect.Algorithm.Framework.Alphas.Insight for that symbol.

                For insights of direction QuantConnect.Algorithm.Framework.Alphas.InsightDirection.Up, long targets are returned and for insights of direction

                QuantConnect.Algorithm.Framework.Alphas.InsightDirection.Down, short targets are returned.

                If the sum of all the last active QuantConnect.Algorithm.Framework.Alphas.Insight per symbol is bigger than 1, it will factor down each target

                percent holdings proportionally so the sum is 1.

                It will ignore QuantConnect.Algorithm.Framework.Alphas.Insight that have no QuantConnect.Algorithm.Framework.Alphas.Insight.Confidence value.

    

    ConfidenceWeightedPortfolioConstructionModel(rebalancingDateRules: IDateRule, portfolioBias: PortfolioBias)

    ConfidenceWeightedPortfolioConstructionModel(rebalance: PyObject, portfolioBias: PortfolioBias)

    ConfidenceWeightedPortfolioConstructionModel(rebalancingFunc: Func[DateTime, Nullable[DateTime]], portfolioBias: PortfolioBias)

    ConfidenceWeightedPortfolioConstructionModel(rebalancingFunc: Func[DateTime, DateTime], portfolioBias: PortfolioBias)

    ConfidenceWeightedPortfolioConstructionModel(timeSpan: TimeSpan, portfolioBias: PortfolioBias)

    ConfidenceWeightedPortfolioConstructionModel(resolution: Resolution, portfolioBias: PortfolioBias)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, rebalancingDateRules: QuantConnect.Scheduling.IDateRule, portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias) -> None:
        pass

    @typing.overload
    def __new__(self, rebalance: Python.Runtime.PyObject, portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias) -> None:
        pass

    @typing.overload
    def __new__(self, rebalancingFunc: typing.Callable[[datetime.datetime], typing.Optional[datetime.datetime]], portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias) -> None:
        pass

    @typing.overload
    def __new__(self, rebalancingFunc: typing.Callable[[datetime.datetime], datetime.datetime], portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias) -> None:
        pass

    @typing.overload
    def __new__(self, timeSpan: datetime.timedelta, portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias) -> None:
        pass

    @typing.overload
    def __new__(self, resolution: QuantConnect.Resolution, portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    PythonWrapper: QuantConnect.Algorithm.Framework.Portfolio.PortfolioConstructionModelPythonWrapper


class IPortfolioConstructionModel(QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """ Algorithm framework model that """
    def CreateTargets(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, insights: typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight]) -> typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        pass


class IPortfolioOptimizer:
    """ Interface for portfolio optimization algorithms """
    def Optimize(self, historicalReturns: typing.List[typing.List[float]], expectedReturns: typing.List[float], covariance: typing.List[typing.List[float]]) -> typing.List[float]:
        pass
