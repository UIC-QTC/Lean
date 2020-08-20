from .__Fundamental_28 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class FuturePolicyBenefitsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Accounting policy pertaining to an insurance entity's net liability for future benefits (for example, death, cash surrender value) to be

                paid to or on behalf of policyholders, describing the bases, methodologies and components of the reserve, and assumptions

                regarding estimates of expected investment yields, mortality, morbidity, terminations and expenses.

    

    FuturePolicyBenefitsBalanceSheet(store: IDictionary[str, Decimal])
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


class GainLossonDerecognitionofAvailableForSaleFinancialAssetsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Gain/loss on the write-off of financial assets available-for-sale.

    

    GainLossonDerecognitionofAvailableForSaleFinancialAssetsIncomeStatement(store: IDictionary[str, Decimal])
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


class GainLossonFinancialInstrumentsDesignatedasCashFlowHedgesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Gain/Loss through hedging activities.

    

    GainLossonFinancialInstrumentsDesignatedasCashFlowHedgesIncomeStatement(store: IDictionary[str, Decimal])
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


class GainLossOnInvestmentSecuritiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This item represents the net total realized gain (loss) included in earnings for the period as a result of selling or holding marketable

                securities categorized as trading, available-for-sale, or held-to-maturity, including the unrealized holding gain or loss of held-to-

                maturity securities transferred to the trading security category and the cumulative unrealized gain or loss which was included in

                other comprehensive income (a separate component of shareholders' equity) for available-for-sale securities transferred to trading

                securities during the PeriodAsByte. Additionally, this item would include any losses recognized for other than temporary impairments of the

                subject investments in debt and equity securities.

    

    GainLossOnInvestmentSecuritiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class GainLossonSaleofAssetsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Any gain (loss) recognized on the sale of assets or a sale which generates profit or loss, which is a difference between sales price

                and net book value at the disposal time.

    

    GainLossonSaleofAssetsIncomeStatement(store: IDictionary[str, Decimal])
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


class GainLossOnSaleOfBusinessCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The difference between the sale price or salvage price and the book value of an asset that was sold or retired during the reporting

                PeriodAsByte. This element refers to the gain (loss) and not to the cash proceeds of the business. This element is a non-cash adjustment

                to net income when calculating net cash generated by operating activities using the indirect method.

    

    GainLossOnSaleOfBusinessCashFlowStatement(store: IDictionary[str, Decimal])
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


class GainLossOnSaleOfPPECashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The difference between the sale price or salvage price and the book value of the property, plant and equipment that was sold or

                retired during the reporting PeriodAsByte. Includes the amount received from selling any fixed assets such as property, plant and

                equipment. Usually this section also includes any retirement of equipment. Such as Sale of business segments; Sale of credit and

                receivables; Property disposition; Proceeds from sale or disposition of business or investment; Decrease in excess of purchase price

                over acquired net assets; Abandoned project (expenditures) credit; Allowances for other funds during construction.

    

    GainLossOnSaleOfPPECashFlowStatement(store: IDictionary[str, Decimal])
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


class GainonInvestmentPropertiesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Gain on disposal and change in fair value of investment properties.

    

    GainonInvestmentPropertiesIncomeStatement(store: IDictionary[str, Decimal])
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


class GainOnSaleOfBusinessIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount of excess earned in comparison to fair value when selling a business. This item is usually not available for insurance

                industry.

    

    GainOnSaleOfBusinessIncomeStatement(store: IDictionary[str, Decimal])
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


class GainonSaleofInvestmentPropertyIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Gain on the disposal of investment property.

    

    GainonSaleofInvestmentPropertyIncomeStatement(store: IDictionary[str, Decimal])
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


class GainonSaleofLoansIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Gain on sale of any loans investment.

    

    GainonSaleofLoansIncomeStatement(store: IDictionary[str, Decimal])
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
