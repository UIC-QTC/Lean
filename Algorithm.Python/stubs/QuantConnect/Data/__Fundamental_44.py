from .__Fundamental_45 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class NonCurrentPrepaidAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of the carrying amounts that are paid in advance for expenses, which will be charged against earnings in periods after one

                year or beyond the operating cycle, if longer.

    

    NonCurrentPrepaidAssetsBalanceSheet(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    OneMonth: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class NonInterestBearingBorrowingsCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Non-interest bearing deposits in other financial institutions for short periods of time, usually less than 12 months.

    

    NonInterestBearingBorrowingsCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class NonInterestBearingBorrowingsNonCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Non-interest bearing borrowings due after a year.

    

    NonInterestBearingBorrowingsNonCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class NonInterestBearingBorrowingsTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Non-interest bearing deposits in other financial institutions for relatively short periods of time; on a Non-Differentiated Balance

                Sheet.

    

    NonInterestBearingBorrowingsTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class NonInterestBearingDepositsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of all domestic and foreign deposits in the banks that do not draw interest.

    

    NonInterestBearingDepositsBalanceSheet(store: IDictionary[str, Decimal])
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


class NonInterestExpenseIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Any expenses that not related to interest. It includes labor and related expense, occupancy and equipment, commission,

                professional expense and contract services expenses, selling, general and administrative, research and development depreciation,

                amortization and depletion, and any other special income/charges.

    

    NonInterestExpenseIncomeStatement(store: IDictionary[str, Decimal])
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


class NonInterestIncomeIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The total amount of non-interest income which may be derived from: (1) fees and commissions; (2) premiums earned; (3) equity

                investment; (4) the sale or disposal of assets; and (5) other sources not otherwise specified.

    

    NonInterestIncomeIncomeStatement(store: IDictionary[str, Decimal])
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


class NormalizedBasicEPS(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The basic normalized earnings per share. Normalized EPS removes onetime and unusual items from EPS, to provide investors with a

                more accurate measure of the company's true earnings. Normalized Earnings / Basic Weighted Average Shares Outstanding.

    

    NormalizedBasicEPS(store: IDictionary[str, Decimal])
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


class NormalizedBasicEPSGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's Normalized Basic EPS on a percentage basis.

    

    NormalizedBasicEPSGrowth(store: IDictionary[str, Decimal])
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


class NormalizedDilutedEPS(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The diluted normalized earnings per share. Normalized EPS removes onetime and unusual items from EPS, to provide investors with

                a more accurate measure of the company's true earnings. Normalized Earnings / Diluted Weighted Average Shares Outstanding.

    

    NormalizedDilutedEPS(store: IDictionary[str, Decimal])
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


class NormalizedDilutedEPSGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's Normalized Diluted EPS on a percentage basis.

    

    NormalizedDilutedEPSGrowth(store: IDictionary[str, Decimal])
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


class NormalizedEBITAsReportedIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    EBIT less Total Unusual Items. This is as reported by the company, may be the same or not the same as Morningstar's standardized

                definition.

    

    NormalizedEBITAsReportedIncomeStatement(store: IDictionary[str, Decimal])
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


class NormalizedEBITDAAsReportedIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    EBITDA less Total Unusual Items. This is as reported by the company, may be the same or not the same as Morningstar's

                standardized definition.

    

    NormalizedEBITDAAsReportedIncomeStatement(store: IDictionary[str, Decimal])
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
