from .__Fundamental_44 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class NetUtilityPlantBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Net utility plant might include water production, electric utility plan, natural gas, fuel and other, common utility plant and

                accumulated depreciation. This item is usually only available for utility industry.

    

    NetUtilityPlantBalanceSheet(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class NonCurrentAccountsReceivableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Accounts receivable represents sums owed to the business that the business records as revenue. Gross accounts receivable is

                accounts receivable before the business deducts uncollectable accounts to calculate the true value of accounts receivable.

    

    NonCurrentAccountsReceivableBalanceSheet(store: IDictionary[str, Decimal])
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


class NonCurrentAccruedExpensesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An expense that has occurred but the transaction has not been entered in the accounting records. Accordingly, an adjusting entry

                is made to debit the appropriate expense account and to credit a liability account such as accrued expenses payable or accounts

                payable.

    

    NonCurrentAccruedExpensesBalanceSheet(store: IDictionary[str, Decimal])
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


class NonCurrentDeferredAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Payments that will be assigned as expenses longer than one accounting period, but that are paid in advance and temporarily set up

                as non-current assets on the balance sheet.

    

    NonCurrentDeferredAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class NonCurrentDeferredLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents the non-current portion of obligations, which is a liability that usually would have been paid but is now past due.

    

    NonCurrentDeferredLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class NonCurrentDeferredRevenueBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The non-current portion of deferred revenue amount as of the balance sheet date. Deferred revenue is a liability related to revenue

                producing activity for which revenue has not yet been recognized, and is not expected be recognized in the next twelve months.

    

    NonCurrentDeferredRevenueBalanceSheet(store: IDictionary[str, Decimal])
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


class NonCurrentDeferredTaxesAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A result of timing differences between taxable incomes reported on the income statement and taxable income from the company's

                tax return. Depending on the positioning of deferred income taxes, the field may be either current (within current assets) or non-

                current (below total current assets). Typically a company will have two deferred income taxes fields.

    

    NonCurrentDeferredTaxesAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class NonCurrentDeferredTaxesLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The estimated future tax obligations, which usually arise when different accounting methods are used for financial statements and

                tax statement It is also an add-back to the cash flow statement. Deferred income taxes include accumulated tax deferrals due to

                accelerated depreciation and investment credit.

    

    NonCurrentDeferredTaxesLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class NonCurrentNoteReceivablesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An amount representing an agreement for an unconditional promise by the maker to pay the entity (holder) a definite sum of money

                at a future date(s), excluding the portion that is expected to be received within one year of the balance sheet date or the normal

                operating cycle, whichever is longer.

    

    NonCurrentNoteReceivablesBalanceSheet(store: IDictionary[str, Decimal])
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


class NonCurrentOtherFinancialLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other long term financial liabilities not categorized and due over one year or a normal operating cycle (whichever is longer).

    

    NonCurrentOtherFinancialLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class NonCurrentPensionAndOtherPostretirementBenefitPlansBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A loan issued by an insurance company that uses the cash value of a person's life insurance policy as collateral.  This item is usually

                only available in the insurance industry.

    

    NonCurrentPensionAndOtherPostretirementBenefitPlansBalanceSheet(store: IDictionary[str, Decimal])
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

    TwoMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]
