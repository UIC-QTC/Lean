# encoding: utf-8
# module QuantConnect.Statistics calls itself Statistics
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import QuantConnect
import QuantConnect.Interfaces
import QuantConnect.Orders
import QuantConnect.Statistics
import System
import System.Collections.Generic
import typing

# no functions
# classes

class AlgorithmPerformance(System.object):
    """
    The QuantConnect.Statistics.AlgorithmPerformance class is a wrapper for QuantConnect.Statistics.AlgorithmPerformance.TradeStatistics and QuantConnect.Statistics.AlgorithmPerformance.PortfolioStatistics
    
    AlgorithmPerformance(trades: List[Trade], profitLoss: SortedDictionary[DateTime, Decimal], equity: SortedDictionary[DateTime, Decimal], listPerformance: List[float], listBenchmark: List[float], startingCapital: Decimal)
    AlgorithmPerformance()
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, trades: typing.List[QuantConnect.Statistics.Trade], profitLoss: System.Collections.Generic.SortedDictionary[datetime.datetime, float], equity: System.Collections.Generic.SortedDictionary[datetime.datetime, float], listPerformance: typing.List[float], listBenchmark: typing.List[float], startingCapital: float) -> None:
        pass

    @typing.overload
    def __new__(self) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    ClosedTrades: typing.List[QuantConnect.Statistics.Trade]

    PortfolioStatistics: QuantConnect.Statistics.PortfolioStatistics

    TradeStatistics: QuantConnect.Statistics.TradeStatistics



class FillGroupingMethod(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    The method used to group order fills into trades
    
    enum FillGroupingMethod, values: FillToFill (0), FlatToFlat (1), FlatToReduced (2)
    """
    value__: int
    FillToFill: FillGroupingMethod
    FlatToFlat: FillGroupingMethod
    FlatToReduced: FillGroupingMethod


