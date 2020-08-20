from .__Fundamental_30 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class GrossNotesReceivableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An amount representing an agreement for an unconditional promise by the maker to pay the entity (holder) a definite sum of money

                at a future date(s) within one year of the balance sheet date or the normal operating cycle. Such amount may include accrued

                interest receivable in accordance with the terms of the note. The note also may contain provisions including a discount or premium,

                payable on demand, secured, or unsecured, interest bearing or non-interest bearing, among myriad other features and

                characteristics. This item is typically available for bank industry.

    

    GrossNotesReceivableBalanceSheet(store: IDictionary[str, Decimal])
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


class GrossPPEBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Carrying amount at the balance sheet date for long-lived physical assets used in the normal conduct of business and not intended

                for resale. This can include land, physical structures, machinery, vehicles, furniture, computer equipment, construction in progress,

                and similar items. Amount does not include depreciation.

    

    GrossPPEBalanceSheet(store: IDictionary[str, Decimal])
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


class GrossPremiumsWrittenIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total premiums generated from all policies written by an insurance company within a given period of time. This item is usually only

                available for insurance industry.

    

    GrossPremiumsWrittenIncomeStatement(store: IDictionary[str, Decimal])
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


class GrossProfitAnnual5YrGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This is the compound annual growth rate of the company's Gross Profit over the last 5 years.

    

    GrossProfitAnnual5YrGrowth(store: IDictionary[str, Decimal])
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


class GrossProfitIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total revenue less cost of revenue. The number is as reported by the company on the income statement; however, the number will

                be calculated if it is not reported. This field is null if the cost of revenue is not given.

                Gross Profit = Total Revenue - Cost of Revenue.

    

    GrossProfitIncomeStatement(store: IDictionary[str, Decimal])
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


class HedgingAssetsCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A security transaction which expires within a 12 month period that reduces the risk on an existing investment position.

    

    HedgingAssetsCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class HeldToMaturitySecuritiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Debt securities that a firm has the ability and intent to hold until maturity.

    

    HeldToMaturitySecuritiesBalanceSheet(store: IDictionary[str, Decimal])
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


class ImpairmentLossesReversalsFinancialInstrumentsNetIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Impairment or reversal of impairment on financial instrument such as derivative. This is a contra account under Total Revenue in

                banks.

    

    ImpairmentLossesReversalsFinancialInstrumentsNetIncomeStatement(store: IDictionary[str, Decimal])
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


class ImpairmentLossReversalRecognizedinProfitorLossCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The difference between the future net cash flows expected to be received from the asset and its book value, recognized in the

                Income Statement.

    

    ImpairmentLossReversalRecognizedinProfitorLossCashFlowStatement(store: IDictionary[str, Decimal])
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


class ImpairmentOfCapitalAssetsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Impairments are considered to be permanent, which is a downward revaluation of fixed assets. If the sum of all estimated future

                cash flows is less than the carrying value of the asset, then the asset would be considered impaired and would have to be written

                down to its fair value. Once an asset is written down, it may only be written back up under very few circumstances. Usually the

                company uses the sum of undiscounted future cash flows to determine if the impairment should occur, and uses the sum of

                discounted future cash flows to make the impairment judgment. The impairment decision emphasizes on capital assets' future

                profit collection ability.

    

    ImpairmentOfCapitalAssetsIncomeStatement(store: IDictionary[str, Decimal])
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


class IncomefromAssociatesandOtherParticipatingInterestsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total income from the associates and joint venture via investment, accounted for in the Non-Operating section.

    

    IncomefromAssociatesandOtherParticipatingInterestsIncomeStatement(store: IDictionary[str, Decimal])
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
