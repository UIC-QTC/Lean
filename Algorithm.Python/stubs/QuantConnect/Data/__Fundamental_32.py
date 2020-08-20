from .__Fundamental_33 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class InterestBearingBorrowingsNonCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Carrying amount of any interest-bearing loan which is due after one year.

    

    InterestBearingBorrowingsNonCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class InterestBearingDepositsAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Deposit of money with a financial institution, in consideration of which the financial institution pays or credits interest, or amounts in the nature

                of interest.

    

    InterestBearingDepositsAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class InterestBearingDepositsLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate of all domestic and foreign deposits in the bank that earns interests.

    

    InterestBearingDepositsLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class InterestCoverage(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of EBIT to Interest Expense. Morningstar calculates the ratio by using the underlying data reported in the Income

                Statement within the company filings or reports:    EBIT / Interest Expense.

    

    InterestCoverage(store: IDictionary[str, Decimal])
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


class InterestCreditedOnPolicyholderDepositsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An expense reported in the income statement and needs to be removed from net income to arrive at cash provided by (used in)

                operations to the extent that such interest has not been paid. This item is usually only available for insurance industry.

    

    InterestCreditedOnPolicyholderDepositsCashFlowStatement(store: IDictionary[str, Decimal])
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


class InterestExpenseForDepositIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Includes interest expense on the following deposit accounts: Interest-bearing Demand deposit; Checking account; Savings account;

                Deposit in foreign offices; Money Market Certificates & Deposit Accounts. This item is usually only available for bank industry.

    

    InterestExpenseForDepositIncomeStatement(store: IDictionary[str, Decimal])
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

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class InterestExpenseForFederalFundsSoldAndSecuritiesPurchaseUnderAgreementsToResellIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Gross expenses on the purchase of Federal funds at a specified price with a simultaneous agreement to sell the same to the same

                counterparty at a fixed or determinable price at a future date. This item is usually only available for bank industry.

    

    InterestExpenseForFederalFundsSoldAndSecuritiesPurchaseUnderAgreementsToResellIncomeStatement(store: IDictionary[str, Decimal])
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


class InterestExpenseForLongTermDebtAndCapitalSecuritiesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate interest expenses incurred on long-term borrowings and any interest expenses on fixed assets (property, plant,

                equipment) that are leased due longer than one year. This item is usually only available for bank industry.

    

    InterestExpenseForLongTermDebtAndCapitalSecuritiesIncomeStatement(store: IDictionary[str, Decimal])
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

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class InterestExpenseForShortTermDebtIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate interest expenses incurred on short-term borrowings and any interest expenses on fixed assets (property, plant,

                equipment) that are leased within one year. This item is usually only available for bank industry.

    

    InterestExpenseForShortTermDebtIncomeStatement(store: IDictionary[str, Decimal])
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


class InterestExpenseIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Relates to the general cost of borrowing money. It is the price that a lender charges a borrower for the use of the lender's money.

    

    InterestExpenseIncomeStatement(store: IDictionary[str, Decimal])
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


class InterestExpenseNonOperatingIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Interest expense caused by long term financing activities; such as interest expense incurred on trading liabilities, commercial paper,

                long-term debt, capital leases, deposits, and all other borrowings.

    

    InterestExpenseNonOperatingIncomeStatement(store: IDictionary[str, Decimal])
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


class InterestIncomeAfterProvisionForLoanLossIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Net interest and dividend income or expense, including any amortization and accretion (as applicable) of discounts and premiums,

                including consideration of the provisions for loan, lease, credit, and other related losses, if any.

    

    InterestIncomeAfterProvisionForLoanLossIncomeStatement(store: IDictionary[str, Decimal])
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
