from .__Fundamental_37 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class LiabilitiesHeldforSaleTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Liabilities related to an asset classified as held for sale.

    

    LiabilitiesHeldforSaleTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class LiabilitiesOfDiscontinuedOperationsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The obligations arising from the sale, disposal, or planned sale in the near future (generally within one year) of a disposal group,

                including a component of the entity (discontinued operation). This item is typically available for bank industry.

    

    LiabilitiesOfDiscontinuedOperationsBalanceSheet(store: IDictionary[str, Decimal])
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


class LimitedPartnershipCapitalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    In a limited partnership or master limited partnership form of business, this represents the balance of capital held by the limited

                partners.

    

    LimitedPartnershipCapitalBalanceSheet(store: IDictionary[str, Decimal])
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


class LineOfCreditBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The carrying value as of the balance sheet date of obligations drawn from a line of credit, which is a bank's commitment to make

                loans up to a specific amount.

    

    LineOfCreditBalanceSheet(store: IDictionary[str, Decimal])
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

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class LoansandAdvancestoBankBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of loans and advances made to a bank or financial institution.

    

    LoansandAdvancestoBankBalanceSheet(store: IDictionary[str, Decimal])
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


class LoansandAdvancestoCustomerBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of loans and advances made to customers.

    

    LoansandAdvancestoCustomerBalanceSheet(store: IDictionary[str, Decimal])
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


class LoansHeldForSaleBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    It means the aggregate amount of loans receivable that will be sold to other entities.  This item is typically available for bank

                industry.

    

    LoansHeldForSaleBalanceSheet(store: IDictionary[str, Decimal])
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


class LoansReceivableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Reflects the carrying amount of unpaid loans issued to other institutions for cash needs or an asset purchase.

    

    LoansReceivableBalanceSheet(store: IDictionary[str, Decimal])
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


class LongTermCapitalLeaseObligationBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents the total liability for long-term leases lasting over one year. Amount equal to the present value (the principal) at the

                beginning of the lease term less lease payments during the lease term.

    

    LongTermCapitalLeaseObligationBalanceSheet(store: IDictionary[str, Decimal])
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


class LongTermDebtAndCapitalLeaseObligationBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    All borrowings lasting over one year including long-term debt and long-term portion of capital lease obligations.

    

    LongTermDebtAndCapitalLeaseObligationBalanceSheet(store: IDictionary[str, Decimal])
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


class LongTermDebtBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of the carrying values as of the balance sheet date of all long-term debt, which is debt initially having maturities due after one

                year or beyond the operating cycle, if longer, but excluding the portions thereof scheduled to be repaid within one year or the

                normal operating cycle, if longer. Long-term debt includes notes payable, bonds payable, mortgage loans, convertible debt,

                subordinated debt and other types of long term debt.

    

    LongTermDebtBalanceSheet(store: IDictionary[str, Decimal])
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


class LongTermDebtEquityRatio(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of Long Term Debt to Common Equity. Morningstar calculates the ratio by using the underlying data reported in

                the Balance Sheet within the company filings or reports:    Long-Term Debt And Capital Lease Obligation / Common Equity.

                [Note: Common Equity = Total Shareholder's Equity - Preferred Stock]

    

    LongTermDebtEquityRatio(store: IDictionary[str, Decimal])
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


class LongTermDebtIssuanceCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash inflow from a debt initially having maturity due after one year or beyond the operating cycle, if longer.

    

    LongTermDebtIssuanceCashFlowStatement(store: IDictionary[str, Decimal])
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
