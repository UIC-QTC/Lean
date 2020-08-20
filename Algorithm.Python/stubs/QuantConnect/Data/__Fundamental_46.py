from .__Fundamental_47 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class OperatingExpenseIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Operating expenses are primary recurring costs associated with central operations (other than cost of goods sold) that are incurred

                in order to generate sales.

    

    OperatingExpenseIncomeStatement(store: IDictionary[str, Decimal])
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


class OperatingGainsLossesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The gain or loss from the entity's ongoing operations.

    

    OperatingGainsLossesCashFlowStatement(store: IDictionary[str, Decimal])
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


class OperatingIncomeIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Income from normal business operations after deducting cost of revenue and operating expenses. It does not include income from

                any investing activities.

    

    OperatingIncomeIncomeStatement(store: IDictionary[str, Decimal])
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


class OperatingLeaseAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A contract that allows for the use of an asset, but does not convey rights of ownership of the asset. An operating lease is not

                capitalized; it is accounted for as a rental expense in what is known as "off balance sheet financing." For the lessor, the asset being

                leased is accounted for as an asset and is depreciated as such.

    

    OperatingLeaseAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class OperatingRevenueIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sales and income that the company makes from its business operations. This applies only to non-bank and insurance companies.

                For Utility template companies, this is the sum of revenue from electric, gas, transportation and other operating revenue.

                For Transportation template companies, this is the sum of revenue-passenger, revenue-cargo, and other operating revenue.

    

    OperatingRevenueIncomeStatement(store: IDictionary[str, Decimal])
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


class OperationAndMaintenanceIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of operation and maintenance expenses, which is the one important operating expense for the utility

                industry. It includes any costs related to production and maintenance cost of the property during the revenue generation process.

                This item is usually only available for mining and utility industries.

    

    OperationAndMaintenanceIncomeStatement(store: IDictionary[str, Decimal])
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


class OperationIncomeGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's operating income on a percentage basis. Morningstar calculates the growth percentage based on the

                underlying operating income data reported in the Income Statement within the company filings or reports.

    

    OperationIncomeGrowth(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    FiveYears: float

    OneYear: float

    ThreeMonths: float

    ThreeYears: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class OperationMargin(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of operating income to revenue. Morningstar calculates the ratio by using the underlying data reported in the

                company filings or reports:   Operating Income / Revenue.

    

    OperationMargin(store: IDictionary[str, Decimal])
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

    OneYear: float

    SixMonths: float

    ThreeMonths: float

    TwoMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class OperationRatios(System.object):
    """
    Definition of the OperationRatios class

    

    OperationRatios()
    """
    def UpdateValues(self, update: QuantConnect.Data.Fundamental.OperationRatios) -> None:
        pass

    AssetsTurnover: QuantConnect.Data.Fundamental.AssetsTurnover

    AVG5YrsROIC: QuantConnect.Data.Fundamental.AVG5YrsROIC

    CapExGrowth: QuantConnect.Data.Fundamental.CapExGrowth

    CapExSalesRatio: QuantConnect.Data.Fundamental.CapExSalesRatio

    CapitalExpenditureAnnual5YrGrowth: QuantConnect.Data.Fundamental.CapitalExpenditureAnnual5YrGrowth

    CapitalExpendituretoEBITDA: QuantConnect.Data.Fundamental.CapitalExpendituretoEBITDA

    CashConversionCycle: QuantConnect.Data.Fundamental.CashConversionCycle

    CashFlowfromFinancingGrowth: QuantConnect.Data.Fundamental.CashFlowfromFinancingGrowth

    CashFlowfromInvestingGrowth: QuantConnect.Data.Fundamental.CashFlowfromInvestingGrowth

    CashRatio: QuantConnect.Data.Fundamental.CashRatio

    CashRatioGrowth: QuantConnect.Data.Fundamental.CashRatioGrowth

    CashtoTotalAssets: QuantConnect.Data.Fundamental.CashtoTotalAssets

    CFOGrowth: QuantConnect.Data.Fundamental.CFOGrowth

    CommonEquityToAssets: QuantConnect.Data.Fundamental.CommonEquityToAssets

    CurrentRatio: QuantConnect.Data.Fundamental.CurrentRatio

    CurrentRatioGrowth: QuantConnect.Data.Fundamental.CurrentRatioGrowth

    DaysInInventory: QuantConnect.Data.Fundamental.DaysInInventory

    DaysInPayment: QuantConnect.Data.Fundamental.DaysInPayment

    DaysInSales: QuantConnect.Data.Fundamental.DaysInSales

    DebttoAssets: QuantConnect.Data.Fundamental.DebttoAssets

    EBITDAGrowth: QuantConnect.Data.Fundamental.EBITDAGrowth

    EBITDAMargin: QuantConnect.Data.Fundamental.EBITDAMargin

    EBITMargin: QuantConnect.Data.Fundamental.EBITMargin

    ExpenseRatio: QuantConnect.Data.Fundamental.ExpenseRatio

    FCFGrowth: QuantConnect.Data.Fundamental.FCFGrowth

    FCFNetIncomeRatio: QuantConnect.Data.Fundamental.FCFNetIncomeRatio

    FCFSalesRatio: QuantConnect.Data.Fundamental.FCFSalesRatio

    FCFtoCFO: QuantConnect.Data.Fundamental.FCFtoCFO

    FinancialLeverage: QuantConnect.Data.Fundamental.FinancialLeverage

    FixAssetsTuronver: QuantConnect.Data.Fundamental.FixAssetsTuronver

    GrossMargin: QuantConnect.Data.Fundamental.GrossMargin

    GrossMargin5YrAvg: QuantConnect.Data.Fundamental.GrossMargin5YrAvg

    GrossProfitAnnual5YrGrowth: QuantConnect.Data.Fundamental.GrossProfitAnnual5YrGrowth

    InterestCoverage: QuantConnect.Data.Fundamental.InterestCoverage

    InventoryTurnover: QuantConnect.Data.Fundamental.InventoryTurnover

    LongTermDebtEquityRatio: QuantConnect.Data.Fundamental.LongTermDebtEquityRatio

    LongTermDebtTotalCapitalRatio: QuantConnect.Data.Fundamental.LongTermDebtTotalCapitalRatio

    LossRatio: QuantConnect.Data.Fundamental.LossRatio

    NetIncomeContOpsGrowth: QuantConnect.Data.Fundamental.NetIncomeContOpsGrowth

    NetIncomeGrowth: QuantConnect.Data.Fundamental.NetIncomeGrowth

    NetIncomePerEmployee: QuantConnect.Data.Fundamental.NetIncomePerEmployee

    NetMargin: QuantConnect.Data.Fundamental.NetMargin

    NormalizedNetProfitMargin: QuantConnect.Data.Fundamental.NormalizedNetProfitMargin

    NormalizedROIC: QuantConnect.Data.Fundamental.NormalizedROIC

    OperationIncomeGrowth: QuantConnect.Data.Fundamental.OperationIncomeGrowth

    OperationMargin: QuantConnect.Data.Fundamental.OperationMargin

    OperationRevenueGrowth3MonthAvg: QuantConnect.Data.Fundamental.OperationRevenueGrowth3MonthAvg

    PaymentTurnover: QuantConnect.Data.Fundamental.PaymentTurnover

    PostTaxMargin5YrAvg: QuantConnect.Data.Fundamental.PostTaxMargin5YrAvg

    PretaxMargin: QuantConnect.Data.Fundamental.PretaxMargin

    PreTaxMargin5YrAvg: QuantConnect.Data.Fundamental.PreTaxMargin5YrAvg

    ProfitMargin5YrAvg: QuantConnect.Data.Fundamental.ProfitMargin5YrAvg

    QuickRatio: QuantConnect.Data.Fundamental.QuickRatio

    ReceivableTurnover: QuantConnect.Data.Fundamental.ReceivableTurnover

    RegressionGrowthOperatingRevenue5Years: QuantConnect.Data.Fundamental.RegressionGrowthOperatingRevenue5Years

    RevenueGrowth: QuantConnect.Data.Fundamental.RevenueGrowth

    ROA: QuantConnect.Data.Fundamental.ROA

    ROA5YrAvg: QuantConnect.Data.Fundamental.ROA5YrAvg

    ROE: QuantConnect.Data.Fundamental.ROE

    ROE5YrAvg: QuantConnect.Data.Fundamental.ROE5YrAvg

    ROIC: QuantConnect.Data.Fundamental.ROIC

    SalesPerEmployee: QuantConnect.Data.Fundamental.SalesPerEmployee

    SolvencyRatio: QuantConnect.Data.Fundamental.SolvencyRatio

    StockholdersEquityGrowth: QuantConnect.Data.Fundamental.StockholdersEquityGrowth

    TaxRate: QuantConnect.Data.Fundamental.TaxRate

    TotalAssetsGrowth: QuantConnect.Data.Fundamental.TotalAssetsGrowth

    TotalDebtEquityRatio: QuantConnect.Data.Fundamental.TotalDebtEquityRatio

    TotalDebtEquityRatioGrowth: QuantConnect.Data.Fundamental.TotalDebtEquityRatioGrowth

    TotalLiabilitiesGrowth: QuantConnect.Data.Fundamental.TotalLiabilitiesGrowth

    WorkingCapitalTurnoverRatio: QuantConnect.Data.Fundamental.WorkingCapitalTurnoverRatio
