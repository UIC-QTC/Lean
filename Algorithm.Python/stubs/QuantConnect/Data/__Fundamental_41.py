from .__Fundamental_42 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class NetIncomeIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Includes all the operations (continuing and discontinued) and all the other income or charges (extraordinary, accounting changes,

                tax loss carry forward, and other gains and losses).

    

    NetIncomeIncomeStatement(store: IDictionary[str, Decimal])
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


class NetIncomePerEmployee(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of Net Income to Employees. Morningstar calculates the ratio by using the underlying data reported in the

                company filings or reports:     Net Income / Employee Number.

    

    NetIncomePerEmployee(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    OneYear: float

    ThreeMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class NetIntangiblesPurchaseAndSaleCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net change between Purchases/Sales of Intangibles.

    

    NetIntangiblesPurchaseAndSaleCashFlowStatement(store: IDictionary[str, Decimal])
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


class NetInterestIncomeIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total interest income minus total interest expense. It represents the difference between interest and dividends earned on interest-

                bearing assets and interest paid to depositors and other creditors.

    

    NetInterestIncomeIncomeStatement(store: IDictionary[str, Decimal])
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


class NetInvestmentIncomeIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total of interest, dividends, and other earnings derived from the insurance company's invested assets minus the expenses

                associated with these investments. Excluded from this income are capital gains or losses as the result of the sale of assets, as well

                as any unrealized capital gains or losses.

    

    NetInvestmentIncomeIncomeStatement(store: IDictionary[str, Decimal])
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


class NetInvestmentPropertiesPurchaseAndSaleCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Net increase or decrease in cash due to purchases or sales of investment properties during the accounting PeriodAsByte.

    

    NetInvestmentPropertiesPurchaseAndSaleCashFlowStatement(store: IDictionary[str, Decimal])
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


class NetInvestmentPurchaseAndSaleCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net change between Purchases/Sales of Investments.

    

    NetInvestmentPurchaseAndSaleCashFlowStatement(store: IDictionary[str, Decimal])
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


class NetIssuancePaymentsOfDebtCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of debt.

    

    NetIssuancePaymentsOfDebtCashFlowStatement(store: IDictionary[str, Decimal])
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


class NetLoanBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents the value of all loans after deduction of the appropriate allowances for loan and lease losses.

    

    NetLoanBalanceSheet(store: IDictionary[str, Decimal])
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


class NetLongTermDebtIssuanceCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of long term debt. Long term debt includes notes payable, bonds payable, mortgage

                loans, convertible debt, subordinated debt and other types of long term debt.

    

    NetLongTermDebtIssuanceCashFlowStatement(store: IDictionary[str, Decimal])
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


class NetMargin(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of net income to revenue. Morningstar calculates the ratio by using the underlying data reported in the company

                filings or reports:   Net Income / Revenue.

    

    NetMargin(store: IDictionary[str, Decimal])
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


class NetNonOperatingInterestIncomeExpenseIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Net-Non Operating interest income or expenses caused by financing activities.

    

    NetNonOperatingInterestIncomeExpenseIncomeStatement(store: IDictionary[str, Decimal])
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


class NetOccupancyExpenseIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Occupancy expense may include items, such as depreciation of facilities and equipment, lease expenses, property taxes and

                property and casualty insurance expense. This item is usually only available for bank industry.

    

    NetOccupancyExpenseIncomeStatement(store: IDictionary[str, Decimal])
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
