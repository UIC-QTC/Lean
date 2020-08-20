from .__Fundamental_24 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class EquitySharesInvestmentsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Investments in shares of a company representing ownership in that company.

    

    EquitySharesInvestmentsBalanceSheet(store: IDictionary[str, Decimal])
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


class ExcessTaxBenefitFromStockBasedCompensationCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Reductions in the entity's income taxes that arise when compensation cost (from non-qualified share-based compensation)

                recognized on the entities tax return exceeds compensation cost from share-based compensation recognized in financial

                statements. This element reduces net cash provided by operating activities.

    

    ExcessTaxBenefitFromStockBasedCompensationCashFlowStatement(store: IDictionary[str, Decimal])
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


class ExciseTaxesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Excise taxes are taxes paid when purchases are made on a specific good, such as gasoline. Excise taxes are often included in the

                price of the product. There are also excise taxes on activities, such as on wagering or on highway usage by trucks.

    

    ExciseTaxesIncomeStatement(store: IDictionary[str, Decimal])
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


class ExpenseRatio(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A measure of operating performance for Insurance companies, as it shows the relationship between the premiums earned and

                administrative expenses related to claims such as fees and commissions. A number of 1 or lower is preferred, as this means the

                premiums exceed the expenses. Calculated as: (Deferred Policy Acquisition Amortization Expense+Fees and Commission

                Expense+Other Underwriting Expenses+Selling, General and Administrative) / Net Premiums Earned

    

    ExpenseRatio(store: IDictionary[str, Decimal])
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


class ExplorationDevelopmentAndMineralPropertyLeaseExpensesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Costs incurred in identifying areas that may warrant examination and in examining specific areas that are considered to have

                prospects of containing energy or metal reserves, including costs of drilling exploratory wells. Development expense is the

                capitalized costs incurred to obtain access to proved reserves and to provide facilities for extracting, treating, gathering and storing

                the energy and metal. Mineral property includes oil and gas wells, mines, and other natural deposits (including geothermal

                deposits). The payment for leasing those properties is called mineral property lease expense. Exploration expense is included in

                operation expenses for mining industry.

    

    ExplorationDevelopmentAndMineralPropertyLeaseExpensesIncomeStatement(store: IDictionary[str, Decimal])
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


class FCFGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's free cash flow on a percentage basis. Morningstar calculates the growth percentage based on the

                underlying cash flow from operations and capital expenditures data reported in the Cash Flow Statement within the company filings

                or reports:   Free Cash Flow = Cash flow from operations - Capital Expenditures.

    

    FCFGrowth(store: IDictionary[str, Decimal])
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


class FCFNetIncomeRatio(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Free Cash Flow / Net Income

    

    FCFNetIncomeRatio(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    OneYear: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class FCFPerShareGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's free cash flow per share on a percentage basis. Morningstar calculates the growth percentage based

                on the free cash flow divided by average diluted shares outstanding reported in the Financial Statements within the company filings

                or reports.

    

    FCFPerShareGrowth(store: IDictionary[str, Decimal])
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


class FCFSalesRatio(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Free Cash flow / Revenue

    

    FCFSalesRatio(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    OneYear: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class FCFtoCFO(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Indicates the percentage of a company's operating cash flow is free to be invested in its business after capital expenditures.

    

    FCFtoCFO(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    OneYear: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class FederalFundsPurchasedAndSecuritiesSoldUnderAgreementToRepurchaseBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This liability refers to the amount shown on the books that a bank with insufficient reserves borrows, at the federal funds rate, from

                another bank to meet its reserve requirements; and the amount of securities that an institution sells and agrees to repurchase at a

                specified date for a specified price, net of any reductions or offsets.

    

    FederalFundsPurchasedAndSecuritiesSoldUnderAgreementToRepurchaseBalanceSheet(store: IDictionary[str, Decimal])
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


class FederalFundsPurchasedBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount borrowed by a bank, at the federal funds rate, from another bank to meet its reserve requirements.  This item is

                typically available for the bank industry.

    

    FederalFundsPurchasedBalanceSheet(store: IDictionary[str, Decimal])
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
