from .__Fundamental_64 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class TotalAssetsGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the total assets on a percentage basis. Morningstar calculates the growth percentage based on the total assets

                reported in the Balance Sheet within the company filings or reports.

    

    TotalAssetsGrowth(store: IDictionary[str, Decimal])
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

    ThreeYears: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class TotalCapitalizationBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Stockholder's Equity plus Long Term Debt.

    

    TotalCapitalizationBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalDebtBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    All borrowings incurred by the company including debt and capital lease obligations.

    

    TotalDebtBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalDebtEquityRatio(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of Total Debt to Common Equity. Morningstar calculates the ratio by using the underlying data reported in the

                Balance Sheet within the company filings or reports: (Current Debt And Current Capital Lease Obligation + Long-Term Debt And

                Long-Term Capital Lease Obligation / Common Equity.   [Note: Common Equity = Total Shareholder's Equity - Preferred Stock]

    

    TotalDebtEquityRatio(store: IDictionary[str, Decimal])
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


class TotalDebtEquityRatioGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's total debt to equity ratio on a percentage basis. Morningstar calculates the growth percentage based

                on the total debt divided by the shareholder's equity reported in the Balance Sheet within the company filings or reports.

    

    TotalDebtEquityRatioGrowth(store: IDictionary[str, Decimal])
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

    ThreeYears: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class TotalDebtInMaturityScheduleBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total Debt in Maturity Schedule is the sum of Debt details above.

    

    TotalDebtInMaturityScheduleBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalDeferredCreditsAndOtherNonCurrentLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Revenue received by a firm but not yet reported as income.  This item is usually only available for utility industry.

    

    TotalDeferredCreditsAndOtherNonCurrentLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalDepositsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A liability account which represents the total amount of funds deposited.

    

    TotalDepositsBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalDividendPaymentofEquitySharesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total amount paid in dividends to equity securities investors.

    

    TotalDividendPaymentofEquitySharesIncomeStatement(store: IDictionary[str, Decimal])
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


class TotalDividendPaymentofNonEquitySharesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total amount paid in dividends to Non-Equity securities investors.

    

    TotalDividendPaymentofNonEquitySharesIncomeStatement(store: IDictionary[str, Decimal])
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


class TotalDividendPerShare(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total Dividend Per Share is cash dividends and special cash dividends paid per share over a certain period of time.

    

    TotalDividendPerShare(store: IDictionary[str, Decimal])
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


class TotalEquityAsReportedBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total Equity as reported by the company, may be the same or not the same as Morningstar's standardized definition.

    

    TotalEquityAsReportedBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalEquityBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total Equity equals Preferred Stock Equity + Common Stock Equity.

    

    TotalEquityBalanceSheet(store: IDictionary[str, Decimal])
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