class FillMatchingMethod(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    The method used to match offsetting order fills
    
    enum FillMatchingMethod, values: FIFO (0), LIFO (1)
    """
    value__: int
    FIFO: FillMatchingMethod
    LIFO: FillMatchingMethod


class FitnessScoreManager(System.object):
    """
    Implements a fitness score calculator needed to account for strategy volatility,
                returns, drawdown, and factor in the turnover to ensure the algorithm engagement
                is statistically significant
    
    FitnessScoreManager()
    """
    def Initialize(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        pass

    @staticmethod
    def SigmoidalScale(valueToScale: float) -> float:
        pass

    def UpdateScores(self) -> None:
        pass

    FitnessScore: float

    PortfolioTurnover: float

    ReturnOverMaxDrawdown: float

    SortinoRatio: float



class KellyCriterionManager(System.object):
    """
    Class in charge of calculating the Kelly Criterion values.
                Will use the sample values of the last year.
    
    KellyCriterionManager()
    """
    def AddNewValue(self, newValue: float, time: datetime.datetime) -> None:
        pass

    def UpdateScores(self) -> None:
        pass

    KellyCriterionEstimate: float

    KellyCriterionProbabilityValue: float



class PortfolioStatistics(System.object):
    """
    The QuantConnect.Statistics.PortfolioStatistics class represents a set of statistics calculated from equity and benchmark samples
    
    PortfolioStatistics(profitLoss: SortedDictionary[DateTime, Decimal], equity: SortedDictionary[DateTime, Decimal], listPerformance: List[float], listBenchmark: List[float], startingCapital: Decimal, tradingDaysPerYear: int)
    PortfolioStatistics()
    """
    @staticmethod
    def GetRiskFreeRate() -> float:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, profitLoss: System.Collections.Generic.SortedDictionary[datetime.datetime, float], equity: System.Collections.Generic.SortedDictionary[datetime.datetime, float], listPerformance: typing.List[float], listBenchmark: typing.List[float], startingCapital: float, tradingDaysPerYear: int) -> None:
        pass

    @typing.overload
    def __new__(self) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Alpha: float

    AnnualStandardDeviation: float

    AnnualVariance: float

    AverageLossRate: float

    AverageWinRate: float

    Beta: float

    CompoundingAnnualReturn: float

    Drawdown: float

    Expectancy: float

    InformationRatio: float

    LossRate: float

    ProbabilisticSharpeRatio: float

    ProfitLossRatio: float

    SharpeRatio: float

    TotalNetProfit: float

    TrackingError: float

    TreynorRatio: float

    WinRate: float



class Statistics(System.object):
    """
    Calculate all the statistics required from the backtest, based on the equity curve and the profit loss statement.
    
    Statistics()
    """
    @staticmethod
    def Alpha(algoPerformance: typing.List[float], benchmarkPerformance: typing.List[float], riskFreeRate: float) -> float:
        pass

    @staticmethod
    def AnnualPerformance(performance: typing.List[float], tradingDaysPerYear: float) -> float:
        pass

    @staticmethod
    def AnnualStandardDeviation(performance: typing.List[float], tradingDaysPerYear: float) -> float:
        pass

    @staticmethod
    def AnnualVariance(performance: typing.List[float], tradingDaysPerYear: float) -> float:
        pass

    @staticmethod
    def Beta(algoPerformance: typing.List[float], benchmarkPerformance: typing.List[float]) -> float:
        pass

    @staticmethod
    def CompoundingAnnualPerformance(startingCapital: float, finalCapital: float, years: float) -> float:
        pass

    @staticmethod
    def DrawdownPercent(equityOverTime: System.Collections.Generic.SortedDictionary[datetime.datetime, float], rounding: int) -> float:
        pass

    @staticmethod
    def DrawdownValue(equityOverTime: System.Collections.Generic.SortedDictionary[datetime.datetime, float], rounding: int) -> float:
        pass

    @staticmethod
    def Generate(pointsEquity: typing.List[QuantConnect.ChartPoint], profitLoss: System.Collections.Generic.SortedDictionary[datetime.datetime, float], pointsPerformance: typing.List[QuantConnect.ChartPoint], unsortedBenchmark: System.Collections.Generic.Dictionary[datetime.datetime, float], startingCash: float, totalFees: float, totalTrades: float, tradingDaysPerYear: float) -> System.Collections.Generic.Dictionary[str, str]:
        pass

    @staticmethod
    def InformationRatio(algoPerformance: typing.List[float], benchmarkPerformance: typing.List[float]) -> float:
        pass

    @staticmethod
    def ObservedSharpeRatio(listPerformance: typing.List[float]) -> float:
        pass

    @staticmethod
    def ProbabilisticSharpeRatio(listPerformance: typing.List[float], benchmarkSharpeRatio: float) -> float:
        pass

    @staticmethod
    def ProfitLossRatio(averageWin: float, averageLoss: float) -> float:
        pass

    @staticmethod
    def SharpeRatio(algoPerformance: typing.List[float], riskFreeRate: float) -> float:
        pass

    @staticmethod
    def TrackingError(algoPerformance: typing.List[float], benchmarkPerformance: typing.List[float], tradingDaysPerYear: float) -> float:
        pass

    @staticmethod
    def TreynorRatio(algoPerformance: typing.List[float], benchmarkPerformance: typing.List[float], riskFreeRate: float) -> float:
        pass


class StatisticsBuilder(System.object):
    """ The QuantConnect.Statistics.StatisticsBuilder class creates summary and rolling statistics from trades, equity and benchmark points """
    @staticmethod
    def Generate(trades: typing.List[QuantConnect.Statistics.Trade], profitLoss: System.Collections.Generic.SortedDictionary[datetime.datetime, float], pointsEquity: typing.List[QuantConnect.ChartPoint], pointsPerformance: typing.List[QuantConnect.ChartPoint], pointsBenchmark: typing.List[QuantConnect.ChartPoint], startingCapital: float, totalFees: float, totalTransactions: int) -> QuantConnect.Statistics.StatisticsResults:
        pass

    __all__: list


class StatisticsResults(System.object):
    """
    The QuantConnect.Statistics.StatisticsResults class represents total and rolling statistics for an algorithm
    
    StatisticsResults(totalPerformance: AlgorithmPerformance, rollingPerformances: Dictionary[str, AlgorithmPerformance], summary: Dictionary[str, str])
    StatisticsResults()
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, totalPerformance: QuantConnect.Statistics.AlgorithmPerformance, rollingPerformances: System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance], summary: System.Collections.Generic.Dictionary[str, str]) -> None:
        pass

    @typing.overload
    def __new__(self) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    RollingPerformances: System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]

    Summary: System.Collections.Generic.Dictionary[str, str]

    TotalPerformance: QuantConnect.Statistics.AlgorithmPerformance



