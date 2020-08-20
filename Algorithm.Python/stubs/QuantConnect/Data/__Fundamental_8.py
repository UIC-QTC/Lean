from .__Fundamental_9 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class CashReceiptsfromDepositsbyBanksandCustomersCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash received from banks and customer deposits in operating cash flow, using the direct method. This item is usually only available

                for bank industry

    

    CashReceiptsfromDepositsbyBanksandCustomersCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashReceiptsfromFeesandCommissionsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash received from agency fees and commissions in operating cash flow, using the direct method. This item is usually available for

                bank and insurance industries

    

    CashReceiptsfromFeesandCommissionsCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashReceiptsfromLoansCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash received from loans in operating cash flow, using the direct method. This item is usually only available for bank industry

    

    CashReceiptsfromLoansCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashReceiptsfromRepaymentofAdvancesandLoansMadetoOtherPartiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash received from the repayment of advances and loans made to other parties, in the Investing Cash Flow section.

    

    CashReceiptsfromRepaymentofAdvancesandLoansMadetoOtherPartiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashReceiptsfromSecuritiesRelatedActivitiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash received from the trading of securities in operating cash flow, using the direct method. This item is usually only available for

                bank and insurance industries

    

    CashReceiptsfromSecuritiesRelatedActivitiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashReceiptsfromTaxRefundsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash received as refunds from tax authorities in operating cash flow, using the direct method

    

    CashReceiptsfromTaxRefundsCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashReceivedfromInsuranceActivitiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash received from insurance activities in operating cash flow, using the direct method. This item is usually only available for

                insurance industry

    

    CashReceivedfromInsuranceActivitiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashRestrictedOrPledgedBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash that the company can use only for specific purposes or cash deposit or placing of owned property by a debtor (the pledger) to

                a creditor (the pledgee) as a security for a loan or obligation.

    

    CashRestrictedOrPledgedBalanceSheet(store: IDictionary[str, Decimal])
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


class CashtoTotalAssets(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents the percentage of a company's total assets is in cash.

    

    CashtoTotalAssets(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    OneYear: float

    ThreeMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class CededPremiumsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount of premiums paid and payable to another insurer as a result of reinsurance arrangements in order to exchange for that

                company accepting all or part of insurance on a risk or exposure. This item is usually only available for insurance industry.

    

    CededPremiumsIncomeStatement(store: IDictionary[str, Decimal])
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


class CFOGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's cash flow from operations on a percentage basis. Morningstar calculates the growth percentage

                based on the underlying cash flow from operations data reported in the Cash Flow Statement within the company filings or reports.

    

    CFOGrowth(store: IDictionary[str, Decimal])
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


class ChangeInAccountPayableCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the account payables.

    

    ChangeInAccountPayableCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInAccruedExpenseCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the accrued expenses.

    

    ChangeInAccruedExpenseCashFlowStatement(store: IDictionary[str, Decimal])
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
