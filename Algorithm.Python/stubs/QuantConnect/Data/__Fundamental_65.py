from .__Fundamental_66 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class TotalPartnershipCapitalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Ownership interest of different classes of partners in the publicly listed limited partnership or master limited partnership. Partners

                include general, limited and preferred partners.

    

    TotalPartnershipCapitalBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalPremiumsEarnedIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Premiums earned is the portion of an insurance written premium which is considered "earned" by the insurer, based on the part of

                the policy period that the insurance has been in effect, and during which the insurer has been exposed to loss.

    

    TotalPremiumsEarnedIncomeStatement(store: IDictionary[str, Decimal])
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


class TotalRevenueAsReportedIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total revenue as reported by the company, may be the same or not the same as Morningstar's standardized definition.

    

    TotalRevenueAsReportedIncomeStatement(store: IDictionary[str, Decimal])
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


class TotalRevenueIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    All sales, business revenues and income that the company makes from its business operations, net of excise taxes. This applies for

                all companies and can be used as comparison for all industries.

                For Normal, Mining, Transportation and Utility templates companies, this is the sum of Operating Revenues, Excise Taxes and Fees.

                For Bank template companies, this is the sum of Net Interest Income and Non-Interest Income.

                For Insurance template companies, this is the sum of Premiums, Interest Income, Fees, Investment and Other Income.

    

    TotalRevenueIncomeStatement(store: IDictionary[str, Decimal])
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


class TotalRiskBasedCapital(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The sum of Tier 1 and Tier 2 Capital. Tier 1 capital consists of common shareholders equity, perpetual preferred shareholders equity

                with non-cumulative dividends, retained earnings, and minority interests in the equity accounts of consolidated subsidiaries. Tier 2

                capital consists of subordinated debt, intermediate-term preferred stock, cumulative and long-term preferred stock, and a portion of

                a bank's allowance for loan and lease losses.

    

    TotalRiskBasedCapital(store: IDictionary[str, Decimal])
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


class TotalTaxPayableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A liability that reflects the taxes owed to federal, state, and local tax authorities. It is the carrying value as of the balance sheet

                date of obligations incurred and payable for statutory income, sales, use, payroll, excise, real, property and other taxes.

    

    TotalTaxPayableBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalUnusualItemsExcludingGoodwillIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The sum of all the identifiable operating and non-operating unusual items.

    

    TotalUnusualItemsExcludingGoodwillIncomeStatement(store: IDictionary[str, Decimal])
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


class TotalUnusualItemsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total unusual items including Negative Goodwill.

    

    TotalUnusualItemsIncomeStatement(store: IDictionary[str, Decimal])
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


class TradeandOtherPayablesNonCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of all non-current payables and accrued expenses.

    

    TradeandOtherPayablesNonCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class TradeAndOtherReceivablesNonCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Amounts due from customers or clients, more than one year from the balance sheet date, for goods or services that have been

                delivered or sold in the normal course of business, or other receivables.

    

    TradeAndOtherReceivablesNonCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class TradingandFinancialLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total carrying amount of total trading, financial liabilities and debt in a non-differentiated balance sheet.

    

    TradingandFinancialLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class TradingAndOtherReceivableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This will serve as the "parent" value to AccountsReceivable (DataId 23001) and OtherReceivables (DataId 23342) for all company

                financials reported in the IFRS GAAP.

    

    TradingAndOtherReceivableBalanceSheet(store: IDictionary[str, Decimal])
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
