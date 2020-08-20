from .__Fundamental_17 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class CurrentRatioGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's current ratio on a percentage basis. Morningstar calculates the growth percentage based on the

                current assets divided by current liabilities reported in the Balance Sheet within the company filings or reports.

    

    CurrentRatioGrowth(store: IDictionary[str, Decimal])
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


class CustomerAcceptancesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Amounts receivable from customers on short-term negotiable time drafts drawn on and accepted by the institution (also known as

                banker's acceptance transactions) that are outstanding on the reporting date.

    

    CustomerAcceptancesBalanceSheet(store: IDictionary[str, Decimal])
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


class CustomerAccountsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Carrying value of amounts transferred by customers to third parties for security purposes that are expected to be returned or

                applied towards payment after one year or beyond the operating cycle, if longer.

    

    CustomerAccountsBalanceSheet(store: IDictionary[str, Decimal])
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


class DaysInInventory(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    365 / Inventory turnover

    

    DaysInInventory(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    OneYear: float

    SixMonths: float

    ThreeMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class DaysInPayment(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    365 / Payable turnover

    

    DaysInPayment(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    OneYear: float

    SixMonths: float

    ThreeMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class DaysInSales(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    365 / Receivable Turnover

    

    DaysInSales(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    OneYear: float

    SixMonths: float

    ThreeMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class DDACostofRevenueIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Costs of depreciation and amortization on assets used for the revenue-generating activities during the accounting period

    

    DDACostofRevenueIncomeStatement(store: IDictionary[str, Decimal])
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


class DebtDueBeyondBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Debt maturing beyond 5 years (eg. 5-10 years) or with no specified maturity, according to the debt maturity schedule reported by

                the company.

    

    DebtDueBeyondBalanceSheet(store: IDictionary[str, Decimal])
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


class DebtDueInYear1BalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Debt due under 1 year according to the debt maturity schedule reported by the company.

    

    DebtDueInYear1BalanceSheet(store: IDictionary[str, Decimal])
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


class DebtDueInYear2BalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Debt due under 2 years according to the debt maturity schedule reported by the company.

    

    DebtDueInYear2BalanceSheet(store: IDictionary[str, Decimal])
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


class DebtDueInYear5BalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Debt due within 5 year if the company provide maturity schedule in range e.g. 1-5 years, 2-5 years. Debt due under 5 years

                according to the debt maturity schedule reported by the company. If a range is reported by the company, the value will be collected

                under the maximum number of years (eg. 1-5 years, 3-5 years or 5 years will all be collected under this data point.)

    

    DebtDueInYear5BalanceSheet(store: IDictionary[str, Decimal])
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


class DebtSecuritiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Debt securities held as investments.

    

    DebtSecuritiesBalanceSheet(store: IDictionary[str, Decimal])
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


class DebtSecuritiesinIssueBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Any debt financial instrument issued instead of cash loan.

    

    DebtSecuritiesinIssueBalanceSheet(store: IDictionary[str, Decimal])
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


class DebttoAssets(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This is a leverage ratio used to determine how much debt (a sum of long term and current portion of debt) a company has on its

                balance sheet relative to total assets. This ratio examines the percent of the company that is financed by debt.

    

    DebttoAssets(store: IDictionary[str, Decimal])
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
