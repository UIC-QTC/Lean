from .__Fundamental_19 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class DepletionIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The non-cash expense recognized on natural resources (eg. Oil and mineral deposits) over the benefit period of the asset.

    

    DepletionIncomeStatement(store: IDictionary[str, Decimal])
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


class DepositCertificatesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A savings certificate entitling the bearer to receive interest. A CD bears a maturity date, a specified fixed interest rate and can be

                issued in any denomination.

    

    DepositCertificatesBalanceSheet(store: IDictionary[str, Decimal])
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


class DepositsbyBankBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Banks investment in the ongoing entity.

    

    DepositsbyBankBalanceSheet(store: IDictionary[str, Decimal])
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


class DepositsMadeunderAssumedReinsuranceContractBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Deposits made under reinsurance.

    

    DepositsMadeunderAssumedReinsuranceContractBalanceSheet(store: IDictionary[str, Decimal])
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


class DepositsReceivedunderCededInsuranceContractBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Deposit received through ceded insurance contract.

    

    DepositsReceivedunderCededInsuranceContractBalanceSheet(store: IDictionary[str, Decimal])
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


class DepreciationAmortizationDepletionCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    It is a non cash charge that represents a reduction in the value of fixed assets due to wear, age or obsolescence. This figure also

                includes amortization of leased property, intangibles, and goodwill, and depletion. This non-cash item is an add-back to the cash

                flow statement.

    

    DepreciationAmortizationDepletionCashFlowStatement(store: IDictionary[str, Decimal])
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


class DepreciationAmortizationDepletionIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The sum of depreciation, amortization and depletion expense in the Income Statement.

                Depreciation is the non-cash expense recognized on tangible assets used in the normal course of business, by allocating the cost of

                assets over their useful lives

                Amortization is the non-cash expense recognized on intangible assets over the benefit period of the asset.

                Depletion is the non-cash expense recognized on natural resources (eg. Oil and mineral deposits) over the benefit period of the

                asset.

    

    DepreciationAmortizationDepletionIncomeStatement(store: IDictionary[str, Decimal])
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


class DepreciationAndAmortizationCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The current period expense charged against earnings on long-lived, physical assets used in the normal conduct of business and not

                intended for resale to allocate or recognize the cost of assets over their useful lives; or to record the reduction in book value of an

                intangible asset over the benefit period of such asset.

    

    DepreciationAndAmortizationCashFlowStatement(store: IDictionary[str, Decimal])
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


class DepreciationAndAmortizationIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The sum of depreciation and amortization expense in the Income Statement.

                Depreciation is the non-cash expense recognized on tangible assets used in the normal course of business, by allocating the cost of

                assets over their useful lives

                Amortization is the non-cash expense recognized on intangible assets over the benefit period of the asset.

    

    DepreciationAndAmortizationIncomeStatement(store: IDictionary[str, Decimal])
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


class DepreciationCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An expense recorded to allocate a tangible asset's cost over its useful life. Since it is a non-cash expense, it increases free cash

                flow while decreasing reported earnings.

    

    DepreciationCashFlowStatement(store: IDictionary[str, Decimal])
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


class DepreciationIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The current period non-cash expense recognized on tangible assets used in the normal course of business, by allocating the cost of

                assets over their useful lives, in the Income Statement. Examples of tangible asset include buildings, production and equipment.

    

    DepreciationIncomeStatement(store: IDictionary[str, Decimal])
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


class DepreciationSupplementalIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The current period expense charged against earnings on tangible asset over its useful life. It is a supplemental value which would

                be reported outside consolidated statements.

    

    DepreciationSupplementalIncomeStatement(store: IDictionary[str, Decimal])
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
