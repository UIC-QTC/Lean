from .__Fundamental_18 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class DebtTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The total aggregate of all written promises and/or agreements to repay a stated amount of borrowed funds at a specified date in

                the future; in a Non-Differentiated Balance Sheet.

    

    DebtTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class DecreaseinInterestBearingDepositsinBankCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net change on interest-bearing deposits in other financial institutions for relatively short periods of time including, for example,

                certificates of deposits.

    

    DecreaseinInterestBearingDepositsinBankCashFlowStatement(store: IDictionary[str, Decimal])
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


class DeferredAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An amount owed to a firm that is not expected to be received by the firm within one year from the date of the balance sheet.

    

    DeferredAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class DeferredCostsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An expenditure not recognized as a cost of operation of the period in which incurred, but carried forward to be written off in future

                periods.

    

    DeferredCostsBalanceSheet(store: IDictionary[str, Decimal])
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


class DeferredIncomeTaxCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The component of income tax expense for the period representing the net change in the entities deferred tax assets and liabilities

                pertaining to continuing operations.

    

    DeferredIncomeTaxCashFlowStatement(store: IDictionary[str, Decimal])
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


class DeferredIncomeTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Collections of cash or other assets related to revenue producing activity for which revenue has not yet been recognized on a Non-

                Differentiated Balance Sheet.

    

    DeferredIncomeTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class DeferredPolicyAcquisitionCostsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Net amount of deferred policy acquisition costs capitalized on contracts remaining in force as of the balance sheet date.

    

    DeferredPolicyAcquisitionCostsBalanceSheet(store: IDictionary[str, Decimal])
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


class DeferredTaxAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An asset on a company's balance sheet that may be used to reduce any subsequent period's income tax expense. Deferred tax

                assets can arise due to net loss carryovers, which are only recorded as assets if it is deemed more likely than not that the asset

                will be used in future fiscal periods.

    

    DeferredTaxAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class DeferredTaxCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Future tax liability or asset, resulting from temporary differences between book (accounting) value of assets and liabilities, and their

                tax value. This arises due to differences between financial accounting for shareholders and tax accounting.

    

    DeferredTaxCashFlowStatement(store: IDictionary[str, Decimal])
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


class DeferredTaxLiabilitiesTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A future tax liability, resulting from temporary differences between book (accounting) value of assets and liabilities and their tax

                value or timing differences between the recognition of gains and losses in financial statements, on a Non-Differentiated Balance

                Sheet.

    

    DeferredTaxLiabilitiesTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class DefinedPensionBenefitBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The recognition of an asset where pension fund assets exceed promised benefits.

    

    DefinedPensionBenefitBalanceSheet(store: IDictionary[str, Decimal])
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


class DepletionCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Unlike depreciation and amortization, which mainly describe the deduction of expenses due to the aging of equipment and property,

                depletion is the actual physical reduction of natural resources by companies.   For example, coalmines, oil fields and other natural

                resources are depleted on company accounting statements. This reduction in the quantity of resources is meant to assist in

                accurately identifying the value of the asset on the balance sheet.

    

    DepletionCashFlowStatement(store: IDictionary[str, Decimal])
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
