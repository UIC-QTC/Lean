from .__Fundamental_16 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class CurrentDebtAndCapitalLeaseObligationBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    All borrowings due within one year including current portions of long-term debt and capital leases as well as short-term debt such

                as bank loans and commercial paper.

    

    CurrentDebtAndCapitalLeaseObligationBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentDebtBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents the total amount of long-term debt such as bank loans and commercial paper, which is due within one year.

    

    CurrentDebtBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentDeferredAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Payments that will be assigned as expenses with one accounting period, but that are paid in advance and temporarily set up as

                current assets on the balance sheet.

    

    CurrentDeferredAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentDeferredLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents the current portion of obligations, which is a liability that usually would have been paid but is now past due.

    

    CurrentDeferredLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentDeferredRevenueBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents collections of cash or other assets related to revenue producing activity for which revenue has not yet been recognized.

                Generally, an entity records deferred revenue when it receives consideration from a customer before achieving certain criteria that

                must be met for revenue to be recognized in conformity with GAAP. It can be either current or non-current item. Also called

                unearned revenue.

    

    CurrentDeferredRevenueBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentDeferredTaxesAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Meaning a future tax asset, resulting from temporary differences between book (accounting) value of assets and liabilities and their

                tax value, or timing differences between the recognition of gains and losses in financial statements and their recognition in a tax

                computation. It is also called future tax.

    

    CurrentDeferredTaxesAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentDeferredTaxesLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Meaning a future tax liability, resulting from temporary differences between book (accounting) value of assets and liabilities and

                their tax value, or timing differences between the recognition of gains and losses in financial statements and their recognition in a

                tax computation. Deferred tax liabilities generally arise where tax relief is provided in advance of an accounting expense, or income

                is accrued but not taxed until received.

    

    CurrentDeferredTaxesLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The debts or obligations of the firm that are due within one year.

    

    CurrentLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentNotesPayableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Written promises to pay a stated sum at one or more specified dates in the future, within the accounting PeriodAsByte.

    

    CurrentNotesPayableBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentOtherFinancialLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other short term financial liabilities not categorized and due within one year or a normal operating cycle (whichever is longer).

    

    CurrentOtherFinancialLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentProvisionsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Provisions are created to protect the interests of one or both parties named in a contract or legal document which is a preparatory

                action or measure. Current provision is expired within one accounting PeriodAsByte.

    

    CurrentProvisionsBalanceSheet(store: IDictionary[str, Decimal])
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

    TwoMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class CurrentRatio(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of Current Assets to Current Liabilities. Morningstar calculates the ratio by using the underlying data reported in

                the Balance Sheet within the company filings or reports:     Current Assets / Current Liabilities.

    

    CurrentRatio(store: IDictionary[str, Decimal])
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
