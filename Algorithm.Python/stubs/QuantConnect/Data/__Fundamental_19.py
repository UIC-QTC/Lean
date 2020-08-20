from .__Fundamental_20 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class DerivativeAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Fair values of assets resulting from contracts that meet the criteria of being accounted for as derivative instruments, net of the

                effects of master netting arrangements.

    

    DerivativeAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class DerivativeProductLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Fair values of all liabilities resulting from contracts that meet the criteria of being accounted for as derivative instruments; and

                which are expected to be extinguished or otherwise disposed of after one year or beyond the normal operating cycle.

    

    DerivativeProductLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class DilutedAccountingChange(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Diluted EPS from Cumulative Effect Accounting Changes is the earnings from accounting changes (in the reporting period) divided

                by the common shares outstanding adjusted for the assumed conversion of all potentially dilutive securities. Securities having a

                dilutive effect may include convertible debentures, warrants, options, and convertible preferred stock.

    

    DilutedAccountingChange(store: IDictionary[str, Decimal])
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


class DilutedAverageShares(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The shares outstanding used to calculate the diluted EPS, assuming the conversion of all convertible securities and the exercise of

                warrants or stock options. It is the weighted average diluted share outstanding through the whole accounting PeriodAsByte.  Note: If

                Diluted Average Shares are not presented by the firm in the Income Statement and Basic Average Shares are presented, Diluted

                Average Shares will equal Basic Average Shares.  However, if neither value is presented by the firm, Diluted Average Shares will be

                null.

    

    DilutedAverageShares(store: IDictionary[str, Decimal])
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


class DilutedContEPSGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's diluted EPS from continuing operations on a percentage basis. Morningstar calculates the annualized

                growth percentage based on the underlying diluted EPS from continuing operations reported in the Income Statement within the

                company filings or reports.

    

    DilutedContEPSGrowth(store: IDictionary[str, Decimal])
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


class DilutedContinuousOperations(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Diluted EPS from Continuing Operations is the earnings from continuing operations divided by the common shares outstanding

                adjusted for the assumed conversion of all potentially dilutive securities.  Securities having a dilutive effect may include convertible

                debentures, warrants, options, and convertible preferred stock.

    

    DilutedContinuousOperations(store: IDictionary[str, Decimal])
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


class DilutedDiscontinuousOperations(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Diluted EPS from Discontinued Operations is the earnings from discontinued operations divided by the common shares outstanding

                adjusted for the assumed conversion of all potentially dilutive securities. Securities having a dilutive effect may include convertible

                debentures, warrants, options, and convertible preferred stock. This only includes gain or loss from discontinued operations.

    

    DilutedDiscontinuousOperations(store: IDictionary[str, Decimal])
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


class DilutedEPS(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Diluted EPS is the bottom line net income divided by the common shares outstanding adjusted for the assumed conversion of all

                potentially dilutive securities. Securities having a dilutive effect may include convertible debentures, warrants, options, and

                convertible preferred stock. This value will be derived when not reported for the fourth quarter and will be less than or equal to

                Basic EPS.

    

    DilutedEPS(store: IDictionary[str, Decimal])
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


class DilutedEPSGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's diluted earnings per share (EPS) on a percentage basis. Morningstar calculates the annualized growth

                percentage based on the underlying diluted EPS reported in the Income Statement within the company filings or reports.

    

    DilutedEPSGrowth(store: IDictionary[str, Decimal])
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


class DilutedEPSOtherGainsLosses(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The earnings from gains and losses (in the reporting period) divided by the common shares outstanding adjusted for the assumed

                conversion of all potentially dilutive securities. Securities having a dilutive effect may include convertible debentures, warrants,

                options, convertible preferred stock, etc.

    

    DilutedEPSOtherGainsLosses(store: IDictionary[str, Decimal])
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
