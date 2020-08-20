from .__Fundamental_63 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class TaxAssetsTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of total tax assets in a Non-Differentiated Balance Sheet, includes Tax Receivables and Deferred Tax Assets.

    

    TaxAssetsTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class TaxEffectOfUnusualItemsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Tax effect of the usual items

    

    TaxEffectOfUnusualItemsIncomeStatement(store: IDictionary[str, Decimal])
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


class TaxesAssetsCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Carrying amount due within one year of the balance sheet date (or one operating cycle, if longer) from tax authorities as of the

                balance sheet date representing refunds of overpayments or recoveries based on agreed-upon resolutions of disputes, and current

                deferred tax assets.

    

    TaxesAssetsCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class TaxesReceivableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Carrying amount due within one year of the balance sheet date (or one operating cycle, if longer) from tax authorities as of the

                balance sheet date representing refunds of overpayments or recoveries based on agreed-upon resolutions of disputes. This item is

                usually not available for bank industry.

    

    TaxesReceivableBalanceSheet(store: IDictionary[str, Decimal])
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


class TaxesRefundPaidCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total tax paid or received on operating activities.

    

    TaxesRefundPaidCashFlowStatement(store: IDictionary[str, Decimal])
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


class TaxesRefundPaidDirectCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Tax paid/refund related to operating activities, for the direct cash flow.

    

    TaxesRefundPaidDirectCashFlowStatement(store: IDictionary[str, Decimal])
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


class TaxLossCarryforwardBasicEPS(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The earnings attributable to the tax loss carry forward (during the reporting period).

    

    TaxLossCarryforwardBasicEPS(store: IDictionary[str, Decimal])
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


class TaxLossCarryforwardDilutedEPS(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The earnings from any tax loss carry forward (in the reporting period).

    

    TaxLossCarryforwardDilutedEPS(store: IDictionary[str, Decimal])
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


class TaxProvisionIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Include any taxes on income, net of any investment tax credits for the current accounting PeriodAsByte.

    

    TaxProvisionIncomeStatement(store: IDictionary[str, Decimal])
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


class TaxRate(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of tax provision to pretax income. Morningstar calculates the ratio by using the underlying data reported in the

                company filings or reports:   Tax Provision / Pretax Income.

                [Note: Valid only when positive pretax income, and positive tax expense (not tax benefit)]

    

    TaxRate(store: IDictionary[str, Decimal])
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


class TaxRateForCalcsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Tax rate used for Morningstar calculations.

    

    TaxRateForCalcsIncomeStatement(store: IDictionary[str, Decimal])
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


class TotalAdjustmentsforNonCashItemsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of all adjustments back from net income but without real cash outflow or inflow.

    

    TotalAdjustmentsforNonCashItemsCashFlowStatement(store: IDictionary[str, Decimal])
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


class TotalAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of probable future economic benefits obtained or controlled by a particular enterprise as a result of past

                transactions or events.

    

    TotalAssetsBalanceSheet(store: IDictionary[str, Decimal])
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