class Trade(System.object):
    """
    Represents a closed trade
    
    Trade()
    """
    Direction: QuantConnect.Statistics.TradeDirection

    Duration: datetime.timedelta

    EndTradeDrawdown: float

    EntryPrice: float

    EntryTime: datetime.datetime

    ExitPrice: float

    ExitTime: datetime.datetime

    MAE: float

    MFE: float

    ProfitLoss: float

    Quantity: float

    Symbol: QuantConnect.Symbol

    TotalFees: float



class TradeBuilder(System.object, QuantConnect.Interfaces.ITradeBuilder):
    """
    The QuantConnect.Statistics.TradeBuilder class generates trades from executions and market price updates
    
    TradeBuilder(groupingMethod: FillGroupingMethod, matchingMethod: FillMatchingMethod)
    """
    def HasOpenPosition(self, symbol: QuantConnect.Symbol) -> bool:
        pass

    def ProcessFill(self, fill: QuantConnect.Orders.OrderEvent, conversionRate: float, feeInAccountCurrency: float, multiplier: float) -> None:
        pass

    def SetLiveMode(self, live: bool) -> None:
        pass

    def SetMarketPrice(self, symbol: QuantConnect.Symbol, price: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, groupingMethod: QuantConnect.Statistics.FillGroupingMethod, matchingMethod: QuantConnect.Statistics.FillMatchingMethod) -> None:
        pass

    ClosedTrades: typing.List[QuantConnect.Statistics.Trade]



class TradeDirection(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Direction of a trade
    
    enum TradeDirection, values: Long (0), Short (1)
    """
    value__: int
    Long: TradeDirection
    Short: TradeDirection


class TradeStatistics(System.object):
    """
    The QuantConnect.Statistics.TradeStatistics class represents a set of statistics calculated from a list of closed trades
    
    TradeStatistics(trades: IEnumerable[Trade])
    TradeStatistics()
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, trades: typing.List[QuantConnect.Statistics.Trade]) -> None:
        pass

    @typing.overload
    def __new__(self) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    AverageEndTradeDrawdown: float

    AverageLosingTradeDuration: datetime.timedelta

    AverageLoss: float

    AverageMAE: float

    AverageMFE: float

    AverageProfit: float

    AverageProfitLoss: float

    AverageTradeDuration: datetime.timedelta

    AverageWinningTradeDuration: datetime.timedelta

    EndDateTime: typing.Optional[datetime.datetime]

    LargestLoss: float

    LargestMAE: float

    LargestMFE: float

    LargestProfit: float

    LossRate: float

    MaxConsecutiveLosingTrades: int

    MaxConsecutiveWinningTrades: int

    MaximumClosedTradeDrawdown: float

    MaximumDrawdownDuration: datetime.timedelta

    MaximumEndTradeDrawdown: float

    MaximumIntraTradeDrawdown: float

    MedianLosingTradeDuration: datetime.timedelta

    MedianTradeDuration: datetime.timedelta

    MedianWinningTradeDuration: datetime.timedelta

    NumberOfLosingTrades: int

    NumberOfWinningTrades: int

    ProfitFactor: float

    ProfitLossDownsideDeviation: float

    ProfitLossRatio: float

    ProfitLossStandardDeviation: float

    ProfitToMaxDrawdownRatio: float

    SharpeRatio: float

    SortinoRatio: float

    StartDateTime: typing.Optional[datetime.datetime]

    TotalFees: float

    TotalLoss: float

    TotalNumberOfTrades: int

    TotalProfit: float

    TotalProfitLoss: float

    WinLossRatio: float

    WinRate: float



