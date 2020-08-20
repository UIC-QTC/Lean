from .__Fundamental_23 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class EBITDAIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Earnings minus expenses (excluding interest, tax, depreciation, and amortization expenses).

    

    EBITDAIncomeStatement(store: IDictionary[str, Decimal])
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


class EBITDAMargin(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of earnings before interest, taxes and depreciation and amortization to revenue. Morningstar calculates the ratio

                by using the underlying data reported in the company filings or reports:   EBITDA / Revenue.

    

    EBITDAMargin(store: IDictionary[str, Decimal])
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


class EBITIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Earnings minus expenses (excluding interest and tax expenses).

    

    EBITIncomeStatement(store: IDictionary[str, Decimal])
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


class EBITMargin(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of earnings before interest and taxes to revenue. Morningstar calculates the ratio by using the underlying data

                reported in the company filings or reports:   EBIT / Revenue.

    

    EBITMargin(store: IDictionary[str, Decimal])
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


class EffectiveTaxRateAsReportedIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The average tax rate for the period as reported by the company, may be the same or not the same as Morningstar's standardized

                definition.

    

    EffectiveTaxRateAsReportedIncomeStatement(store: IDictionary[str, Decimal])
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


class EffectOfExchangeRateChangesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The effect of exchange rate changes on cash balances held in foreign currencies.

    

    EffectOfExchangeRateChangesCashFlowStatement(store: IDictionary[str, Decimal])
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


class ElectricUtilityPlantBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount for the electric plant related to the utility industry.

    

    ElectricUtilityPlantBalanceSheet(store: IDictionary[str, Decimal])
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


class EmployeeBenefitsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Carrying amount as of the balance sheet date of the portion of the obligations recognized for the various benefits provided to former

                or inactive employees, their beneficiaries, and covered dependents after employment but before retirement.

    

    EmployeeBenefitsBalanceSheet(store: IDictionary[str, Decimal])
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


class EndCashPositionCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash and cash equivalents balance at the end of the accounting period, as indicated on the Cash Flow statement. It is equal to

                the Beginning Cash and Equivalents, plus the Net Change in Cash and Equivalents.

    

    EndCashPositionCashFlowStatement(store: IDictionary[str, Decimal])
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


class EquipmentIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Equipment expenses include depreciation, repairs, rentals, and service contract costs. This also includes equipment purchases

                which do not qualify for capitalization in accordance with the entity's accounting policy. This item may also include furniture

                expenses. This item is usually only available for bank industry.

    

    EquipmentIncomeStatement(store: IDictionary[str, Decimal])
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


class EquityAttributableToOwnersOfParentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """ EquityAttributableToOwnersOfParentBalanceSheet(store: IDictionary[str, Decimal]) """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    ThreeMonths: float

    TwelveMonths: float

    TwoMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class EquityInvestmentsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This asset represents equity securities categorized neither as held-to-maturity nor trading.

    

    EquityInvestmentsBalanceSheet(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class EquityPerShareGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's book value per share on a percentage basis. Morningstar calculates the annualized growth

                percentage based on the underlying equity and end of period shares outstanding reported in the company filings or reports.

    

    EquityPerShareGrowth(store: IDictionary[str, Decimal])
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

    ThreeMonths: float

    ThreeYears: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]
