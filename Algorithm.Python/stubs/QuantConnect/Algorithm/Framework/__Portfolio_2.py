from .__Portfolio_3 import *
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


class IPortfolioTarget:
    """
    Represents a portfolio target. This may be a percentage of total portfolio value

                or it may be a fixed number of shares.
    """
    Quantity: float

    Symbol: QuantConnect.Symbol



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


class MeanVarianceOptimizationPortfolioConstructionModel(QuantConnect.Algorithm.Framework.Portfolio.PortfolioConstructionModel, QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides an implementation of Mean-Variance portfolio optimization based on modern portfolio theory.

                The interval of weights in optimization method can be changed based on the long-short algorithm.

                The default model uses the last three months daily price to calculate the optimal weight

                with the weight range from -1 to 1 and minimize the portfolio variance with a target return of 2%

    

    MeanVarianceOptimizationPortfolioConstructionModel(rebalancingDateRules: IDateRule, portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, targetReturn: float, optimizer: IPortfolioOptimizer)

    MeanVarianceOptimizationPortfolioConstructionModel(rebalanceResolution: Resolution, portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, targetReturn: float, optimizer: IPortfolioOptimizer)

    MeanVarianceOptimizationPortfolioConstructionModel(timeSpan: TimeSpan, portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, targetReturn: float, optimizer: IPortfolioOptimizer)

    MeanVarianceOptimizationPortfolioConstructionModel(rebalance: PyObject, portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, targetReturn: float, optimizer: IPortfolioOptimizer)

    MeanVarianceOptimizationPortfolioConstructionModel(rebalancingFunc: Func[DateTime, DateTime], portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, targetReturn: float, optimizer: IPortfolioOptimizer)

    MeanVarianceOptimizationPortfolioConstructionModel(rebalancingFunc: Func[DateTime, Nullable[DateTime]], portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, targetReturn: float, optimizer: IPortfolioOptimizer)
    """
    def OnSecuritiesChanged(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, rebalancingDateRules: QuantConnect.Scheduling.IDateRule, portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias, lookback: int, period: int, resolution: QuantConnect.Resolution, targetReturn: float, optimizer: QuantConnect.Algorithm.Framework.Portfolio.IPortfolioOptimizer) -> None:
        pass

    @typing.overload
    def __new__(self, rebalanceResolution: QuantConnect.Resolution, portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias, lookback: int, period: int, resolution: QuantConnect.Resolution, targetReturn: float, optimizer: QuantConnect.Algorithm.Framework.Portfolio.IPortfolioOptimizer) -> None:
        pass

    @typing.overload
    def __new__(self, timeSpan: datetime.timedelta, portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias, lookback: int, period: int, resolution: QuantConnect.Resolution, targetReturn: float, optimizer: QuantConnect.Algorithm.Framework.Portfolio.IPortfolioOptimizer) -> None:
        pass

    @typing.overload
    def __new__(self, rebalance: Python.Runtime.PyObject, portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias, lookback: int, period: int, resolution: QuantConnect.Resolution, targetReturn: float, optimizer: QuantConnect.Algorithm.Framework.Portfolio.IPortfolioOptimizer) -> None:
        pass

    @typing.overload
    def __new__(self, rebalancingFunc: typing.Callable[[datetime.datetime], datetime.datetime], portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias, lookback: int, period: int, resolution: QuantConnect.Resolution, targetReturn: float, optimizer: QuantConnect.Algorithm.Framework.Portfolio.IPortfolioOptimizer) -> None:
        pass

    @typing.overload
    def __new__(self, rebalancingFunc: typing.Callable[[datetime.datetime], typing.Optional[datetime.datetime]], portfolioBias: QuantConnect.Algorithm.Framework.Portfolio.PortfolioBias, lookback: int, period: int, resolution: QuantConnect.Resolution, targetReturn: float, optimizer: QuantConnect.Algorithm.Framework.Portfolio.IPortfolioOptimizer) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    PythonWrapper: QuantConnect.Algorithm.Framework.Portfolio.PortfolioConstructionModelPythonWrapper


class MinimumVariancePortfolioOptimizer(System.object, QuantConnect.Algorithm.Framework.Portfolio.IPortfolioOptimizer):
    """
    Provides an implementation of a minimum variance portfolio optimizer that calculate the optimal weights

                with the weight range from -1 to 1 and minimize the portfolio variance with a target return of 2%

    

    MinimumVariancePortfolioOptimizer(lower: float, upper: float, targetReturn: float)
    """
    def Optimize(self, historicalReturns: typing.List[typing.List[float]], expectedReturns: typing.List[float], covariance: typing.List[typing.List[float]]) -> typing.List[float]:
        pass

    @staticmethod # known case of __new__
    def __new__(self, lower: float, upper: float, targetReturn: float) -> None:
        pass


class NullPortfolioConstructionModel(QuantConnect.Algorithm.Framework.Portfolio.PortfolioConstructionModel, QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel that does nothing

    

    NullPortfolioConstructionModel()
    """
    def CreateTargets(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, insights: typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight]) -> typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        pass

    PythonWrapper: QuantConnect.Algorithm.Framework.Portfolio.PortfolioConstructionModelPythonWrapper


