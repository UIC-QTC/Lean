from .__Fundamental_46 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class NormalizedEBITDAIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    EBITDA less Total Unusual Items

    

    NormalizedEBITDAIncomeStatement(store: IDictionary[str, Decimal])
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


class NormalizedIncomeAsReportedIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Earnings adjusted for items that are irregular or unusual in nature, and/or are non-recurring. This can be used to fairly measure a

                company's profitability. This is as reported by the company, may be the same or not the same as Morningstar's standardized

                definition.

    

    NormalizedIncomeAsReportedIncomeStatement(store: IDictionary[str, Decimal])
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


class NormalizedIncomeIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This calculation represents earnings adjusted for items that are irregular or unusual in nature, and/or are non-recurring. This can be

                used to fairly measure a company's profitability. This is calculated using Net Income from Continuing Operations plus/minus any tax

                affected unusual Items and Goodwill Impairments/Write Offs.

    

    NormalizedIncomeIncomeStatement(store: IDictionary[str, Decimal])
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


class NormalizedNetProfitMargin(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Normalized Income / Total Revenue. A measure of profitability of the company calculated by finding Normalized Net Profit as a

                percentage of Total Revenues.

    

    NormalizedNetProfitMargin(store: IDictionary[str, Decimal])
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


class NormalizedOperatingProfitAsReportedIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Operating profit adjusted for items that are irregular or unusual in nature, and/or are non-recurring. This can be used to fairly

                measure a company's profitability. This is as reported by the company, may be the same or not the same as Morningstar's

                standardized definition.

    

    NormalizedOperatingProfitAsReportedIncomeStatement(store: IDictionary[str, Decimal])
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


class NormalizedPreTaxIncomeIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This calculation represents pre-tax earnings adjusted for items that are irregular or unusual in nature, and/or are non-recurring. This

                can be used to fairly measure a company's profitability. This is calculated using Pre-Tax Income plus/minus any unusual Items and

                Goodwill Impairments/Write Offs.

    

    NormalizedPreTaxIncomeIncomeStatement(store: IDictionary[str, Decimal])
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


class NormalizedROIC(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    [Normalized Income + (Interest Expense * (1-Tax Rate))]  / Invested Capital

    

    NormalizedROIC(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    OneYear: float

    SixMonths: float

    ThreeMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class NotesReceivableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An amount representing an agreement for an unconditional promise by the maker to pay the entity (holder) a definite sum of money

                at a future date(s) within one year of the balance sheet date or the normal operating cycle, whichever is longer. Such amount may

                include accrued interest receivable in accordance with the terms of the note. The note also may contain provisions including a

                discount or premium, payable on demand, secured, or unsecured, interest bearing or non-interest bearing, among a myriad of other

                features and characteristics.

    

    NotesReceivableBalanceSheet(store: IDictionary[str, Decimal])
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


class OccupancyAndEquipmentIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Includes total expenses of occupancy and equipment. This item is usually only available for bank industry.

    

    OccupancyAndEquipmentIncomeStatement(store: IDictionary[str, Decimal])
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


class OperatingCashFlowCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net cash from (used in) all of the entity's operating activities, including those of discontinued operations, of the reporting entity.

                Operating activities include all transactions and events that are not defined as investing or financing activities. Operating activities

                generally involve producing and delivering goods and providing services. Cash flows from operating activities are generally the cash

                effects of transactions and other events that enter into the determination of net income.

    

    OperatingCashFlowCashFlowStatement(store: IDictionary[str, Decimal])
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


class OperatingExpenseAsReportedIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Operating expense as reported by the company, may be the same or not the same as Morningstar's standardized definition.

    

    OperatingExpenseAsReportedIncomeStatement(store: IDictionary[str, Decimal])
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
