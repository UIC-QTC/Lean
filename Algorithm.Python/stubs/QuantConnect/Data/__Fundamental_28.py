from .__Fundamental_29 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class GainOnSaleOfPPEIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount of excess earned in comparison to the net book value for sale of property, plant, equipment. This item is usually not

                available for bank and insurance industries.

    

    GainOnSaleOfPPEIncomeStatement(store: IDictionary[str, Decimal])
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


class GainOnSaleOfSecurityIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount of excess earned in comparison to the original purchase value of the security.

    

    GainOnSaleOfSecurityIncomeStatement(store: IDictionary[str, Decimal])
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


class GainsLossesNotAffectingRetainedEarningsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of gains or losses that are not part of retained earnings. It is also called other comprehensive income.

    

    GainsLossesNotAffectingRetainedEarningsBalanceSheet(store: IDictionary[str, Decimal])
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


class GainsLossesonFinancialInstrumentsDuetoFairValueAdjustmentsinHedgeAccountingTotalIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Gain or loss on derivatives investment due to the fair value adjustment.

    

    GainsLossesonFinancialInstrumentsDuetoFairValueAdjustmentsinHedgeAccountingTotalIncomeStatement(store: IDictionary[str, Decimal])
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


class GeneralAndAdministrativeExpenseIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate total of general managing and administering expenses for the company.

    

    GeneralAndAdministrativeExpenseIncomeStatement(store: IDictionary[str, Decimal])
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


class GeneralPartnershipCapitalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    In a limited partnership or master limited partnership form of business, this represents the balance of capital held by the general

                partners.

    

    GeneralPartnershipCapitalBalanceSheet(store: IDictionary[str, Decimal])
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


class GoodwillAndOtherIntangibleAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Rights or economic benefits, such as patents and goodwill, that is not physical in nature. They are those that are neither physical

                nor financial in nature, nevertheless, have value to the company. Intangibles are listed net of accumulated amortization.

    

    GoodwillAndOtherIntangibleAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class GoodwillBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The excess of the cost of an acquired company over the sum of the fair market value of its identifiable individual assets less the

                liabilities.

    

    GoodwillBalanceSheet(store: IDictionary[str, Decimal])
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


class GrossAccountsReceivableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Accounts owed to a company by customers within a year as a result of exchanging goods or services on credit.

    

    GrossAccountsReceivableBalanceSheet(store: IDictionary[str, Decimal])
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


class GrossDividendPaymentIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total amount paid in dividends to investors- this includes dividends paid on equity and non-equity shares.

    

    GrossDividendPaymentIncomeStatement(store: IDictionary[str, Decimal])
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


class GrossLoanBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents the sum of all loans (commercial, consumer, mortgage, etc.) as well as leases before any provisions for loan losses or

                unearned discounts.

    

    GrossLoanBalanceSheet(store: IDictionary[str, Decimal])
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


class GrossMargin(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of gross profit to revenue. Morningstar calculates the ratio by using the underlying data reported in the company

                filings or reports:   (Revenue - Cost of Goods Sold) / Revenue.

    

    GrossMargin(store: IDictionary[str, Decimal])
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


class GrossMargin5YrAvg(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This is the simple average of the company's Annual Gross Margin over the last 5 years. Gross Margin is Total Revenue minus Cost

                of Goods Sold divided by Total Revenue and is expressed as a percentage.

    

    GrossMargin5YrAvg(store: IDictionary[str, Decimal])
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
