# encoding: utf-8
# module QuantConnect.Algorithm.Framework.Portfolio calls itself Portfolio
# from QuantConnect.Algorithm, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null, QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import Python.Runtime
import QuantConnect
import QuantConnect.Algorithm
import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.Algorithm.Framework.Portfolio
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import System.Collections.Generic
import typing

# no functions
# classes

class IPortfolioConstructionModel(QuantConnect.Algorithm.Framework.INotifiedSecurityChanges):
    """ Algorithm framework model that """
    def CreateTargets(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, insights: typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight]) -> typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        pass


class IPortfolioOptimizer:
    """ Interface for portfolio optimization algorithms """
    def Optimize(self, historicalReturns: typing.List[typing.List[float]], expectedReturns: typing.List[float], covariance: typing.List[typing.List[float]]) -> typing.List[float]:
        pass


class IPortfolioTarget:
    """
    Represents a portfolio target. This may be a percentage of total portfolio value
                or it may be a fixed number of shares.
    """
    Quantity: float

    Symbol: QuantConnect.Symbol



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
    Long: PortfolioBias
    LongShort: PortfolioBias
    Short: PortfolioBias


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