class PortfolioBias(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Specifies the bias of the portfolio (Short, Long/Short, Long)

    

    enum PortfolioBias, values: Long (1), LongShort (0), Short (-1)
    """
    value__: int
    Long: 'PortfolioBias'
    LongShort: 'PortfolioBias'
    Short: 'PortfolioBias'


class PortfolioConstructionModelPythonWrapper(QuantConnect.Algorithm.Framework.Portfolio.PortfolioConstructionModel, QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel, QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel that wraps a Python.Runtime.PyObject object

    

    PortfolioConstructionModelPythonWrapper(model: PyObject)
    """
    def CreateTargets(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, insights: typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight]) -> typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        pass

    def OnSecuritiesChanged(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, model: Python.Runtime.PyObject) -> None:
        pass

    RebalanceOnInsightChanges: bool

    RebalanceOnSecurityChanges: bool

    PythonWrapper: QuantConnect.Algorithm.Framework.Portfolio.PortfolioConstructionModelPythonWrapper


class PortfolioTarget(System.object, QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget that specifies a

                specified quantity of a security to be held by the algorithm

    

    PortfolioTarget(symbol: Symbol, quantity: Decimal)
    """
    @staticmethod
    @typing.overload
    def Percent(algorithm: QuantConnect.Interfaces.IAlgorithm, symbol: QuantConnect.Symbol, percent: float) -> QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget:
        pass

    @staticmethod
    @typing.overload
    def Percent(algorithm: QuantConnect.Interfaces.IAlgorithm, symbol: QuantConnect.Symbol, percent: float, returnDeltaQuantity: bool) -> QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget:
        pass

    def Percent(self, *args) -> QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    def __new__(self, symbol: QuantConnect.Symbol, quantity: float) -> None:
        pass

    Quantity: float

    Symbol: QuantConnect.Symbol



class PortfolioTargetCollection(System.object, System.Collections.Generic.ICollection[IPortfolioTarget], System.Collections.Generic.IEnumerable[IPortfolioTarget], System.Collections.IEnumerable, System.Collections.Generic.IDictionary[Symbol, IPortfolioTarget], System.Collections.Generic.ICollection[KeyValuePair[Symbol, IPortfolioTarget]], System.Collections.Generic.IEnumerable[KeyValuePair[Symbol, IPortfolioTarget]]):
    """
    Provides a collection for managing QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTargets for each symbol

    

    PortfolioTargetCollection()
    """
    @typing.overload
    def Add(self, target: QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget) -> None:
        pass

    @typing.overload
    def Add(self, target: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> None:
        pass

    @typing.overload
    def Add(self, symbol: QuantConnect.Symbol, target: QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget) -> None:
        pass

    def Add(self, *args) -> None:
        pass

    @typing.overload
    def AddRange(self, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> None:
        pass

    @typing.overload
    def AddRange(self, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> None:
        pass

    def AddRange(self, *args) -> None:
        pass

    def Clear(self) -> None:
        pass

    def ClearFulfilled(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        pass

    @typing.overload
    def Contains(self, target: QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget) -> bool:
        pass

    @typing.overload
    def Contains(self, target: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> bool:
        pass

    def Contains(self, *args) -> bool:
        pass

    def ContainsKey(self, symbol: QuantConnect.Symbol) -> bool:
        pass

    @typing.overload
    def CopyTo(self, array: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget], arrayIndex: int) -> None:
        pass

    @typing.overload
    def CopyTo(self, array: typing.List[System.Collections.Generic.KeyValuePair], arrayIndex: int) -> None:
        pass

    def CopyTo(self, *args) -> None:
        pass

    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        pass

    def OrderByMarginImpact(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        pass

    @typing.overload
    def Remove(self, symbol: QuantConnect.Symbol) -> bool:
        pass

    @typing.overload
    def Remove(self, target: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> bool:
        pass

    @typing.overload
    def Remove(self, target: QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget) -> bool:
        pass

    def Remove(self, *args) -> bool:
        pass

    def TryGetValue(self, symbol: QuantConnect.Symbol, target: QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget) -> bool:
        pass

    Count: int

    IsReadOnly: bool

    Keys: typing.List[QuantConnect.Symbol]

    Values: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]


    Item: indexer#
