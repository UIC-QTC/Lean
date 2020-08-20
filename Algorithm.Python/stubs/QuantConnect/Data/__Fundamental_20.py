from .__Fundamental_21 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class DilutedExtraordinary(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Diluted EPS from Extraordinary Gain/Losses is the gain or loss from extraordinary items divided by the common shares outstanding

                adjusted for the assumed conversion of all potentially dilutive securities. Securities having a dilutive effect may include convertible

                debentures, warrants, options, and convertible preferred stock.

    

    DilutedExtraordinary(store: IDictionary[str, Decimal])
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


class DilutedNIAvailtoComStockholdersIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Net income to calculate Diluted EPS, accounting for adjustments assuming that all the convertible instruments are being converted

                to Common Equity.

    

    DilutedNIAvailtoComStockholdersIncomeStatement(store: IDictionary[str, Decimal])
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


class DividendCoverageRatio(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Reflects a firm's capacity to pay a dividend, and is defined as Earnings Per Share / Dividend Per Share

    

    DividendCoverageRatio(store: IDictionary[str, Decimal])
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


class DividendIncomeIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Dividends earned from equity investment securities. This item is usually only available for bank industry.

    

    DividendIncomeIncomeStatement(store: IDictionary[str, Decimal])
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


class DividendPaidCFOCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Dividend paid to the investors, in the Operating Cash Flow section.

    

    DividendPaidCFOCashFlowStatement(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class DividendPerShare(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount of dividend that a stockholder will receive for each share of stock held. It can be calculated by taking the total amount

                of dividends paid and dividing it by the total shares outstanding. Dividend per share = total dividend payment/total number of

                outstanding shares

    

    DividendPerShare(store: IDictionary[str, Decimal])
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


class DividendReceivedCFOCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Dividend received on investment, in the Operating Cash Flow section.

    

    DividendReceivedCFOCashFlowStatement(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    SixMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class DividendsPaidDirectCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Dividend paid to the investors, for the direct cash flow.

    

    DividendsPaidDirectCashFlowStatement(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class DividendsPayableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of the carrying values of dividends declared but unpaid on equity securities issued and outstanding (also includes dividends

                collected on behalf of another owner of securities that are being held by entity) by the entity.

    

    DividendsPayableBalanceSheet(store: IDictionary[str, Decimal])
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

    ThreeMonths: float

    TwelveMonths: float

    TwoMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class DividendsReceivedCFICashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Dividend received on investment, in the Investing Cash Flow section.

    

    DividendsReceivedCFICashFlowStatement(store: IDictionary[str, Decimal])
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


class DividendsReceivedDirectCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Dividend received on the investment, for the direct cash flow.

    

    DividendsReceivedDirectCashFlowStatement(store: IDictionary[str, Decimal])
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


class DPSGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's dividends per share (DPS) on a percentage basis. Morningstar calculates the annualized growth

                percentage based on the underlying DPS from its dividend database.  Morningstar collects its DPS from company filings and

                reports, as well as from third party sources.

    

    DPSGrowth(store: IDictionary[str, Decimal])
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


class DueFromRelatedPartiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    For an unclassified balance sheet, carrying amount as of the balance sheet date of obligations due all related parties.

    

    DueFromRelatedPartiesBalanceSheet(store: IDictionary[str, Decimal])
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
