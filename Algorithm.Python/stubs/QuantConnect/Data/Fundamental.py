from .__Fundamental_1 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime

# no functions
# classes

class MultiPeriodField(System.object):
    """ Abstract base class for multi-period fields """
    def GetPeriodNames(self) -> typing.List[str]:
        pass

    def GetPeriodValue(self, period: str) -> float:
        pass

    def GetPeriodValues(self) -> System.Collections.Generic.IReadOnlyDictionary[str, float]:
        pass

    def HasPeriodValue(self, period: str) -> bool:
        pass

    def HasValues(self) -> bool:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    def ToString(self) -> str:
        pass

    def UpdateValues(self, update: QuantConnect.Data.Fundamental.MultiPeriodField) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        pass

    HasValue: bool

    Value: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]

    PeriodField: type


class AccountsPayableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Any money that a company owes its suppliers for goods and services purchased on credit and is expected to pay within the next

                year or operating cycle.

    

    AccountsPayableBalanceSheet(store: IDictionary[str, Decimal])
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


class AccountsReceivableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Accounts owed to a company by customers within a year as a result of exchanging goods or services on credit.

    

    AccountsReceivableBalanceSheet(store: IDictionary[str, Decimal])
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


class AccruedandDeferredIncomeBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of accrued liabilities and deferred income (amount received in advance but the services are not provided in respect of

                amount).

    

    AccruedandDeferredIncomeBalanceSheet(store: IDictionary[str, Decimal])
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


class AccruedandDeferredIncomeCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of Accrued Liabilities and Deferred Income (amount received in advance but the services are not provided in respect of

                amount) due within 1 year.

    

    AccruedandDeferredIncomeCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class AccruedandDeferredIncomeNonCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of Accrued Liabilities and Deferred Income (amount received in advance but the services are not provided in respect of

                amount) due after 1 year.

    

    AccruedandDeferredIncomeNonCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class AccruedInterestReceivableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This account shows the amount of unpaid interest accrued to the date of purchase and included in the purchase price of securities

                purchased between interest dates.

    

    AccruedInterestReceivableBalanceSheet(store: IDictionary[str, Decimal])
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


class AccruedInvestmentIncomeBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Interest, dividends, rents, ancillary and other revenues earned but not yet received by the entity on its investments.

    

    AccruedInvestmentIncomeBalanceSheet(store: IDictionary[str, Decimal])
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


class AccruedLiabilitiesTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Liabilities which have occurred, but have not been paid or logged under accounts payable during an accounting PeriodAsByte. In other

                words, obligations for goods and services provided to a company for which invoices have not yet been received; on a Non-

                Differentiated Balance Sheet.

    

    AccruedLiabilitiesTotalBalanceSheet(store: IDictionary[str, Decimal])
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

    TwoMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class AccumulatedDepreciationBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cumulative amount of wear and tear or obsolescence charged against the fixed assets of a company.

    

    AccumulatedDepreciationBalanceSheet(store: IDictionary[str, Decimal])
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


class AdditionalPaidInCapitalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Excess of issue price over par or stated value of the entity's capital stock and amounts received from other transactions involving

                the entity's stock or stockholders. Includes adjustments to additional paid in capital. There are two major categories of additional

                paid in capital: 1) Paid in capital in excess of par/stated value, which is the difference between the actual issue price of the shares

                and the shares' par/stated value. 2) Paid in capital from other transactions which includes treasury stock, retirement of stock, stock

                dividends recorded at market, lapse of stock purchase warrants, conversion of convertible bonds in excess of the par value of the

                stock, and any other additional capital from the company's own stock transactions.

    

    AdditionalPaidInCapitalBalanceSheet(store: IDictionary[str, Decimal])
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


class AdvanceFromFederalHomeLoanBanksBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This item is typically available for bank industry. It's the amount of borrowings as of the balance sheet date from the Federal Home

                Loan Bank, which are primarily used to cover shortages in the required reserve balance and liquidity shortages.

    

    AdvanceFromFederalHomeLoanBanksBalanceSheet(store: IDictionary[str, Decimal])
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
