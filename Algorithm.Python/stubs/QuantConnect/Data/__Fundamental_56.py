from .__Fundamental_57 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class RegressionGrowthofDividends5Years(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The five-year growth rate of dividends per share, calculated using regression analysis.

    

    RegressionGrowthofDividends5Years(store: IDictionary[str, Decimal])
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


class RegressionGrowthOperatingRevenue5Years(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The five-year growth rate of operating revenue, calculated using regression analysis.

    

    RegressionGrowthOperatingRevenue5Years(store: IDictionary[str, Decimal])
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


class RegulatoryAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Carrying amount as of the balance sheet date of capitalized costs of regulated entities that are expected to be recovered through

                revenue sources over one year or beyond the normal operating cycle.

    

    RegulatoryAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class RegulatoryLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount for the individual regulatory noncurrent liability as itemized in a table of regulatory noncurrent liabilities as of the end of

                the PeriodAsByte. Such things as the costs of energy efficiency programs and low-income energy assistances programs and deferred fuel.

                This item is usually only available for utility industry.

    

    RegulatoryLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class ReinsuranceandOtherRecoveriesReceivedCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash received from reinsurance income or other recoveries income in operating cash flow, using the direct method. This item is

                usually only available for insurance industry

    

    ReinsuranceandOtherRecoveriesReceivedCashFlowStatement(store: IDictionary[str, Decimal])
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


class ReinsuranceAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Reinsurance asset is insurance that is purchased by an insurance company from another insurance company.

    

    ReinsuranceAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class ReinsuranceBalancesPayableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The carrying amount as of the balance sheet date of the known and estimated amounts owed to insurers under reinsurance

                treaties or other arrangements. This item is usually only available for insurance industry.

    

    ReinsuranceBalancesPayableBalanceSheet(store: IDictionary[str, Decimal])
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


class ReinsuranceRecoverableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount of benefits the ceding insurer expects to recover on insurance policies ceded to other insurance entities as of the

                balance sheet date for all guaranteed benefit types. It includes estimated amounts for claims incurred but not reported, and policy

                benefits, net of any related valuation allowance.

    

    ReinsuranceRecoverableBalanceSheet(store: IDictionary[str, Decimal])
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


class ReinsuranceRecoveriesClaimsandBenefitsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Claim on the reinsurance company and take the benefits.

    

    ReinsuranceRecoveriesClaimsandBenefitsIncomeStatement(store: IDictionary[str, Decimal])
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


class ReinsuranceRecoveriesofInsuranceLiabilitiesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Income/Expense due to recoveries from reinsurers for insurance liabilities.

    

    ReinsuranceRecoveriesofInsuranceLiabilitiesIncomeStatement(store: IDictionary[str, Decimal])
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


class ReinsuranceRecoveriesofInvestmentContractIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Income/Expense due to recoveries from reinsurers for Investment Contracts.

    

    ReinsuranceRecoveriesofInvestmentContractIncomeStatement(store: IDictionary[str, Decimal])
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


class RentandLandingFeesCostofRevenueIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Costs paid to use the facilities necessary to generate revenue during the accounting PeriodAsByte.

    

    RentandLandingFeesCostofRevenueIncomeStatement(store: IDictionary[str, Decimal])
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


class RentAndLandingFeesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Rent fees are the cost of occupying space during the accounting PeriodAsByte. Landing fees are a change paid to an airport company for

                landing at a particular airport. This item is not available for insurance industry.

    

    RentAndLandingFeesIncomeStatement(store: IDictionary[str, Decimal])
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
