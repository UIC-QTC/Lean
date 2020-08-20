from .__Fundamental_68 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class UnearnedIncomeBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Income received but not yet earned, it represents the unearned amount that is netted against the total loan.

    

    UnearnedIncomeBalanceSheet(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class UnearnedPremiumsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Carrying amount of premiums written on insurance contracts that have not been earned as of the balance sheet date.

    

    UnearnedPremiumsBalanceSheet(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class UnpaidLossAndLossReserveBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Liability amount that reflects claims that are expected based upon statistical projections, but which have not been reported to the

                insurer.

    

    UnpaidLossAndLossReserveBalanceSheet(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class UnrealizedGainLossBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A profit or loss that results from holding onto an asset rather than cashing it in and officially taking the profit or loss.

    

    UnrealizedGainLossBalanceSheet(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class UnrealizedGainLossOnInvestmentSecuritiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increases (decreases) in the market value of unsold securities whose gains (losses) were included in earnings.

    

    UnrealizedGainLossOnInvestmentSecuritiesCashFlowStatement(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    OneMonth: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    TwoMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class UnrealizedGainsLossesOnDerivativesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The gross gains and losses on derivatives. This item is usually only available for insurance industry.

    

    UnrealizedGainsLossesOnDerivativesCashFlowStatement(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class ValuationRatios(System.object):
    """
    Definition of the ValuationRatios class

    

    ValuationRatios()
    """
    def UpdateValues(self, update: QuantConnect.Data.Fundamental.ValuationRatios) -> None:
        pass

    ActualForwardDividend: float

    ActualTrailingDividend: float

    BookValuePerShare: float

    BookValueYield: float

    BuyBackYield: float

    CAPERatio: float

    CashReturn: float

    CFOPerShare: float

    CFYield: float

    DivYield5Year: float

    EarningYield: float

    EVtoEBIT: float

    EVToEBIT3YrAvg: float

    EVToEBIT3YrAvgChange: float

    EVToEBITDA: float

    EVToEBITDA10YearGrowth: float

    EVToEBITDA1YearGrowth: float

    EVToEBITDA3YearGrowth: float

    EVToEBITDA3YrAvg: float

    EVToEBITDA3YrAvgChange: float

    EVToEBITDA5YearGrowth: float

    EVtoFCF: float

    EVToFCF10YearGrowth: float

    EVToFCF1YearGrowth: float

    EVToFCF3YearGrowth: float

    EVToFCF3YrAvg: float

    EVToFCF3YrAvgChange: float

    EVToFCF5YearGrowth: float

    EVToForwardEBIT: float

    EVToForwardEBITDA: float

    EVToForwardRevenue: float

    EVtoPreTaxIncome: float

    EVtoRevenue: float

    EVToRevenue10YearGrowth: float

    EVToRevenue1YearGrowth: float

    EVToRevenue3YearGrowth: float

    EVToRevenue3YrAvg: float

    EVToRevenue3YrAvgChange: float

    EVToRevenue5YearGrowth: float

    EVtoTotalAssets: float

    EVToTotalAssets10YearGrowth: float

    EVToTotalAssets1YearGrowth: float

    EVToTotalAssets3YearGrowth: float

    EVToTotalAssets3YrAvg: float

    EVToTotalAssets3YrAvgChange: float

    EVToTotalAssets5YearGrowth: float

    ExpectedDividendGrowthRate: float

    FCFPerShare: float

    FCFRatio: float

    FCFYield: float

    FFOPerShare: float

    FirstYearEstimatedEPSGrowth: float

    ForwardCalculationStyle: str

    ForwardDividend: float

    ForwardDividendYield: float

    ForwardEarningYield: float

    ForwardPERatio: float

    ForwardROA: float

    ForwardROE: float

    NormalizedPEGatio: float

    NormalizedPERatio: float

    PayoutRatio: float

    PBRatio: float

    PBRatio10YearGrowth: float

    PBRatio1YearGrowth: float

    PBRatio3YearGrowth: float

    PBRatio3YrAvg: float

    PBRatio3YrAvgChange: float

    PBRatio5YearGrowth: float

    PCashRatio3YrAvg: float

    PCFRatio: float

    PEGPayback: float

    PEGRatio: float

    PERatio: float

    PERatio10YearAverage: float

    PERatio10YearGrowth: float

    PERatio10YearHigh: float

    PERatio10YearLow: float

    PERatio1YearAverage: float

    PERatio1YearGrowth: float

    PERatio1YearHigh: float

    PERatio1YearLow: float

    PERatio3YearGrowth: float

    PERatio3YrAvg: float

    PERatio3YrAvgChange: float

    PERatio5YearAverage: float

    PERatio5YearGrowth: float

    PERatio5YearHigh: float

    PERatio5YearLow: float

    PFCFRatio10YearGrowth: float

    PFCFRatio1YearGrowth: float

    PFCFRatio3YearGrowth: float

    PFCFRatio3YrAvg: float

    PFCFRatio3YrAvgChange: float

    PFCFRatio5YearGrowth: float

    PriceChange1M: float

    PricetoCashRatio: float

    PricetoEBITDA: float

    PSRatio: float

    PSRatio10YearGrowth: float

    PSRatio1YearGrowth: float

    PSRatio3YearGrowth: float

    PSRatio3YrAvg: float

    PSRatio3YrAvgChange: float

    PSRatio5YearGrowth: float

    RatioPE5YearAverage: float

    SalesPerShare: float

    SalesYield: float

    SecondYearEstimatedEPSGrowth: float

    SustainableGrowthRate: float

    TangibleBookValuePerShare: float

    TangibleBVPerShare3YrAvg: float

    TangibleBVPerShare5YrAvg: float

    TotalAssetPerShare: float

    TotalYield: float

    TrailingCalculationStyle: str

    TrailingDividendYield: float

    TwoYearsForwardEarningYield: float

    TwoYearsForwardPERatio: float

    TwoYrsEVToForwardEBIT: float

    TwoYrsEVToForwardEBITDA: float

    WorkingCapitalPerShare: float

    WorkingCapitalPerShare3YrAvg: float

    WorkingCapitalPerShare5YrAvg: float



class WagesandSalariesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This is the portion under Staff Costs that represents salary paid to the employees in respect of their work.

    

    WagesandSalariesIncomeStatement(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    SixMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class WaterProductionBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount for a facility and plant that provides water which might include wells, reservoirs, pumping stations, and control

                facilities; and waste water systems which includes the waste treatment and disposal facility and equipment. This item is usually

                only available for utility industry.

    

    WaterProductionBalanceSheet(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]
