from .__Fundamental_65 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class TotalEquityGrossMinorityInterestBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Residual interest, including minority interest, that remains in the assets of the enterprise after deducting its liabilities. Equity is

                increased by owners' investments and by comprehensive income, and it is reduced by distributions to the owners.

    

    TotalEquityGrossMinorityInterestBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalExpensesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The sum of operating expense and cost of revenue. If the company does not give the reported number, it will be calculated by

                adding operating expense and cost of revenue.

    

    TotalExpensesIncomeStatement(store: IDictionary[str, Decimal])
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


class TotalFinancialLeaseObligationsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents the total amount of long-term capital leases that must be paid within the next accounting period for a Non-

                Differentiated Balance Sheet. Capital lease obligations are contractual obligations that arise from obtaining the use of property or

                equipment via a capital lease contract.

    

    TotalFinancialLeaseObligationsBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalInvestmentsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Asset that refers to the sum of all available for sale securities and other investments often reported on the balance sheet of

                insurance firms.

    

    TotalInvestmentsBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalLiabilitiesAsReportedBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total liabilities as reported by the company, may be the same or not the same as Morningstar's standardized definition.

    

    TotalLiabilitiesAsReportedBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalLiabilitiesGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the total liabilities on a percentage basis. Morningstar calculates the growth percentage based on the total liabilities

                reported in the Balance Sheet within the company filings or reports.

    

    TotalLiabilitiesGrowth(store: IDictionary[str, Decimal])
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


class TotalLiabilitiesNetMinorityInterestBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Probable future sacrifices of economic benefits arising from present obligations of an enterprise to transfer assets or provide

                services to others in the future as a result of past transactions or events, excluding minority interest.

    

    TotalLiabilitiesNetMinorityInterestBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalMoneyMarketInvestmentsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The sum of the money market investments held by a bank's depositors, which are FDIC insured.

    

    TotalMoneyMarketInvestmentsIncomeStatement(store: IDictionary[str, Decimal])
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


class TotalNonCurrentAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of the carrying amounts as of the balance sheet date of all assets that are expected to be realized in cash, sold or consumed

                after one year or beyond the normal operating cycle, if longer.

    

    TotalNonCurrentAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalNonCurrentLiabilitiesNetMinorityInterestBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total obligations, net minority interest, incurred as part of normal operations that is expected to be repaid beyond the following

                twelve months or one business cycle; excludes minority interest.

    

    TotalNonCurrentLiabilitiesNetMinorityInterestBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalOperatingIncomeAsReportedIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Operating profit/loss as reported by the company, may be the same or not the same as Morningstar's standardized definition.

    

    TotalOperatingIncomeAsReportedIncomeStatement(store: IDictionary[str, Decimal])
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


class TotalOtherFinanceCostIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Any other finance cost which is not clearly defined in the Non-Operating section.

    

    TotalOtherFinanceCostIncomeStatement(store: IDictionary[str, Decimal])
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
