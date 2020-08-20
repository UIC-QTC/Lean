from .__Fundamental_36 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class InvestmentPropertiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Company's investments in properties net of accumulated depreciation, which generate a return.

    

    InvestmentPropertiesBalanceSheet(store: IDictionary[str, Decimal])
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


class InvestmentsAndAdvancesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    All investments in affiliates, real estate, securities, etc. Non-current investment, not including marketable securities.

    

    InvestmentsAndAdvancesBalanceSheet(store: IDictionary[str, Decimal])
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


class InvestmentsinAssociatesatCostBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A stake in any company which is more than 20% but less than 50%.

    

    InvestmentsinAssociatesatCostBalanceSheet(store: IDictionary[str, Decimal])
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


class InvestmentsinJointVenturesatCostBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A 50% stake in any company in which remaining 50% belongs to other company.

    

    InvestmentsinJointVenturesatCostBalanceSheet(store: IDictionary[str, Decimal])
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


class InvestmentsInOtherVenturesUnderEquityMethodBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This item represents the carrying amount on the company's balance sheet of its investments in common stock of an equity method.

                This item is typically available for the insurance industry.

    

    InvestmentsInOtherVenturesUnderEquityMethodBalanceSheet(store: IDictionary[str, Decimal])
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


class InvestmentsinSubsidiariesatCostBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A stake in any company which is more than 51%.

    

    InvestmentsinSubsidiariesatCostBalanceSheet(store: IDictionary[str, Decimal])
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


class IssuanceOfCapitalStockCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash inflow from offering common stock, which is the additional capital contribution to the entity during the PeriodAsByte.

    

    IssuanceOfCapitalStockCashFlowStatement(store: IDictionary[str, Decimal])
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


class IssuanceOfDebtCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash inflow due to an increase in long term debt.

    

    IssuanceOfDebtCashFlowStatement(store: IDictionary[str, Decimal])
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


class IssueExpensesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cost associated with issuance of debt/equity capital in the Financing Cash Flow section.

    

    IssueExpensesCashFlowStatement(store: IDictionary[str, Decimal])
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


class ItemsinTheCourseofTransmissiontoOtherBanksBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Carrying amount as of the balance sheet date of drafts and bills of exchange that have been accepted by the reporting bank or by

                others for its own account, as its liability to holders of the drafts.

    

    ItemsinTheCourseofTransmissiontoOtherBanksBalanceSheet(store: IDictionary[str, Decimal])
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


class LandAndImprovementsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Fixed Assets that specifically deal with land a company owns. Includes the improvements associated with land. This excludes land

                held for sale.

    

    LandAndImprovementsBalanceSheet(store: IDictionary[str, Decimal])
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


class LeasesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Carrying amount at the balance sheet date of a long-lived, depreciable asset that is an addition or improvement to assets held

                under lease arrangement. This item is usually not available for the insurance industry.

    

    LeasesBalanceSheet(store: IDictionary[str, Decimal])
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


class LiabilitiesHeldforSaleCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Liabilities due within the next 12 months related from an asset classified as Held for Sale.

    

    LiabilitiesHeldforSaleCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class LiabilitiesHeldforSaleNonCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Liabilities related to an asset classified as held for sale excluding the portion due the next 12 months or operating cycle.

    

    LiabilitiesHeldforSaleNonCurrentBalanceSheet(store: IDictionary[str, Decimal])
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
