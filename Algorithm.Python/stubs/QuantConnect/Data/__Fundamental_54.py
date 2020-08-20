from .__Fundamental_55 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class ProfitMargin5YrAvg(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This is the simple average of the company's Annual Net Profit Margin over the last 5 years. Net profit margin is post tax income

                divided by total revenue for the same PeriodAsByte.

    

    ProfitMargin5YrAvg(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    FiveYears: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class ProfitonDisposalsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The difference between the sale price or salvage price and the book value of an asset that was sold or retired during the reporting

                PeriodAsByte.

    

    ProfitonDisposalsCashFlowStatement(store: IDictionary[str, Decimal])
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


class PropertiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Tangible assets that are held by an entity for use in the production or supply of goods and services, for rental to others, or for

                administrative purposes and that are expected to provide economic benefit for more than one year. This item is available for

                manufacturing, bank and transportation industries.

    

    PropertiesBalanceSheet(store: IDictionary[str, Decimal])
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


class ProvisionandWriteOffofAssetsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A non-cash adjustment for total provision and write off on assets & liabilities.

    

    ProvisionandWriteOffofAssetsCashFlowStatement(store: IDictionary[str, Decimal])
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


class ProvisionForDoubtfulAccountsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Amount of the current period expense charged against operations, the offset which is generally to the allowance for doubtful

                accounts for the purpose of reducing receivables, including notes receivable, to an amount that approximates their net realizable

                value (the amount expected to be collected). The category includes provision for loan losses, provision for any doubtful account

                receivable, and bad debt expenses. This item is usually not available for bank and insurance industries.

    

    ProvisionForDoubtfulAccountsIncomeStatement(store: IDictionary[str, Decimal])
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


class ProvisionForLoanLeaseAndOtherLossesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The sum of the periodic provision charged to earnings, based on an assessment of uncollectible from the counterparty on account

                of loan, lease or other credit losses, to reduce these accounts to the amount that approximates their net realizable value. This item

                is usually only available for bank industry.

    

    ProvisionForLoanLeaseAndOtherLossesCashFlowStatement(store: IDictionary[str, Decimal])
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


class ProvisionsTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Provisions are created to protect the interests of one or both parties named in a contract or legal document, which is a preparatory

                action or measure. Current provision is expired within one accounting PeriodAsByte.

    

    ProvisionsTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class PurchaseOfBusinessCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    All the purchases of business including business acquisitions, investment in subsidiary; investing in affiliated companies, and join

                venture.

    

    PurchaseOfBusinessCashFlowStatement(store: IDictionary[str, Decimal])
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


class PurchaseOfIntangiblesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount of capital outlays undertaken to increase, construct or improve intangible assets.

    

    PurchaseOfIntangiblesCashFlowStatement(store: IDictionary[str, Decimal])
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


class PurchaseOfInvestmentCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    All purchases of investments, including both long term and short term.

    

    PurchaseOfInvestmentCashFlowStatement(store: IDictionary[str, Decimal])
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


class PurchaseOfInvestmentPropertiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash outflow for purchases of investment properties during the accounting PeriodAsByte.

    

    PurchaseOfInvestmentPropertiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class PurchaseofJointVentureAssociateCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Purchase of joint venture/associates (investment below 50%).

    

    PurchaseofJointVentureAssociateCashFlowStatement(store: IDictionary[str, Decimal])
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
