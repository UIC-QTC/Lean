# encoding: utf-8
# module QuantConnect.Data.Fundamental calls itself Fundamental
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Fundamental
import System
import System.Collections.Generic
import System.IO
import typing

# no functions
# classes

class MultiPeriodField(System.object):
    """ Abstract base class for multi-period fields """
    def GetPeriodNames(self) -> typing.List[str]:
        pass

    def GetPeriodValue(self, period: str) -> float:
        pass

    def GetPeriodValues(self) -> System.Collections.Generic.IReadOnlyDictionary[str, float]:
        pass

    def HasPeriodValue(self, period: str) -> bool:
        pass

    def HasValues(self) -> bool:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    def ToString(self) -> str:
        pass

    def UpdateValues(self, update: QuantConnect.Data.Fundamental.MultiPeriodField) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        pass

    HasValue: bool

    Value: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]

    PeriodField: type


class AccountsPayableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Any money that a company owes its suppliers for goods and services purchased on credit and is expected to pay within the next
                year or operating cycle.
    
    AccountsPayableBalanceSheet(store: IDictionary[str, Decimal])
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


class AccountsReceivableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Accounts owed to a company by customers within a year as a result of exchanging goods or services on credit.
    
    AccountsReceivableBalanceSheet(store: IDictionary[str, Decimal])
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


class AccruedandDeferredIncomeBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of accrued liabilities and deferred income (amount received in advance but the services are not provided in respect of
                amount).
    
    AccruedandDeferredIncomeBalanceSheet(store: IDictionary[str, Decimal])
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


class AccruedandDeferredIncomeCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of Accrued Liabilities and Deferred Income (amount received in advance but the services are not provided in respect of
                amount) due within 1 year.
    
    AccruedandDeferredIncomeCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class AccruedandDeferredIncomeNonCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of Accrued Liabilities and Deferred Income (amount received in advance but the services are not provided in respect of
                amount) due after 1 year.
    
    AccruedandDeferredIncomeNonCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class AccruedInterestReceivableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This account shows the amount of unpaid interest accrued to the date of purchase and included in the purchase price of securities
                purchased between interest dates.
    
    AccruedInterestReceivableBalanceSheet(store: IDictionary[str, Decimal])
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


class AccruedInvestmentIncomeBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Interest, dividends, rents, ancillary and other revenues earned but not yet received by the entity on its investments.
    
    AccruedInvestmentIncomeBalanceSheet(store: IDictionary[str, Decimal])
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


class AccruedLiabilitiesTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Liabilities which have occurred, but have not been paid or logged under accounts payable during an accounting PeriodAsByte. In other
                words, obligations for goods and services provided to a company for which invoices have not yet been received; on a Non-
                Differentiated Balance Sheet.
    
    AccruedLiabilitiesTotalBalanceSheet(store: IDictionary[str, Decimal])
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

    TwoMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class AccumulatedDepreciationBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cumulative amount of wear and tear or obsolescence charged against the fixed assets of a company.
    
    AccumulatedDepreciationBalanceSheet(store: IDictionary[str, Decimal])
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


class AdditionalPaidInCapitalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Excess of issue price over par or stated value of the entity's capital stock and amounts received from other transactions involving
                the entity's stock or stockholders. Includes adjustments to additional paid in capital. There are two major categories of additional
                paid in capital: 1) Paid in capital in excess of par/stated value, which is the difference between the actual issue price of the shares
                and the shares' par/stated value. 2) Paid in capital from other transactions which includes treasury stock, retirement of stock, stock
                dividends recorded at market, lapse of stock purchase warrants, conversion of convertible bonds in excess of the par value of the
                stock, and any other additional capital from the company's own stock transactions.
    
    AdditionalPaidInCapitalBalanceSheet(store: IDictionary[str, Decimal])
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


class AdvanceFromFederalHomeLoanBanksBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This item is typically available for bank industry. It's the amount of borrowings as of the balance sheet date from the Federal Home
                Loan Bank, which are primarily used to cover shortages in the required reserve balance and liquidity shortages.
    
    AdvanceFromFederalHomeLoanBanksBalanceSheet(store: IDictionary[str, Decimal])
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


class AdvancesfromCentralBanksBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Borrowings from the central bank, which are primarily used to cover shortages in the required reserve balance and liquidity
                shortages.
    
    AdvancesfromCentralBanksBalanceSheet(store: IDictionary[str, Decimal])
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


class AllowanceForDoubtfulAccountsReceivableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An Allowance for Doubtful Accounts measures receivables recorded but not expected to be collected.
    
    AllowanceForDoubtfulAccountsReceivableBalanceSheet(store: IDictionary[str, Decimal])
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


class AllowanceForLoansAndLeaseLossesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A contra account sets aside as an allowance for bad loans (e.g. customer defaults).
    
    AllowanceForLoansAndLeaseLossesBalanceSheet(store: IDictionary[str, Decimal])
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


class AllowanceForNotesReceivableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This item is typically available for bank industry. It represents a provision relating to a written agreement to receive money  with the
                terms of the note (at a specified future date(s) within one year from the reporting date (or the normal operating cycle, whichever is
                longer), consisting of principal as well as any accrued interest) for the portion that is expected to be uncollectible.
    
    AllowanceForNotesReceivableBalanceSheet(store: IDictionary[str, Decimal])
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


class AllTaxesPaidCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash paid to tax authorities in operating cash flow, using the direct method
    
    AllTaxesPaidCashFlowStatement(store: IDictionary[str, Decimal])
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


class AmortizationCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The systematic and rational apportionment of the acquisition cost of intangible operational assets to future periods in which the benefits
                contribute to revenue. This field is to include Amortization and any variation where Amortization is the first account listed in the line item,
                excluding Amortization of Intangibles.
    
    AmortizationCashFlowStatement(store: IDictionary[str, Decimal])
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


class AmortizationIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The non-cash expense recognized on intangible assets over the benefit period of the asset.
    
    AmortizationIncomeStatement(store: IDictionary[str, Decimal])
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


class AmortizationOfFinancingCostsAndDiscountsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The component of interest expense representing the non-cash expenses charged against earnings in the period to allocate debt
                discount and premium, and the costs to issue debt and obtain financing over the related debt instruments. This item is usually only
                available for bank industry.
    
    AmortizationOfFinancingCostsAndDiscountsCashFlowStatement(store: IDictionary[str, Decimal])
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


class AmortizationOfIntangiblesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate expense charged against earnings to allocate the cost of intangible assets (nonphysical assets not used in
                production) in a systematic and rational manner to the periods expected to benefit from such assets.
    
    AmortizationOfIntangiblesCashFlowStatement(store: IDictionary[str, Decimal])
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


class AmortizationOfIntangiblesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate expense charged against earnings to allocate the cost of intangible assets (nonphysical assets not used in
                production) in a systematic and rational manner to the periods expected to benefit from such assets.
    
    AmortizationOfIntangiblesIncomeStatement(store: IDictionary[str, Decimal])
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


class AmortizationOfSecuritiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents amortization of the allocation of a lump sum amount to different time periods, particularly for securities, debt, loans,
                and other forms of financing. Does not include amortization, amortization of capital expenditure and intangible assets.
    
    AmortizationOfSecuritiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class AmortizationSupplementalIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The current period expense charged against earnings on intangible asset over its useful life. It is a supplemental value which would
                be reported outside consolidated statements.
    
    AmortizationSupplementalIncomeStatement(store: IDictionary[str, Decimal])
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


class AssetClassification(System.object):
    """
    Definition of the AssetClassification class
    
    AssetClassification()
    """
    def UpdateValues(self, update: QuantConnect.Data.Fundamental.AssetClassification) -> None:
        pass

    CANNAICS: int

    FinancialHealthGrade: str

    GrowthGrade: str

    GrowthScore: float

    MorningstarEconomySphereCode: int

    MorningstarIndustryCode: int

    MorningstarIndustryGroupCode: int

    MorningstarSectorCode: int

    NACE: float

    NAICS: int

    ProfitabilityGrade: str

    SIC: int

    SizeScore: float

    StockType: int

    StyleBox: int

    StyleScore: float

    ValueScore: float



class AssetImpairmentChargeCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The charge against earnings resulting from the aggregate write down of all assets from their carrying value to their fair value.
    
    AssetImpairmentChargeCashFlowStatement(store: IDictionary[str, Decimal])
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


class AssetsHeldForSaleBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This item is typically available for bank industry. It's a part of long-lived assets, which has been decided for sale in the future.
    
    AssetsHeldForSaleBalanceSheet(store: IDictionary[str, Decimal])
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


class AssetsHeldForSaleCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Short term assets set apart for sale to liquidate in the future and are measured at the lower of carrying amount and fair value less
                costs to sell.
    
    AssetsHeldForSaleCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class AssetsHeldForSaleNonCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Long term assets set apart for sale to liquidate in the future and are measured at the lower of carrying amount and fair value less
                costs to sell.
    
    AssetsHeldForSaleNonCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class AssetsOfDiscontinuedOperationsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A portion of a company's business that has been disposed of or sold.
    
    AssetsOfDiscontinuedOperationsBalanceSheet(store: IDictionary[str, Decimal])
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


class AssetsPledgedasCollateralSubjecttoSaleorRepledgingTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total value collateral assets pledged to the bank that can be sold or used as collateral for other loans.
    
    AssetsPledgedasCollateralSubjecttoSaleorRepledgingTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class AssetsTurnover(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Revenue / Average Total Assets
    
    AssetsTurnover(store: IDictionary[str, Decimal])
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


class AvailableForSaleSecuritiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    For an unclassified balance sheet, this item represents equity securities categorized neither as held-to-maturity nor trading. Equity
                securities represent ownership interests or the right to acquire ownership interests in corporations and other legal entities which
                ownership interest is represented by shares of common or preferred stock (which is not mandatory redeemable or redeemable at
                the option of the holder), convertible securities, stock rights, or stock warrants. This category includes preferred stocks, available-
                for-sale and common stock, available-for-sale.
    
    AvailableForSaleSecuritiesBalanceSheet(store: IDictionary[str, Decimal])
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


class AverageDilutionEarningsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Adjustments to reported net income to calculate Diluted EPS, by assuming that all convertible instruments are converted to
                Common Equity. The adjustments usually include the interest expense of debentures when assumed converted and preferred
                dividends of convertible preferred stock when assumed converted.
    
    AverageDilutionEarningsIncomeStatement(store: IDictionary[str, Decimal])
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


class AVG5YrsROIC(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This is the simple average of the company's ROIC over the last 5 years. Return on invested capital is calculated by taking net
                operating profit after taxes and dividends and dividing by the total amount of capital invested and expressing the result as a
                percentage.
    
    AVG5YrsROIC(store: IDictionary[str, Decimal])
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


class BalanceSheet(System.object):
    """
    Definition of the BalanceSheet class
    
    BalanceSheet()
    """
    def UpdateValues(self, update: QuantConnect.Data.Fundamental.BalanceSheet) -> None:
        pass

    AccountsPayable: QuantConnect.Data.Fundamental.AccountsPayableBalanceSheet

    AccountsReceivable: QuantConnect.Data.Fundamental.AccountsReceivableBalanceSheet

    AccruedandDeferredIncome: QuantConnect.Data.Fundamental.AccruedandDeferredIncomeBalanceSheet

    AccruedandDeferredIncomeCurrent: QuantConnect.Data.Fundamental.AccruedandDeferredIncomeCurrentBalanceSheet

    AccruedandDeferredIncomeNonCurrent: QuantConnect.Data.Fundamental.AccruedandDeferredIncomeNonCurrentBalanceSheet

    AccruedInterestReceivable: QuantConnect.Data.Fundamental.AccruedInterestReceivableBalanceSheet

    AccruedInvestmentIncome: QuantConnect.Data.Fundamental.AccruedInvestmentIncomeBalanceSheet

    AccruedLiabilitiesTotal: QuantConnect.Data.Fundamental.AccruedLiabilitiesTotalBalanceSheet

    AccumulatedDepreciation: QuantConnect.Data.Fundamental.AccumulatedDepreciationBalanceSheet

    AdditionalPaidInCapital: QuantConnect.Data.Fundamental.AdditionalPaidInCapitalBalanceSheet

    AdvanceFromFederalHomeLoanBanks: QuantConnect.Data.Fundamental.AdvanceFromFederalHomeLoanBanksBalanceSheet

    AdvancesfromCentralBanks: QuantConnect.Data.Fundamental.AdvancesfromCentralBanksBalanceSheet

    AllowanceForDoubtfulAccountsReceivable: QuantConnect.Data.Fundamental.AllowanceForDoubtfulAccountsReceivableBalanceSheet

    AllowanceForLoansAndLeaseLosses: QuantConnect.Data.Fundamental.AllowanceForLoansAndLeaseLossesBalanceSheet

    AllowanceForNotesReceivable: QuantConnect.Data.Fundamental.AllowanceForNotesReceivableBalanceSheet

    AssetsHeldForSale: QuantConnect.Data.Fundamental.AssetsHeldForSaleBalanceSheet

    AssetsHeldForSaleCurrent: QuantConnect.Data.Fundamental.AssetsHeldForSaleCurrentBalanceSheet

    AssetsHeldForSaleNonCurrent: QuantConnect.Data.Fundamental.AssetsHeldForSaleNonCurrentBalanceSheet

    AssetsOfDiscontinuedOperations: QuantConnect.Data.Fundamental.AssetsOfDiscontinuedOperationsBalanceSheet

    AssetsPledgedasCollateralSubjecttoSaleorRepledgingTotal: QuantConnect.Data.Fundamental.AssetsPledgedasCollateralSubjecttoSaleorRepledgingTotalBalanceSheet

    AvailableForSaleSecurities: QuantConnect.Data.Fundamental.AvailableForSaleSecuritiesBalanceSheet

    BankIndebtedness: QuantConnect.Data.Fundamental.BankIndebtednessBalanceSheet

    BankLoansCurrent: QuantConnect.Data.Fundamental.BankLoansCurrentBalanceSheet

    BankLoansNonCurrent: QuantConnect.Data.Fundamental.BankLoansNonCurrentBalanceSheet

    BankLoansTotal: QuantConnect.Data.Fundamental.BankLoansTotalBalanceSheet

    BankOwnedLifeInsurance: QuantConnect.Data.Fundamental.BankOwnedLifeInsuranceBalanceSheet

    BiologicalAssets: QuantConnect.Data.Fundamental.BiologicalAssetsBalanceSheet

    BSFileDate: datetime.datetime

    BuildingsAndImprovements: QuantConnect.Data.Fundamental.BuildingsAndImprovementsBalanceSheet

    CapitalLeaseObligations: QuantConnect.Data.Fundamental.CapitalLeaseObligationsBalanceSheet

    CapitalStock: QuantConnect.Data.Fundamental.CapitalStockBalanceSheet

    Cash: QuantConnect.Data.Fundamental.CashBalanceSheet

    CashAndCashEquivalents: QuantConnect.Data.Fundamental.CashAndCashEquivalentsBalanceSheet

    CashAndDueFromBanks: QuantConnect.Data.Fundamental.CashAndDueFromBanksBalanceSheet

    CashCashEquivalentsAndFederalFundsSold: QuantConnect.Data.Fundamental.CashCashEquivalentsAndFederalFundsSoldBalanceSheet

    CashCashEquivalentsAndMarketableSecurities: QuantConnect.Data.Fundamental.CashCashEquivalentsAndMarketableSecuritiesBalanceSheet

    CashEquivalents: QuantConnect.Data.Fundamental.CashEquivalentsBalanceSheet

    CashRestrictedOrPledged: QuantConnect.Data.Fundamental.CashRestrictedOrPledgedBalanceSheet

    ClaimsOutstanding: QuantConnect.Data.Fundamental.ClaimsOutstandingBalanceSheet

    CommercialLoan: QuantConnect.Data.Fundamental.CommercialLoanBalanceSheet

    CommercialPaper: QuantConnect.Data.Fundamental.CommercialPaperBalanceSheet

    CommonStock: QuantConnect.Data.Fundamental.CommonStockBalanceSheet

    CommonStockEquity: QuantConnect.Data.Fundamental.CommonStockEquityBalanceSheet

    CommonUtilityPlant: QuantConnect.Data.Fundamental.CommonUtilityPlantBalanceSheet

    ComTreShaNum: QuantConnect.Data.Fundamental.ComTreShaNumBalanceSheet

    ConstructionInProgress: QuantConnect.Data.Fundamental.ConstructionInProgressBalanceSheet

    ConsumerLoan: QuantConnect.Data.Fundamental.ConsumerLoanBalanceSheet

    ConvertibleLoansCurrent: QuantConnect.Data.Fundamental.ConvertibleLoansCurrentBalanceSheet

    ConvertibleLoansNonCurrent: QuantConnect.Data.Fundamental.ConvertibleLoansNonCurrentBalanceSheet

    ConvertibleLoansTotal: QuantConnect.Data.Fundamental.ConvertibleLoansTotalBalanceSheet

    CurrentAccruedExpenses: QuantConnect.Data.Fundamental.CurrentAccruedExpensesBalanceSheet

    CurrentAssets: QuantConnect.Data.Fundamental.CurrentAssetsBalanceSheet

    CurrentCapitalLeaseObligation: QuantConnect.Data.Fundamental.CurrentCapitalLeaseObligationBalanceSheet

    CurrentDebt: QuantConnect.Data.Fundamental.CurrentDebtBalanceSheet

    CurrentDebtAndCapitalLeaseObligation: QuantConnect.Data.Fundamental.CurrentDebtAndCapitalLeaseObligationBalanceSheet

    CurrentDeferredAssets: QuantConnect.Data.Fundamental.CurrentDeferredAssetsBalanceSheet

    CurrentDeferredLiabilities: QuantConnect.Data.Fundamental.CurrentDeferredLiabilitiesBalanceSheet

    CurrentDeferredRevenue: QuantConnect.Data.Fundamental.CurrentDeferredRevenueBalanceSheet

    CurrentDeferredTaxesAssets: QuantConnect.Data.Fundamental.CurrentDeferredTaxesAssetsBalanceSheet

    CurrentDeferredTaxesLiabilities: QuantConnect.Data.Fundamental.CurrentDeferredTaxesLiabilitiesBalanceSheet

    CurrentLiabilities: QuantConnect.Data.Fundamental.CurrentLiabilitiesBalanceSheet

    CurrentNotesPayable: QuantConnect.Data.Fundamental.CurrentNotesPayableBalanceSheet

    CurrentOtherFinancialLiabilities: QuantConnect.Data.Fundamental.CurrentOtherFinancialLiabilitiesBalanceSheet

    CurrentProvisions: QuantConnect.Data.Fundamental.CurrentProvisionsBalanceSheet

    CustomerAcceptances: QuantConnect.Data.Fundamental.CustomerAcceptancesBalanceSheet

    CustomerAccounts: QuantConnect.Data.Fundamental.CustomerAccountsBalanceSheet

    DebtDueBeyond: QuantConnect.Data.Fundamental.DebtDueBeyondBalanceSheet

    DebtDueInYear1: QuantConnect.Data.Fundamental.DebtDueInYear1BalanceSheet

    DebtDueInYear2: QuantConnect.Data.Fundamental.DebtDueInYear2BalanceSheet

    DebtDueInYear5: QuantConnect.Data.Fundamental.DebtDueInYear5BalanceSheet

    DebtSecurities: QuantConnect.Data.Fundamental.DebtSecuritiesBalanceSheet

    DebtSecuritiesinIssue: QuantConnect.Data.Fundamental.DebtSecuritiesinIssueBalanceSheet

    DebtTotal: QuantConnect.Data.Fundamental.DebtTotalBalanceSheet

    DeferredAssets: QuantConnect.Data.Fundamental.DeferredAssetsBalanceSheet

    DeferredCosts: QuantConnect.Data.Fundamental.DeferredCostsBalanceSheet

    DeferredIncomeTotal: QuantConnect.Data.Fundamental.DeferredIncomeTotalBalanceSheet

    DeferredPolicyAcquisitionCosts: QuantConnect.Data.Fundamental.DeferredPolicyAcquisitionCostsBalanceSheet

    DeferredTaxAssets: QuantConnect.Data.Fundamental.DeferredTaxAssetsBalanceSheet

    DeferredTaxLiabilitiesTotal: QuantConnect.Data.Fundamental.DeferredTaxLiabilitiesTotalBalanceSheet

    DefinedPensionBenefit: QuantConnect.Data.Fundamental.DefinedPensionBenefitBalanceSheet

    DepositCertificates: QuantConnect.Data.Fundamental.DepositCertificatesBalanceSheet

    DepositsbyBank: QuantConnect.Data.Fundamental.DepositsbyBankBalanceSheet

    DepositsMadeunderAssumedReinsuranceContract: QuantConnect.Data.Fundamental.DepositsMadeunderAssumedReinsuranceContractBalanceSheet

    DepositsReceivedunderCededInsuranceContract: QuantConnect.Data.Fundamental.DepositsReceivedunderCededInsuranceContractBalanceSheet

    DerivativeAssets: QuantConnect.Data.Fundamental.DerivativeAssetsBalanceSheet

    DerivativeProductLiabilities: QuantConnect.Data.Fundamental.DerivativeProductLiabilitiesBalanceSheet

    DividendsPayable: QuantConnect.Data.Fundamental.DividendsPayableBalanceSheet

    DueFromRelatedParties: QuantConnect.Data.Fundamental.DueFromRelatedPartiesBalanceSheet

    DuefromRelatedPartiesCurrent: QuantConnect.Data.Fundamental.DuefromRelatedPartiesCurrentBalanceSheet

    DuefromRelatedPartiesNonCurrent: QuantConnect.Data.Fundamental.DuefromRelatedPartiesNonCurrentBalanceSheet

    DuetoRelatedParties: QuantConnect.Data.Fundamental.DuetoRelatedPartiesBalanceSheet

    DuetoRelatedPartiesCurrent: QuantConnect.Data.Fundamental.DuetoRelatedPartiesCurrentBalanceSheet

    DuetoRelatedPartiesNonCurrent: QuantConnect.Data.Fundamental.DuetoRelatedPartiesNonCurrentBalanceSheet

    ElectricUtilityPlant: QuantConnect.Data.Fundamental.ElectricUtilityPlantBalanceSheet

    EmployeeBenefits: QuantConnect.Data.Fundamental.EmployeeBenefitsBalanceSheet

    EquityAttributableToOwnersOfParent: QuantConnect.Data.Fundamental.EquityAttributableToOwnersOfParentBalanceSheet

    EquityInvestments: QuantConnect.Data.Fundamental.EquityInvestmentsBalanceSheet

    EquitySharesInvestments: QuantConnect.Data.Fundamental.EquitySharesInvestmentsBalanceSheet

    FederalFundsPurchased: QuantConnect.Data.Fundamental.FederalFundsPurchasedBalanceSheet

    FederalFundsPurchasedAndSecuritiesSoldUnderAgreementToRepurchase: QuantConnect.Data.Fundamental.FederalFundsPurchasedAndSecuritiesSoldUnderAgreementToRepurchaseBalanceSheet

    FederalFundsSold: QuantConnect.Data.Fundamental.FederalFundsSoldBalanceSheet

    FederalFundsSoldAndSecuritiesPurchaseUnderAgreementsToResell: QuantConnect.Data.Fundamental.FederalFundsSoldAndSecuritiesPurchaseUnderAgreementsToResellBalanceSheet

    FederalHomeLoanBankStock: QuantConnect.Data.Fundamental.FederalHomeLoanBankStockBalanceSheet

    FinanceLeaseReceivables: QuantConnect.Data.Fundamental.FinanceLeaseReceivablesBalanceSheet

    FinanceLeaseReceivablesCurrent: QuantConnect.Data.Fundamental.FinanceLeaseReceivablesCurrentBalanceSheet

    FinanceLeaseReceivablesNonCurrent: QuantConnect.Data.Fundamental.FinanceLeaseReceivablesNonCurrentBalanceSheet

    FinancialAssets: QuantConnect.Data.Fundamental.FinancialAssetsBalanceSheet

    FinancialAssetsDesignatedasFairValueThroughProfitorLossTotal: QuantConnect.Data.Fundamental.FinancialAssetsDesignatedasFairValueThroughProfitorLossTotalBalanceSheet

    FinancialInstrumentsSoldUnderAgreementsToRepurchase: QuantConnect.Data.Fundamental.FinancialInstrumentsSoldUnderAgreementsToRepurchaseBalanceSheet

    FinancialLiabilitiesCurrent: QuantConnect.Data.Fundamental.FinancialLiabilitiesCurrentBalanceSheet

    FinancialLiabilitiesDesignatedasFairValueThroughProfitorLossTotal: QuantConnect.Data.Fundamental.FinancialLiabilitiesDesignatedasFairValueThroughProfitorLossTotalBalanceSheet

    FinancialLiabilitiesMeasuredatAmortizedCostTotal: QuantConnect.Data.Fundamental.FinancialLiabilitiesMeasuredatAmortizedCostTotalBalanceSheet

    FinancialLiabilitiesNonCurrent: QuantConnect.Data.Fundamental.FinancialLiabilitiesNonCurrentBalanceSheet

    FinancialOrDerivativeInvestmentCurrentLiabilities: QuantConnect.Data.Fundamental.FinancialOrDerivativeInvestmentCurrentLiabilitiesBalanceSheet

    FinishedGoods: QuantConnect.Data.Fundamental.FinishedGoodsBalanceSheet

    FixedAssetsRevaluationReserve: QuantConnect.Data.Fundamental.FixedAssetsRevaluationReserveBalanceSheet

    FixedMaturityInvestments: QuantConnect.Data.Fundamental.FixedMaturityInvestmentsBalanceSheet

    FlightFleetVehicleAndRelatedEquipments: QuantConnect.Data.Fundamental.FlightFleetVehicleAndRelatedEquipmentsBalanceSheet

    ForeclosedAssets: QuantConnect.Data.Fundamental.ForeclosedAssetsBalanceSheet

    ForeignCurrencyTranslationAdjustments: QuantConnect.Data.Fundamental.ForeignCurrencyTranslationAdjustmentsBalanceSheet

    FuturePolicyBenefits: QuantConnect.Data.Fundamental.FuturePolicyBenefitsBalanceSheet

    GainsLossesNotAffectingRetainedEarnings: QuantConnect.Data.Fundamental.GainsLossesNotAffectingRetainedEarningsBalanceSheet

    GeneralPartnershipCapital: QuantConnect.Data.Fundamental.GeneralPartnershipCapitalBalanceSheet

    Goodwill: QuantConnect.Data.Fundamental.GoodwillBalanceSheet

    GoodwillAndOtherIntangibleAssets: QuantConnect.Data.Fundamental.GoodwillAndOtherIntangibleAssetsBalanceSheet

    GrossAccountsReceivable: QuantConnect.Data.Fundamental.GrossAccountsReceivableBalanceSheet

    GrossLoan: QuantConnect.Data.Fundamental.GrossLoanBalanceSheet

    GrossNotesReceivable: QuantConnect.Data.Fundamental.GrossNotesReceivableBalanceSheet

    GrossPPE: QuantConnect.Data.Fundamental.GrossPPEBalanceSheet

    HedgingAssetsCurrent: QuantConnect.Data.Fundamental.HedgingAssetsCurrentBalanceSheet

    HeldToMaturitySecurities: QuantConnect.Data.Fundamental.HeldToMaturitySecuritiesBalanceSheet

    IncomeTaxPayable: QuantConnect.Data.Fundamental.IncomeTaxPayableBalanceSheet

    InsuranceContractAssets: QuantConnect.Data.Fundamental.InsuranceContractAssetsBalanceSheet

    InsuranceContractLiabilities: QuantConnect.Data.Fundamental.InsuranceContractLiabilitiesBalanceSheet

    InsuranceFundsNonCurrent: QuantConnect.Data.Fundamental.InsuranceFundsNonCurrentBalanceSheet

    InterestBearingBorrowingsNonCurrent: QuantConnect.Data.Fundamental.InterestBearingBorrowingsNonCurrentBalanceSheet

    InterestBearingDepositsAssets: QuantConnect.Data.Fundamental.InterestBearingDepositsAssetsBalanceSheet

    InterestBearingDepositsLiabilities: QuantConnect.Data.Fundamental.InterestBearingDepositsLiabilitiesBalanceSheet

    InterestPayable: QuantConnect.Data.Fundamental.InterestPayableBalanceSheet

    InventoriesAdjustmentsAllowances: QuantConnect.Data.Fundamental.InventoriesAdjustmentsAllowancesBalanceSheet

    Inventory: QuantConnect.Data.Fundamental.InventoryBalanceSheet

    InvestedCapital: QuantConnect.Data.Fundamental.InvestedCapitalBalanceSheet

    InvestmentContractLiabilities: QuantConnect.Data.Fundamental.InvestmentContractLiabilitiesBalanceSheet

    InvestmentinFinancialAssets: QuantConnect.Data.Fundamental.InvestmentinFinancialAssetsBalanceSheet

    InvestmentProperties: QuantConnect.Data.Fundamental.InvestmentPropertiesBalanceSheet

    InvestmentsAndAdvances: QuantConnect.Data.Fundamental.InvestmentsAndAdvancesBalanceSheet

    InvestmentsinAssociatesatCost: QuantConnect.Data.Fundamental.InvestmentsinAssociatesatCostBalanceSheet

    InvestmentsinJointVenturesatCost: QuantConnect.Data.Fundamental.InvestmentsinJointVenturesatCostBalanceSheet

    InvestmentsInOtherVenturesUnderEquityMethod: QuantConnect.Data.Fundamental.InvestmentsInOtherVenturesUnderEquityMethodBalanceSheet

    InvestmentsinSubsidiariesatCost: QuantConnect.Data.Fundamental.InvestmentsinSubsidiariesatCostBalanceSheet

    ItemsinTheCourseofTransmissiontoOtherBanks: QuantConnect.Data.Fundamental.ItemsinTheCourseofTransmissiontoOtherBanksBalanceSheet

    LandAndImprovements: QuantConnect.Data.Fundamental.LandAndImprovementsBalanceSheet

    Leases: QuantConnect.Data.Fundamental.LeasesBalanceSheet

    LiabilitiesHeldforSaleCurrent: QuantConnect.Data.Fundamental.LiabilitiesHeldforSaleCurrentBalanceSheet

    LiabilitiesHeldforSaleNonCurrent: QuantConnect.Data.Fundamental.LiabilitiesHeldforSaleNonCurrentBalanceSheet

    LiabilitiesHeldforSaleTotal: QuantConnect.Data.Fundamental.LiabilitiesHeldforSaleTotalBalanceSheet

    LiabilitiesOfDiscontinuedOperations: QuantConnect.Data.Fundamental.LiabilitiesOfDiscontinuedOperationsBalanceSheet

    LimitedPartnershipCapital: QuantConnect.Data.Fundamental.LimitedPartnershipCapitalBalanceSheet

    LineOfCredit: QuantConnect.Data.Fundamental.LineOfCreditBalanceSheet

    LoansandAdvancestoBank: QuantConnect.Data.Fundamental.LoansandAdvancestoBankBalanceSheet

    LoansandAdvancestoCustomer: QuantConnect.Data.Fundamental.LoansandAdvancestoCustomerBalanceSheet

    LoansHeldForSale: QuantConnect.Data.Fundamental.LoansHeldForSaleBalanceSheet

    LoansReceivable: QuantConnect.Data.Fundamental.LoansReceivableBalanceSheet

    LongTermCapitalLeaseObligation: QuantConnect.Data.Fundamental.LongTermCapitalLeaseObligationBalanceSheet

    LongTermDebt: QuantConnect.Data.Fundamental.LongTermDebtBalanceSheet

    LongTermDebtAndCapitalLeaseObligation: QuantConnect.Data.Fundamental.LongTermDebtAndCapitalLeaseObligationBalanceSheet

    LongTermInvestments: QuantConnect.Data.Fundamental.LongTermInvestmentsBalanceSheet

    LongTermProvisions: QuantConnect.Data.Fundamental.LongTermProvisionsBalanceSheet

    MachineryFurnitureEquipment: QuantConnect.Data.Fundamental.MachineryFurnitureEquipmentBalanceSheet

    MaterialsAndSupplies: QuantConnect.Data.Fundamental.MaterialsAndSuppliesBalanceSheet

    MineralProperties: QuantConnect.Data.Fundamental.MineralPropertiesBalanceSheet

    MinimumPensionLiabilities: QuantConnect.Data.Fundamental.MinimumPensionLiabilitiesBalanceSheet

    MinorityInterest: QuantConnect.Data.Fundamental.MinorityInterestBalanceSheet

    MoneyMarketInvestments: QuantConnect.Data.Fundamental.MoneyMarketInvestmentsBalanceSheet

    MortgageAndConsumerloans: QuantConnect.Data.Fundamental.MortgageAndConsumerloansBalanceSheet

    MortgageLoan: QuantConnect.Data.Fundamental.MortgageLoanBalanceSheet

    NaturalGasFuelAndOther: QuantConnect.Data.Fundamental.NaturalGasFuelAndOtherBalanceSheet

    NetDebt: QuantConnect.Data.Fundamental.NetDebtBalanceSheet

    NetLoan: QuantConnect.Data.Fundamental.NetLoanBalanceSheet

    NetPPE: QuantConnect.Data.Fundamental.NetPPEBalanceSheet

    NetTangibleAssets: QuantConnect.Data.Fundamental.NetTangibleAssetsBalanceSheet

    NetUtilityPlant: QuantConnect.Data.Fundamental.NetUtilityPlantBalanceSheet

    NonCurrentAccountsReceivable: QuantConnect.Data.Fundamental.NonCurrentAccountsReceivableBalanceSheet

    NonCurrentAccruedExpenses: QuantConnect.Data.Fundamental.NonCurrentAccruedExpensesBalanceSheet

    NonCurrentDeferredAssets: QuantConnect.Data.Fundamental.NonCurrentDeferredAssetsBalanceSheet

    NonCurrentDeferredLiabilities: QuantConnect.Data.Fundamental.NonCurrentDeferredLiabilitiesBalanceSheet

    NonCurrentDeferredRevenue: QuantConnect.Data.Fundamental.NonCurrentDeferredRevenueBalanceSheet

    NonCurrentDeferredTaxesAssets: QuantConnect.Data.Fundamental.NonCurrentDeferredTaxesAssetsBalanceSheet

    NonCurrentDeferredTaxesLiabilities: QuantConnect.Data.Fundamental.NonCurrentDeferredTaxesLiabilitiesBalanceSheet

    NonCurrentNoteReceivables: QuantConnect.Data.Fundamental.NonCurrentNoteReceivablesBalanceSheet

    NonCurrentOtherFinancialLiabilities: QuantConnect.Data.Fundamental.NonCurrentOtherFinancialLiabilitiesBalanceSheet

    NonCurrentPensionAndOtherPostretirementBenefitPlans: QuantConnect.Data.Fundamental.NonCurrentPensionAndOtherPostretirementBenefitPlansBalanceSheet

    NonCurrentPrepaidAssets: QuantConnect.Data.Fundamental.NonCurrentPrepaidAssetsBalanceSheet

    NonInterestBearingBorrowingsCurrent: QuantConnect.Data.Fundamental.NonInterestBearingBorrowingsCurrentBalanceSheet

    NonInterestBearingBorrowingsNonCurrent: QuantConnect.Data.Fundamental.NonInterestBearingBorrowingsNonCurrentBalanceSheet

    NonInterestBearingBorrowingsTotal: QuantConnect.Data.Fundamental.NonInterestBearingBorrowingsTotalBalanceSheet

    NonInterestBearingDeposits: QuantConnect.Data.Fundamental.NonInterestBearingDepositsBalanceSheet

    NotesReceivable: QuantConnect.Data.Fundamental.NotesReceivableBalanceSheet

    OperatingLeaseAssets: QuantConnect.Data.Fundamental.OperatingLeaseAssetsBalanceSheet

    OrdinarySharesNumber: QuantConnect.Data.Fundamental.OrdinarySharesNumberBalanceSheet

    OtherAssets: QuantConnect.Data.Fundamental.OtherAssetsBalanceSheet

    OtherBorrowedFunds: QuantConnect.Data.Fundamental.OtherBorrowedFundsBalanceSheet

    OtherCapitalStock: QuantConnect.Data.Fundamental.OtherCapitalStockBalanceSheet

    OtherCurrentAssets: QuantConnect.Data.Fundamental.OtherCurrentAssetsBalanceSheet

    OtherCurrentBorrowings: QuantConnect.Data.Fundamental.OtherCurrentBorrowingsBalanceSheet

    OtherCurrentLiabilities: QuantConnect.Data.Fundamental.OtherCurrentLiabilitiesBalanceSheet

    OtherEquityAdjustments: QuantConnect.Data.Fundamental.OtherEquityAdjustmentsBalanceSheet

    OtherEquityInterest: QuantConnect.Data.Fundamental.OtherEquityInterestBalanceSheet

    OtherFinancialLiabilities: QuantConnect.Data.Fundamental.OtherFinancialLiabilitiesBalanceSheet

    OtherIntangibleAssets: QuantConnect.Data.Fundamental.OtherIntangibleAssetsBalanceSheet

    OtherInventories: QuantConnect.Data.Fundamental.OtherInventoriesBalanceSheet

    OtherInvestedAssets: QuantConnect.Data.Fundamental.OtherInvestedAssetsBalanceSheet

    OtherInvestments: QuantConnect.Data.Fundamental.OtherInvestmentsBalanceSheet

    OtherLiabilities: QuantConnect.Data.Fundamental.OtherLiabilitiesBalanceSheet

    OtherLoanAssets: QuantConnect.Data.Fundamental.OtherLoanAssetsBalanceSheet

    OtherLoansCurrent: QuantConnect.Data.Fundamental.OtherLoansCurrentBalanceSheet

    OtherLoansNonCurrent: QuantConnect.Data.Fundamental.OtherLoansNonCurrentBalanceSheet

    OtherLoansTotal: QuantConnect.Data.Fundamental.OtherLoansTotalBalanceSheet

    OtherNonCurrentAssets: QuantConnect.Data.Fundamental.OtherNonCurrentAssetsBalanceSheet

    OtherNonCurrentLiabilities: QuantConnect.Data.Fundamental.OtherNonCurrentLiabilitiesBalanceSheet

    OtherPayable: QuantConnect.Data.Fundamental.OtherPayableBalanceSheet

    OtherProperties: QuantConnect.Data.Fundamental.OtherPropertiesBalanceSheet

    OtherRealEstateOwned: QuantConnect.Data.Fundamental.OtherRealEstateOwnedBalanceSheet

    OtherReceivables: QuantConnect.Data.Fundamental.OtherReceivablesBalanceSheet

    OtherReserves: QuantConnect.Data.Fundamental.OtherReservesBalanceSheet

    OtherShortTermInvestments: QuantConnect.Data.Fundamental.OtherShortTermInvestmentsBalanceSheet

    Payables: QuantConnect.Data.Fundamental.PayablesBalanceSheet

    PayablesAndAccruedExpenses: QuantConnect.Data.Fundamental.PayablesAndAccruedExpensesBalanceSheet

    PensionandOtherPostRetirementBenefitPlansCurrent: QuantConnect.Data.Fundamental.PensionandOtherPostRetirementBenefitPlansCurrentBalanceSheet

    PensionAndOtherPostretirementBenefitPlansTotal: QuantConnect.Data.Fundamental.PensionAndOtherPostretirementBenefitPlansTotalBalanceSheet

    PolicyholderFunds: QuantConnect.Data.Fundamental.PolicyholderFundsBalanceSheet

    PolicyLoans: QuantConnect.Data.Fundamental.PolicyLoansBalanceSheet

    PolicyReservesBenefits: QuantConnect.Data.Fundamental.PolicyReservesBenefitsBalanceSheet

    PreferredSecuritiesOutsideStockEquity: QuantConnect.Data.Fundamental.PreferredSecuritiesOutsideStockEquityBalanceSheet

    PreferredSharesNumber: QuantConnect.Data.Fundamental.PreferredSharesNumberBalanceSheet

    PreferredStock: QuantConnect.Data.Fundamental.PreferredStockBalanceSheet

    PreferredStockEquity: QuantConnect.Data.Fundamental.PreferredStockEquityBalanceSheet

    PrepaidAssets: QuantConnect.Data.Fundamental.PrepaidAssetsBalanceSheet

    PreTreShaNum: QuantConnect.Data.Fundamental.PreTreShaNumBalanceSheet

    Properties: QuantConnect.Data.Fundamental.PropertiesBalanceSheet

    ProvisionsTotal: QuantConnect.Data.Fundamental.ProvisionsTotalBalanceSheet

    RawMaterials: QuantConnect.Data.Fundamental.RawMaterialsBalanceSheet

    Receivables: QuantConnect.Data.Fundamental.ReceivablesBalanceSheet

    ReceivablesAdjustmentsAllowances: QuantConnect.Data.Fundamental.ReceivablesAdjustmentsAllowancesBalanceSheet

    RegulatoryAssets: QuantConnect.Data.Fundamental.RegulatoryAssetsBalanceSheet

    RegulatoryLiabilities: QuantConnect.Data.Fundamental.RegulatoryLiabilitiesBalanceSheet

    ReinsuranceAssets: QuantConnect.Data.Fundamental.ReinsuranceAssetsBalanceSheet

    ReinsuranceBalancesPayable: QuantConnect.Data.Fundamental.ReinsuranceBalancesPayableBalanceSheet

    ReinsuranceRecoverable: QuantConnect.Data.Fundamental.ReinsuranceRecoverableBalanceSheet

    RestrictedCash: QuantConnect.Data.Fundamental.RestrictedCashBalanceSheet

    RestrictedCashAndCashEquivalents: QuantConnect.Data.Fundamental.RestrictedCashAndCashEquivalentsBalanceSheet

    RestrictedCashAndInvestments: QuantConnect.Data.Fundamental.RestrictedCashAndInvestmentsBalanceSheet

    RestrictedCommonStock: QuantConnect.Data.Fundamental.RestrictedCommonStockBalanceSheet

    RestrictedInvestments: QuantConnect.Data.Fundamental.RestrictedInvestmentsBalanceSheet

    RetainedEarnings: QuantConnect.Data.Fundamental.RetainedEarningsBalanceSheet

    SecuritiesAndInvestments: QuantConnect.Data.Fundamental.SecuritiesAndInvestmentsBalanceSheet

    SecuritiesLendingCollateral: QuantConnect.Data.Fundamental.SecuritiesLendingCollateralBalanceSheet

    SecuritiesLoaned: QuantConnect.Data.Fundamental.SecuritiesLoanedBalanceSheet

    SecurityAgreeToBeResell: QuantConnect.Data.Fundamental.SecurityAgreeToBeResellBalanceSheet

    SecurityBorrowed: QuantConnect.Data.Fundamental.SecurityBorrowedBalanceSheet

    SecuritySoldNotYetRepurchased: QuantConnect.Data.Fundamental.SecuritySoldNotYetRepurchasedBalanceSheet

    SeparateAccountAssets: QuantConnect.Data.Fundamental.SeparateAccountAssetsBalanceSheet

    SeparateAccountBusiness: QuantConnect.Data.Fundamental.SeparateAccountBusinessBalanceSheet

    ShareIssued: QuantConnect.Data.Fundamental.ShareIssuedBalanceSheet

    ShortTermInvestmentsAvailableForSale: QuantConnect.Data.Fundamental.ShortTermInvestmentsAvailableForSaleBalanceSheet

    ShortTermInvestmentsHeldToMaturity: QuantConnect.Data.Fundamental.ShortTermInvestmentsHeldToMaturityBalanceSheet

    ShortTermInvestmentsTrading: QuantConnect.Data.Fundamental.ShortTermInvestmentsTradingBalanceSheet

    StockholdersEquity: QuantConnect.Data.Fundamental.StockholdersEquityBalanceSheet

    SubordinatedLiabilities: QuantConnect.Data.Fundamental.SubordinatedLiabilitiesBalanceSheet

    TangibleBookValue: QuantConnect.Data.Fundamental.TangibleBookValueBalanceSheet

    TaxAssetsTotal: QuantConnect.Data.Fundamental.TaxAssetsTotalBalanceSheet

    TaxesAssetsCurrent: QuantConnect.Data.Fundamental.TaxesAssetsCurrentBalanceSheet

    TaxesReceivable: QuantConnect.Data.Fundamental.TaxesReceivableBalanceSheet

    TotalAssets: QuantConnect.Data.Fundamental.TotalAssetsBalanceSheet

    TotalCapitalization: QuantConnect.Data.Fundamental.TotalCapitalizationBalanceSheet

    TotalDebt: QuantConnect.Data.Fundamental.TotalDebtBalanceSheet

    TotalDebtInMaturitySchedule: QuantConnect.Data.Fundamental.TotalDebtInMaturityScheduleBalanceSheet

    TotalDeferredCreditsAndOtherNonCurrentLiabilities: QuantConnect.Data.Fundamental.TotalDeferredCreditsAndOtherNonCurrentLiabilitiesBalanceSheet

    TotalDeposits: QuantConnect.Data.Fundamental.TotalDepositsBalanceSheet

    TotalEquity: QuantConnect.Data.Fundamental.TotalEquityBalanceSheet

    TotalEquityAsReported: QuantConnect.Data.Fundamental.TotalEquityAsReportedBalanceSheet

    TotalEquityGrossMinorityInterest: QuantConnect.Data.Fundamental.TotalEquityGrossMinorityInterestBalanceSheet

    TotalFinancialLeaseObligations: QuantConnect.Data.Fundamental.TotalFinancialLeaseObligationsBalanceSheet

    TotalInvestments: QuantConnect.Data.Fundamental.TotalInvestmentsBalanceSheet

    TotalLiabilitiesAsReported: QuantConnect.Data.Fundamental.TotalLiabilitiesAsReportedBalanceSheet

    TotalLiabilitiesNetMinorityInterest: QuantConnect.Data.Fundamental.TotalLiabilitiesNetMinorityInterestBalanceSheet

    TotalNonCurrentAssets: QuantConnect.Data.Fundamental.TotalNonCurrentAssetsBalanceSheet

    TotalNonCurrentLiabilitiesNetMinorityInterest: QuantConnect.Data.Fundamental.TotalNonCurrentLiabilitiesNetMinorityInterestBalanceSheet

    TotalPartnershipCapital: QuantConnect.Data.Fundamental.TotalPartnershipCapitalBalanceSheet

    TotalTaxPayable: QuantConnect.Data.Fundamental.TotalTaxPayableBalanceSheet

    TradeandOtherPayablesNonCurrent: QuantConnect.Data.Fundamental.TradeandOtherPayablesNonCurrentBalanceSheet

    TradeAndOtherReceivablesNonCurrent: QuantConnect.Data.Fundamental.TradeAndOtherReceivablesNonCurrentBalanceSheet

    TradingandFinancialLiabilities: QuantConnect.Data.Fundamental.TradingandFinancialLiabilitiesBalanceSheet

    TradingAndOtherReceivable: QuantConnect.Data.Fundamental.TradingAndOtherReceivableBalanceSheet

    TradingAssets: QuantConnect.Data.Fundamental.TradingAssetsBalanceSheet

    TradingLiabilities: QuantConnect.Data.Fundamental.TradingLiabilitiesBalanceSheet

    TradingSecurities: QuantConnect.Data.Fundamental.TradingSecuritiesBalanceSheet

    TreasuryBillsandOtherEligibleBills: QuantConnect.Data.Fundamental.TreasuryBillsandOtherEligibleBillsBalanceSheet

    TreasurySharesNumber: QuantConnect.Data.Fundamental.TreasurySharesNumberBalanceSheet

    TreasuryStock: QuantConnect.Data.Fundamental.TreasuryStockBalanceSheet

    UnallocatedSurplus: QuantConnect.Data.Fundamental.UnallocatedSurplusBalanceSheet

    UnbilledReceivables: QuantConnect.Data.Fundamental.UnbilledReceivablesBalanceSheet

    UnearnedIncome: QuantConnect.Data.Fundamental.UnearnedIncomeBalanceSheet

    UnearnedPremiums: QuantConnect.Data.Fundamental.UnearnedPremiumsBalanceSheet

    UnpaidLossAndLossReserve: QuantConnect.Data.Fundamental.UnpaidLossAndLossReserveBalanceSheet

    UnrealizedGainLoss: QuantConnect.Data.Fundamental.UnrealizedGainLossBalanceSheet

    WaterProduction: QuantConnect.Data.Fundamental.WaterProductionBalanceSheet

    WorkingCapital: QuantConnect.Data.Fundamental.WorkingCapitalBalanceSheet

    WorkInProcess: QuantConnect.Data.Fundamental.WorkInProcessBalanceSheet



class BankIndebtednessBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    All indebtedness for borrowed money or the deferred purchase price of property or services, including without limitation
                reimbursement and other obligations with respect to surety bonds and letters of credit, all obligations evidenced by notes, bonds
                debentures or similar instruments, all capital lease obligations and all contingent obligations.
    
    BankIndebtednessBalanceSheet(store: IDictionary[str, Decimal])
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


class BankLoansCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A debt financing obligation issued by a bank or similar financial institution to a company, that entitles the lender or holder of the
                instrument to interest payments and the repayment of principal at a specified time within the next 12 months or operating cycle.
    
    BankLoansCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class BankLoansNonCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A debt financing obligation issued by a bank or similar financial institution to a company, that entitles the lender or holder of the
                instrument to interest payments and the repayment of principal at a specified time beyond the current accounting PeriodAsByte.
    
    BankLoansNonCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class BankLoansTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total debt financing obligation issued by a bank or similar financial institution to a company that entitles the lender or holder of the
                instrument to interest payments and the repayment of principal at a specified time; in a Non-Differentiated Balance Sheet.
    
    BankLoansTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class BankOwnedLifeInsuranceBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The carrying amount of a life insurance policy on an officer, executive or employee for which the reporting entity (a bank) is entitled
                to proceeds from the policy upon death of the insured or surrender of the insurance policy.
    
    BankOwnedLifeInsuranceBalanceSheet(store: IDictionary[str, Decimal])
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


class BasicAccountingChange(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Basic EPS from the Cumulative Effect of Accounting Change is the earnings attributable to the accounting change (during the
                reporting period) divided by the weighted average number of common shares outstanding.
    
    BasicAccountingChange(store: IDictionary[str, Decimal])
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


class BasicAverageShares(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The shares outstanding used to calculate Basic EPS, which is the weighted average common share outstanding through the whole
                accounting PeriodAsByte.  Note: If Basic Average Shares are not presented by the firm in the Income Statement, this data point will be
                null.
    
    BasicAverageShares(store: IDictionary[str, Decimal])
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


class BasicContinuousOperations(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Basic EPS from Continuing Operations is the earnings from continuing operations reported by the company divided by the weighted
                average number of common shares outstanding.
    
    BasicContinuousOperations(store: IDictionary[str, Decimal])
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


class BasicDiscontinuousOperations(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Basic EPS from Discontinued Operations is the earnings from discontinued operations reported by the company divided by the
                weighted average number of common shares outstanding. This only includes gain or loss from discontinued operations.
    
    BasicDiscontinuousOperations(store: IDictionary[str, Decimal])
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


class BasicEPS(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Basic EPS is the bottom line net income divided by the weighted average number of common shares outstanding.
    
    BasicEPS(store: IDictionary[str, Decimal])
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


class BasicEPSOtherGainsLosses(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Basic EPS from the Other Gains/Losses is the earnings attributable to the other gains/losses (during the reporting period) divided by
                the weighted average number of common shares outstanding.
    
    BasicEPSOtherGainsLosses(store: IDictionary[str, Decimal])
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


class BasicExtraordinary(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Basic EPS from the Extraordinary Gains/Losses is the earnings attributable to the gains or losses (during the reporting period) from
                extraordinary items divided by the weighted average number of common shares outstanding.
    
    BasicExtraordinary(store: IDictionary[str, Decimal])
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


class BeginningCashPositionCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash and equivalents balance at the beginning of the accounting period, as indicated on the Cash Flow statement.
    
    BeginningCashPositionCashFlowStatement(store: IDictionary[str, Decimal])
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


class BiologicalAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Biological assets include plants and animals.
    
    BiologicalAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class BookValuePerShareGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's book value per share on a percentage basis. Morningstar calculates the growth percentage based on
                the common shareholder's equity reported in the Balance Sheet divided by the diluted shares outstanding within the company
                filings or reports.
    
    BookValuePerShareGrowth(store: IDictionary[str, Decimal])
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


class BuildingsAndImprovementsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Fixed assets that specifically deal with the facilities a company owns. Include the improvements associated with buildings.
    
    BuildingsAndImprovementsBalanceSheet(store: IDictionary[str, Decimal])
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


class CapExGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's capital expenditures on a percentage basis. Morningstar calculates the growth percentage based on
                the capital expenditures reported in the Cash Flow Statement within the company filings or reports.
    
    CapExGrowth(store: IDictionary[str, Decimal])
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


class CapExReportedCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Capital expenditure, capitalized software development cost, maintenance capital expenditure, etc. as reported by the company.
    
    CapExReportedCashFlowStatement(store: IDictionary[str, Decimal])
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


class CapExSalesRatio(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Capital Expenditure / Revenue
    
    CapExSalesRatio(store: IDictionary[str, Decimal])
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


class CapitalExpenditureAnnual5YrGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This is the compound annual growth rate of the company's capital spending over the last 5 years. Capital Spending is the sum of
                the Capital Expenditure items found in the Statement of Cash Flows.
    
    CapitalExpenditureAnnual5YrGrowth(store: IDictionary[str, Decimal])
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


class CapitalExpenditureCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Funds used by a company to acquire or upgrade physical assets such as property, industrial buildings or equipment. This
                type of outlay is made by companies to maintain or increase the scope of their operations. Capital expenditures are generally
                depreciated or depleted over their useful life, as distinguished from repairs, which are subtracted from the income of the current
                year.
    
    CapitalExpenditureCashFlowStatement(store: IDictionary[str, Decimal])
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


class CapitalExpendituretoEBITDA(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Measures the amount a company is investing in its business relative to EBITDA generated in a given PeriodAsByte.
    
    CapitalExpendituretoEBITDA(store: IDictionary[str, Decimal])
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


class CapitalLeaseObligationsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Current Portion of Capital Lease Obligation plus Long Term Portion of Capital Lease Obligation.
    
    CapitalLeaseObligationsBalanceSheet(store: IDictionary[str, Decimal])
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


class CapitalStockBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The total amount of stock authorized for issue by a corporation, including common and preferred stock.
    
    CapitalStockBalanceSheet(store: IDictionary[str, Decimal])
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


class CashAdvancesandLoansMadetoOtherPartiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash outlay for cash advances and loans made to other parties.
    
    CashAdvancesandLoansMadetoOtherPartiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashAndCashEquivalentsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Includes unrestricted cash on hand, money market instruments and other debt securities which can be converted to cash
                immediately.
    
    CashAndCashEquivalentsBalanceSheet(store: IDictionary[str, Decimal])
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


class CashAndDueFromBanksBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Includes cash on hand (currency and coin), cash items in process of collection, non-interest bearing deposits due from other
                financial institutions (including corporate credit unions), and balances with the Federal Reserve Banks, Federal Home Loan Banks
                and central banks.
    
    CashAndDueFromBanksBalanceSheet(store: IDictionary[str, Decimal])
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


class CashBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash includes currency on hand as well as demand deposits with banks or financial institutions. It also includes other kinds of
                accounts that have the general characteristics of demand deposits in that the customer may deposit additional funds at any time
                and also effectively may withdraw funds at any time without prior notice or penalty.
    
    CashBalanceSheet(store: IDictionary[str, Decimal])
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


class CashCashEquivalentsAndFederalFundsSoldBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of cash, cash equivalents, and federal funds sold.
    
    CashCashEquivalentsAndFederalFundsSoldBalanceSheet(store: IDictionary[str, Decimal])
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


class CashCashEquivalentsAndMarketableSecuritiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of cash, cash equivalents, and marketable securities.
    
    CashCashEquivalentsAndMarketableSecuritiesBalanceSheet(store: IDictionary[str, Decimal])
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


class CashConversionCycle(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Days In Inventory + Days In Sales - Days In Payment
    
    CashConversionCycle(store: IDictionary[str, Decimal])
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


class CashDividendsForMinoritiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash Distribution of earnings to Minority Stockholders.
    
    CashDividendsForMinoritiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashDividendsPaidCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Payments for the cash dividends declared by an entity to shareholders during the PeriodAsByte. This element includes paid and unpaid
                dividends declared during the period for both common and preferred stock.
    
    CashDividendsPaidCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashEquivalentsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash equivalents, excluding items classified as marketable securities, include short-term, highly liquid investments that are both
                readily convertible to known amounts of cash, and so near their maturity that they present insignificant risk of changes in value
                because of changes in interest rates.  Generally, only investments with original maturities of three months or less qualify under this
                definition. Original maturity means original maturity to the entity holding the investment. For example, both a three-month US
                Treasury bill and a three-year Treasury note purchased three months from maturity qualify as cash equivalents. However, a Treasury
                note purchased three years ago does not become a cash equivalent when its remaining maturity is three months.
    
    CashEquivalentsBalanceSheet(store: IDictionary[str, Decimal])
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


class CashFlowFromContinuingFinancingActivitiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash generated by or used in financing activities of continuing operations; excludes cash flows from discontinued operations.
    
    CashFlowFromContinuingFinancingActivitiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashFlowFromContinuingInvestingActivitiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash generated by or used in investing activities of continuing operations; excludes cash flows from discontinued operations.
    
    CashFlowFromContinuingInvestingActivitiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashFlowFromContinuingOperatingActivitiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash generated by or used in operating activities of continuing operations; excludes cash flows from discontinued operations.
    
    CashFlowFromContinuingOperatingActivitiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashFlowFromDiscontinuedOperationCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of cash flow from discontinued operation, including operating activities, investing activities, and financing
                activities.
    
    CashFlowFromDiscontinuedOperationCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashFlowfromFinancingGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's cash flows from financing on a percentage basis. Morningstar calculates the growth percentage
                based on the financing cash flows reported in the Cash Flow Statement within the company filings or reports.
    
    CashFlowfromFinancingGrowth(store: IDictionary[str, Decimal])
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


class CashFlowfromInvestingGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's cash flows from investing on a percentage basis. Morningstar calculates the growth percentage
                based on the cash flows from investing reported in the Cash Flow Statement within the company filings or reports.
    
    CashFlowfromInvestingGrowth(store: IDictionary[str, Decimal])
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


class CashFlowsfromusedinOperatingActivitiesDirectCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net cash from (used in) all of the entity's operating activities, including those of discontinued operations, of the reporting entity
                under the direct method.
    
    CashFlowsfromusedinOperatingActivitiesDirectCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashFlowStatement(System.object):
    """
    Definition of the CashFlowStatement class
    
    CashFlowStatement()
    """
    def UpdateValues(self, update: QuantConnect.Data.Fundamental.CashFlowStatement) -> None:
        pass

    AllTaxesPaid: QuantConnect.Data.Fundamental.AllTaxesPaidCashFlowStatement

    Amortization: QuantConnect.Data.Fundamental.AmortizationCashFlowStatement

    AmortizationOfFinancingCostsAndDiscounts: QuantConnect.Data.Fundamental.AmortizationOfFinancingCostsAndDiscountsCashFlowStatement

    AmortizationOfIntangibles: QuantConnect.Data.Fundamental.AmortizationOfIntangiblesCashFlowStatement

    AmortizationOfSecurities: QuantConnect.Data.Fundamental.AmortizationOfSecuritiesCashFlowStatement

    AssetImpairmentCharge: QuantConnect.Data.Fundamental.AssetImpairmentChargeCashFlowStatement

    BeginningCashPosition: QuantConnect.Data.Fundamental.BeginningCashPositionCashFlowStatement

    CapExReported: QuantConnect.Data.Fundamental.CapExReportedCashFlowStatement

    CapitalExpenditure: QuantConnect.Data.Fundamental.CapitalExpenditureCashFlowStatement

    CashAdvancesandLoansMadetoOtherParties: QuantConnect.Data.Fundamental.CashAdvancesandLoansMadetoOtherPartiesCashFlowStatement

    CashDividendsForMinorities: QuantConnect.Data.Fundamental.CashDividendsForMinoritiesCashFlowStatement

    CashDividendsPaid: QuantConnect.Data.Fundamental.CashDividendsPaidCashFlowStatement

    CashFlowFromContinuingFinancingActivities: QuantConnect.Data.Fundamental.CashFlowFromContinuingFinancingActivitiesCashFlowStatement

    CashFlowFromContinuingInvestingActivities: QuantConnect.Data.Fundamental.CashFlowFromContinuingInvestingActivitiesCashFlowStatement

    CashFlowFromContinuingOperatingActivities: QuantConnect.Data.Fundamental.CashFlowFromContinuingOperatingActivitiesCashFlowStatement

    CashFlowFromDiscontinuedOperation: QuantConnect.Data.Fundamental.CashFlowFromDiscontinuedOperationCashFlowStatement

    CashFlowsfromusedinOperatingActivitiesDirect: QuantConnect.Data.Fundamental.CashFlowsfromusedinOperatingActivitiesDirectCashFlowStatement

    CashFromDiscontinuedFinancing: QuantConnect.Data.Fundamental.CashFromDiscontinuedFinancingCashFlowStatement

    CashFromDiscontinuedFinancingActivities: QuantConnect.Data.Fundamental.CashFromDiscontinuedFinancingActivitiesCashFlowStatement

    CashFromDiscontinuedInvesting: QuantConnect.Data.Fundamental.CashFromDiscontinuedInvestingCashFlowStatement

    CashFromDiscontinuedInvestingActivities: QuantConnect.Data.Fundamental.CashFromDiscontinuedInvestingActivitiesCashFlowStatement

    CashFromDiscontinuedOperating: QuantConnect.Data.Fundamental.CashFromDiscontinuedOperatingCashFlowStatement

    CashFromDiscontinuedOperatingActivities: QuantConnect.Data.Fundamental.CashFromDiscontinuedOperatingActivitiesCashFlowStatement

    CashGeneratedfromOperatingActivities: QuantConnect.Data.Fundamental.CashGeneratedfromOperatingActivitiesCashFlowStatement

    CashPaidforInsuranceActivities: QuantConnect.Data.Fundamental.CashPaidforInsuranceActivitiesCashFlowStatement

    CashPaidtoReinsurers: QuantConnect.Data.Fundamental.CashPaidtoReinsurersCashFlowStatement

    CashPaymentsforDepositsbyBanksandCustomers: QuantConnect.Data.Fundamental.CashPaymentsforDepositsbyBanksandCustomersCashFlowStatement

    CashPaymentsforLoans: QuantConnect.Data.Fundamental.CashPaymentsforLoansCashFlowStatement

    CashReceiptsfromDepositsbyBanksandCustomers: QuantConnect.Data.Fundamental.CashReceiptsfromDepositsbyBanksandCustomersCashFlowStatement

    CashReceiptsfromFeesandCommissions: QuantConnect.Data.Fundamental.CashReceiptsfromFeesandCommissionsCashFlowStatement

    CashReceiptsfromLoans: QuantConnect.Data.Fundamental.CashReceiptsfromLoansCashFlowStatement

    CashReceiptsfromRepaymentofAdvancesandLoansMadetoOtherParties: QuantConnect.Data.Fundamental.CashReceiptsfromRepaymentofAdvancesandLoansMadetoOtherPartiesCashFlowStatement

    CashReceiptsfromSecuritiesRelatedActivities: QuantConnect.Data.Fundamental.CashReceiptsfromSecuritiesRelatedActivitiesCashFlowStatement

    CashReceiptsfromTaxRefunds: QuantConnect.Data.Fundamental.CashReceiptsfromTaxRefundsCashFlowStatement

    CashReceivedfromInsuranceActivities: QuantConnect.Data.Fundamental.CashReceivedfromInsuranceActivitiesCashFlowStatement

    CFFileDate: datetime.datetime

    ChangeInAccountPayable: QuantConnect.Data.Fundamental.ChangeInAccountPayableCashFlowStatement

    ChangeInAccruedExpense: QuantConnect.Data.Fundamental.ChangeInAccruedExpenseCashFlowStatement

    ChangeinAccruedIncome: QuantConnect.Data.Fundamental.ChangeinAccruedIncomeCashFlowStatement

    ChangeInAccruedInvestmentIncome: QuantConnect.Data.Fundamental.ChangeInAccruedInvestmentIncomeCashFlowStatement

    ChangeinAdvancesfromCentralBanks: QuantConnect.Data.Fundamental.ChangeinAdvancesfromCentralBanksCashFlowStatement

    ChangeinCashSupplementalAsReported: QuantConnect.Data.Fundamental.ChangeinCashSupplementalAsReportedCashFlowStatement

    ChangeInDeferredAcquisitionCosts: QuantConnect.Data.Fundamental.ChangeInDeferredAcquisitionCostsCashFlowStatement

    ChangeinDeferredAcquisitionCostsNet: QuantConnect.Data.Fundamental.ChangeinDeferredAcquisitionCostsNetCashFlowStatement

    ChangeInDeferredCharges: QuantConnect.Data.Fundamental.ChangeInDeferredChargesCashFlowStatement

    ChangeinDepositsbyBanksandCustomers: QuantConnect.Data.Fundamental.ChangeinDepositsbyBanksandCustomersCashFlowStatement

    ChangeInDividendPayable: QuantConnect.Data.Fundamental.ChangeInDividendPayableCashFlowStatement

    ChangeInFederalFundsAndSecuritiesSoldForRepurchase: QuantConnect.Data.Fundamental.ChangeInFederalFundsAndSecuritiesSoldForRepurchaseCashFlowStatement

    ChangeinFinancialAssets: QuantConnect.Data.Fundamental.ChangeinFinancialAssetsCashFlowStatement

    ChangeinFinancialLiabilities: QuantConnect.Data.Fundamental.ChangeinFinancialLiabilitiesCashFlowStatement

    ChangeInFundsWithheld: QuantConnect.Data.Fundamental.ChangeInFundsWithheldCashFlowStatement

    ChangeInIncomeTaxPayable: QuantConnect.Data.Fundamental.ChangeInIncomeTaxPayableCashFlowStatement

    ChangeinInsuranceContractAssets: QuantConnect.Data.Fundamental.ChangeinInsuranceContractAssetsCashFlowStatement

    ChangeinInsuranceContractLiabilities: QuantConnect.Data.Fundamental.ChangeinInsuranceContractLiabilitiesCashFlowStatement

    ChangeinInsuranceFunds: QuantConnect.Data.Fundamental.ChangeinInsuranceFundsCashFlowStatement

    ChangeInInterestPayable: QuantConnect.Data.Fundamental.ChangeInInterestPayableCashFlowStatement

    ChangeInInventory: QuantConnect.Data.Fundamental.ChangeInInventoryCashFlowStatement

    ChangeinInvestmentContractLiabilities: QuantConnect.Data.Fundamental.ChangeinInvestmentContractLiabilitiesCashFlowStatement

    ChangeInLoans: QuantConnect.Data.Fundamental.ChangeInLoansCashFlowStatement

    ChangeInLossAndLossAdjustmentExpenseReserves: QuantConnect.Data.Fundamental.ChangeInLossAndLossAdjustmentExpenseReservesCashFlowStatement

    ChangeInOtherCurrentAssets: QuantConnect.Data.Fundamental.ChangeInOtherCurrentAssetsCashFlowStatement

    ChangeInOtherCurrentLiabilities: QuantConnect.Data.Fundamental.ChangeInOtherCurrentLiabilitiesCashFlowStatement

    ChangeInOtherWorkingCapital: QuantConnect.Data.Fundamental.ChangeInOtherWorkingCapitalCashFlowStatement

    ChangeInPayable: QuantConnect.Data.Fundamental.ChangeInPayableCashFlowStatement

    ChangeInPayablesAndAccruedExpense: QuantConnect.Data.Fundamental.ChangeInPayablesAndAccruedExpenseCashFlowStatement

    ChangeInPrepaidAssets: QuantConnect.Data.Fundamental.ChangeInPrepaidAssetsCashFlowStatement

    ChangeInReceivables: QuantConnect.Data.Fundamental.ChangeInReceivablesCashFlowStatement

    ChangeinReinsuranceReceivables: QuantConnect.Data.Fundamental.ChangeinReinsuranceReceivablesCashFlowStatement

    ChangeInReinsuranceRecoverableOnPaidAndUnpaidLosses: QuantConnect.Data.Fundamental.ChangeInReinsuranceRecoverableOnPaidAndUnpaidLossesCashFlowStatement

    ChangeInRestrictedCash: QuantConnect.Data.Fundamental.ChangeInRestrictedCashCashFlowStatement

    ChangeInTaxPayable: QuantConnect.Data.Fundamental.ChangeInTaxPayableCashFlowStatement

    ChangeInTradingAccountSecurities: QuantConnect.Data.Fundamental.ChangeInTradingAccountSecuritiesCashFlowStatement

    ChangeInUnearnedPremiums: QuantConnect.Data.Fundamental.ChangeInUnearnedPremiumsCashFlowStatement

    ChangeInWorkingCapital: QuantConnect.Data.Fundamental.ChangeInWorkingCapitalCashFlowStatement

    ChangesInAccountReceivables: QuantConnect.Data.Fundamental.ChangesInAccountReceivablesCashFlowStatement

    ChangesInCash: QuantConnect.Data.Fundamental.ChangesInCashCashFlowStatement

    ClaimsPaid: QuantConnect.Data.Fundamental.ClaimsPaidCashFlowStatement

    ClassesofCashPayments: QuantConnect.Data.Fundamental.ClassesofCashPaymentsCashFlowStatement

    ClassesofCashReceiptsfromOperatingActivities: QuantConnect.Data.Fundamental.ClassesofCashReceiptsfromOperatingActivitiesCashFlowStatement

    CommissionPaid: QuantConnect.Data.Fundamental.CommissionPaidCashFlowStatement

    CommonStockDividendPaid: QuantConnect.Data.Fundamental.CommonStockDividendPaidCashFlowStatement

    CommonStockIssuance: QuantConnect.Data.Fundamental.CommonStockIssuanceCashFlowStatement

    CommonStockPayments: QuantConnect.Data.Fundamental.CommonStockPaymentsCashFlowStatement

    DecreaseinInterestBearingDepositsinBank: QuantConnect.Data.Fundamental.DecreaseinInterestBearingDepositsinBankCashFlowStatement

    DeferredIncomeTax: QuantConnect.Data.Fundamental.DeferredIncomeTaxCashFlowStatement

    DeferredTax: QuantConnect.Data.Fundamental.DeferredTaxCashFlowStatement

    Depletion: QuantConnect.Data.Fundamental.DepletionCashFlowStatement

    Depreciation: QuantConnect.Data.Fundamental.DepreciationCashFlowStatement

    DepreciationAmortizationDepletion: QuantConnect.Data.Fundamental.DepreciationAmortizationDepletionCashFlowStatement

    DepreciationAndAmortization: QuantConnect.Data.Fundamental.DepreciationAndAmortizationCashFlowStatement

    DividendPaidCFO: QuantConnect.Data.Fundamental.DividendPaidCFOCashFlowStatement

    DividendReceivedCFO: QuantConnect.Data.Fundamental.DividendReceivedCFOCashFlowStatement

    DividendsPaidDirect: QuantConnect.Data.Fundamental.DividendsPaidDirectCashFlowStatement

    DividendsReceivedCFI: QuantConnect.Data.Fundamental.DividendsReceivedCFICashFlowStatement

    DividendsReceivedDirect: QuantConnect.Data.Fundamental.DividendsReceivedDirectCashFlowStatement

    EarningsLossesFromEquityInvestments: QuantConnect.Data.Fundamental.EarningsLossesFromEquityInvestmentsCashFlowStatement

    EffectOfExchangeRateChanges: QuantConnect.Data.Fundamental.EffectOfExchangeRateChangesCashFlowStatement

    EndCashPosition: QuantConnect.Data.Fundamental.EndCashPositionCashFlowStatement

    ExcessTaxBenefitFromStockBasedCompensation: QuantConnect.Data.Fundamental.ExcessTaxBenefitFromStockBasedCompensationCashFlowStatement

    FinancingCashFlow: QuantConnect.Data.Fundamental.FinancingCashFlowCashFlowStatement

    FreeCashFlow: QuantConnect.Data.Fundamental.FreeCashFlowCashFlowStatement

    FundFromOperation: QuantConnect.Data.Fundamental.FundFromOperationCashFlowStatement

    GainLossOnInvestmentSecurities: QuantConnect.Data.Fundamental.GainLossOnInvestmentSecuritiesCashFlowStatement

    GainLossOnSaleOfBusiness: QuantConnect.Data.Fundamental.GainLossOnSaleOfBusinessCashFlowStatement

    GainLossOnSaleOfPPE: QuantConnect.Data.Fundamental.GainLossOnSaleOfPPECashFlowStatement

    ImpairmentLossReversalRecognizedinProfitorLoss: QuantConnect.Data.Fundamental.ImpairmentLossReversalRecognizedinProfitorLossCashFlowStatement

    IncomeTaxPaidSupplementalData: QuantConnect.Data.Fundamental.IncomeTaxPaidSupplementalDataCashFlowStatement

    IncreaseDecreaseInDeposit: QuantConnect.Data.Fundamental.IncreaseDecreaseInDepositCashFlowStatement

    IncreaseDecreaseinLeaseFinancing: QuantConnect.Data.Fundamental.IncreaseDecreaseinLeaseFinancingCashFlowStatement

    IncreaseinInterestBearingDepositsinBank: QuantConnect.Data.Fundamental.IncreaseinInterestBearingDepositsinBankCashFlowStatement

    IncreaseinLeaseFinancing: QuantConnect.Data.Fundamental.IncreaseinLeaseFinancingCashFlowStatement

    InterestandCommissionPaid: QuantConnect.Data.Fundamental.InterestandCommissionPaidCashFlowStatement

    InterestCreditedOnPolicyholderDeposits: QuantConnect.Data.Fundamental.InterestCreditedOnPolicyholderDepositsCashFlowStatement

    InterestPaidCFF: QuantConnect.Data.Fundamental.InterestPaidCFFCashFlowStatement

    InterestPaidCFO: QuantConnect.Data.Fundamental.InterestPaidCFOCashFlowStatement

    InterestPaidDirect: QuantConnect.Data.Fundamental.InterestPaidDirectCashFlowStatement

    InterestPaidSupplementalData: QuantConnect.Data.Fundamental.InterestPaidSupplementalDataCashFlowStatement

    InterestReceivedCFI: QuantConnect.Data.Fundamental.InterestReceivedCFICashFlowStatement

    InterestReceivedCFO: QuantConnect.Data.Fundamental.InterestReceivedCFOCashFlowStatement

    InterestReceivedDirect: QuantConnect.Data.Fundamental.InterestReceivedDirectCashFlowStatement

    InvestingCashFlow: QuantConnect.Data.Fundamental.InvestingCashFlowCashFlowStatement

    IssuanceOfCapitalStock: QuantConnect.Data.Fundamental.IssuanceOfCapitalStockCashFlowStatement

    IssuanceOfDebt: QuantConnect.Data.Fundamental.IssuanceOfDebtCashFlowStatement

    IssueExpenses: QuantConnect.Data.Fundamental.IssueExpensesCashFlowStatement

    LongTermDebtIssuance: QuantConnect.Data.Fundamental.LongTermDebtIssuanceCashFlowStatement

    LongTermDebtPayments: QuantConnect.Data.Fundamental.LongTermDebtPaymentsCashFlowStatement

    MinorityInterest: QuantConnect.Data.Fundamental.MinorityInterestCashFlowStatement

    NetBusinessPurchaseAndSale: QuantConnect.Data.Fundamental.NetBusinessPurchaseAndSaleCashFlowStatement

    NetCashFromDiscontinuedOperations: QuantConnect.Data.Fundamental.NetCashFromDiscontinuedOperationsCashFlowStatement

    NetCommonStockIssuance: QuantConnect.Data.Fundamental.NetCommonStockIssuanceCashFlowStatement

    NetForeignCurrencyExchangeGainLoss: QuantConnect.Data.Fundamental.NetForeignCurrencyExchangeGainLossCashFlowStatement

    NetIncomeFromContinuingOperations: QuantConnect.Data.Fundamental.NetIncomeFromContinuingOperationsCashFlowStatement

    NetIntangiblesPurchaseAndSale: QuantConnect.Data.Fundamental.NetIntangiblesPurchaseAndSaleCashFlowStatement

    NetInvestmentPropertiesPurchaseAndSale: QuantConnect.Data.Fundamental.NetInvestmentPropertiesPurchaseAndSaleCashFlowStatement

    NetInvestmentPurchaseAndSale: QuantConnect.Data.Fundamental.NetInvestmentPurchaseAndSaleCashFlowStatement

    NetIssuancePaymentsOfDebt: QuantConnect.Data.Fundamental.NetIssuancePaymentsOfDebtCashFlowStatement

    NetLongTermDebtIssuance: QuantConnect.Data.Fundamental.NetLongTermDebtIssuanceCashFlowStatement

    NetOtherFinancingCharges: QuantConnect.Data.Fundamental.NetOtherFinancingChargesCashFlowStatement

    NetOtherInvestingChanges: QuantConnect.Data.Fundamental.NetOtherInvestingChangesCashFlowStatement

    NetOutwardLoans: QuantConnect.Data.Fundamental.NetOutwardLoansCashFlowStatement

    NetPPEPurchaseAndSale: QuantConnect.Data.Fundamental.NetPPEPurchaseAndSaleCashFlowStatement

    NetPreferredStockIssuance: QuantConnect.Data.Fundamental.NetPreferredStockIssuanceCashFlowStatement

    NetProceedsPaymentForLoan: QuantConnect.Data.Fundamental.NetProceedsPaymentForLoanCashFlowStatement

    NetShortTermDebtIssuance: QuantConnect.Data.Fundamental.NetShortTermDebtIssuanceCashFlowStatement

    OperatingCashFlow: QuantConnect.Data.Fundamental.OperatingCashFlowCashFlowStatement

    OperatingGainsLosses: QuantConnect.Data.Fundamental.OperatingGainsLossesCashFlowStatement

    OtherCashAdjustExcludeFromChangeinCash: QuantConnect.Data.Fundamental.OtherCashAdjustExcludeFromChangeinCashCashFlowStatement

    OtherCashAdjustIncludedIntoChangeinCash: QuantConnect.Data.Fundamental.OtherCashAdjustIncludedIntoChangeinCashCashFlowStatement

    OtherCashPaymentsfromOperatingActivities: QuantConnect.Data.Fundamental.OtherCashPaymentsfromOperatingActivitiesCashFlowStatement

    OtherCashReceiptsfromOperatingActivities: QuantConnect.Data.Fundamental.OtherCashReceiptsfromOperatingActivitiesCashFlowStatement

    OtherNonCashItems: QuantConnect.Data.Fundamental.OtherNonCashItemsCashFlowStatement

    OtherOperatingInflowsOutflowsofCash: QuantConnect.Data.Fundamental.OtherOperatingInflowsOutflowsofCashCashFlowStatement

    OtherUnderwritingExpensesPaid: QuantConnect.Data.Fundamental.OtherUnderwritingExpensesPaidCashFlowStatement

    PaymentForLoans: QuantConnect.Data.Fundamental.PaymentForLoansCashFlowStatement

    PaymentsonBehalfofEmployees: QuantConnect.Data.Fundamental.PaymentsonBehalfofEmployeesCashFlowStatement

    PaymentstoSuppliersforGoodsandServices: QuantConnect.Data.Fundamental.PaymentstoSuppliersforGoodsandServicesCashFlowStatement

    PensionAndEmployeeBenefitExpense: QuantConnect.Data.Fundamental.PensionAndEmployeeBenefitExpenseCashFlowStatement

    PolicyholderDepositInvestmentReceived: QuantConnect.Data.Fundamental.PolicyholderDepositInvestmentReceivedCashFlowStatement

    PreferredStockDividendPaid: QuantConnect.Data.Fundamental.PreferredStockDividendPaidCashFlowStatement

    PreferredStockIssuance: QuantConnect.Data.Fundamental.PreferredStockIssuanceCashFlowStatement

    PreferredStockPayments: QuantConnect.Data.Fundamental.PreferredStockPaymentsCashFlowStatement

    PremiumReceived: QuantConnect.Data.Fundamental.PremiumReceivedCashFlowStatement

    ProceedsFromLoans: QuantConnect.Data.Fundamental.ProceedsFromLoansCashFlowStatement

    ProceedsFromStockOptionExercised: QuantConnect.Data.Fundamental.ProceedsFromStockOptionExercisedCashFlowStatement

    ProceedsPaymentFederalFundsSoldAndSecuritiesPurchasedUnderAgreementToResell: QuantConnect.Data.Fundamental.ProceedsPaymentFederalFundsSoldAndSecuritiesPurchasedUnderAgreementToResellCashFlowStatement

    ProceedsPaymentInInterestBearingDepositsInBank: QuantConnect.Data.Fundamental.ProceedsPaymentInInterestBearingDepositsInBankCashFlowStatement

    ProfitonDisposals: QuantConnect.Data.Fundamental.ProfitonDisposalsCashFlowStatement

    ProvisionandWriteOffofAssets: QuantConnect.Data.Fundamental.ProvisionandWriteOffofAssetsCashFlowStatement

    ProvisionForLoanLeaseAndOtherLosses: QuantConnect.Data.Fundamental.ProvisionForLoanLeaseAndOtherLossesCashFlowStatement

    PurchaseOfBusiness: QuantConnect.Data.Fundamental.PurchaseOfBusinessCashFlowStatement

    PurchaseOfIntangibles: QuantConnect.Data.Fundamental.PurchaseOfIntangiblesCashFlowStatement

    PurchaseOfInvestment: QuantConnect.Data.Fundamental.PurchaseOfInvestmentCashFlowStatement

    PurchaseOfInvestmentProperties: QuantConnect.Data.Fundamental.PurchaseOfInvestmentPropertiesCashFlowStatement

    PurchaseofJointVentureAssociate: QuantConnect.Data.Fundamental.PurchaseofJointVentureAssociateCashFlowStatement

    PurchaseOfPPE: QuantConnect.Data.Fundamental.PurchaseOfPPECashFlowStatement

    PurchaseofSubsidiaries: QuantConnect.Data.Fundamental.PurchaseofSubsidiariesCashFlowStatement

    RealizedGainLossOnSaleOfLoansAndLease: QuantConnect.Data.Fundamental.RealizedGainLossOnSaleOfLoansAndLeaseCashFlowStatement

    ReceiptsfromCustomers: QuantConnect.Data.Fundamental.ReceiptsfromCustomersCashFlowStatement

    ReceiptsfromGovernmentGrants: QuantConnect.Data.Fundamental.ReceiptsfromGovernmentGrantsCashFlowStatement

    ReinsuranceandOtherRecoveriesReceived: QuantConnect.Data.Fundamental.ReinsuranceandOtherRecoveriesReceivedCashFlowStatement

    ReorganizationOtherCosts: QuantConnect.Data.Fundamental.ReorganizationOtherCostsCashFlowStatement

    RepaymentinLeaseFinancing: QuantConnect.Data.Fundamental.RepaymentinLeaseFinancingCashFlowStatement

    RepaymentOfDebt: QuantConnect.Data.Fundamental.RepaymentOfDebtCashFlowStatement

    RepurchaseOfCapitalStock: QuantConnect.Data.Fundamental.RepurchaseOfCapitalStockCashFlowStatement

    SaleOfBusiness: QuantConnect.Data.Fundamental.SaleOfBusinessCashFlowStatement

    SaleOfIntangibles: QuantConnect.Data.Fundamental.SaleOfIntangiblesCashFlowStatement

    SaleOfInvestment: QuantConnect.Data.Fundamental.SaleOfInvestmentCashFlowStatement

    SaleOfInvestmentProperties: QuantConnect.Data.Fundamental.SaleOfInvestmentPropertiesCashFlowStatement

    SaleofJointVentureAssociate: QuantConnect.Data.Fundamental.SaleofJointVentureAssociateCashFlowStatement

    SaleOfPPE: QuantConnect.Data.Fundamental.SaleOfPPECashFlowStatement

    SaleofSubsidiaries: QuantConnect.Data.Fundamental.SaleofSubsidiariesCashFlowStatement

    ShareofAssociates: QuantConnect.Data.Fundamental.ShareofAssociatesCashFlowStatement

    ShortTermDebtIssuance: QuantConnect.Data.Fundamental.ShortTermDebtIssuanceCashFlowStatement

    ShortTermDebtPayments: QuantConnect.Data.Fundamental.ShortTermDebtPaymentsCashFlowStatement

    StockBasedCompensation: QuantConnect.Data.Fundamental.StockBasedCompensationCashFlowStatement

    TaxesRefundPaid: QuantConnect.Data.Fundamental.TaxesRefundPaidCashFlowStatement

    TaxesRefundPaidDirect: QuantConnect.Data.Fundamental.TaxesRefundPaidDirectCashFlowStatement

    TotalAdjustmentsforNonCashItems: QuantConnect.Data.Fundamental.TotalAdjustmentsforNonCashItemsCashFlowStatement

    UnrealizedGainLossOnInvestmentSecurities: QuantConnect.Data.Fundamental.UnrealizedGainLossOnInvestmentSecuritiesCashFlowStatement

    UnrealizedGainsLossesOnDerivatives: QuantConnect.Data.Fundamental.UnrealizedGainsLossesOnDerivativesCashFlowStatement



class CashFromDiscontinuedFinancingActivitiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash generated by or used in financing activities of discontinued operations; excludes cash flows from continued operations.
    
    CashFromDiscontinuedFinancingActivitiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashFromDiscontinuedFinancingCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash generated by or used in financing activities of discontinued operations; excludes cash flows from continued operations.
    
    CashFromDiscontinuedFinancingCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashFromDiscontinuedInvestingActivitiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net cash inflow (outflow) from discontinued investing activities over the designated time PeriodAsByte.
    
    CashFromDiscontinuedInvestingActivitiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashFromDiscontinuedInvestingCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net cash inflow (outflow) from discontinued investing activities over the designated time PeriodAsByte.
    
    CashFromDiscontinuedInvestingCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashFromDiscontinuedOperatingActivitiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net cash from (used in) all of the entity's discontinued operating activities, excluding those of continued operations, of the
                reporting entity.
    
    CashFromDiscontinuedOperatingActivitiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashFromDiscontinuedOperatingCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net cash from (used in) all of the entity's discontinued operating activities, excluding those of continued operations, of the
                reporting entity.
    
    CashFromDiscontinuedOperatingCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashGeneratedfromOperatingActivitiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net cash from an entity's operating activities before real cash inflow or outflow for Dividend, Interest, Tax, or other unclassified
                operating activities.
    
    CashGeneratedfromOperatingActivitiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashPaidforInsuranceActivitiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash paid out for insurance activities during the period in operating cash flow, using the direct method. This item is usually only
                available for insurance industry
    
    CashPaidforInsuranceActivitiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashPaidtoReinsurersCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash paid out to reinsurers in operating cash flow, using the direct method. This item is usually only available for insurance industry
    
    CashPaidtoReinsurersCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashPaymentsforDepositsbyBanksandCustomersCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash paid for deposits by banks and customers in operating cash flow, using the direct method. This item is usually only available
                for bank industry
    
    CashPaymentsforDepositsbyBanksandCustomersCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashPaymentsforLoansCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash paid for loans in operating cash flow, using the direct method. This item is usually only available for bank industry
    
    CashPaymentsforLoansCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashRatio(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Indicates a company's short-term liquidity, defined as short term liquid investments (cash, cash equivalents, short term
                investments) divided by current liabilities.
    
    CashRatio(store: IDictionary[str, Decimal])
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


class CashRatioGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's cash ratio on a percentage basis. Morningstar calculates the growth percentage based on the short
                term liquid investments (cash, cash equivalents, short term investments) divided by current liabilities reported in the Balance Sheet
                within the company filings or reports.
    
    CashRatioGrowth(store: IDictionary[str, Decimal])
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


class CashReceiptsfromDepositsbyBanksandCustomersCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash received from banks and customer deposits in operating cash flow, using the direct method. This item is usually only available
                for bank industry
    
    CashReceiptsfromDepositsbyBanksandCustomersCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashReceiptsfromFeesandCommissionsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash received from agency fees and commissions in operating cash flow, using the direct method. This item is usually available for
                bank and insurance industries
    
    CashReceiptsfromFeesandCommissionsCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashReceiptsfromLoansCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash received from loans in operating cash flow, using the direct method. This item is usually only available for bank industry
    
    CashReceiptsfromLoansCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashReceiptsfromRepaymentofAdvancesandLoansMadetoOtherPartiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash received from the repayment of advances and loans made to other parties, in the Investing Cash Flow section.
    
    CashReceiptsfromRepaymentofAdvancesandLoansMadetoOtherPartiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashReceiptsfromSecuritiesRelatedActivitiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash received from the trading of securities in operating cash flow, using the direct method. This item is usually only available for
                bank and insurance industries
    
    CashReceiptsfromSecuritiesRelatedActivitiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashReceiptsfromTaxRefundsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash received as refunds from tax authorities in operating cash flow, using the direct method
    
    CashReceiptsfromTaxRefundsCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashReceivedfromInsuranceActivitiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash received from insurance activities in operating cash flow, using the direct method. This item is usually only available for
                insurance industry
    
    CashReceivedfromInsuranceActivitiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class CashRestrictedOrPledgedBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash that the company can use only for specific purposes or cash deposit or placing of owned property by a debtor (the pledger) to
                a creditor (the pledgee) as a security for a loan or obligation.
    
    CashRestrictedOrPledgedBalanceSheet(store: IDictionary[str, Decimal])
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


class CashtoTotalAssets(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents the percentage of a company's total assets is in cash.
    
    CashtoTotalAssets(store: IDictionary[str, Decimal])
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


class CededPremiumsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount of premiums paid and payable to another insurer as a result of reinsurance arrangements in order to exchange for that
                company accepting all or part of insurance on a risk or exposure. This item is usually only available for insurance industry.
    
    CededPremiumsIncomeStatement(store: IDictionary[str, Decimal])
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


class CFOGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's cash flow from operations on a percentage basis. Morningstar calculates the growth percentage
                based on the underlying cash flow from operations data reported in the Cash Flow Statement within the company filings or reports.
    
    CFOGrowth(store: IDictionary[str, Decimal])
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


class ChangeInAccountPayableCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the account payables.
    
    ChangeInAccountPayableCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInAccruedExpenseCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the accrued expenses.
    
    ChangeInAccruedExpenseCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeinAccruedIncomeCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods in the amount of outstanding money owed by a customer for goods or services provided
                by the company.
    
    ChangeinAccruedIncomeCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInAccruedInvestmentIncomeCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net change during the reporting period in investment income that has been earned but not yet received in cash.
    
    ChangeInAccruedInvestmentIncomeCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeinAdvancesfromCentralBanksCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the advances from central banks.
    
    ChangeinAdvancesfromCentralBanksCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeinCashSupplementalAsReportedCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The change in cash flow from the previous period to the current, as reported by the company, may be the same or not the same as
                Morningstar's standardized definition. It is a supplemental value which would be reported outside consolidated statements.
    
    ChangeinCashSupplementalAsReportedCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInDeferredAcquisitionCostsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The change of the unamortized portion as of the balance sheet date of capitalized costs that vary with and are primarily related to
                the acquisition of new and renewal insurance contracts.
    
    ChangeInDeferredAcquisitionCostsCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeinDeferredAcquisitionCostsNetCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the deferred acquisition costs.
    
    ChangeinDeferredAcquisitionCostsNetCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInDeferredChargesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net change during the reporting period in the value of expenditures made during the current reporting period for benefits that
                will be received over a period of years. This item is usually only available for bank industry.
    
    ChangeInDeferredChargesCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeinDepositsbyBanksandCustomersCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the deposits by banks and customers.
    
    ChangeinDepositsbyBanksandCustomersCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInDividendPayableCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the dividend payables.
    
    ChangeInDividendPayableCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInFederalFundsAndSecuritiesSoldForRepurchaseCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount shown on the books that a bank with insufficient reserves borrows, at the federal funds rate, from another bank to
                meet its reserve requirements and the amount of securities that an institution sells and agrees to repurchase at a specified date for
                a specified price, net of any reductions or offsets.
    
    ChangeInFederalFundsAndSecuritiesSoldForRepurchaseCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeinFinancialAssetsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the financial assets.
    
    ChangeinFinancialAssetsCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeinFinancialLiabilitiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the financial liabilities.
    
    ChangeinFinancialLiabilitiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInFundsWithheldCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net change during the reporting period associated with funds withheld.
    
    ChangeInFundsWithheldCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInIncomeTaxPayableCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the income tax payables.
    
    ChangeInIncomeTaxPayableCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeinInsuranceContractAssetsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the contract assets.
    
    ChangeinInsuranceContractAssetsCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeinInsuranceContractLiabilitiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the insurance contract liabilities.
    
    ChangeinInsuranceContractLiabilitiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeinInsuranceFundsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the insurance funds.
    
    ChangeinInsuranceFundsCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeinInsuranceLiabilitiesNetofReinsuranceIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Income/Expense due to changes between periods in insurance liabilities.
    
    ChangeinInsuranceLiabilitiesNetofReinsuranceIncomeStatement(store: IDictionary[str, Decimal])
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


class ChangeInInterestPayableCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the interest payable. Interest payable means carrying value as of the balance sheet
                date of interest payable on all forms of debt.
    
    ChangeInInterestPayableCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInInventoryCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the Inventories. Inventories represent merchandise bought for resale and supplies and
                raw materials purchased for use in revenue producing operations.
    
    ChangeInInventoryCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeinInvestmentContractIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Income/Expense due to changes between periods in Investment Contracts.
    
    ChangeinInvestmentContractIncomeStatement(store: IDictionary[str, Decimal])
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


class ChangeinInvestmentContractLiabilitiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the investment contract liabilities.
    
    ChangeinInvestmentContractLiabilitiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInLoansCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net change that a lender gives money or property to a borrower and the borrower agrees to return the property or repay the
                borrowed money, along with interest, at a predetermined date in the future.
    
    ChangeInLoansCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInLossAndLossAdjustmentExpenseReservesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net change during the reporting period in the reserve account established to account for expected but unspecified losses.
    
    ChangeInLossAndLossAdjustmentExpenseReservesCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInOtherCurrentAssetsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the Other Current Assets. This category typically includes prepayments, deferred
                charges, and amounts (other than trade accounts) due from parents and subsidiaries.
    
    ChangeInOtherCurrentAssetsCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInOtherCurrentLiabilitiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the Other Current liabilities. Other Current liabilities is a balance sheet entry used by
                companies to group together current liabilities that are not assigned to common liabilities such as debt obligations or accounts
                payable.
    
    ChangeInOtherCurrentLiabilitiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInOtherWorkingCapitalCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the other working capital.
    
    ChangeInOtherWorkingCapitalCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInPayableCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the payables.
    
    ChangeInPayableCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInPayablesAndAccruedExpenseCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the payables and accrued expenses. Accrued expenses represent expenses incurred
                at the end of the reporting period but not yet paid; also called accrued liabilities. The accrued liability is shown under current
                liabilities in the balance sheet.
    
    ChangeInPayablesAndAccruedExpenseCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInPrepaidAssetsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the prepaid assets.
    
    ChangeInPrepaidAssetsCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInReceivablesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the receivables. Receivables are amounts due to be paid to the company from clients
                and other.
    
    ChangeInReceivablesCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeinReinsuranceReceivablesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the reinsurance receivable.
    
    ChangeinReinsuranceReceivablesCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInReinsuranceRecoverableOnPaidAndUnpaidLossesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net change during the reporting period in the amount of benefits the ceding insurer expects to recover on insurance policies
                ceded to other insurance entities as of the balance sheet date for all guaranteed benefit types.
    
    ChangeInReinsuranceRecoverableOnPaidAndUnpaidLossesCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInRestrictedCashCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net cash inflow (outflow) for the net change associated with funds that are not available for withdrawal or use (such as funds
                held in escrow).
    
    ChangeInRestrictedCashCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInTaxPayableCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the tax payables.
    
    ChangeInTaxPayableCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeinTheGrossProvisionforUnearnedPremiumsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The change in the amount of the unearned premium reserves maintained by insurers.
    
    ChangeinTheGrossProvisionforUnearnedPremiumsIncomeStatement(store: IDictionary[str, Decimal])
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


class ChangeinTheGrossProvisionforUnearnedPremiumsReinsurersShareIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The change in the amount of unearned premium reserve to be covered by reinsurers.
    
    ChangeinTheGrossProvisionforUnearnedPremiumsReinsurersShareIncomeStatement(store: IDictionary[str, Decimal])
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


class ChangeInTradingAccountSecuritiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net change during the reporting period associated with trading account assets. Trading account assets are bought and held
                principally for the purpose of selling them in the near term (thus held for only a short period of time). Unrealized holding gains and
                losses for trading securities are included in earnings.
    
    ChangeInTradingAccountSecuritiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInUnearnedPremiumsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The change during the period in the unearned portion of premiums written, excluding the portion amortized into income. This item is
                usually only available for insurance industry.
    
    ChangeInUnearnedPremiumsCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangeInWorkingCapitalCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the working capital.  Working Capital is the amount left to the company to finance
                operations and expansion after current liabilities have been covered.
    
    ChangeInWorkingCapitalCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangesInAccountReceivablesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of the accounts receivables.
    
    ChangesInAccountReceivablesCashFlowStatement(store: IDictionary[str, Decimal])
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


class ChangesInCashCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net change between the beginning and ending balance of cash and cash equivalents.
    
    ChangesInCashCashFlowStatement(store: IDictionary[str, Decimal])
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


class ClaimsandChangeinInsuranceLiabilitiesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Income/Expense due to the insurer's changes in insurance liabilities.
    
    ClaimsandChangeinInsuranceLiabilitiesIncomeStatement(store: IDictionary[str, Decimal])
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


class ClaimsandPaidIncurredIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    All reported claims arising out of incidents in that year are considered incurred grouped with claims paid out.
    
    ClaimsandPaidIncurredIncomeStatement(store: IDictionary[str, Decimal])
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


class ClaimsOutstandingBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Amounts owing to policy holders who have filed claims but have not yet been settled or paid.
    
    ClaimsOutstandingBalanceSheet(store: IDictionary[str, Decimal])
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


class ClaimsPaidCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash paid out for claims by a insurance company during the period in operating cash flow, using the direct method. This item is
                usually only available for insurance industry
    
    ClaimsPaidCashFlowStatement(store: IDictionary[str, Decimal])
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


class ClassesofCashPaymentsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of total cash payment in the direct cash flow.
    
    ClassesofCashPaymentsCashFlowStatement(store: IDictionary[str, Decimal])
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


class ClassesofCashReceiptsfromOperatingActivitiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of total cash receipts in the direct cash flow.
    
    ClassesofCashReceiptsfromOperatingActivitiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class CommercialLoanBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Short-term loan, typically 90 days, used by a company to finance seasonal working capital needs.
    
    CommercialLoanBalanceSheet(store: IDictionary[str, Decimal])
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


class CommercialPaperBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Commercial paper is a money-market security issued by large banks and corporations. It represents the current obligation for the
                company. There are four basic kinds of commercial paper: promissory notes, drafts, checks, and certificates of deposit. The
                maturities of these money market securities generally do not exceed 270 days.
    
    CommercialPaperBalanceSheet(store: IDictionary[str, Decimal])
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


class CommissionExpensesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """ CommissionExpensesIncomeStatement(store: IDictionary[str, Decimal]) """
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


class CommissionPaidCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash paid for commissions in operating cash flow, using the direct method
    
    CommissionPaidCashFlowStatement(store: IDictionary[str, Decimal])
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


class CommonEquityToAssets(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This is a financial ratio of common stock equity to total assets that indicates the relative proportion of equity used to finance a
                company's assets.
    
    CommonEquityToAssets(store: IDictionary[str, Decimal])
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


class CommonStockBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Common stock (all issues) at par value, as reported within the Stockholder's Equity section of the balance sheet; i.e. it is one
                component of Common Stockholder's Equity
    
    CommonStockBalanceSheet(store: IDictionary[str, Decimal])
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


class CommonStockDividendPaidCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash outflow from the distribution of an entity's earnings in the form of dividends to common shareholders.
    
    CommonStockDividendPaidCashFlowStatement(store: IDictionary[str, Decimal])
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


class CommonStockEquityBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The portion of the Stockholders' Equity that reflects the amount of common stock, which are units of ownership.
    
    CommonStockEquityBalanceSheet(store: IDictionary[str, Decimal])
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


class CommonStockIssuanceCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash inflow from offering common stock, which is the additional capital contribution to the entity during the PeriodAsByte.
    
    CommonStockIssuanceCashFlowStatement(store: IDictionary[str, Decimal])
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


class CommonStockPaymentsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash outflow to reacquire common stock during the PeriodAsByte.
    
    CommonStockPaymentsCashFlowStatement(store: IDictionary[str, Decimal])
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


class CommonUtilityPlantBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount for the other plant related to the utility industry fix assets.
    
    CommonUtilityPlantBalanceSheet(store: IDictionary[str, Decimal])
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


class CompanyProfile(System.object):
    """
    Definition of the CompanyProfile class
    
    CompanyProfile()
    """
    def UpdateValues(self, update: QuantConnect.Data.Fundamental.CompanyProfile) -> None:
        pass

    AverageEmployeeNumber: int

    ContactEmail: str

    EnterpriseValue: int

    HeadquarterAddressLine1: str

    HeadquarterAddressLine2: str

    HeadquarterAddressLine3: str

    HeadquarterAddressLine4: str

    HeadquarterAddressLine5: str

    HeadquarterCity: str

    HeadquarterCountry: str

    HeadquarterFax: str

    HeadquarterHomepage: str

    HeadquarterPhone: str

    HeadquarterPostalCode: str

    HeadquarterProvince: str

    IsHeadOfficeSameWithRegisteredOfficeFlag: bool

    MarketCap: int

    ReasonofSharesChange: str

    RegisteredAddressLine1: str

    RegisteredAddressLine2: str

    RegisteredAddressLine3: str

    RegisteredAddressLine4: str

    RegisteredCity: str

    RegisteredCountry: str

    RegisteredFax: str

    RegisteredPhone: str

    RegisteredPostalCode: str

    RegisteredProvince: str

    ShareClassLevelSharesOutstanding: int

    SharesOutstanding: int

    SharesOutstandingWithBalanceSheetEndingDate: int

    TotalEmployeeNumber: int



class CompanyReference(System.object):
    """
    Definition of the CompanyReference class
    
    CompanyReference()
    """
    def UpdateValues(self, update: QuantConnect.Data.Fundamental.CompanyReference) -> None:
        pass

    Advisor: str

    AdvisorLanguageCode: str

    Auditor: str

    AuditorLanguageCode: str

    BusinessCountryID: str

    CIK: str

    CompanyId: str

    CompanyStatus: str

    CountryId: str

    ExpectedFiscalYearEnd: datetime.datetime

    FiscalYearEnd: int

    IndustryTemplateCode: str

    IsLimitedLiabilityCompany: bool

    IsLimitedPartnership: bool

    IsREIT: bool

    LegalName: str

    LegalNameLanguageCode: str

    PrimaryExchangeID: str

    PrimaryMIC: str

    PrimaryShareClassID: str

    PrimarySymbol: str

    ReportStyle: int

    ShortName: str

    StandardName: str

    YearofEstablishment: str



class ComTreShaNumBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The treasury stock number of common shares. This represents the number of common shares owned by the company as a result of
                share repurchase programs or donations.
    
    ComTreShaNumBalanceSheet(store: IDictionary[str, Decimal])
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


class ConstructionInProgressBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    It represents carrying amount of long-lived asset under construction that includes construction costs to date on capital projects.
                Assets constructed, but not completed.
    
    ConstructionInProgressBalanceSheet(store: IDictionary[str, Decimal])
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


class ConsumerLoanBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A loan that establishes consumer credit that is granted for personal use; usually unsecured and based on the borrower's integrity
                and ability to pay.
    
    ConsumerLoanBalanceSheet(store: IDictionary[str, Decimal])
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


class ContinuingAndDiscontinuedBasicEPS(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Basic EPS from Continuing Operations plus Basic EPS from Discontinued Operations.
    
    ContinuingAndDiscontinuedBasicEPS(store: IDictionary[str, Decimal])
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


class ContinuingAndDiscontinuedDilutedEPS(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Diluted EPS from Continuing Operations plus Diluted EPS from Discontinued Operations.
    
    ContinuingAndDiscontinuedDilutedEPS(store: IDictionary[str, Decimal])
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


class ConvertibleLoansCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This represents loans that entitle the lender (or the holder of loan debenture) to convert the loan to common or preferred stock
                (ordinary or preference shares) within the next 12 months or operating cycle.
    
    ConvertibleLoansCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class ConvertibleLoansNonCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A long term loan with a warrant attached that gives the debt holder the option to exchange all or a portion of the loan principal for
                an equity position in the company at a predetermined rate of conversion within a specified period of time.
    
    ConvertibleLoansNonCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class ConvertibleLoansTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Loans that entitles the lender (or the holder of loan debenture) to convert the loan to common or preferred stock (ordinary or
                preference shares) at a specified rate conversion rate and a specified time frame; in a Non-Differentiated Balance Sheet.
    
    ConvertibleLoansTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class CostOfRevenueIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate cost of goods produced and sold and services rendered during the reporting PeriodAsByte. It excludes all operating
                expenses such as depreciation, depletion, amortization, and SG&A. For the must have cost industry, if the number is not reported
                by the company, it will be calculated based on accounting equation.
                Cost of Revenue = Revenue - Operating Expenses - Operating Profit.
    
    CostOfRevenueIncomeStatement(store: IDictionary[str, Decimal])
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


class CreditCardIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Income earned from credit card services including late, over limit, and annual fees. This item is usually only available for bank
                industry.
    
    CreditCardIncomeStatement(store: IDictionary[str, Decimal])
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


class CreditLossesProvisionIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A charge to income which represents an expense deemed adequate by management given the composition of a bank's credit
                portfolios, their probability of default, the economic environment and the allowance for credit losses already established. Specific
                provisions are established to reduce the book value of specific assets (primarily loans) to establish the amount expected to be
                recovered on the loans.
    
    CreditLossesProvisionIncomeStatement(store: IDictionary[str, Decimal])
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


class CreditRiskProvisionsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Provision for the risk of loss of principal or loss of a financial reward stemming from a borrower's failure to repay a loan or otherwise
                meet a contractual obligation. Credit risk arises whenever a borrower is expecting to use future cash flows to pay a current debt.
                Investors are compensated for assuming credit risk by way of interest payments from the borrower or issuer of a debt obligation.
                This is a contra account under Total Revenue in banks.
    
    CreditRiskProvisionsIncomeStatement(store: IDictionary[str, Decimal])
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


class CurrentAccruedExpensesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An expense recognized before it is paid for. Includes compensation, interest, pensions and all other miscellaneous accruals
                reported by the company. Expenses incurred during the accounting period, but not required to be paid until a later date.
    
    CurrentAccruedExpensesBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The total amount of assets considered to be convertible into cash within a relatively short period of time, usually a year.
    
    CurrentAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentCapitalLeaseObligationBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents the total amount of long-term capital leases that must be paid within the next accounting PeriodAsByte. Capital lease
                obligations are contractual obligations that arise from obtaining the use of property or equipment via a capital lease contract.
    
    CurrentCapitalLeaseObligationBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentDebtAndCapitalLeaseObligationBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    All borrowings due within one year including current portions of long-term debt and capital leases as well as short-term debt such
                as bank loans and commercial paper.
    
    CurrentDebtAndCapitalLeaseObligationBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentDebtBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents the total amount of long-term debt such as bank loans and commercial paper, which is due within one year.
    
    CurrentDebtBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentDeferredAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Payments that will be assigned as expenses with one accounting period, but that are paid in advance and temporarily set up as
                current assets on the balance sheet.
    
    CurrentDeferredAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentDeferredLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents the current portion of obligations, which is a liability that usually would have been paid but is now past due.
    
    CurrentDeferredLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentDeferredRevenueBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents collections of cash or other assets related to revenue producing activity for which revenue has not yet been recognized.
                Generally, an entity records deferred revenue when it receives consideration from a customer before achieving certain criteria that
                must be met for revenue to be recognized in conformity with GAAP. It can be either current or non-current item. Also called
                unearned revenue.
    
    CurrentDeferredRevenueBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentDeferredTaxesAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Meaning a future tax asset, resulting from temporary differences between book (accounting) value of assets and liabilities and their
                tax value, or timing differences between the recognition of gains and losses in financial statements and their recognition in a tax
                computation. It is also called future tax.
    
    CurrentDeferredTaxesAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentDeferredTaxesLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Meaning a future tax liability, resulting from temporary differences between book (accounting) value of assets and liabilities and
                their tax value, or timing differences between the recognition of gains and losses in financial statements and their recognition in a
                tax computation. Deferred tax liabilities generally arise where tax relief is provided in advance of an accounting expense, or income
                is accrued but not taxed until received.
    
    CurrentDeferredTaxesLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The debts or obligations of the firm that are due within one year.
    
    CurrentLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentNotesPayableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Written promises to pay a stated sum at one or more specified dates in the future, within the accounting PeriodAsByte.
    
    CurrentNotesPayableBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentOtherFinancialLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other short term financial liabilities not categorized and due within one year or a normal operating cycle (whichever is longer).
    
    CurrentOtherFinancialLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class CurrentProvisionsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Provisions are created to protect the interests of one or both parties named in a contract or legal document which is a preparatory
                action or measure. Current provision is expired within one accounting PeriodAsByte.
    
    CurrentProvisionsBalanceSheet(store: IDictionary[str, Decimal])
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

    TwoMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class CurrentRatio(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of Current Assets to Current Liabilities. Morningstar calculates the ratio by using the underlying data reported in
                the Balance Sheet within the company filings or reports:     Current Assets / Current Liabilities.
    
    CurrentRatio(store: IDictionary[str, Decimal])
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


class CurrentRatioGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's current ratio on a percentage basis. Morningstar calculates the growth percentage based on the
                current assets divided by current liabilities reported in the Balance Sheet within the company filings or reports.
    
    CurrentRatioGrowth(store: IDictionary[str, Decimal])
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


class CustomerAcceptancesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Amounts receivable from customers on short-term negotiable time drafts drawn on and accepted by the institution (also known as
                banker's acceptance transactions) that are outstanding on the reporting date.
    
    CustomerAcceptancesBalanceSheet(store: IDictionary[str, Decimal])
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


class CustomerAccountsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Carrying value of amounts transferred by customers to third parties for security purposes that are expected to be returned or
                applied towards payment after one year or beyond the operating cycle, if longer.
    
    CustomerAccountsBalanceSheet(store: IDictionary[str, Decimal])
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


class DaysInInventory(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    365 / Inventory turnover
    
    DaysInInventory(store: IDictionary[str, Decimal])
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


class DaysInPayment(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    365 / Payable turnover
    
    DaysInPayment(store: IDictionary[str, Decimal])
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


class DaysInSales(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    365 / Receivable Turnover
    
    DaysInSales(store: IDictionary[str, Decimal])
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


class DDACostofRevenueIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Costs of depreciation and amortization on assets used for the revenue-generating activities during the accounting period
    
    DDACostofRevenueIncomeStatement(store: IDictionary[str, Decimal])
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


class DebtDueBeyondBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Debt maturing beyond 5 years (eg. 5-10 years) or with no specified maturity, according to the debt maturity schedule reported by
                the company.
    
    DebtDueBeyondBalanceSheet(store: IDictionary[str, Decimal])
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


class DebtDueInYear1BalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Debt due under 1 year according to the debt maturity schedule reported by the company.
    
    DebtDueInYear1BalanceSheet(store: IDictionary[str, Decimal])
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


class DebtDueInYear2BalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Debt due under 2 years according to the debt maturity schedule reported by the company.
    
    DebtDueInYear2BalanceSheet(store: IDictionary[str, Decimal])
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


class DebtDueInYear5BalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Debt due within 5 year if the company provide maturity schedule in range e.g. 1-5 years, 2-5 years. Debt due under 5 years
                according to the debt maturity schedule reported by the company. If a range is reported by the company, the value will be collected
                under the maximum number of years (eg. 1-5 years, 3-5 years or 5 years will all be collected under this data point.)
    
    DebtDueInYear5BalanceSheet(store: IDictionary[str, Decimal])
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


class DebtSecuritiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Debt securities held as investments.
    
    DebtSecuritiesBalanceSheet(store: IDictionary[str, Decimal])
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


class DebtSecuritiesinIssueBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Any debt financial instrument issued instead of cash loan.
    
    DebtSecuritiesinIssueBalanceSheet(store: IDictionary[str, Decimal])
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


class DebttoAssets(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This is a leverage ratio used to determine how much debt (a sum of long term and current portion of debt) a company has on its
                balance sheet relative to total assets. This ratio examines the percent of the company that is financed by debt.
    
    DebttoAssets(store: IDictionary[str, Decimal])
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


class DebtTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The total aggregate of all written promises and/or agreements to repay a stated amount of borrowed funds at a specified date in
                the future; in a Non-Differentiated Balance Sheet.
    
    DebtTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class DecreaseinInterestBearingDepositsinBankCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net change on interest-bearing deposits in other financial institutions for relatively short periods of time including, for example,
                certificates of deposits.
    
    DecreaseinInterestBearingDepositsinBankCashFlowStatement(store: IDictionary[str, Decimal])
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


class DeferredAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An amount owed to a firm that is not expected to be received by the firm within one year from the date of the balance sheet.
    
    DeferredAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class DeferredCostsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An expenditure not recognized as a cost of operation of the period in which incurred, but carried forward to be written off in future
                periods.
    
    DeferredCostsBalanceSheet(store: IDictionary[str, Decimal])
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


class DeferredIncomeTaxCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The component of income tax expense for the period representing the net change in the entities deferred tax assets and liabilities
                pertaining to continuing operations.
    
    DeferredIncomeTaxCashFlowStatement(store: IDictionary[str, Decimal])
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


class DeferredIncomeTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Collections of cash or other assets related to revenue producing activity for which revenue has not yet been recognized on a Non-
                Differentiated Balance Sheet.
    
    DeferredIncomeTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class DeferredPolicyAcquisitionCostsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Net amount of deferred policy acquisition costs capitalized on contracts remaining in force as of the balance sheet date.
    
    DeferredPolicyAcquisitionCostsBalanceSheet(store: IDictionary[str, Decimal])
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


class DeferredTaxAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An asset on a company's balance sheet that may be used to reduce any subsequent period's income tax expense. Deferred tax
                assets can arise due to net loss carryovers, which are only recorded as assets if it is deemed more likely than not that the asset
                will be used in future fiscal periods.
    
    DeferredTaxAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class DeferredTaxCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Future tax liability or asset, resulting from temporary differences between book (accounting) value of assets and liabilities, and their
                tax value. This arises due to differences between financial accounting for shareholders and tax accounting.
    
    DeferredTaxCashFlowStatement(store: IDictionary[str, Decimal])
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


class DeferredTaxLiabilitiesTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A future tax liability, resulting from temporary differences between book (accounting) value of assets and liabilities and their tax
                value or timing differences between the recognition of gains and losses in financial statements, on a Non-Differentiated Balance
                Sheet.
    
    DeferredTaxLiabilitiesTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class DefinedPensionBenefitBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The recognition of an asset where pension fund assets exceed promised benefits.
    
    DefinedPensionBenefitBalanceSheet(store: IDictionary[str, Decimal])
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


class DepletionCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Unlike depreciation and amortization, which mainly describe the deduction of expenses due to the aging of equipment and property,
                depletion is the actual physical reduction of natural resources by companies.   For example, coalmines, oil fields and other natural
                resources are depleted on company accounting statements. This reduction in the quantity of resources is meant to assist in
                accurately identifying the value of the asset on the balance sheet.
    
    DepletionCashFlowStatement(store: IDictionary[str, Decimal])
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


class DepletionIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The non-cash expense recognized on natural resources (eg. Oil and mineral deposits) over the benefit period of the asset.
    
    DepletionIncomeStatement(store: IDictionary[str, Decimal])
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


class DepositCertificatesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A savings certificate entitling the bearer to receive interest. A CD bears a maturity date, a specified fixed interest rate and can be
                issued in any denomination.
    
    DepositCertificatesBalanceSheet(store: IDictionary[str, Decimal])
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


class DepositsbyBankBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Banks investment in the ongoing entity.
    
    DepositsbyBankBalanceSheet(store: IDictionary[str, Decimal])
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


class DepositsMadeunderAssumedReinsuranceContractBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Deposits made under reinsurance.
    
    DepositsMadeunderAssumedReinsuranceContractBalanceSheet(store: IDictionary[str, Decimal])
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


class DepositsReceivedunderCededInsuranceContractBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Deposit received through ceded insurance contract.
    
    DepositsReceivedunderCededInsuranceContractBalanceSheet(store: IDictionary[str, Decimal])
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


class DepreciationAmortizationDepletionCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    It is a non cash charge that represents a reduction in the value of fixed assets due to wear, age or obsolescence. This figure also
                includes amortization of leased property, intangibles, and goodwill, and depletion. This non-cash item is an add-back to the cash
                flow statement.
    
    DepreciationAmortizationDepletionCashFlowStatement(store: IDictionary[str, Decimal])
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


class DepreciationAmortizationDepletionIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The sum of depreciation, amortization and depletion expense in the Income Statement.
                Depreciation is the non-cash expense recognized on tangible assets used in the normal course of business, by allocating the cost of
                assets over their useful lives
                Amortization is the non-cash expense recognized on intangible assets over the benefit period of the asset.
                Depletion is the non-cash expense recognized on natural resources (eg. Oil and mineral deposits) over the benefit period of the
                asset.
    
    DepreciationAmortizationDepletionIncomeStatement(store: IDictionary[str, Decimal])
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


class DepreciationAndAmortizationCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The current period expense charged against earnings on long-lived, physical assets used in the normal conduct of business and not
                intended for resale to allocate or recognize the cost of assets over their useful lives; or to record the reduction in book value of an
                intangible asset over the benefit period of such asset.
    
    DepreciationAndAmortizationCashFlowStatement(store: IDictionary[str, Decimal])
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


class DepreciationAndAmortizationIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The sum of depreciation and amortization expense in the Income Statement.
                Depreciation is the non-cash expense recognized on tangible assets used in the normal course of business, by allocating the cost of
                assets over their useful lives
                Amortization is the non-cash expense recognized on intangible assets over the benefit period of the asset.
    
    DepreciationAndAmortizationIncomeStatement(store: IDictionary[str, Decimal])
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


class DepreciationCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An expense recorded to allocate a tangible asset's cost over its useful life. Since it is a non-cash expense, it increases free cash
                flow while decreasing reported earnings.
    
    DepreciationCashFlowStatement(store: IDictionary[str, Decimal])
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


class DepreciationIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The current period non-cash expense recognized on tangible assets used in the normal course of business, by allocating the cost of
                assets over their useful lives, in the Income Statement. Examples of tangible asset include buildings, production and equipment.
    
    DepreciationIncomeStatement(store: IDictionary[str, Decimal])
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


class DepreciationSupplementalIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The current period expense charged against earnings on tangible asset over its useful life. It is a supplemental value which would
                be reported outside consolidated statements.
    
    DepreciationSupplementalIncomeStatement(store: IDictionary[str, Decimal])
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


class DuefromRelatedPartiesCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Amounts owed to the company from a non-arm's length entity, due within the company's current operating cycle.
    
    DuefromRelatedPartiesCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class DuefromRelatedPartiesNonCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Amounts owed to the company from a non-arm's length entity, due after the company's current operating cycle.
    
    DuefromRelatedPartiesNonCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class DuetoRelatedPartiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Amounts owed by the company to a non-arm's length entity.
    
    DuetoRelatedPartiesBalanceSheet(store: IDictionary[str, Decimal])
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


class DuetoRelatedPartiesCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Amounts owed by the company to a non-arm's length entity that has to be repaid within the company's current operating cycle.
    
    DuetoRelatedPartiesCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class DuetoRelatedPartiesNonCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Amounts owed by the company to a non-arm's length entity that has to be repaid after the company's current operating cycle.
    
    DuetoRelatedPartiesNonCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class EarningRatios(System.object):
    """
    Definition of the EarningRatios class
    
    EarningRatios()
    """
    def UpdateValues(self, update: QuantConnect.Data.Fundamental.EarningRatios) -> None:
        pass

    BookValuePerShareGrowth: QuantConnect.Data.Fundamental.BookValuePerShareGrowth

    DilutedContEPSGrowth: QuantConnect.Data.Fundamental.DilutedContEPSGrowth

    DilutedEPSGrowth: QuantConnect.Data.Fundamental.DilutedEPSGrowth

    DPSGrowth: QuantConnect.Data.Fundamental.DPSGrowth

    EquityPerShareGrowth: QuantConnect.Data.Fundamental.EquityPerShareGrowth

    FCFPerShareGrowth: QuantConnect.Data.Fundamental.FCFPerShareGrowth

    NormalizedBasicEPSGrowth: QuantConnect.Data.Fundamental.NormalizedBasicEPSGrowth

    NormalizedDilutedEPSGrowth: QuantConnect.Data.Fundamental.NormalizedDilutedEPSGrowth

    RegressionGrowthofDividends5Years: QuantConnect.Data.Fundamental.RegressionGrowthofDividends5Years



class EarningReports(System.object):
    """
    Definition of the EarningReports class
    
    EarningReports()
    """
    def UpdateValues(self, update: QuantConnect.Data.Fundamental.EarningReports) -> None:
        pass

    AccessionNumber: str

    BasicAccountingChange: QuantConnect.Data.Fundamental.BasicAccountingChange

    BasicAverageShares: QuantConnect.Data.Fundamental.BasicAverageShares

    BasicContinuousOperations: QuantConnect.Data.Fundamental.BasicContinuousOperations

    BasicDiscontinuousOperations: QuantConnect.Data.Fundamental.BasicDiscontinuousOperations

    BasicEPS: QuantConnect.Data.Fundamental.BasicEPS

    BasicEPSOtherGainsLosses: QuantConnect.Data.Fundamental.BasicEPSOtherGainsLosses

    BasicExtraordinary: QuantConnect.Data.Fundamental.BasicExtraordinary

    ContinuingAndDiscontinuedBasicEPS: QuantConnect.Data.Fundamental.ContinuingAndDiscontinuedBasicEPS

    ContinuingAndDiscontinuedDilutedEPS: QuantConnect.Data.Fundamental.ContinuingAndDiscontinuedDilutedEPS

    DilutedAccountingChange: QuantConnect.Data.Fundamental.DilutedAccountingChange

    DilutedAverageShares: QuantConnect.Data.Fundamental.DilutedAverageShares

    DilutedContinuousOperations: QuantConnect.Data.Fundamental.DilutedContinuousOperations

    DilutedDiscontinuousOperations: QuantConnect.Data.Fundamental.DilutedDiscontinuousOperations

    DilutedEPS: QuantConnect.Data.Fundamental.DilutedEPS

    DilutedEPSOtherGainsLosses: QuantConnect.Data.Fundamental.DilutedEPSOtherGainsLosses

    DilutedExtraordinary: QuantConnect.Data.Fundamental.DilutedExtraordinary

    DividendCoverageRatio: QuantConnect.Data.Fundamental.DividendCoverageRatio

    DividendPerShare: QuantConnect.Data.Fundamental.DividendPerShare

    FileDate: datetime.datetime

    FormType: str

    NormalizedBasicEPS: QuantConnect.Data.Fundamental.NormalizedBasicEPS

    NormalizedDilutedEPS: QuantConnect.Data.Fundamental.NormalizedDilutedEPS

    PeriodEndingDate: datetime.datetime

    PeriodType: str

    ReportedNormalizedBasicEPS: QuantConnect.Data.Fundamental.ReportedNormalizedBasicEPS

    ReportedNormalizedDilutedEPS: QuantConnect.Data.Fundamental.ReportedNormalizedDilutedEPS

    TaxLossCarryforwardBasicEPS: QuantConnect.Data.Fundamental.TaxLossCarryforwardBasicEPS

    TaxLossCarryforwardDilutedEPS: QuantConnect.Data.Fundamental.TaxLossCarryforwardDilutedEPS

    TotalDividendPerShare: QuantConnect.Data.Fundamental.TotalDividendPerShare



class EarningsFromEquityInterestIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The earnings from equity interest can be a result of any of the following: Income from earnings distribution of the business, either
                as dividends paid to corporate shareholders or as drawings in a partnership; Capital gain realized upon sale of the business; Capital
                gain realized from selling his or her interest to other partners. This item is usually not available for bank and insurance industries.
    
    EarningsFromEquityInterestIncomeStatement(store: IDictionary[str, Decimal])
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


class EarningsfromEquityInterestNetOfTaxIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Income from other equity interest reported after Provision of Tax. This applies to all industries.
    
    EarningsfromEquityInterestNetOfTaxIncomeStatement(store: IDictionary[str, Decimal])
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


class EarningsLossesFromEquityInvestmentsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This item represents the entity's proportionate share for the period of the net income (loss) of its investee (such as unconsolidated
                subsidiaries and joint ventures) to which the equity method of accounting is applied. The amount typically reflects adjustments.
    
    EarningsLossesFromEquityInvestmentsCashFlowStatement(store: IDictionary[str, Decimal])
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


class EBITDAGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's EBITDA on a percentage basis. Morningstar calculates the growth percentage based on the earnings
                minus expenses (excluding interest, tax, depreciation, and amortization expenses) reported in the Financial Statements within the
                company filings or reports.
    
    EBITDAGrowth(store: IDictionary[str, Decimal])
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


class FederalFundsSoldAndSecuritiesPurchaseUnderAgreementsToResellBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This asset refers to very-short-term loans of funds to other banks and securities dealers.
    
    FederalFundsSoldAndSecuritiesPurchaseUnderAgreementsToResellBalanceSheet(store: IDictionary[str, Decimal])
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


class FederalFundsSoldBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Federal funds transactions involve lending (federal funds sold) or borrowing (federal funds purchased) of immediately available
                reserve balances.  This item is typically available for the bank industry.
    
    FederalFundsSoldBalanceSheet(store: IDictionary[str, Decimal])
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


class FederalHomeLoanBankStockBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Federal Home Loan Bank stock represents an equity interest in a FHLB. It does not have a readily determinable fair value because
                its ownership is restricted and it lacks a market (liquidity).  This item is typically available for the bank industry.
    
    FederalHomeLoanBankStockBalanceSheet(store: IDictionary[str, Decimal])
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


class FeeRevenueAndOtherIncomeIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of fees, commissions, and other income.
    
    FeeRevenueAndOtherIncomeIncomeStatement(store: IDictionary[str, Decimal])
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


class FeesandCommissionExpenseIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cost incurred by bank and insurance companies for fees and commission income.
    
    FeesandCommissionExpenseIncomeStatement(store: IDictionary[str, Decimal])
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


class FeesandCommissionIncomeIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Fees and commission income earned by bank and insurance companies on the rendering services.
    
    FeesandCommissionIncomeIncomeStatement(store: IDictionary[str, Decimal])
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


class FeesAndCommissionsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total fees and commissions earned from providing services such as leasing of space or maintaining: (1) depositor accounts; (2)
                transfer agent; (3) fiduciary and trust; (4) brokerage and underwriting; (5) mortgage; (6) credit cards; (7) correspondent clearing;
                and (8) other such services and activities performed for others. This item is usually available for bank and insurance industries.
    
    FeesAndCommissionsIncomeStatement(store: IDictionary[str, Decimal])
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


class FinanceLeaseReceivablesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Accounts owed to the bank in relation to capital leases. Capital/ finance lease obligation are contractual obligations that arise from
                obtaining the use of property or equipment via a capital lease contract.
    
    FinanceLeaseReceivablesBalanceSheet(store: IDictionary[str, Decimal])
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


class FinanceLeaseReceivablesCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Accounts owed to the bank in relation to capital leases to be received within the next accounting PeriodAsByte. Capital/ finance lease
                obligations are contractual obligations that arise from obtaining the use of property or equipment via a capital lease contract.
    
    FinanceLeaseReceivablesCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class FinanceLeaseReceivablesNonCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Accounts owed to the bank in relation to capital leases to be received beyond the next accounting PeriodAsByte. Capital/ finance lease
                obligations are contractual obligations that arise from obtaining the use of property or equipment via a capital lease contract.
    
    FinanceLeaseReceivablesNonCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class FinancialAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Fair values as of the balance sheet date of all assets resulting from contracts that meet the criteria of being accounted for as
                derivative instruments, net of the effects of master netting arrangements.
    
    FinancialAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class FinancialAssetsDesignatedasFairValueThroughProfitorLossTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Financial assets that are held at fair value through profit or loss comprise assets held for trading and those financial assets
                designated as being held at fair value through profit or loss.
    
    FinancialAssetsDesignatedasFairValueThroughProfitorLossTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class FinancialInstrumentsSoldUnderAgreementsToRepurchaseBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The carrying value as of the balance sheet date of securities that an institution sells and agrees to repurchase (the identical or
                substantially the same securities) as a seller-borrower at a specified date for a specified price, also known as a repurchase
                agreement.  This item is typically available for bank industry.
    
    FinancialInstrumentsSoldUnderAgreementsToRepurchaseBalanceSheet(store: IDictionary[str, Decimal])
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


class FinancialLeverage(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of Total Assets to Common Equity. Morningstar calculates the ratio by using the underlying data reported in the
                Balance Sheet within the company filings or reports:    Total Assets / Common Equity.   [Note: Common Equity = Total
                Shareholder's Equity - Preferred Stock]
    
    FinancialLeverage(store: IDictionary[str, Decimal])
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


class FinancialLiabilitiesCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Financial related liabilities due within one year, including short term and current portions of long-term debt, capital leases and
                derivative liabilities.
    
    FinancialLiabilitiesCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class FinancialLiabilitiesDesignatedasFairValueThroughProfitorLossTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Financial liabilities that are held at fair value through profit or loss.
    
    FinancialLiabilitiesDesignatedasFairValueThroughProfitorLossTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class FinancialLiabilitiesMeasuredatAmortizedCostTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Financial liabilities carried at amortized cost.
    
    FinancialLiabilitiesMeasuredatAmortizedCostTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class FinancialLiabilitiesNonCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Financial related liabilities due beyond one year, including long term debt, capital leases and derivative liabilities.
    
    FinancialLiabilitiesNonCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class FinancialOrDerivativeInvestmentCurrentLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Financial instruments that are linked to a specific financial instrument or indicator or commodity, and through which specific
                financial risks can be traded in financial markets in their own right, such as financial options, futures, forwards, etc.
    
    FinancialOrDerivativeInvestmentCurrentLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class FinancialStatements(System.object):
    """
    Definition of the FinancialStatements class
    
    FinancialStatements()
    """
    def UpdateValues(self, update: QuantConnect.Data.Fundamental.FinancialStatements) -> None:
        pass

    AccessionNumber: str

    AuditorReportStatus: str

    BalanceSheet: QuantConnect.Data.Fundamental.BalanceSheet

    CashFlowStatement: QuantConnect.Data.Fundamental.CashFlowStatement

    FileDate: datetime.datetime

    FormType: str

    IncomeStatement: QuantConnect.Data.Fundamental.IncomeStatement

    InventoryValuationMethod: str

    NumberOfShareHolders: int

    PeriodAuditor: str

    PeriodEndingDate: datetime.datetime

    PeriodType: str

    TotalRiskBasedCapital: QuantConnect.Data.Fundamental.TotalRiskBasedCapital



class FinancingCashFlowCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net cash inflow (outflow) from financing activity for the period, which involve changes to the long-term liabilities and
                stockholders' equity.
    
    FinancingCashFlowCashFlowStatement(store: IDictionary[str, Decimal])
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


class FineFundamental(QuantConnect.Data.BaseData, QuantConnect.Data.IBaseData):
    """
    Definition of the FineFundamental class
    
    FineFundamental()
    """
    @staticmethod
    def CreateUniverseSymbol(market: str, addGuid: bool) -> QuantConnect.Symbol:
        pass

    @typing.overload
    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        pass

    @typing.overload
    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, datafeed: QuantConnect.DataFeedEndpoint) -> str:
        pass

    def GetSource(self, *args) -> str:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, stream: System.IO.StreamReader, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, datafeed: QuantConnect.DataFeedEndpoint) -> QuantConnect.Data.BaseData:
        pass

    def Reader(self, *args) -> QuantConnect.Data.BaseData:
        pass

    def UpdateValues(self, update: QuantConnect.Data.Fundamental.FineFundamental) -> None:
        pass

    AssetClassification: QuantConnect.Data.Fundamental.AssetClassification

    CompanyProfile: QuantConnect.Data.Fundamental.CompanyProfile

    CompanyReference: QuantConnect.Data.Fundamental.CompanyReference

    EarningRatios: QuantConnect.Data.Fundamental.EarningRatios

    EarningReports: QuantConnect.Data.Fundamental.EarningReports

    EndTime: datetime.datetime

    FinancialStatements: QuantConnect.Data.Fundamental.FinancialStatements

    MarketCap: int

    OperationRatios: QuantConnect.Data.Fundamental.OperationRatios

    SecurityReference: QuantConnect.Data.Fundamental.SecurityReference

    ValuationRatios: QuantConnect.Data.Fundamental.ValuationRatios



class FinishedGoodsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The carrying amount as of the balance sheet date of merchandise or goods held by the company that are readily available for sale.
                This item is typically available for mining and manufacturing industries.
    
    FinishedGoodsBalanceSheet(store: IDictionary[str, Decimal])
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


class FixAssetsTuronver(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Revenue / Average PP&E
    
    FixAssetsTuronver(store: IDictionary[str, Decimal])
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


class FixedAssetsRevaluationReserveBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Reserves created by revaluation of assets.
    
    FixedAssetsRevaluationReserveBalanceSheet(store: IDictionary[str, Decimal])
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


class FixedMaturityInvestmentsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This asset refers to types of investments that may be contained within the fixed maturity category which securities are having a
                stated final repayment date. Examples of items within this category may include bonds, including convertibles and bonds with
                warrants, and redeemable preferred stocks.
    
    FixedMaturityInvestmentsBalanceSheet(store: IDictionary[str, Decimal])
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


class FlightFleetVehicleAndRelatedEquipmentsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    It is one of the important fixed assets for transportation industry, which includes bicycles, cars, motorcycles, trains, ships, boats,
                and aircraft.  This item is typically available for transportation industry.
    
    FlightFleetVehicleAndRelatedEquipmentsBalanceSheet(store: IDictionary[str, Decimal])
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


class ForeclosedAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The carrying amount as of the balance sheet date of all assets obtained in full or partial satisfaction of a debt arrangement through
                foreclosure proceedings or defeasance; includes real and personal property; equity interests in corporations, partnerships, and joint
                ventures; and beneficial interest in trusts.  This item is typically typically available for bank industry.
    
    ForeclosedAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class ForeignCurrencyTranslationAdjustmentsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Changes to accumulated comprehensive income that results from the process of translating subsidiary financial statements and
                foreign equity investments into functional currency of the reporting company.
    
    ForeignCurrencyTranslationAdjustmentsBalanceSheet(store: IDictionary[str, Decimal])
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


class ForeignExchangeTradingGainsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Trading revenues that result from foreign exchange exposures such as cash instruments and off-balance sheet derivative
                instruments. This item is usually only available for bank industry.
    
    ForeignExchangeTradingGainsIncomeStatement(store: IDictionary[str, Decimal])
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


class FreeCashFlowCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash Flow Operations minus Capital Expenditures.
    
    FreeCashFlowCashFlowStatement(store: IDictionary[str, Decimal])
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


class FuelAndPurchasePowerIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cost of fuel, purchase power and gas associated with revenue generation. This item is usually only available for utility industry.
    
    FuelAndPurchasePowerIncomeStatement(store: IDictionary[str, Decimal])
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


class FuelIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of fuel cost for current period associated with the revenue generation. This item is usually only available for
                transportation industry.
    
    FuelIncomeStatement(store: IDictionary[str, Decimal])
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


class Fundamentals(QuantConnect.Data.Fundamental.FineFundamental, QuantConnect.Data.IBaseData):
    """
    Defines a merged viw of QuantConnect.Data.Fundamental.FineFundamental and QuantConnect.Data.UniverseSelection.CoarseFundamental
    
    Fundamentals()
    """
    @typing.overload
    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        pass

    @typing.overload
    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, datafeed: QuantConnect.DataFeedEndpoint) -> str:
        pass

    def GetSource(self, *args) -> str:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, stream: System.IO.StreamReader, date: datetime.datetime, isLiveMode: bool) -> QuantConnect.Data.BaseData:
        pass

    @typing.overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, datafeed: QuantConnect.DataFeedEndpoint) -> QuantConnect.Data.BaseData:
        pass

    def Reader(self, *args) -> QuantConnect.Data.BaseData:
        pass

    DollarVolume: float

    HasFundamentalData: bool

    Market: str

    Volume: int



class FundFromOperationCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Funds from operations; populated only for real estate investment trusts (REITs), defined as the sum of net income, gain/loss
                (realized and unrealized) on investment securities, asset impairment charge, depreciation and amortization and gain/ loss on the
                sale of business and property plant and equipment.
    
    FundFromOperationCashFlowStatement(store: IDictionary[str, Decimal])
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


class IncomeStatement(System.object):
    """
    Definition of the IncomeStatement class
    
    IncomeStatement()
    """
    def UpdateValues(self, update: QuantConnect.Data.Fundamental.IncomeStatement) -> None:
        pass

    Amortization: QuantConnect.Data.Fundamental.AmortizationIncomeStatement

    AmortizationOfIntangibles: QuantConnect.Data.Fundamental.AmortizationOfIntangiblesIncomeStatement

    AmortizationSupplemental: QuantConnect.Data.Fundamental.AmortizationSupplementalIncomeStatement

    AverageDilutionEarnings: QuantConnect.Data.Fundamental.AverageDilutionEarningsIncomeStatement

    CededPremiums: QuantConnect.Data.Fundamental.CededPremiumsIncomeStatement

    ChangeinInsuranceLiabilitiesNetofReinsurance: QuantConnect.Data.Fundamental.ChangeinInsuranceLiabilitiesNetofReinsuranceIncomeStatement

    ChangeinInvestmentContract: QuantConnect.Data.Fundamental.ChangeinInvestmentContractIncomeStatement

    ChangeinTheGrossProvisionforUnearnedPremiums: QuantConnect.Data.Fundamental.ChangeinTheGrossProvisionforUnearnedPremiumsIncomeStatement

    ChangeinTheGrossProvisionforUnearnedPremiumsReinsurersShare: QuantConnect.Data.Fundamental.ChangeinTheGrossProvisionforUnearnedPremiumsReinsurersShareIncomeStatement

    ClaimsandChangeinInsuranceLiabilities: QuantConnect.Data.Fundamental.ClaimsandChangeinInsuranceLiabilitiesIncomeStatement

    ClaimsandPaidIncurred: QuantConnect.Data.Fundamental.ClaimsandPaidIncurredIncomeStatement

    CommissionExpenses: QuantConnect.Data.Fundamental.CommissionExpensesIncomeStatement

    CostOfRevenue: QuantConnect.Data.Fundamental.CostOfRevenueIncomeStatement

    CreditCard: QuantConnect.Data.Fundamental.CreditCardIncomeStatement

    CreditLossesProvision: QuantConnect.Data.Fundamental.CreditLossesProvisionIncomeStatement

    CreditRiskProvisions: QuantConnect.Data.Fundamental.CreditRiskProvisionsIncomeStatement

    DDACostofRevenue: QuantConnect.Data.Fundamental.DDACostofRevenueIncomeStatement

    Depletion: QuantConnect.Data.Fundamental.DepletionIncomeStatement

    Depreciation: QuantConnect.Data.Fundamental.DepreciationIncomeStatement

    DepreciationAmortizationDepletion: QuantConnect.Data.Fundamental.DepreciationAmortizationDepletionIncomeStatement

    DepreciationAndAmortization: QuantConnect.Data.Fundamental.DepreciationAndAmortizationIncomeStatement

    DepreciationSupplemental: QuantConnect.Data.Fundamental.DepreciationSupplementalIncomeStatement

    DilutedNIAvailtoComStockholders: QuantConnect.Data.Fundamental.DilutedNIAvailtoComStockholdersIncomeStatement

    DividendIncome: QuantConnect.Data.Fundamental.DividendIncomeIncomeStatement

    EarningsFromEquityInterest: QuantConnect.Data.Fundamental.EarningsFromEquityInterestIncomeStatement

    EarningsfromEquityInterestNetOfTax: QuantConnect.Data.Fundamental.EarningsfromEquityInterestNetOfTaxIncomeStatement

    EBIT: QuantConnect.Data.Fundamental.EBITIncomeStatement

    EBITDA: QuantConnect.Data.Fundamental.EBITDAIncomeStatement

    EffectiveTaxRateAsReported: QuantConnect.Data.Fundamental.EffectiveTaxRateAsReportedIncomeStatement

    Equipment: QuantConnect.Data.Fundamental.EquipmentIncomeStatement

    ExciseTaxes: QuantConnect.Data.Fundamental.ExciseTaxesIncomeStatement

    ExplorationDevelopmentAndMineralPropertyLeaseExpenses: QuantConnect.Data.Fundamental.ExplorationDevelopmentAndMineralPropertyLeaseExpensesIncomeStatement

    FeeRevenueAndOtherIncome: QuantConnect.Data.Fundamental.FeeRevenueAndOtherIncomeIncomeStatement

    FeesandCommissionExpense: QuantConnect.Data.Fundamental.FeesandCommissionExpenseIncomeStatement

    FeesandCommissionIncome: QuantConnect.Data.Fundamental.FeesandCommissionIncomeIncomeStatement

    FeesAndCommissions: QuantConnect.Data.Fundamental.FeesAndCommissionsIncomeStatement

    ForeignExchangeTradingGains: QuantConnect.Data.Fundamental.ForeignExchangeTradingGainsIncomeStatement

    Fuel: QuantConnect.Data.Fundamental.FuelIncomeStatement

    FuelAndPurchasePower: QuantConnect.Data.Fundamental.FuelAndPurchasePowerIncomeStatement

    GainLossonDerecognitionofAvailableForSaleFinancialAssets: QuantConnect.Data.Fundamental.GainLossonDerecognitionofAvailableForSaleFinancialAssetsIncomeStatement

    GainLossonFinancialInstrumentsDesignatedasCashFlowHedges: QuantConnect.Data.Fundamental.GainLossonFinancialInstrumentsDesignatedasCashFlowHedgesIncomeStatement

    GainLossonSaleofAssets: QuantConnect.Data.Fundamental.GainLossonSaleofAssetsIncomeStatement

    GainonInvestmentProperties: QuantConnect.Data.Fundamental.GainonInvestmentPropertiesIncomeStatement

    GainOnSaleOfBusiness: QuantConnect.Data.Fundamental.GainOnSaleOfBusinessIncomeStatement

    GainonSaleofInvestmentProperty: QuantConnect.Data.Fundamental.GainonSaleofInvestmentPropertyIncomeStatement

    GainonSaleofLoans: QuantConnect.Data.Fundamental.GainonSaleofLoansIncomeStatement

    GainOnSaleOfPPE: QuantConnect.Data.Fundamental.GainOnSaleOfPPEIncomeStatement

    GainOnSaleOfSecurity: QuantConnect.Data.Fundamental.GainOnSaleOfSecurityIncomeStatement

    GainsLossesonFinancialInstrumentsDuetoFairValueAdjustmentsinHedgeAccountingTotal: QuantConnect.Data.Fundamental.GainsLossesonFinancialInstrumentsDuetoFairValueAdjustmentsinHedgeAccountingTotalIncomeStatement

    GeneralAndAdministrativeExpense: QuantConnect.Data.Fundamental.GeneralAndAdministrativeExpenseIncomeStatement

    GrossDividendPayment: QuantConnect.Data.Fundamental.GrossDividendPaymentIncomeStatement

    GrossPremiumsWritten: QuantConnect.Data.Fundamental.GrossPremiumsWrittenIncomeStatement

    GrossProfit: QuantConnect.Data.Fundamental.GrossProfitIncomeStatement

    ImpairmentLossesReversalsFinancialInstrumentsNet: QuantConnect.Data.Fundamental.ImpairmentLossesReversalsFinancialInstrumentsNetIncomeStatement

    ImpairmentOfCapitalAssets: QuantConnect.Data.Fundamental.ImpairmentOfCapitalAssetsIncomeStatement

    IncomefromAssociatesandOtherParticipatingInterests: QuantConnect.Data.Fundamental.IncomefromAssociatesandOtherParticipatingInterestsIncomeStatement

    IncreaseDecreaseInNetUnearnedPremiumReserves: QuantConnect.Data.Fundamental.IncreaseDecreaseInNetUnearnedPremiumReservesIncomeStatement

    InsuranceAndClaims: QuantConnect.Data.Fundamental.InsuranceAndClaimsIncomeStatement

    InterestExpense: QuantConnect.Data.Fundamental.InterestExpenseIncomeStatement

    InterestExpenseForDeposit: QuantConnect.Data.Fundamental.InterestExpenseForDepositIncomeStatement

    InterestExpenseForFederalFundsSoldAndSecuritiesPurchaseUnderAgreementsToResell: QuantConnect.Data.Fundamental.InterestExpenseForFederalFundsSoldAndSecuritiesPurchaseUnderAgreementsToResellIncomeStatement

    InterestExpenseForLongTermDebtAndCapitalSecurities: QuantConnect.Data.Fundamental.InterestExpenseForLongTermDebtAndCapitalSecuritiesIncomeStatement

    InterestExpenseForShortTermDebt: QuantConnect.Data.Fundamental.InterestExpenseForShortTermDebtIncomeStatement

    InterestExpenseNonOperating: QuantConnect.Data.Fundamental.InterestExpenseNonOperatingIncomeStatement

    InterestIncome: QuantConnect.Data.Fundamental.InterestIncomeIncomeStatement

    InterestIncomeAfterProvisionForLoanLoss: QuantConnect.Data.Fundamental.InterestIncomeAfterProvisionForLoanLossIncomeStatement

    InterestIncomeFromDeposits: QuantConnect.Data.Fundamental.InterestIncomeFromDepositsIncomeStatement

    InterestIncomeFromFederalFundsSoldAndSecuritiesPurchaseUnderAgreementsToResell: QuantConnect.Data.Fundamental.InterestIncomeFromFederalFundsSoldAndSecuritiesPurchaseUnderAgreementsToResellIncomeStatement

    InterestIncomeFromLeases: QuantConnect.Data.Fundamental.InterestIncomeFromLeasesIncomeStatement

    InterestIncomeFromLoans: QuantConnect.Data.Fundamental.InterestIncomeFromLoansIncomeStatement

    InterestIncomeFromLoansAndLease: QuantConnect.Data.Fundamental.InterestIncomeFromLoansAndLeaseIncomeStatement

    InterestIncomeFromSecurities: QuantConnect.Data.Fundamental.InterestIncomeFromSecuritiesIncomeStatement

    InterestIncomeNonOperating: QuantConnect.Data.Fundamental.InterestIncomeNonOperatingIncomeStatement

    InvestmentBankingProfit: QuantConnect.Data.Fundamental.InvestmentBankingProfitIncomeStatement

    InvestmentContractLiabilitiesIncurred: QuantConnect.Data.Fundamental.InvestmentContractLiabilitiesIncurredIncomeStatement

    ISFileDate: datetime.datetime

    LossAdjustmentExpense: QuantConnect.Data.Fundamental.LossAdjustmentExpenseIncomeStatement

    LossonExtinguishmentofDebt: QuantConnect.Data.Fundamental.LossonExtinguishmentofDebtIncomeStatement

    MaintenanceAndRepairs: QuantConnect.Data.Fundamental.MaintenanceAndRepairsIncomeStatement

    MinorityInterests: QuantConnect.Data.Fundamental.MinorityInterestsIncomeStatement

    NegativeGoodwillImmediatelyRecognized: QuantConnect.Data.Fundamental.NegativeGoodwillImmediatelyRecognizedIncomeStatement

    NetForeignExchangeGainLoss: QuantConnect.Data.Fundamental.NetForeignExchangeGainLossIncomeStatement

    NetIncome: QuantConnect.Data.Fundamental.NetIncomeIncomeStatement

    NetIncomeCommonStockholders: QuantConnect.Data.Fundamental.NetIncomeCommonStockholdersIncomeStatement

    NetIncomeContinuousOperations: QuantConnect.Data.Fundamental.NetIncomeContinuousOperationsIncomeStatement

    NetIncomeContinuousOperationsNetMinorityInterest: QuantConnect.Data.Fundamental.NetIncomeContinuousOperationsNetMinorityInterestIncomeStatement

    NetIncomeDiscontinuousOperations: QuantConnect.Data.Fundamental.NetIncomeDiscontinuousOperationsIncomeStatement

    NetIncomeExtraordinary: QuantConnect.Data.Fundamental.NetIncomeExtraordinaryIncomeStatement

    NetIncomeFromContinuingAndDiscontinuedOperation: QuantConnect.Data.Fundamental.NetIncomeFromContinuingAndDiscontinuedOperationIncomeStatement

    NetIncomeFromContinuingOperationNetMinorityInterest: QuantConnect.Data.Fundamental.NetIncomeFromContinuingOperationNetMinorityInterestIncomeStatement

    NetIncomeFromTaxLossCarryforward: QuantConnect.Data.Fundamental.NetIncomeFromTaxLossCarryforwardIncomeStatement

    NetIncomeIncludingNoncontrollingInterests: QuantConnect.Data.Fundamental.NetIncomeIncludingNoncontrollingInterestsIncomeStatement

    NetInterestIncome: QuantConnect.Data.Fundamental.NetInterestIncomeIncomeStatement

    NetInvestmentIncome: QuantConnect.Data.Fundamental.NetInvestmentIncomeIncomeStatement

    NetNonOperatingInterestIncomeExpense: QuantConnect.Data.Fundamental.NetNonOperatingInterestIncomeExpenseIncomeStatement

    NetOccupancyExpense: QuantConnect.Data.Fundamental.NetOccupancyExpenseIncomeStatement

    NetPolicyholderBenefitsAndClaims: QuantConnect.Data.Fundamental.NetPolicyholderBenefitsAndClaimsIncomeStatement

    NetPremiumsWritten: QuantConnect.Data.Fundamental.NetPremiumsWrittenIncomeStatement

    NetRealizedGainLossOnInvestments: QuantConnect.Data.Fundamental.NetRealizedGainLossOnInvestmentsIncomeStatement

    NetTradingIncome: QuantConnect.Data.Fundamental.NetTradingIncomeIncomeStatement

    NonInterestExpense: QuantConnect.Data.Fundamental.NonInterestExpenseIncomeStatement

    NonInterestIncome: QuantConnect.Data.Fundamental.NonInterestIncomeIncomeStatement

    NormalizedEBITAsReported: QuantConnect.Data.Fundamental.NormalizedEBITAsReportedIncomeStatement

    NormalizedEBITDA: QuantConnect.Data.Fundamental.NormalizedEBITDAIncomeStatement

    NormalizedEBITDAAsReported: QuantConnect.Data.Fundamental.NormalizedEBITDAAsReportedIncomeStatement

    NormalizedIncome: QuantConnect.Data.Fundamental.NormalizedIncomeIncomeStatement

    NormalizedIncomeAsReported: QuantConnect.Data.Fundamental.NormalizedIncomeAsReportedIncomeStatement

    NormalizedOperatingProfitAsReported: QuantConnect.Data.Fundamental.NormalizedOperatingProfitAsReportedIncomeStatement

    NormalizedPreTaxIncome: QuantConnect.Data.Fundamental.NormalizedPreTaxIncomeIncomeStatement

    OccupancyAndEquipment: QuantConnect.Data.Fundamental.OccupancyAndEquipmentIncomeStatement

    OperatingExpense: QuantConnect.Data.Fundamental.OperatingExpenseIncomeStatement

    OperatingExpenseAsReported: QuantConnect.Data.Fundamental.OperatingExpenseAsReportedIncomeStatement

    OperatingIncome: QuantConnect.Data.Fundamental.OperatingIncomeIncomeStatement

    OperatingRevenue: QuantConnect.Data.Fundamental.OperatingRevenueIncomeStatement

    OperationAndMaintenance: QuantConnect.Data.Fundamental.OperationAndMaintenanceIncomeStatement

    OtherCostofRevenue: QuantConnect.Data.Fundamental.OtherCostofRevenueIncomeStatement

    OtherCustomerServices: QuantConnect.Data.Fundamental.OtherCustomerServicesIncomeStatement

    OtherGA: QuantConnect.Data.Fundamental.OtherGAIncomeStatement

    OtherIncomeExpense: QuantConnect.Data.Fundamental.OtherIncomeExpenseIncomeStatement

    OtherInterestExpense: QuantConnect.Data.Fundamental.OtherInterestExpenseIncomeStatement

    OtherInterestIncome: QuantConnect.Data.Fundamental.OtherInterestIncomeIncomeStatement

    OtherNonInterestExpense: QuantConnect.Data.Fundamental.OtherNonInterestExpenseIncomeStatement

    OtherNonInterestIncome: QuantConnect.Data.Fundamental.OtherNonInterestIncomeIncomeStatement

    OtherNonOperatingExpenses: QuantConnect.Data.Fundamental.OtherNonOperatingExpensesIncomeStatement

    OtherNonOperatingIncome: QuantConnect.Data.Fundamental.OtherNonOperatingIncomeIncomeStatement

    OtherNonOperatingIncomeExpenses: QuantConnect.Data.Fundamental.OtherNonOperatingIncomeExpensesIncomeStatement

    OtherOperatingExpenses: QuantConnect.Data.Fundamental.OtherOperatingExpensesIncomeStatement

    OtherOperatingIncomeTotal: QuantConnect.Data.Fundamental.OtherOperatingIncomeTotalIncomeStatement

    OtherSpecialCharges: QuantConnect.Data.Fundamental.OtherSpecialChargesIncomeStatement

    OtherStaffCosts: QuantConnect.Data.Fundamental.OtherStaffCostsIncomeStatement

    OtherTaxes: QuantConnect.Data.Fundamental.OtherTaxesIncomeStatement

    OtherunderPreferredStockDividend: QuantConnect.Data.Fundamental.OtherunderPreferredStockDividendIncomeStatement

    PensionCosts: QuantConnect.Data.Fundamental.PensionCostsIncomeStatement

    PolicyAcquisitionExpense: QuantConnect.Data.Fundamental.PolicyAcquisitionExpenseIncomeStatement

    PolicyholderBenefitsCeded: QuantConnect.Data.Fundamental.PolicyholderBenefitsCededIncomeStatement

    PolicyholderBenefitsGross: QuantConnect.Data.Fundamental.PolicyholderBenefitsGrossIncomeStatement

    PolicyholderDividends: QuantConnect.Data.Fundamental.PolicyholderDividendsIncomeStatement

    PolicyholderInterest: QuantConnect.Data.Fundamental.PolicyholderInterestIncomeStatement

    PreferredStockDividends: QuantConnect.Data.Fundamental.PreferredStockDividendsIncomeStatement

    PretaxIncome: QuantConnect.Data.Fundamental.PretaxIncomeIncomeStatement

    ProfessionalExpenseAndContractServicesExpense: QuantConnect.Data.Fundamental.ProfessionalExpenseAndContractServicesExpenseIncomeStatement

    ProvisionForDoubtfulAccounts: QuantConnect.Data.Fundamental.ProvisionForDoubtfulAccountsIncomeStatement

    ReconciledCostOfRevenue: QuantConnect.Data.Fundamental.ReconciledCostOfRevenueIncomeStatement

    ReconciledDepreciation: QuantConnect.Data.Fundamental.ReconciledDepreciationIncomeStatement

    ReinsuranceRecoveriesClaimsandBenefits: QuantConnect.Data.Fundamental.ReinsuranceRecoveriesClaimsandBenefitsIncomeStatement

    ReinsuranceRecoveriesofInsuranceLiabilities: QuantConnect.Data.Fundamental.ReinsuranceRecoveriesofInsuranceLiabilitiesIncomeStatement

    ReinsuranceRecoveriesofInvestmentContract: QuantConnect.Data.Fundamental.ReinsuranceRecoveriesofInvestmentContractIncomeStatement

    RentAndLandingFees: QuantConnect.Data.Fundamental.RentAndLandingFeesIncomeStatement

    RentandLandingFeesCostofRevenue: QuantConnect.Data.Fundamental.RentandLandingFeesCostofRevenueIncomeStatement

    RentExpenseSupplemental: QuantConnect.Data.Fundamental.RentExpenseSupplementalIncomeStatement

    ResearchAndDevelopment: QuantConnect.Data.Fundamental.ResearchAndDevelopmentIncomeStatement

    ResearchAndDevelopmentExpensesSupplemental: QuantConnect.Data.Fundamental.ResearchAndDevelopmentExpensesSupplementalIncomeStatement

    RestructuringAndMergernAcquisition: QuantConnect.Data.Fundamental.RestructuringAndMergernAcquisitionIncomeStatement

    SalariesAndWages: QuantConnect.Data.Fundamental.SalariesAndWagesIncomeStatement

    SecuritiesActivities: QuantConnect.Data.Fundamental.SecuritiesActivitiesIncomeStatement

    SecuritiesAmortization: QuantConnect.Data.Fundamental.SecuritiesAmortizationIncomeStatement

    SellingAndMarketingExpense: QuantConnect.Data.Fundamental.SellingAndMarketingExpenseIncomeStatement

    SellingGeneralAndAdministration: QuantConnect.Data.Fundamental.SellingGeneralAndAdministrationIncomeStatement

    ServiceChargeOnDepositorAccounts: QuantConnect.Data.Fundamental.ServiceChargeOnDepositorAccountsIncomeStatement

    SocialSecurityCosts: QuantConnect.Data.Fundamental.SocialSecurityCostsIncomeStatement

    SpecialIncomeCharges: QuantConnect.Data.Fundamental.SpecialIncomeChargesIncomeStatement

    StaffCosts: QuantConnect.Data.Fundamental.StaffCostsIncomeStatement

    StockBasedCompensation: QuantConnect.Data.Fundamental.StockBasedCompensationIncomeStatement

    TaxEffectOfUnusualItems: QuantConnect.Data.Fundamental.TaxEffectOfUnusualItemsIncomeStatement

    TaxProvision: QuantConnect.Data.Fundamental.TaxProvisionIncomeStatement

    TaxRateForCalcs: QuantConnect.Data.Fundamental.TaxRateForCalcsIncomeStatement

    TotalDividendPaymentofEquityShares: QuantConnect.Data.Fundamental.TotalDividendPaymentofEquitySharesIncomeStatement

    TotalDividendPaymentofNonEquityShares: QuantConnect.Data.Fundamental.TotalDividendPaymentofNonEquitySharesIncomeStatement

    TotalExpenses: QuantConnect.Data.Fundamental.TotalExpensesIncomeStatement

    TotalMoneyMarketInvestments: QuantConnect.Data.Fundamental.TotalMoneyMarketInvestmentsIncomeStatement

    TotalOperatingIncomeAsReported: QuantConnect.Data.Fundamental.TotalOperatingIncomeAsReportedIncomeStatement

    TotalOtherFinanceCost: QuantConnect.Data.Fundamental.TotalOtherFinanceCostIncomeStatement

    TotalPremiumsEarned: QuantConnect.Data.Fundamental.TotalPremiumsEarnedIncomeStatement

    TotalRevenue: QuantConnect.Data.Fundamental.TotalRevenueIncomeStatement

    TotalRevenueAsReported: QuantConnect.Data.Fundamental.TotalRevenueAsReportedIncomeStatement

    TotalUnusualItems: QuantConnect.Data.Fundamental.TotalUnusualItemsIncomeStatement

    TotalUnusualItemsExcludingGoodwill: QuantConnect.Data.Fundamental.TotalUnusualItemsExcludingGoodwillIncomeStatement

    TradingGainLoss: QuantConnect.Data.Fundamental.TradingGainLossIncomeStatement

    TrustFeesbyCommissions: QuantConnect.Data.Fundamental.TrustFeesbyCommissionsIncomeStatement

    UnderwritingExpenses: QuantConnect.Data.Fundamental.UnderwritingExpensesIncomeStatement

    WagesandSalaries: QuantConnect.Data.Fundamental.WagesandSalariesIncomeStatement

    WriteOff: QuantConnect.Data.Fundamental.WriteOffIncomeStatement



class IncomeTaxPaidSupplementalDataCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount of cash paid during the current period to foreign, federal state and local authorities as taxes on income.
    
    IncomeTaxPaidSupplementalDataCashFlowStatement(store: IDictionary[str, Decimal])
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


class IncomeTaxPayableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A current liability account which reflects the amount of income taxes currently due to the federal, state, and local governments.
    
    IncomeTaxPayableBalanceSheet(store: IDictionary[str, Decimal])
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


class IncreaseDecreaseInDepositCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate net change during the reporting period in moneys given as security, collateral, or margin deposits.
    
    IncreaseDecreaseInDepositCashFlowStatement(store: IDictionary[str, Decimal])
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


class IncreaseDecreaseinLeaseFinancingCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Change in cash flow resulting from increase/decrease in lease financing.
    
    IncreaseDecreaseinLeaseFinancingCashFlowStatement(store: IDictionary[str, Decimal])
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


class IncreaseDecreaseInNetUnearnedPremiumReservesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Premium might contain a portion of the amount that has been paid in advance for insurance that has not yet been provided, which
                is called unearned premium. If either party cancels the contract, the insurer must have the unearned premium ready to refund.
                Hence, the amount of premium reserve maintained by insurers is called unearned premium reserves, which is prepared for
                liquidation.  This item is usually only available for insurance industry.
    
    IncreaseDecreaseInNetUnearnedPremiumReservesIncomeStatement(store: IDictionary[str, Decimal])
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


class IncreaseinInterestBearingDepositsinBankCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Increase in interest-bearing deposits in bank.
    
    IncreaseinInterestBearingDepositsinBankCashFlowStatement(store: IDictionary[str, Decimal])
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


class IncreaseinLeaseFinancingCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash inflow from increase in lease financing.
    
    IncreaseinLeaseFinancingCashFlowStatement(store: IDictionary[str, Decimal])
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


class InsuranceAndClaimsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Insurance and claims are the expenses in the period incurred with respect to protection provided by insurance entities against risks
                other than risks associated with production (which is allocated to cost of sales). This item is usually not available for insurance
                industries.
    
    InsuranceAndClaimsIncomeStatement(store: IDictionary[str, Decimal])
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


class InsuranceContractAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A contract under which one party (the insurer) accepts significant insurance risk from another party (the policyholder) by agreeing
                to compensate the policyholder if a specified uncertain future event (the insured event) adversely affects the policyholder. This
                includes Insurance Receivables and Premiums Receivables.
    
    InsuranceContractAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class InsuranceContractLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Any type of insurance policy that protects an individual or business from the risk that they may be sued and held legally liable for
                something such as malpractice, injury or negligence. Liability insurance policies cover both legal costs and any legal payouts for
                which the insured would be responsible if found legally liable. Intentional damage and contractual liabilities are typically not covered
                in these types of policies.
    
    InsuranceContractLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class InsuranceFundsNonCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Liabilities related to insurance funds that are dissolved after one year.
    
    InsuranceFundsNonCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class InterestandCommissionPaidCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash paid for interest and commission in operating cash flow, using the direct method
    
    InterestandCommissionPaidCashFlowStatement(store: IDictionary[str, Decimal])
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


class InterestBearingBorrowingsNonCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Carrying amount of any interest-bearing loan which is due after one year.
    
    InterestBearingBorrowingsNonCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class InterestBearingDepositsAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Deposit of money with a financial institution, in consideration of which the financial institution pays or credits interest, or amounts in the nature
                of interest.
    
    InterestBearingDepositsAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class InterestBearingDepositsLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate of all domestic and foreign deposits in the bank that earns interests.
    
    InterestBearingDepositsLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class InterestCoverage(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of EBIT to Interest Expense. Morningstar calculates the ratio by using the underlying data reported in the Income
                Statement within the company filings or reports:    EBIT / Interest Expense.
    
    InterestCoverage(store: IDictionary[str, Decimal])
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


class InterestCreditedOnPolicyholderDepositsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An expense reported in the income statement and needs to be removed from net income to arrive at cash provided by (used in)
                operations to the extent that such interest has not been paid. This item is usually only available for insurance industry.
    
    InterestCreditedOnPolicyholderDepositsCashFlowStatement(store: IDictionary[str, Decimal])
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


class InterestExpenseForDepositIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Includes interest expense on the following deposit accounts: Interest-bearing Demand deposit; Checking account; Savings account;
                Deposit in foreign offices; Money Market Certificates & Deposit Accounts. This item is usually only available for bank industry.
    
    InterestExpenseForDepositIncomeStatement(store: IDictionary[str, Decimal])
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


class InterestExpenseForFederalFundsSoldAndSecuritiesPurchaseUnderAgreementsToResellIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Gross expenses on the purchase of Federal funds at a specified price with a simultaneous agreement to sell the same to the same
                counterparty at a fixed or determinable price at a future date. This item is usually only available for bank industry.
    
    InterestExpenseForFederalFundsSoldAndSecuritiesPurchaseUnderAgreementsToResellIncomeStatement(store: IDictionary[str, Decimal])
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


class InterestExpenseForLongTermDebtAndCapitalSecuritiesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate interest expenses incurred on long-term borrowings and any interest expenses on fixed assets (property, plant,
                equipment) that are leased due longer than one year. This item is usually only available for bank industry.
    
    InterestExpenseForLongTermDebtAndCapitalSecuritiesIncomeStatement(store: IDictionary[str, Decimal])
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


class InterestExpenseForShortTermDebtIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate interest expenses incurred on short-term borrowings and any interest expenses on fixed assets (property, plant,
                equipment) that are leased within one year. This item is usually only available for bank industry.
    
    InterestExpenseForShortTermDebtIncomeStatement(store: IDictionary[str, Decimal])
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


class InterestExpenseIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Relates to the general cost of borrowing money. It is the price that a lender charges a borrower for the use of the lender's money.
    
    InterestExpenseIncomeStatement(store: IDictionary[str, Decimal])
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


class InterestExpenseNonOperatingIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Interest expense caused by long term financing activities; such as interest expense incurred on trading liabilities, commercial paper,
                long-term debt, capital leases, deposits, and all other borrowings.
    
    InterestExpenseNonOperatingIncomeStatement(store: IDictionary[str, Decimal])
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


class InterestIncomeAfterProvisionForLoanLossIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Net interest and dividend income or expense, including any amortization and accretion (as applicable) of discounts and premiums,
                including consideration of the provisions for loan, lease, credit, and other related losses, if any.
    
    InterestIncomeAfterProvisionForLoanLossIncomeStatement(store: IDictionary[str, Decimal])
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


class InterestIncomeFromDepositsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Interest income generated from all deposit accounts. This item is usually only available for bank industry.
    
    InterestIncomeFromDepositsIncomeStatement(store: IDictionary[str, Decimal])
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


class InterestIncomeFromFederalFundsSoldAndSecuritiesPurchaseUnderAgreementsToResellIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The carrying value of funds outstanding loaned in the form of security resale agreements if the agreement requires the purchaser to
                resell the identical security purchased or a security that meets the definition of ""substantially the same"" in the case of a dollar roll.
                Also includes purchases of participations in pools of securities that are subject to a resale agreement; This category includes all
                interest income generated from federal funds sold and securities purchases under agreements to resell; This category includes all
                interest income generated from federal funds sold and securities purchases under agreements to resell.
    
    InterestIncomeFromFederalFundsSoldAndSecuritiesPurchaseUnderAgreementsToResellIncomeStatement(store: IDictionary[str, Decimal])
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


class InterestIncomeFromLeasesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Includes interest and fee income generated by direct lease financing. This item is usually only available for bank industry.
    
    InterestIncomeFromLeasesIncomeStatement(store: IDictionary[str, Decimal])
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


class InterestIncomeFromLoansAndLeaseIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total interest and fee income generated by loans and lease. This item is usually only available for bank industry.
    
    InterestIncomeFromLoansAndLeaseIncomeStatement(store: IDictionary[str, Decimal])
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


class InterestIncomeFromLoansIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Loan is a common field to banks. Interest Income from Loans is interest and fee income generated from all loans, which includes
                Commercial loans; Credit loans; Other consumer loans; Real Estate - Construction; Real Estate - Mortgage; Foreign loans. Banks
                earn interest from loans. This item is usually only available for bank industry.
    
    InterestIncomeFromLoansIncomeStatement(store: IDictionary[str, Decimal])
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


class InterestIncomeFromSecuritiesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents total interest and dividend income from U.S. Treasury securities, U.S. government agency and corporation obligations,
                securities issued by states and political subdivisions, other domestic debt securities, foreign debt securities, and equity securities
                (including investments in mutual funds). Excludes interest income from securities held in trading accounts. This item is usually only
                available for bank industry.
    
    InterestIncomeFromSecuritiesIncomeStatement(store: IDictionary[str, Decimal])
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


class InterestIncomeIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Income generated from interest-bearing deposits or accounts.
    
    InterestIncomeIncomeStatement(store: IDictionary[str, Decimal])
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


class InterestIncomeNonOperatingIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Interest income earned from long term financing activities.
    
    InterestIncomeNonOperatingIncomeStatement(store: IDictionary[str, Decimal])
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


class InterestPaidCFFCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Interest paid on loans, debt or borrowings, in the Financing Cash Flow section.
    
    InterestPaidCFFCashFlowStatement(store: IDictionary[str, Decimal])
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


class InterestPaidCFOCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Interest paid on loans, debt or borrowings, in the Operating Cash Flow section.
    
    InterestPaidCFOCashFlowStatement(store: IDictionary[str, Decimal])
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


class InterestPaidDirectCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Interest paid on loans, debt or borrowings, in the direct cash flow.
    
    InterestPaidDirectCashFlowStatement(store: IDictionary[str, Decimal])
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


class InterestPaidSupplementalDataCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount of cash paid during the current period for interest owed on money borrowed; including amount of interest capitalized.
    
    InterestPaidSupplementalDataCashFlowStatement(store: IDictionary[str, Decimal])
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


class InterestPayableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of the carrying values as of the balance sheet date of interest payable on all forms of debt, including trade payable that has
                been incurred.
    
    InterestPayableBalanceSheet(store: IDictionary[str, Decimal])
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


class InterestReceivedCFICashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Interest received by the company, in the Investing Cash Flow section.
    
    InterestReceivedCFICashFlowStatement(store: IDictionary[str, Decimal])
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


class InterestReceivedCFOCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Interest received by the company, in the Operating Cash Flow section.
    
    InterestReceivedCFOCashFlowStatement(store: IDictionary[str, Decimal])
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


class InterestReceivedDirectCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Interest received by the company, in the direct cash flow.
    
    InterestReceivedDirectCashFlowStatement(store: IDictionary[str, Decimal])
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


class InventoriesAdjustmentsAllowancesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This item represents certain charges made in the current period in inventory resulting from such factors as breakage, spoilage,
                employee theft and shoplifting. This item is typically available for manufacturing, mining and utility industries.
    
    InventoriesAdjustmentsAllowancesBalanceSheet(store: IDictionary[str, Decimal])
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


class InventoryBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A company's merchandise, raw materials, and finished and unfinished products which have not yet been sold.
    
    InventoryBalanceSheet(store: IDictionary[str, Decimal])
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


class InventoryTurnover(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cost Of Goods Sold / Average Inventory
    
    InventoryTurnover(store: IDictionary[str, Decimal])
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


class InvestedCapitalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Invested capital = common shareholders' equity + long term debt + current debt
    
    InvestedCapitalBalanceSheet(store: IDictionary[str, Decimal])
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


class InvestingCashFlowCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An item on the cash flow statement that reports the aggregate change in a company's cash position resulting from any gains (or
                losses) from investments in the financial markets and operating subsidiaries, and changes resulting from amounts spent on
                investments in capital assets such as plant and equipment.
    
    InvestingCashFlowCashFlowStatement(store: IDictionary[str, Decimal])
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


class InvestmentBankingProfitIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Includes (1) underwriting revenue (the spread between the resale price received and the cost of the securities and related
                expenses) generated through the purchasing, distributing and reselling of new issues of securities (alternatively, could be a
                secondary offering of a large block of previously issued securities); and (2) fees earned for mergers, acquisitions, divestitures,
                restructurings, and other types of financial advisory services. This item is usually only available for bank industry.
    
    InvestmentBankingProfitIncomeStatement(store: IDictionary[str, Decimal])
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


class InvestmentContractLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Liabilities due on the insurance investment contract.
    
    InvestmentContractLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class InvestmentContractLiabilitiesIncurredIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Income/Expenses due to the insurer's liabilities incurred in Investment Contracts.
    
    InvestmentContractLiabilitiesIncurredIncomeStatement(store: IDictionary[str, Decimal])
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


class InvestmentinFinancialAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents the sum of all financial investments (trading securities, available-for-sale securities, held-to-maturity securities, etc.)
    
    InvestmentinFinancialAssetsBalanceSheet(store: IDictionary[str, Decimal])
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

    TwoMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class InvestmentPropertiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Company's investments in properties net of accumulated depreciation, which generate a return.
    
    InvestmentPropertiesBalanceSheet(store: IDictionary[str, Decimal])
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


class InvestmentsAndAdvancesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    All investments in affiliates, real estate, securities, etc. Non-current investment, not including marketable securities.
    
    InvestmentsAndAdvancesBalanceSheet(store: IDictionary[str, Decimal])
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


class InvestmentsinAssociatesatCostBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A stake in any company which is more than 20% but less than 50%.
    
    InvestmentsinAssociatesatCostBalanceSheet(store: IDictionary[str, Decimal])
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


class InvestmentsinJointVenturesatCostBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A 50% stake in any company in which remaining 50% belongs to other company.
    
    InvestmentsinJointVenturesatCostBalanceSheet(store: IDictionary[str, Decimal])
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


class InvestmentsInOtherVenturesUnderEquityMethodBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This item represents the carrying amount on the company's balance sheet of its investments in common stock of an equity method.
                This item is typically available for the insurance industry.
    
    InvestmentsInOtherVenturesUnderEquityMethodBalanceSheet(store: IDictionary[str, Decimal])
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


class InvestmentsinSubsidiariesatCostBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A stake in any company which is more than 51%.
    
    InvestmentsinSubsidiariesatCostBalanceSheet(store: IDictionary[str, Decimal])
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


class IssuanceOfCapitalStockCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash inflow from offering common stock, which is the additional capital contribution to the entity during the PeriodAsByte.
    
    IssuanceOfCapitalStockCashFlowStatement(store: IDictionary[str, Decimal])
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


class IssuanceOfDebtCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash inflow due to an increase in long term debt.
    
    IssuanceOfDebtCashFlowStatement(store: IDictionary[str, Decimal])
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


class IssueExpensesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cost associated with issuance of debt/equity capital in the Financing Cash Flow section.
    
    IssueExpensesCashFlowStatement(store: IDictionary[str, Decimal])
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


class ItemsinTheCourseofTransmissiontoOtherBanksBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Carrying amount as of the balance sheet date of drafts and bills of exchange that have been accepted by the reporting bank or by
                others for its own account, as its liability to holders of the drafts.
    
    ItemsinTheCourseofTransmissiontoOtherBanksBalanceSheet(store: IDictionary[str, Decimal])
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


class LandAndImprovementsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Fixed Assets that specifically deal with land a company owns. Includes the improvements associated with land. This excludes land
                held for sale.
    
    LandAndImprovementsBalanceSheet(store: IDictionary[str, Decimal])
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


class LeasesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Carrying amount at the balance sheet date of a long-lived, depreciable asset that is an addition or improvement to assets held
                under lease arrangement. This item is usually not available for the insurance industry.
    
    LeasesBalanceSheet(store: IDictionary[str, Decimal])
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


class LiabilitiesHeldforSaleCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Liabilities due within the next 12 months related from an asset classified as Held for Sale.
    
    LiabilitiesHeldforSaleCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class LiabilitiesHeldforSaleNonCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Liabilities related to an asset classified as held for sale excluding the portion due the next 12 months or operating cycle.
    
    LiabilitiesHeldforSaleNonCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class LiabilitiesHeldforSaleTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Liabilities related to an asset classified as held for sale.
    
    LiabilitiesHeldforSaleTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class LiabilitiesOfDiscontinuedOperationsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The obligations arising from the sale, disposal, or planned sale in the near future (generally within one year) of a disposal group,
                including a component of the entity (discontinued operation). This item is typically available for bank industry.
    
    LiabilitiesOfDiscontinuedOperationsBalanceSheet(store: IDictionary[str, Decimal])
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


class LimitedPartnershipCapitalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    In a limited partnership or master limited partnership form of business, this represents the balance of capital held by the limited
                partners.
    
    LimitedPartnershipCapitalBalanceSheet(store: IDictionary[str, Decimal])
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


class LineOfCreditBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The carrying value as of the balance sheet date of obligations drawn from a line of credit, which is a bank's commitment to make
                loans up to a specific amount.
    
    LineOfCreditBalanceSheet(store: IDictionary[str, Decimal])
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

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class LoansandAdvancestoBankBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of loans and advances made to a bank or financial institution.
    
    LoansandAdvancestoBankBalanceSheet(store: IDictionary[str, Decimal])
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


class LoansandAdvancestoCustomerBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of loans and advances made to customers.
    
    LoansandAdvancestoCustomerBalanceSheet(store: IDictionary[str, Decimal])
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


class LoansHeldForSaleBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    It means the aggregate amount of loans receivable that will be sold to other entities.  This item is typically available for bank
                industry.
    
    LoansHeldForSaleBalanceSheet(store: IDictionary[str, Decimal])
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


class LoansReceivableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Reflects the carrying amount of unpaid loans issued to other institutions for cash needs or an asset purchase.
    
    LoansReceivableBalanceSheet(store: IDictionary[str, Decimal])
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


class LongTermCapitalLeaseObligationBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents the total liability for long-term leases lasting over one year. Amount equal to the present value (the principal) at the
                beginning of the lease term less lease payments during the lease term.
    
    LongTermCapitalLeaseObligationBalanceSheet(store: IDictionary[str, Decimal])
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


class LongTermDebtAndCapitalLeaseObligationBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    All borrowings lasting over one year including long-term debt and long-term portion of capital lease obligations.
    
    LongTermDebtAndCapitalLeaseObligationBalanceSheet(store: IDictionary[str, Decimal])
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


class LongTermDebtBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of the carrying values as of the balance sheet date of all long-term debt, which is debt initially having maturities due after one
                year or beyond the operating cycle, if longer, but excluding the portions thereof scheduled to be repaid within one year or the
                normal operating cycle, if longer. Long-term debt includes notes payable, bonds payable, mortgage loans, convertible debt,
                subordinated debt and other types of long term debt.
    
    LongTermDebtBalanceSheet(store: IDictionary[str, Decimal])
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


class LongTermDebtEquityRatio(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of Long Term Debt to Common Equity. Morningstar calculates the ratio by using the underlying data reported in
                the Balance Sheet within the company filings or reports:    Long-Term Debt And Capital Lease Obligation / Common Equity.
                [Note: Common Equity = Total Shareholder's Equity - Preferred Stock]
    
    LongTermDebtEquityRatio(store: IDictionary[str, Decimal])
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


class LongTermDebtIssuanceCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash inflow from a debt initially having maturity due after one year or beyond the operating cycle, if longer.
    
    LongTermDebtIssuanceCashFlowStatement(store: IDictionary[str, Decimal])
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


class LongTermDebtPaymentsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash outflow for debt initially having maturity due after one year or beyond the normal operating cycle, if longer.
    
    LongTermDebtPaymentsCashFlowStatement(store: IDictionary[str, Decimal])
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


class LongTermDebtTotalCapitalRatio(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of Long Term Debt to Total Capital. Morningstar calculates the ratio by using the underlying data reported in the
                Balance Sheet within the company filings or reports:    Long-Term Debt And Capital Lease Obligation / (Long-Term Debt And Capital
                Lease Obligation + Total Shareholder's Equity)
    
    LongTermDebtTotalCapitalRatio(store: IDictionary[str, Decimal])
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


class LongTermInvestmentsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Often referred to simply as "investments". Long-term investments are to be held for many years and are not intended to be
                disposed in the near future. This group usually consists of four types of investments.
    
    LongTermInvestmentsBalanceSheet(store: IDictionary[str, Decimal])
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


class LongTermProvisionsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Provisions are created to protect the interests of one or both parties named in a contract or legal document which is a preparatory
                action or measure. Long-term provision is expired beyond one accounting PeriodAsByte.
    
    LongTermProvisionsBalanceSheet(store: IDictionary[str, Decimal])
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


class LossAdjustmentExpenseIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Losses generally refer to (1) the amount of reduction in the value of an insured's property caused by an insured peril, (2) the amount
                sought through an insured's claim, or (3) the amount paid on behalf of an insured under an insurance contract.  Loss Adjustment
                Expenses is expenses incurred in the course of investigating and settling claims that includes any legal and adjusters' fees and the
                costs of paying claims and all related expenses.
    
    LossAdjustmentExpenseIncomeStatement(store: IDictionary[str, Decimal])
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


class LossonExtinguishmentofDebtIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Loss on extinguishment of debt is the accounting loss that results from a debt extinguishment. A debt shall be accounted for as
                having been extinguished in a number of circumstances, including when it has been settled through repayment or replacement by
                another liability. It generally results in an accounting gain or loss. Amount represents the difference between the fair value of the
                payments made and the carrying amount of the debt at the time of its extinguishment.
    
    LossonExtinguishmentofDebtIncomeStatement(store: IDictionary[str, Decimal])
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


class LossRatio(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A measure of operating performance for Insurance companies, as it shows the relationship between the premiums earned and the
                expenses related to claims. A number of 1 or lower is preferred, as this means the premiums exceed the expenses. Calculated as:
                Benefits, Claims and Loss Adjustment Expense, Net / Net Premiums Earned
    
    LossRatio(store: IDictionary[str, Decimal])
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


class MachineryFurnitureEquipmentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Fixed assets specifically dealing with tools, equipment and office furniture. This item is usually not available for the insurance and
                utility industries.
    
    MachineryFurnitureEquipmentBalanceSheet(store: IDictionary[str, Decimal])
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


class MaintenanceAndRepairsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of maintenance and repair expenses in the current period associated with the revenue generation. Mainly
                for fixed assets. This item is usually only available for transportation industry.
    
    MaintenanceAndRepairsIncomeStatement(store: IDictionary[str, Decimal])
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


class MaterialsAndSuppliesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Aggregated amount of unprocessed materials to be used in manufacturing or production process and supplies that will be
                consumed. This item is typically available for the utility industry.
    
    MaterialsAndSuppliesBalanceSheet(store: IDictionary[str, Decimal])
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


class MineralPropertiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A fixed asset that represents strictly mineral type properties.  This item is typically available for mining industry.
    
    MineralPropertiesBalanceSheet(store: IDictionary[str, Decimal])
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


class MinimumPensionLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The company's minimum pension obligations to its former employees, paid into a defined pension plan to satisfy all pension
                entitlements that have been earned by employees to date.
    
    MinimumPensionLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class MinorityInterestBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Carrying amount of the equity interests owned by non-controlling shareholders, partners, or other equity holders in one or more of
                the entities included in the reporting entity's consolidated financial statements.
    
    MinorityInterestBalanceSheet(store: IDictionary[str, Decimal])
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


class MinorityInterestCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Amount of net income (loss) for the period allocated to non-controlling shareholders, partners, or other equity holders in one or
                more of the entities included.
    
    MinorityInterestCashFlowStatement(store: IDictionary[str, Decimal])
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


class MinorityInterestsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents par or stated value of the subsidiary stock not owned by the parent company plus the minority interest's equity in the
                surplus of the subsidiary. This item includes preferred dividend averages on the minority preferred stock (preferred shares not
                owned by the reporting parent company). Minority interest also refers to stockholders who own less than 50% of a subsidiary's
                outstanding voting common stock. The minority stockholders hold an interest in the subsidiary's net assets and share earnings with
                the parent company.
    
    MinorityInterestsIncomeStatement(store: IDictionary[str, Decimal])
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


class MoneyMarketInvestmentsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Short-term (typical maturity is less than one year), highly liquid government or corporate debt instrument such as bankers'
                acceptance, promissory notes, and treasury bills.
    
    MoneyMarketInvestmentsBalanceSheet(store: IDictionary[str, Decimal])
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


class MorningstarEconomySphereCode(System.object):
    """ Helper class for the AssetClassification's MorningstarEconomySphereCode field QuantConnect.Data.Fundamental.AssetClassification.MorningstarEconomySphereCode. """
    Cyclical: int
    Defensive: int
    Sensitive: int
    __all__: list


class MorningstarIndustryCode(System.object):
    """ Helper class for the AssetClassification's MorningstarIndustryCode field QuantConnect.Data.Fundamental.AssetClassification.MorningstarIndustryCode. """
    AdvertisingAgencies: int
    AerospaceAndDefense: int
    AgriculturalInputs: int
    Airlines: int
    AirportsAndAirServices: int
    Aluminum: int
    ApparelManufacturing: int
    ApparelRetail: int
    AssetManagement: int
    AutoAndTruckDealerships: int
    AutoManufacturers: int
    AutoParts: int
    BanksDiversified: int
    BanksRegional: int
    BeveragesBrewers: int
    BeveragesNonAlcoholic: int
    BeveragesWineriesAndDistilleries: int
    Biotechnology: int
    Broadcasting: int
    BuildingMaterials: int
    BuildingProductsAndEquipment: int
    BusinessEquipmentAndSupplies: int
    CapitalMarkets: int
    Chemicals: int
    CokingCoal: int
    CommunicationEquipment: int
    ComputerHardware: int
    Confectioners: int
    Conglomerates: int
    ConsultingServices: int
    ConsumerElectronics: int
    Copper: int
    CreditServices: int
    DepartmentStores: int
    DiagnosticsAndResearch: int
    DiscountStores: int
    DrugManufacturersGeneral: int
    DrugManufacturersSpecialtyAndGeneric: int
    EducationAndTrainingServices: int
    ElectricalEquipmentAndParts: int
    ElectronicComponents: int
    ElectronicGamingAndMultimedia: int
    ElectronicsAndComputerDistribution: int
    EngineeringAndConstruction: int
    Entertainment: int
    FarmAndHeavyConstructionMachinery: int
    FarmProducts: int
    FinancialConglomerates: int
    FinancialDataAndStockExchanges: int
    FixturesAndAppliances: int
    FoodDistribution: int
    FootwearAndAccessories: int
    Furnishings: int
    Gambling: int
    Gold: int
    GroceryStores: int
    HealthcarePlans: int
    HealthInformationServices: int
    HomeImprovementRetail: int
    HouseholdAndPersonalProducts: int
    IndustrialDistribution: int
    InformationTechnologyServices: int
    InfrastructureOperations: int
    InsuranceBrokers: int
    InsuranceDiversified: int
    InsuranceLife: int
    InsurancePropertyAndCasualty: int
    InsuranceReinsurance: int
    InsuranceSpecialty: int
    IntegratedFreightAndLogistics: int
    InternetContentAndInformation: int
    InternetRetail: int
    Leisure: int
    Lodging: int
    LumberAndWoodProduction: int
    LuxuryGoods: int
    MarineShipping: int
    MedicalCareFacilities: int
    MedicalDevices: int
    MedicalDistribution: int
    MedicalInstrumentsAndSupplies: int
    MetalFabrication: int
    MortgageFinance: int
    OilAndGasDrilling: int
    OilAndGasEAndP: int
    OilAndGasEquipmentAndServices: int
    OilAndGasIntegrated: int
    OilAndGasMidstream: int
    OilAndGasRefiningAndMarketing: int
    OtherIndustrialMetalsAndMining: int
    OtherPreciousMetalsAndMining: int
    PackagedFoods: int
    PackagingAndContainers: int
    PaperAndPaperProducts: int
    PersonalServices: int
    PharmaceuticalRetailers: int
    PollutionAndTreatmentControls: int
    Publishing: int
    Railroads: int
    RealEstateDevelopment: int
    RealEstateDiversified: int
    RealEstateServices: int
    RecreationalVehicles: int
    REITDiversified: int
    REITHealthcareFacilities: int
    REITHotelAndMotel: int
    REITIndustrial: int
    REITMortgage: int
    REITOffice: int
    REITResidential: int
    REITRetail: int
    REITSpecialty: int
    RentalAndLeasingServices: int
    ResidentialConstruction: int
    ResortsAndCasinos: int
    Restaurants: int
    ScientificAndTechnicalInstruments: int
    SecurityAndProtectionServices: int
    SemiconductorEquipmentAndMaterials: int
    Semiconductors: int
    ShellCompanies: int
    Silver: int
    SoftwareApplication: int
    SoftwareInfrastructure: int
    Solar: int
    SpecialtyBusinessServices: int
    SpecialtyChemicals: int
    SpecialtyIndustrialMachinery: int
    SpecialtyRetail: int
    StaffingAndEmploymentServices: int
    Steel: int
    TelecomServices: int
    TextileManufacturing: int
    ThermalCoal: int
    Tobacco: int
    ToolsAndAccessories: int
    TravelServices: int
    Trucking: int
    Uranium: int
    UtilitiesDiversified: int
    UtilitiesIndependentPowerProducers: int
    UtilitiesRegulatedElectric: int
    UtilitiesRegulatedGas: int
    UtilitiesRegulatedWater: int
    UtilitiesRenewable: int
    WasteManagement: int
    __all__: list


class MorningstarIndustryGroupCode(System.object):
    """ Helper class for the AssetClassification's MorningstarIndustryGroupCode field QuantConnect.Data.Fundamental.AssetClassification.MorningstarIndustryGroupCode. """
    AerospaceAndDefense: int
    Agriculture: int
    AssetManagement: int
    Banks: int
    BeveragesAlcoholic: int
    BeveragesNonAlcoholic: int
    Biotechnology: int
    BuildingMaterials: int
    BusinessServices: int
    CapitalMarkets: int
    Chemicals: int
    Conglomerates: int
    Construction: int
    ConsumerPackagedGoods: int
    CreditServices: int
    DiversifiedFinancialServices: int
    DrugManufacturers: int
    Education: int
    FarmAndHeavyConstructionMachinery: int
    FixturesAndAppliances: int
    ForestProducts: int
    Furnishings: int
    Hardware: int
    HealthcarePlans: int
    HealthcareProvidersAndServices: int
    HomebuildingAndConstruction: int
    IndustrialDistribution: int
    IndustrialProducts: int
    Insurance: int
    InteractiveMedia: int
    ManufacturingApparelAndAccessories: int
    MediaDiversified: int
    MedicalDevicesAndInstruments: int
    MedicalDiagnosticsAndResearch: int
    MedicalDistribution: int
    MetalsAndMining: int
    OilAndGas: int
    OtherEnergySources: int
    PackagingAndContainers: int
    PersonalServices: int
    RealEstate: int
    REITs: int
    Restaurants: int
    RetailCyclical: int
    RetailDefensive: int
    Semiconductors: int
    Software: int
    Steel: int
    TelecommunicationServices: int
    TobaccoProducts: int
    Transportation: int
    TravelAndLeisure: int
    UtilitiesIndependentPowerProducers: int
    UtilitiesRegulated: int
    VehiclesAndParts: int
    WasteManagement: int
    __all__: list


class MorningstarSectorCode(System.object):
    """ Helper class for the AssetClassification's MorningstarSectorCode field QuantConnect.Data.Fundamental.AssetClassification.MorningstarSectorCode. """
    BasicMaterials: int
    CommunicationServices: int
    ConsumerCyclical: int
    ConsumerDefensive: int
    Energy: int
    FinancialServices: int
    Healthcare: int
    Industrials: int
    RealEstate: int
    Technology: int
    Utilities: int
    __all__: list


class MortgageAndConsumerloansBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    It means the aggregate amount of mortgage and consumer loans.  This item is typically available for the insurance industry.
    
    MortgageAndConsumerloansBalanceSheet(store: IDictionary[str, Decimal])
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


class MortgageLoanBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This is a lien on real estate to protect a lender.  This item is typically available for bank industry.
    
    MortgageLoanBalanceSheet(store: IDictionary[str, Decimal])
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


class NaturalGasFuelAndOtherBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount for the natural gas, fuel and other items related to the utility industry, which might include oil and gas wells, the
                properties to exploit oil and gas or liquefied natural gas sites.
    
    NaturalGasFuelAndOtherBalanceSheet(store: IDictionary[str, Decimal])
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


class NegativeGoodwillImmediatelyRecognizedIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Negative Goodwill recognized in the Income Statement. Negative Goodwill arises where the net assets at the date of acquisition,
                fairly valued, falls below the cost of acquisition.
    
    NegativeGoodwillImmediatelyRecognizedIncomeStatement(store: IDictionary[str, Decimal])
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


class NetBusinessPurchaseAndSaleCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net change between Purchases/Sales of Business.
    
    NetBusinessPurchaseAndSaleCashFlowStatement(store: IDictionary[str, Decimal])
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


class NetCashFromDiscontinuedOperationsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net cash from (used in) all of the entity's discontinued operating activities, excluding those of continued operations, of the
                reporting entity.
    
    NetCashFromDiscontinuedOperationsCashFlowStatement(store: IDictionary[str, Decimal])
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


class NetCommonStockIssuanceCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of common stock.
    
    NetCommonStockIssuanceCashFlowStatement(store: IDictionary[str, Decimal])
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


class NetDebtBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This is a metric that shows a company's overall debt situation by netting the value of a company's liabilities and
                debts with its cash and other similar liquid assets. It is calculated using [Current Debt] + [Long Term Debt] - [Cash and Cash
                Equivalents].
    
    NetDebtBalanceSheet(store: IDictionary[str, Decimal])
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


class NetForeignCurrencyExchangeGainLossCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of realized and unrealized gain or loss resulting from changes in exchange rates between currencies.
                (Excludes foreign currency transactions designated as hedges of net investment in a foreign entity and inter-company foreign
                currency transactions that are of a long-term nature, when the entities to the transaction are consolidated, combined, or accounted
                for by the equity method in the reporting entity's financial statements. For certain entities, primarily banks, which are dealers in
                foreign exchange, foreign currency transaction gains or losses, may be disclosed as dealer gains or losses.)
    
    NetForeignCurrencyExchangeGainLossCashFlowStatement(store: IDictionary[str, Decimal])
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


class NetForeignExchangeGainLossIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate foreign currency translation gain or loss (both realized and unrealized) included as part of revenue. This item is
                usually only available for insurance industry.
    
    NetForeignExchangeGainLossIncomeStatement(store: IDictionary[str, Decimal])
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


class NetIncomeCommonStockholdersIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Net income minus the preferred dividends paid as presented in the Income Statement.
    
    NetIncomeCommonStockholdersIncomeStatement(store: IDictionary[str, Decimal])
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


class NetIncomeContinuousOperationsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Revenue less expenses and taxes from the entity's ongoing operations and before income (loss) from: Preferred Dividends;
                Extraordinary Gains and Losses; Income from Cumulative Effects of Accounting Change; Discontinuing Operation; Income from Tax
                Loss Carry forward; Other Gains/Losses.
    
    NetIncomeContinuousOperationsIncomeStatement(store: IDictionary[str, Decimal])
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


class NetIncomeContinuousOperationsNetMinorityInterestIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Revenue less expenses and taxes from the entity's ongoing operations net of minority interest and before income (loss) from:
                Preferred Dividends; Extraordinary Gains and Losses; Income from Cumulative Effects of Accounting Change; Discontinuing
                Operation; Income from Tax Loss Carry forward; Other Gains/Losses.
    
    NetIncomeContinuousOperationsNetMinorityInterestIncomeStatement(store: IDictionary[str, Decimal])
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


class NetIncomeContOpsGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's net income from continuing operations on a percentage basis. Morningstar calculates the growth
                percentage based on the underlying net income from continuing operations data reported in the Income Statement within the
                company filings or reports. This figure represents the rate of net income growth for parts of the business that will continue to
                generate revenue in the future.
    
    NetIncomeContOpsGrowth(store: IDictionary[str, Decimal])
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


class NetIncomeDiscontinuousOperationsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    To be classified as discontinued operations, if both of the following conditions are met:
                1: The operations and cash flow of the component have been or will be removed from the ongoing operations of the entity as a
                result of the disposal transaction, and
                2: The entity will have no significant continuing involvement in the operations of the component after the disposal transaction.
                The discontinued operation is reported net of tax.
                Gains/Loss on Disposal of Discontinued Operations: Any gains or loss recognized on disposal of discontinued operations,
                which is the difference between the carrying value of the division and its fair value less costs to sell.
                Provision for Gain/Loss on Disposal: The amount of current expense charged in order to prepare for the disposal of
                discontinued operations.
    
    NetIncomeDiscontinuousOperationsIncomeStatement(store: IDictionary[str, Decimal])
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


class NetIncomeExtraordinaryIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Gains (losses), whether arising from extinguishment of debt, prior period adjustments, or from other events or transactions, that are
                both unusual in nature and infrequent in occurrence thereby meeting the criteria for an event or transaction to be classified as an
                extraordinary item.
    
    NetIncomeExtraordinaryIncomeStatement(store: IDictionary[str, Decimal])
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


class NetIncomeFromContinuingAndDiscontinuedOperationIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Net Income from Continuing Operations and Discontinued Operations, added together.
    
    NetIncomeFromContinuingAndDiscontinuedOperationIncomeStatement(store: IDictionary[str, Decimal])
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


class NetIncomeFromContinuingOperationNetMinorityInterestIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Revenue less expenses and taxes from the entity's ongoing operations net of minority interest and before income (loss) from:
                Preferred Dividends; Extraordinary Gains and Losses; Income from Cumulative Effects of Accounting Change; Discontinuing
                Operation; Income from Tax Loss Carry forward; Other Gains/Losses.
    
    NetIncomeFromContinuingOperationNetMinorityInterestIncomeStatement(store: IDictionary[str, Decimal])
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


class NetIncomeFromContinuingOperationsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Revenue less expenses and taxes from the entity's ongoing operations and before income (loss) from discontinued operations,
                extraordinary items, impact of changes in accounting principles, minority interest, and various other reconciling adjustments;
                represents the starting line for Operating Cash Flow.
    
    NetIncomeFromContinuingOperationsCashFlowStatement(store: IDictionary[str, Decimal])
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


class NetIncomeFromTaxLossCarryforwardIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Occurs if a company has had a net loss from operations on a previous year that can be carried forward to reduce net income for tax
                purposes.
    
    NetIncomeFromTaxLossCarryforwardIncomeStatement(store: IDictionary[str, Decimal])
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


class NetIncomeGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's net income on a percentage basis. Morningstar calculates the growth percentage based on the
                underlying net income data reported in the Income Statement within the company filings or reports.
    
    NetIncomeGrowth(store: IDictionary[str, Decimal])
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


class NetIncomeIncludingNoncontrollingInterestsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Net income of the group after the adjustment of all expenses and benefit.
    
    NetIncomeIncludingNoncontrollingInterestsIncomeStatement(store: IDictionary[str, Decimal])
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


class NetOtherFinancingChargesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Miscellaneous charges incurred due to Financing activities.
    
    NetOtherFinancingChargesCashFlowStatement(store: IDictionary[str, Decimal])
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


class NetOtherInvestingChangesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Miscellaneous charges incurred due to Investing activities.
    
    NetOtherInvestingChangesCashFlowStatement(store: IDictionary[str, Decimal])
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


class NetOutwardLoansCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Adjustments due to net loans to/from outsiders in the Investing Cash Flow section.
    
    NetOutwardLoansCashFlowStatement(store: IDictionary[str, Decimal])
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


class NetPolicyholderBenefitsAndClaimsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net provision in current period for future policy benefits, claims, and claims settlement expenses incurred in the claims
                settlement process before the effects of reinsurance arrangements. The value is net of the effects of contracts assumed and
                ceded.
    
    NetPolicyholderBenefitsAndClaimsIncomeStatement(store: IDictionary[str, Decimal])
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


class NetPPEBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Tangible assets that are held by an entity for use in the production or supply of goods and services, for rental to others, or for
                administrative purposes and that are expected to provide economic benefit for more than one year; net of accumulated
                depreciation.
    
    NetPPEBalanceSheet(store: IDictionary[str, Decimal])
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


class NetPPEPurchaseAndSaleCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net change between Purchases/Sales of PPE.
    
    NetPPEPurchaseAndSaleCashFlowStatement(store: IDictionary[str, Decimal])
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


class NetPreferredStockIssuanceCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of preferred stock.
    
    NetPreferredStockIssuanceCashFlowStatement(store: IDictionary[str, Decimal])
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


class NetPremiumsWrittenIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Net premiums written are gross premiums written less ceded premiums. This item is usually only available for insurance industry.
    
    NetPremiumsWrittenIncomeStatement(store: IDictionary[str, Decimal])
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


class NetProceedsPaymentForLoanCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net value of proceeds or payments of loans.
    
    NetProceedsPaymentForLoanCashFlowStatement(store: IDictionary[str, Decimal])
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


class NetRealizedGainLossOnInvestmentsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Gain or loss realized during the period of time for all kinds of investment securities. In might include trading, available-for-sale, or
                held-to-maturity securities. This item is usually only available for insurance industry.
    
    NetRealizedGainLossOnInvestmentsIncomeStatement(store: IDictionary[str, Decimal])
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


class NetShortTermDebtIssuanceCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of short term debt.
    
    NetShortTermDebtIssuanceCashFlowStatement(store: IDictionary[str, Decimal])
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


class NetTangibleAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Net assets in physical form. This is calculated using Stockholders' Equity less Intangible Assets (including Goodwill).
    
    NetTangibleAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class NetTradingIncomeIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Any trading income on the securities.
    
    NetTradingIncomeIncomeStatement(store: IDictionary[str, Decimal])
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


class NetUtilityPlantBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Net utility plant might include water production, electric utility plan, natural gas, fuel and other, common utility plant and
                accumulated depreciation. This item is usually only available for utility industry.
    
    NetUtilityPlantBalanceSheet(store: IDictionary[str, Decimal])
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


class NonCurrentAccountsReceivableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Accounts receivable represents sums owed to the business that the business records as revenue. Gross accounts receivable is
                accounts receivable before the business deducts uncollectable accounts to calculate the true value of accounts receivable.
    
    NonCurrentAccountsReceivableBalanceSheet(store: IDictionary[str, Decimal])
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


class NonCurrentAccruedExpensesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An expense that has occurred but the transaction has not been entered in the accounting records. Accordingly, an adjusting entry
                is made to debit the appropriate expense account and to credit a liability account such as accrued expenses payable or accounts
                payable.
    
    NonCurrentAccruedExpensesBalanceSheet(store: IDictionary[str, Decimal])
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


class NonCurrentDeferredAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Payments that will be assigned as expenses longer than one accounting period, but that are paid in advance and temporarily set up
                as non-current assets on the balance sheet.
    
    NonCurrentDeferredAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class NonCurrentDeferredLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents the non-current portion of obligations, which is a liability that usually would have been paid but is now past due.
    
    NonCurrentDeferredLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class NonCurrentDeferredRevenueBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The non-current portion of deferred revenue amount as of the balance sheet date. Deferred revenue is a liability related to revenue
                producing activity for which revenue has not yet been recognized, and is not expected be recognized in the next twelve months.
    
    NonCurrentDeferredRevenueBalanceSheet(store: IDictionary[str, Decimal])
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


class NonCurrentDeferredTaxesAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A result of timing differences between taxable incomes reported on the income statement and taxable income from the company's
                tax return. Depending on the positioning of deferred income taxes, the field may be either current (within current assets) or non-
                current (below total current assets). Typically a company will have two deferred income taxes fields.
    
    NonCurrentDeferredTaxesAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class NonCurrentDeferredTaxesLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The estimated future tax obligations, which usually arise when different accounting methods are used for financial statements and
                tax statement It is also an add-back to the cash flow statement. Deferred income taxes include accumulated tax deferrals due to
                accelerated depreciation and investment credit.
    
    NonCurrentDeferredTaxesLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class NonCurrentNoteReceivablesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An amount representing an agreement for an unconditional promise by the maker to pay the entity (holder) a definite sum of money
                at a future date(s), excluding the portion that is expected to be received within one year of the balance sheet date or the normal
                operating cycle, whichever is longer.
    
    NonCurrentNoteReceivablesBalanceSheet(store: IDictionary[str, Decimal])
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


class NonCurrentOtherFinancialLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other long term financial liabilities not categorized and due over one year or a normal operating cycle (whichever is longer).
    
    NonCurrentOtherFinancialLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class NonCurrentPensionAndOtherPostretirementBenefitPlansBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A loan issued by an insurance company that uses the cash value of a person's life insurance policy as collateral.  This item is usually
                only available in the insurance industry.
    
    NonCurrentPensionAndOtherPostretirementBenefitPlansBalanceSheet(store: IDictionary[str, Decimal])
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


class NonCurrentPrepaidAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of the carrying amounts that are paid in advance for expenses, which will be charged against earnings in periods after one
                year or beyond the operating cycle, if longer.
    
    NonCurrentPrepaidAssetsBalanceSheet(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    OneMonth: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class NonInterestBearingBorrowingsCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Non-interest bearing deposits in other financial institutions for short periods of time, usually less than 12 months.
    
    NonInterestBearingBorrowingsCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class NonInterestBearingBorrowingsNonCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Non-interest bearing borrowings due after a year.
    
    NonInterestBearingBorrowingsNonCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class NonInterestBearingBorrowingsTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Non-interest bearing deposits in other financial institutions for relatively short periods of time; on a Non-Differentiated Balance
                Sheet.
    
    NonInterestBearingBorrowingsTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class NonInterestBearingDepositsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of all domestic and foreign deposits in the banks that do not draw interest.
    
    NonInterestBearingDepositsBalanceSheet(store: IDictionary[str, Decimal])
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


class NonInterestExpenseIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Any expenses that not related to interest. It includes labor and related expense, occupancy and equipment, commission,
                professional expense and contract services expenses, selling, general and administrative, research and development depreciation,
                amortization and depletion, and any other special income/charges.
    
    NonInterestExpenseIncomeStatement(store: IDictionary[str, Decimal])
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


class NonInterestIncomeIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The total amount of non-interest income which may be derived from: (1) fees and commissions; (2) premiums earned; (3) equity
                investment; (4) the sale or disposal of assets; and (5) other sources not otherwise specified.
    
    NonInterestIncomeIncomeStatement(store: IDictionary[str, Decimal])
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


class NormalizedBasicEPS(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The basic normalized earnings per share. Normalized EPS removes onetime and unusual items from EPS, to provide investors with a
                more accurate measure of the company's true earnings. Normalized Earnings / Basic Weighted Average Shares Outstanding.
    
    NormalizedBasicEPS(store: IDictionary[str, Decimal])
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


class NormalizedBasicEPSGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's Normalized Basic EPS on a percentage basis.
    
    NormalizedBasicEPSGrowth(store: IDictionary[str, Decimal])
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


class NormalizedDilutedEPS(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The diluted normalized earnings per share. Normalized EPS removes onetime and unusual items from EPS, to provide investors with
                a more accurate measure of the company's true earnings. Normalized Earnings / Diluted Weighted Average Shares Outstanding.
    
    NormalizedDilutedEPS(store: IDictionary[str, Decimal])
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


class NormalizedDilutedEPSGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's Normalized Diluted EPS on a percentage basis.
    
    NormalizedDilutedEPSGrowth(store: IDictionary[str, Decimal])
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


class NormalizedEBITAsReportedIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    EBIT less Total Unusual Items. This is as reported by the company, may be the same or not the same as Morningstar's standardized
                definition.
    
    NormalizedEBITAsReportedIncomeStatement(store: IDictionary[str, Decimal])
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


class NormalizedEBITDAAsReportedIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    EBITDA less Total Unusual Items. This is as reported by the company, may be the same or not the same as Morningstar's
                standardized definition.
    
    NormalizedEBITDAAsReportedIncomeStatement(store: IDictionary[str, Decimal])
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


class OperatingExpenseIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Operating expenses are primary recurring costs associated with central operations (other than cost of goods sold) that are incurred
                in order to generate sales.
    
    OperatingExpenseIncomeStatement(store: IDictionary[str, Decimal])
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


class OperatingGainsLossesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The gain or loss from the entity's ongoing operations.
    
    OperatingGainsLossesCashFlowStatement(store: IDictionary[str, Decimal])
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


class OperatingIncomeIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Income from normal business operations after deducting cost of revenue and operating expenses. It does not include income from
                any investing activities.
    
    OperatingIncomeIncomeStatement(store: IDictionary[str, Decimal])
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


class OperatingLeaseAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A contract that allows for the use of an asset, but does not convey rights of ownership of the asset. An operating lease is not
                capitalized; it is accounted for as a rental expense in what is known as "off balance sheet financing." For the lessor, the asset being
                leased is accounted for as an asset and is depreciated as such.
    
    OperatingLeaseAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class OperatingRevenueIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sales and income that the company makes from its business operations. This applies only to non-bank and insurance companies.
                For Utility template companies, this is the sum of revenue from electric, gas, transportation and other operating revenue.
                For Transportation template companies, this is the sum of revenue-passenger, revenue-cargo, and other operating revenue.
    
    OperatingRevenueIncomeStatement(store: IDictionary[str, Decimal])
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


class OperationAndMaintenanceIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of operation and maintenance expenses, which is the one important operating expense for the utility
                industry. It includes any costs related to production and maintenance cost of the property during the revenue generation process.
                This item is usually only available for mining and utility industries.
    
    OperationAndMaintenanceIncomeStatement(store: IDictionary[str, Decimal])
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


class OperationIncomeGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's operating income on a percentage basis. Morningstar calculates the growth percentage based on the
                underlying operating income data reported in the Income Statement within the company filings or reports.
    
    OperationIncomeGrowth(store: IDictionary[str, Decimal])
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


class OperationMargin(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of operating income to revenue. Morningstar calculates the ratio by using the underlying data reported in the
                company filings or reports:   Operating Income / Revenue.
    
    OperationMargin(store: IDictionary[str, Decimal])
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


class OperationRatios(System.object):
    """
    Definition of the OperationRatios class
    
    OperationRatios()
    """
    def UpdateValues(self, update: QuantConnect.Data.Fundamental.OperationRatios) -> None:
        pass

    AssetsTurnover: QuantConnect.Data.Fundamental.AssetsTurnover

    AVG5YrsROIC: QuantConnect.Data.Fundamental.AVG5YrsROIC

    CapExGrowth: QuantConnect.Data.Fundamental.CapExGrowth

    CapExSalesRatio: QuantConnect.Data.Fundamental.CapExSalesRatio

    CapitalExpenditureAnnual5YrGrowth: QuantConnect.Data.Fundamental.CapitalExpenditureAnnual5YrGrowth

    CapitalExpendituretoEBITDA: QuantConnect.Data.Fundamental.CapitalExpendituretoEBITDA

    CashConversionCycle: QuantConnect.Data.Fundamental.CashConversionCycle

    CashFlowfromFinancingGrowth: QuantConnect.Data.Fundamental.CashFlowfromFinancingGrowth

    CashFlowfromInvestingGrowth: QuantConnect.Data.Fundamental.CashFlowfromInvestingGrowth

    CashRatio: QuantConnect.Data.Fundamental.CashRatio

    CashRatioGrowth: QuantConnect.Data.Fundamental.CashRatioGrowth

    CashtoTotalAssets: QuantConnect.Data.Fundamental.CashtoTotalAssets

    CFOGrowth: QuantConnect.Data.Fundamental.CFOGrowth

    CommonEquityToAssets: QuantConnect.Data.Fundamental.CommonEquityToAssets

    CurrentRatio: QuantConnect.Data.Fundamental.CurrentRatio

    CurrentRatioGrowth: QuantConnect.Data.Fundamental.CurrentRatioGrowth

    DaysInInventory: QuantConnect.Data.Fundamental.DaysInInventory

    DaysInPayment: QuantConnect.Data.Fundamental.DaysInPayment

    DaysInSales: QuantConnect.Data.Fundamental.DaysInSales

    DebttoAssets: QuantConnect.Data.Fundamental.DebttoAssets

    EBITDAGrowth: QuantConnect.Data.Fundamental.EBITDAGrowth

    EBITDAMargin: QuantConnect.Data.Fundamental.EBITDAMargin

    EBITMargin: QuantConnect.Data.Fundamental.EBITMargin

    ExpenseRatio: QuantConnect.Data.Fundamental.ExpenseRatio

    FCFGrowth: QuantConnect.Data.Fundamental.FCFGrowth

    FCFNetIncomeRatio: QuantConnect.Data.Fundamental.FCFNetIncomeRatio

    FCFSalesRatio: QuantConnect.Data.Fundamental.FCFSalesRatio

    FCFtoCFO: QuantConnect.Data.Fundamental.FCFtoCFO

    FinancialLeverage: QuantConnect.Data.Fundamental.FinancialLeverage

    FixAssetsTuronver: QuantConnect.Data.Fundamental.FixAssetsTuronver

    GrossMargin: QuantConnect.Data.Fundamental.GrossMargin

    GrossMargin5YrAvg: QuantConnect.Data.Fundamental.GrossMargin5YrAvg

    GrossProfitAnnual5YrGrowth: QuantConnect.Data.Fundamental.GrossProfitAnnual5YrGrowth

    InterestCoverage: QuantConnect.Data.Fundamental.InterestCoverage

    InventoryTurnover: QuantConnect.Data.Fundamental.InventoryTurnover

    LongTermDebtEquityRatio: QuantConnect.Data.Fundamental.LongTermDebtEquityRatio

    LongTermDebtTotalCapitalRatio: QuantConnect.Data.Fundamental.LongTermDebtTotalCapitalRatio

    LossRatio: QuantConnect.Data.Fundamental.LossRatio

    NetIncomeContOpsGrowth: QuantConnect.Data.Fundamental.NetIncomeContOpsGrowth

    NetIncomeGrowth: QuantConnect.Data.Fundamental.NetIncomeGrowth

    NetIncomePerEmployee: QuantConnect.Data.Fundamental.NetIncomePerEmployee

    NetMargin: QuantConnect.Data.Fundamental.NetMargin

    NormalizedNetProfitMargin: QuantConnect.Data.Fundamental.NormalizedNetProfitMargin

    NormalizedROIC: QuantConnect.Data.Fundamental.NormalizedROIC

    OperationIncomeGrowth: QuantConnect.Data.Fundamental.OperationIncomeGrowth

    OperationMargin: QuantConnect.Data.Fundamental.OperationMargin

    OperationRevenueGrowth3MonthAvg: QuantConnect.Data.Fundamental.OperationRevenueGrowth3MonthAvg

    PaymentTurnover: QuantConnect.Data.Fundamental.PaymentTurnover

    PostTaxMargin5YrAvg: QuantConnect.Data.Fundamental.PostTaxMargin5YrAvg

    PretaxMargin: QuantConnect.Data.Fundamental.PretaxMargin

    PreTaxMargin5YrAvg: QuantConnect.Data.Fundamental.PreTaxMargin5YrAvg

    ProfitMargin5YrAvg: QuantConnect.Data.Fundamental.ProfitMargin5YrAvg

    QuickRatio: QuantConnect.Data.Fundamental.QuickRatio

    ReceivableTurnover: QuantConnect.Data.Fundamental.ReceivableTurnover

    RegressionGrowthOperatingRevenue5Years: QuantConnect.Data.Fundamental.RegressionGrowthOperatingRevenue5Years

    RevenueGrowth: QuantConnect.Data.Fundamental.RevenueGrowth

    ROA: QuantConnect.Data.Fundamental.ROA

    ROA5YrAvg: QuantConnect.Data.Fundamental.ROA5YrAvg

    ROE: QuantConnect.Data.Fundamental.ROE

    ROE5YrAvg: QuantConnect.Data.Fundamental.ROE5YrAvg

    ROIC: QuantConnect.Data.Fundamental.ROIC

    SalesPerEmployee: QuantConnect.Data.Fundamental.SalesPerEmployee

    SolvencyRatio: QuantConnect.Data.Fundamental.SolvencyRatio

    StockholdersEquityGrowth: QuantConnect.Data.Fundamental.StockholdersEquityGrowth

    TaxRate: QuantConnect.Data.Fundamental.TaxRate

    TotalAssetsGrowth: QuantConnect.Data.Fundamental.TotalAssetsGrowth

    TotalDebtEquityRatio: QuantConnect.Data.Fundamental.TotalDebtEquityRatio

    TotalDebtEquityRatioGrowth: QuantConnect.Data.Fundamental.TotalDebtEquityRatioGrowth

    TotalLiabilitiesGrowth: QuantConnect.Data.Fundamental.TotalLiabilitiesGrowth

    WorkingCapitalTurnoverRatio: QuantConnect.Data.Fundamental.WorkingCapitalTurnoverRatio



class OperationRevenueGrowth3MonthAvg(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's operating revenue on a percentage basis. Morningstar calculates the growth percentage based on
                the underlying operating revenue data reported in the Income Statement within the company filings or reports.
    
    OperationRevenueGrowth3MonthAvg(store: IDictionary[str, Decimal])
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


class OrdinarySharesNumberBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Number of Common or Ordinary Shares.
    
    OrdinarySharesNumberBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other non-current assets that are not otherwise classified.
    
    OtherAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherBorrowedFundsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other borrowings by the bank to fund its activities that cannot be identified by other specific items in the Liabilities section.
    
    OtherBorrowedFundsBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherCapitalStockBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other Capital Stock that is not otherwise classified.
    
    OtherCapitalStockBalanceSheet(store: IDictionary[str, Decimal])
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

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class OtherCashAdjustExcludeFromChangeinCashCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other changes to cash and cash equivalents during the accounting PeriodAsByte.
    
    OtherCashAdjustExcludeFromChangeinCashCashFlowStatement(store: IDictionary[str, Decimal])
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


class OtherCashAdjustIncludedIntoChangeinCashCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other cash adjustments included in change in cash not categorized above.
    
    OtherCashAdjustIncludedIntoChangeinCashCashFlowStatement(store: IDictionary[str, Decimal])
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


class OtherCashPaymentsfromOperatingActivitiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other cash payments for the direct cash flow.
    
    OtherCashPaymentsfromOperatingActivitiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class OtherCashReceiptsfromOperatingActivitiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other cash receipts for the direct cash flow.
    
    OtherCashReceiptsfromOperatingActivitiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class OtherCostofRevenueIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other costs associated with the revenue-generating activities of the company not categorized above.
    
    OtherCostofRevenueIncomeStatement(store: IDictionary[str, Decimal])
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


class OtherCurrentAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other current assets that are not otherwise classified.
    
    OtherCurrentAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherCurrentBorrowingsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Short Term Borrowings that are not otherwise classified.
    
    OtherCurrentBorrowingsBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherCurrentLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other current liabilities = Total current liabilities - Payables and accrued Expenses - Current debt and capital lease obligation -
                provisions, current - deferred liabilities, current.
    
    OtherCurrentLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherCustomerServicesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents fees and commissions earned from provide other services. This item is usually only available for bank industry.
    
    OtherCustomerServicesIncomeStatement(store: IDictionary[str, Decimal])
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


class OtherEquityAdjustmentsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other adjustments to stockholders' equity that is not otherwise classified, including other reserves.
    
    OtherEquityAdjustmentsBalanceSheet(store: IDictionary[str, Decimal])
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

    TwoMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class OtherEquityInterestBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other equity instruments issued by the company that cannot be identified by other specific items in the Equity section.
    
    OtherEquityInterestBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherFinancialLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other financial liabilities not categorized.
    
    OtherFinancialLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherGAIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other General and Administrative Expenses not categorized that the company incurs that are not directly tied to a specific function
                such as manufacturing, production, or sales.
    
    OtherGAIncomeStatement(store: IDictionary[str, Decimal])
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


class OtherIncomeExpenseIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Income or expense that comes from miscellaneous sources.
    
    OtherIncomeExpenseIncomeStatement(store: IDictionary[str, Decimal])
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


class OtherIntangibleAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of the carrying amounts of all intangible assets, excluding goodwill.
    
    OtherIntangibleAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherInterestExpenseIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    All other interest expense that is not otherwise classified
    
    OtherInterestExpenseIncomeStatement(store: IDictionary[str, Decimal])
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


class OtherInterestIncomeIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    All other interest income that is not otherwise classified
    
    OtherInterestIncomeIncomeStatement(store: IDictionary[str, Decimal])
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


class OtherInventoriesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other non-current inventories not otherwise classified.
    
    OtherInventoriesBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherInvestedAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An item represents all the other investments or/and securities that cannot be defined into any category above. This item is typically
                available for the insurance industry.
    
    OtherInvestedAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherInvestmentsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Investments that are neither Investment in Financial Assets nor Long term equity investment, not expected to be cashed within a
                year.
    
    OtherInvestmentsBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This item is available for bank and insurance industries.
    
    OtherLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherLoanAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Reflects the carrying amount of any other unpaid loans, an asset of the bank.
    
    OtherLoanAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherLoansCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other loans between the customer and bank which cannot be identified by other specific items in the Debt section, due within the
                next 12 months or operating cycle.
    
    OtherLoansCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherLoansNonCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other loans between the customer and bank which cannot be identified by other specific items in the Debt section, due beyond the
                current operating cycle.
    
    OtherLoansNonCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherLoansTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total other loans between the customer and bank which cannot be identified by other specific items in the Debt section; in a Non-
                Differentiated Balance Sheet.
    
    OtherLoansTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherNonCashItemsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Items which adjusted back from net income but without real cash outflow or inflow.
    
    OtherNonCashItemsCashFlowStatement(store: IDictionary[str, Decimal])
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


class OtherNonCurrentAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other non-current assets that are not otherwise classified.
    
    OtherNonCurrentAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherNonCurrentLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This item is usually not available for bank and insurance industries.
    
    OtherNonCurrentLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherNonInterestExpenseIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    All other non interest expense that is not otherwise classified
    
    OtherNonInterestExpenseIncomeStatement(store: IDictionary[str, Decimal])
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


class OtherNonInterestIncomeIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Usually available for the banking industry.  This is Non-Interest Income that is not otherwise classified.
    
    OtherNonInterestIncomeIncomeStatement(store: IDictionary[str, Decimal])
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


class OtherNonOperatingExpensesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other expenses of the company that cannot be identified by other specific items in the Non-Operating section.
    
    OtherNonOperatingExpensesIncomeStatement(store: IDictionary[str, Decimal])
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


class OtherNonOperatingIncomeExpensesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total other income and expense of the company that cannot be identified by other specific items in the Non-Operating section.
    
    OtherNonOperatingIncomeExpensesIncomeStatement(store: IDictionary[str, Decimal])
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


class OtherNonOperatingIncomeIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other income of the company that cannot be identified by other specific items in the Non-Operating section.
    
    OtherNonOperatingIncomeIncomeStatement(store: IDictionary[str, Decimal])
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


class OtherOperatingExpensesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of operating expenses associated with normal operations. Will not include any gain, loss, benefit, or income;
                and its value reported by the company should be <0.
    
    OtherOperatingExpensesIncomeStatement(store: IDictionary[str, Decimal])
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


class OtherOperatingIncomeTotalIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total Other Operating Income- including interest income, dividend income and other types of operating income.
    
    OtherOperatingIncomeTotalIncomeStatement(store: IDictionary[str, Decimal])
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


class OtherOperatingInflowsOutflowsofCashCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Any other cash inflows or outflows in the Operating Cash Flow section, not accounted for in the other specified items.
    
    OtherOperatingInflowsOutflowsofCashCashFlowStatement(store: IDictionary[str, Decimal])
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


class OtherPayableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Payables and Accrued Expenses that are not defined as Trade, Tax or Dividends related.
    
    OtherPayableBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherPropertiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other fixed assets not otherwise classified.
    
    OtherPropertiesBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherRealEstateOwnedBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The Carrying amount as of the balance sheet date of other real estate, which may include real estate investments, real estate loans
                that qualify as investments in real estate, and premises that are no longer used in operations may also be included in real estate
                owned. This does not include real estate assets taken in settlement of troubled loans through surrender or foreclosure.  This item is
                typically available for bank industry.
    
    OtherRealEstateOwnedBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherReceivablesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other non-current receivables not otherwise classified.
    
    OtherReceivablesBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherReservesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other reserves owned by the company that cannot be identified by other specific items in the Reserves section.
    
    OtherReservesBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherShortTermInvestmentsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of short term investments, which will be expired within one year that are not specifically classified as
                Available-for-Sale, Held-to-Maturity,  nor Trading investments.
    
    OtherShortTermInvestmentsBalanceSheet(store: IDictionary[str, Decimal])
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


class OtherSpecialChargesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    All other special charges that are not otherwise classified
    
    OtherSpecialChargesIncomeStatement(store: IDictionary[str, Decimal])
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


class OtherStaffCostsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Other costs in incurred in lieu of the employees that cannot be identified by other specific items in the Staff Costs section.
    
    OtherStaffCostsIncomeStatement(store: IDictionary[str, Decimal])
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


class OtherTaxesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Any taxes that are not part of income taxes. This item is usually not available for bank and insurance industries.
    
    OtherTaxesIncomeStatement(store: IDictionary[str, Decimal])
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


class OtherunderPreferredStockDividendIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Dividend paid to the preferred shareholders before the common stock shareholders.
    
    OtherunderPreferredStockDividendIncomeStatement(store: IDictionary[str, Decimal])
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


class OtherUnderwritingExpensesPaidCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash paid out for underwriting expenses, such as the acquisition of new and renewal insurance contracts, in operating cash flow,
                using the direct method. This item is usually only available for insurance industry
    
    OtherUnderwritingExpensesPaidCashFlowStatement(store: IDictionary[str, Decimal])
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


class PayablesAndAccruedExpensesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This balance sheet account includes all current payables and accrued expenses.
    
    PayablesAndAccruedExpensesBalanceSheet(store: IDictionary[str, Decimal])
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


class PayablesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The sum of all payables owed and expected to be paid within one year or one operating cycle, including accounts payables, taxes
                payable, dividends payable and all other current payables.
    
    PayablesBalanceSheet(store: IDictionary[str, Decimal])
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


class PaymentForLoansCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Payment from a bank or insurance company to the lender who lends money or property based on the agreement, along with
                interest, at a predetermined date in the future.
    
    PaymentForLoansCashFlowStatement(store: IDictionary[str, Decimal])
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


class PaymentsonBehalfofEmployeesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash paid in a form of salaries or other benefits to employees of the company, in the direct cash flow.
    
    PaymentsonBehalfofEmployeesCashFlowStatement(store: IDictionary[str, Decimal])
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


class PaymentstoSuppliersforGoodsandServicesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash paid to suppliers when purchasing goods or services by the company, in the direct cash flow.
    
    PaymentstoSuppliersforGoodsandServicesCashFlowStatement(store: IDictionary[str, Decimal])
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


class PaymentTurnover(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cost of Goods Sold / Average Accounts Payables
    
    PaymentTurnover(store: IDictionary[str, Decimal])
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


class PensionAndEmployeeBenefitExpenseCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount of pension and other (such as medical, dental and life insurance) postretirement benefit costs recognized during the
                PeriodAsByte.
    
    PensionAndEmployeeBenefitExpenseCashFlowStatement(store: IDictionary[str, Decimal])
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


class PensionandOtherPostRetirementBenefitPlansCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total of the carrying values as of the balance sheet date of obligations incurred through that date and payable for obligations related
                to services received from employees, such as accrued salaries and bonuses, payroll taxes and fringe benefits.
    
    PensionandOtherPostRetirementBenefitPlansCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class PensionAndOtherPostretirementBenefitPlansTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total of the carrying values as of the balance sheet date of obligations incurred through that date and payable for obligations related
                to services received from employees, such as accrued salaries and bonuses, payroll taxes and fringe benefits. Used to reflect the
                current portion of the liabilities (due within one year or within the normal operating cycle if longer).
    
    PensionAndOtherPostretirementBenefitPlansTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class PensionCostsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The expense that a company incurs each year by providing a pension plan for its employees. Major expenses in the pension cost
                include employer matching contributions and management fees.
    
    PensionCostsIncomeStatement(store: IDictionary[str, Decimal])
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


class Period(System.object):
    """ Period constants for multi-period fields """
    FiveYears: str
    NineMonths: str
    OneMonth: str
    OneYear: str
    SixMonths: str
    TenYears: str
    ThreeMonths: str
    ThreeYears: str
    TwelveMonths: str
    TwoMonths: str
    TwoYears: str
    __all__: list


class PolicyAcquisitionExpenseIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Costs that vary with and are primarily related to the acquisition of new and renewal insurance contracts. Also referred to as
                underwriting expenses.
    
    PolicyAcquisitionExpenseIncomeStatement(store: IDictionary[str, Decimal])
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


class PolicyholderBenefitsCededIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The provision in current period for future policy benefits, claims, and claims settlement, which is under reinsurance arrangements.
                This item is usually only available for insurance industry.
    
    PolicyholderBenefitsCededIncomeStatement(store: IDictionary[str, Decimal])
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


class PolicyholderBenefitsGrossIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The gross amount of provision in current period for future policyholder benefits, claims, and claims settlement, incurred in the
                claims settlement process before the effects of reinsurance arrangements. This item is usually only available for insurance industry.
    
    PolicyholderBenefitsGrossIncomeStatement(store: IDictionary[str, Decimal])
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


class PolicyholderDepositInvestmentReceivedCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash received from policyholder deposit investment activities in operating cash flow, using the direct method. This item is usually
                only available for insurance industry
    
    PolicyholderDepositInvestmentReceivedCashFlowStatement(store: IDictionary[str, Decimal])
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


class PolicyholderDividendsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Payments made or credits extended to the insured by the company, usually at the end of a policy year results in reducing the net
                insurance cost to the policyholder. Such dividends may be paid in cash to the insured or applied by the insured as reductions of the
                premiums due for the next policy year. This item is usually only available for insurance industry.
    
    PolicyholderDividendsIncomeStatement(store: IDictionary[str, Decimal])
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


class PolicyholderFundsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The total liability as of the balance sheet date of amounts due to policy holders, excluding future policy benefits and claims,
                including unpaid policy dividends, retrospective refunds, and undistributed earnings on participating business.
    
    PolicyholderFundsBalanceSheet(store: IDictionary[str, Decimal])
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


class PolicyholderInterestIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The periodic income payment provided to the annuitant by the insurance company, which is determined by the assumed interest
                rate (AIR) and other factors. This item is usually only available for insurance industry.
    
    PolicyholderInterestIncomeStatement(store: IDictionary[str, Decimal])
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


class PolicyLoansBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A loan issued by an insurance company that uses the cash value of a person's life insurance policy as collateral. This item is usually
                only available for insurance industry.
    
    PolicyLoansBalanceSheet(store: IDictionary[str, Decimal])
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


class PolicyReservesBenefitsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Accounting policy pertaining to an insurance entity's net liability for future benefits (for example, death, cash surrender value) to be
                paid to or on behalf of policyholders, describing the bases, methodologies and components of the reserve, and assumptions
                regarding estimates of expected investment yields, mortality, morbidity, terminations and expenses.
    
    PolicyReservesBenefitsBalanceSheet(store: IDictionary[str, Decimal])
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


class PostTaxMargin5YrAvg(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This is the simple average of the company's Annual Post Tax Margin over the last 5 years. Post tax margin is Post tax divided by
                total revenue for the same PeriodAsByte.
    
    PostTaxMargin5YrAvg(store: IDictionary[str, Decimal])
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


class PreferredSecuritiesOutsideStockEquityBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Preferred securities that that firm treats as a liability. It includes convertible preferred stock or redeemable preferred stock.
    
    PreferredSecuritiesOutsideStockEquityBalanceSheet(store: IDictionary[str, Decimal])
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


class PreferredSharesNumberBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Number of Preferred Shares.
    
    PreferredSharesNumberBalanceSheet(store: IDictionary[str, Decimal])
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


class PreferredStockBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Preferred stock (all issues) at par value, as reported within the Stockholder's Equity section of the balance sheet.
    
    PreferredStockBalanceSheet(store: IDictionary[str, Decimal])
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


class PreferredStockDividendPaidCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Pay for the amount of dividends declared or paid in the period to preferred shareholders or the amount for which the obligation to
                pay them dividends rose in the PeriodAsByte.
    
    PreferredStockDividendPaidCashFlowStatement(store: IDictionary[str, Decimal])
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


class PreferredStockDividendsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount of dividends declared or paid in the period to preferred shareholders, or the amount for which the obligation to pay
                them dividends arose in the PeriodAsByte. Preferred dividends are the amount required for the current year only, and not for any amount
                required in past years.
    
    PreferredStockDividendsIncomeStatement(store: IDictionary[str, Decimal])
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


class PreferredStockEquityBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A class of ownership in a company that has a higher claim on the assets and earnings than common stock. Preferred stock
                generally has a dividend that must be paid out before dividends to common stockholders and the shares usually do not have voting
                rights.
    
    PreferredStockEquityBalanceSheet(store: IDictionary[str, Decimal])
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


class PreferredStockIssuanceCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash inflow from offering preferred stock.
    
    PreferredStockIssuanceCashFlowStatement(store: IDictionary[str, Decimal])
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


class PreferredStockPaymentsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash outflow to reacquire preferred stock during the PeriodAsByte.
    
    PreferredStockPaymentsCashFlowStatement(store: IDictionary[str, Decimal])
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


class PremiumReceivedCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash received from premium income in operating cash flow, using the direct method. This item is usually only available for
                insurance industry
    
    PremiumReceivedCashFlowStatement(store: IDictionary[str, Decimal])
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


class PrepaidAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of the carrying amounts that are paid in advance for expenses, which will be charged against earnings in subsequent periods.
    
    PrepaidAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class PretaxIncomeIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Reported income before the deduction or benefit of income taxes.
    
    PretaxIncomeIncomeStatement(store: IDictionary[str, Decimal])
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


class PretaxMargin(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of pretax income to revenue. Morningstar calculates the ratio by using the underlying data reported in the
                company filings or reports:   Pretax Income / Revenue.
    
    PretaxMargin(store: IDictionary[str, Decimal])
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


class PreTaxMargin5YrAvg(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This is the simple average of the company's Annual Pre Tax Margin over the last 5 years. Pre tax margin is Pre tax divided by total
                revenue for the same PeriodAsByte.
    
    PreTaxMargin5YrAvg(store: IDictionary[str, Decimal])
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


class PreTreShaNumBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The treasury stock number of preferred shares. This represents the number of preferred shares owned by the company as a result
                of share repurchase programs or donations.
    
    PreTreShaNumBalanceSheet(store: IDictionary[str, Decimal])
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


class ProceedsFromLoansCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash inflow from borrowing money or property for a bank or insurance company.
    
    ProceedsFromLoansCashFlowStatement(store: IDictionary[str, Decimal])
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


class ProceedsFromStockOptionExercisedCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash inflow associated with the amount received from holders exercising their stock options.
    
    ProceedsFromStockOptionExercisedCashFlowStatement(store: IDictionary[str, Decimal])
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


class ProceedsPaymentFederalFundsSoldAndSecuritiesPurchasedUnderAgreementToResellCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount change of (1) the lending of excess federal funds to another commercial bank requiring such for its legal
                reserve requirements and (2) securities purchased under agreements to resell. This item is usually only available for bank industry.
    
    ProceedsPaymentFederalFundsSoldAndSecuritiesPurchasedUnderAgreementToResellCashFlowStatement(store: IDictionary[str, Decimal])
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


class ProceedsPaymentInInterestBearingDepositsInBankCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net change on interest-bearing deposits in other financial institutions for relatively short periods of time including, for example,
                certificates of deposits.
    
    ProceedsPaymentInInterestBearingDepositsInBankCashFlowStatement(store: IDictionary[str, Decimal])
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


class ProfessionalExpenseAndContractServicesExpenseIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Professional and contract service expense includes cost reimbursements for support services related to contracted projects,
                outsourced management, technical and staff support. This item is usually only available for bank industry.
    
    ProfessionalExpenseAndContractServicesExpenseIncomeStatement(store: IDictionary[str, Decimal])
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


class ProfitMargin5YrAvg(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This is the simple average of the company's Annual Net Profit Margin over the last 5 years. Net profit margin is post tax income
                divided by total revenue for the same PeriodAsByte.
    
    ProfitMargin5YrAvg(store: IDictionary[str, Decimal])
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


class ProfitonDisposalsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The difference between the sale price or salvage price and the book value of an asset that was sold or retired during the reporting
                PeriodAsByte.
    
    ProfitonDisposalsCashFlowStatement(store: IDictionary[str, Decimal])
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


class PropertiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Tangible assets that are held by an entity for use in the production or supply of goods and services, for rental to others, or for
                administrative purposes and that are expected to provide economic benefit for more than one year. This item is available for
                manufacturing, bank and transportation industries.
    
    PropertiesBalanceSheet(store: IDictionary[str, Decimal])
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


class ProvisionandWriteOffofAssetsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A non-cash adjustment for total provision and write off on assets & liabilities.
    
    ProvisionandWriteOffofAssetsCashFlowStatement(store: IDictionary[str, Decimal])
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


class ProvisionForDoubtfulAccountsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Amount of the current period expense charged against operations, the offset which is generally to the allowance for doubtful
                accounts for the purpose of reducing receivables, including notes receivable, to an amount that approximates their net realizable
                value (the amount expected to be collected). The category includes provision for loan losses, provision for any doubtful account
                receivable, and bad debt expenses. This item is usually not available for bank and insurance industries.
    
    ProvisionForDoubtfulAccountsIncomeStatement(store: IDictionary[str, Decimal])
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


class ProvisionForLoanLeaseAndOtherLossesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The sum of the periodic provision charged to earnings, based on an assessment of uncollectible from the counterparty on account
                of loan, lease or other credit losses, to reduce these accounts to the amount that approximates their net realizable value. This item
                is usually only available for bank industry.
    
    ProvisionForLoanLeaseAndOtherLossesCashFlowStatement(store: IDictionary[str, Decimal])
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


class ProvisionsTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Provisions are created to protect the interests of one or both parties named in a contract or legal document, which is a preparatory
                action or measure. Current provision is expired within one accounting PeriodAsByte.
    
    ProvisionsTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class PurchaseOfBusinessCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    All the purchases of business including business acquisitions, investment in subsidiary; investing in affiliated companies, and join
                venture.
    
    PurchaseOfBusinessCashFlowStatement(store: IDictionary[str, Decimal])
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


class PurchaseOfIntangiblesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount of capital outlays undertaken to increase, construct or improve intangible assets.
    
    PurchaseOfIntangiblesCashFlowStatement(store: IDictionary[str, Decimal])
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


class PurchaseOfInvestmentCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    All purchases of investments, including both long term and short term.
    
    PurchaseOfInvestmentCashFlowStatement(store: IDictionary[str, Decimal])
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


class PurchaseOfInvestmentPropertiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash outflow for purchases of investment properties during the accounting PeriodAsByte.
    
    PurchaseOfInvestmentPropertiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class PurchaseofJointVentureAssociateCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Purchase of joint venture/associates (investment below 50%).
    
    PurchaseofJointVentureAssociateCashFlowStatement(store: IDictionary[str, Decimal])
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


class PurchaseOfPPECashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount of capital outlays undertaken to increase, construct or improve capital assets. This category includes property, plant
                equipment, furniture, fixed assets, buildings, and improvement.
    
    PurchaseOfPPECashFlowStatement(store: IDictionary[str, Decimal])
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


class PurchaseofSubsidiariesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Purchase of subsidiaries or interest in subsidiaries (investments 51% and above).
    
    PurchaseofSubsidiariesCashFlowStatement(store: IDictionary[str, Decimal])
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


class QuickRatio(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of liquid assets to Current Liabilities. Morningstar calculates the ratio by using the underlying data reported in the
                Balance Sheet within the company filings or reports:(Cash, Cash Equivalents, and Short Term Investments + Receivables ) /
                Current Liabilities.
    
    QuickRatio(store: IDictionary[str, Decimal])
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


class RawMaterialsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Carrying amount as of the balance sheet data of unprocessed items to be consumed in the manufacturing or production process.
                This item is available for manufacturing and mining industries.
    
    RawMaterialsBalanceSheet(store: IDictionary[str, Decimal])
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


class RealizedGainLossOnSaleOfLoansAndLeaseCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The gains and losses included in earnings that represent the difference between the sale price and the carrying value of loans and
                leases that were sold during the reporting PeriodAsByte. This element refers to the gain (loss) and not to the cash proceeds of the sales.
                This element is a non-cash adjustment to net income when calculating net cash generated by operating activities using the indirect
                method. This item is usually only available for bank industry.
    
    RealizedGainLossOnSaleOfLoansAndLeaseCashFlowStatement(store: IDictionary[str, Decimal])
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


class ReceiptsfromCustomersCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Payment received from customers in the Direct Cash Flow.
    
    ReceiptsfromCustomersCashFlowStatement(store: IDictionary[str, Decimal])
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


class ReceiptsfromGovernmentGrantsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash received from governments in the form of grants in the Direct Cash Flow.
    
    ReceiptsfromGovernmentGrantsCashFlowStatement(store: IDictionary[str, Decimal])
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


class ReceivablesAdjustmentsAllowancesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A provision relating to a written agreement to receive money at a specified future date(s) (within one year from the reporting date
                or the normal operating cycle, whichever is longer), consisting of principal as well as any accrued interest).
    
    ReceivablesAdjustmentsAllowancesBalanceSheet(store: IDictionary[str, Decimal])
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


class ReceivablesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The sum of all receivables owed by customers and affiliates within one year, including accounts receivable, notes receivable,
                premiums receivable, and other current receivables.
    
    ReceivablesBalanceSheet(store: IDictionary[str, Decimal])
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


class ReceivableTurnover(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Revenue / Average Accounts Receivables
    
    ReceivableTurnover(store: IDictionary[str, Decimal])
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


class ReconciledCostOfRevenueIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The Cost Of Revenue plus Depreciation, Depletion & Amortization from the IncomeStatement; minus Depreciation, Depletion &
                Amortization from the Cash Flow Statement
    
    ReconciledCostOfRevenueIncomeStatement(store: IDictionary[str, Decimal])
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


class ReconciledDepreciationIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Is Depreciation, Depletion & Amortization from the Cash Flow Statement
    
    ReconciledDepreciationIncomeStatement(store: IDictionary[str, Decimal])
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


class RegressionGrowthofDividends5Years(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The five-year growth rate of dividends per share, calculated using regression analysis.
    
    RegressionGrowthofDividends5Years(store: IDictionary[str, Decimal])
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


class RegressionGrowthOperatingRevenue5Years(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The five-year growth rate of operating revenue, calculated using regression analysis.
    
    RegressionGrowthOperatingRevenue5Years(store: IDictionary[str, Decimal])
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


class RegulatoryAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Carrying amount as of the balance sheet date of capitalized costs of regulated entities that are expected to be recovered through
                revenue sources over one year or beyond the normal operating cycle.
    
    RegulatoryAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class RegulatoryLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount for the individual regulatory noncurrent liability as itemized in a table of regulatory noncurrent liabilities as of the end of
                the PeriodAsByte. Such things as the costs of energy efficiency programs and low-income energy assistances programs and deferred fuel.
                This item is usually only available for utility industry.
    
    RegulatoryLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class ReinsuranceandOtherRecoveriesReceivedCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash received from reinsurance income or other recoveries income in operating cash flow, using the direct method. This item is
                usually only available for insurance industry
    
    ReinsuranceandOtherRecoveriesReceivedCashFlowStatement(store: IDictionary[str, Decimal])
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


class ReinsuranceAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Reinsurance asset is insurance that is purchased by an insurance company from another insurance company.
    
    ReinsuranceAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class ReinsuranceBalancesPayableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The carrying amount as of the balance sheet date of the known and estimated amounts owed to insurers under reinsurance
                treaties or other arrangements. This item is usually only available for insurance industry.
    
    ReinsuranceBalancesPayableBalanceSheet(store: IDictionary[str, Decimal])
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


class ReinsuranceRecoverableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount of benefits the ceding insurer expects to recover on insurance policies ceded to other insurance entities as of the
                balance sheet date for all guaranteed benefit types. It includes estimated amounts for claims incurred but not reported, and policy
                benefits, net of any related valuation allowance.
    
    ReinsuranceRecoverableBalanceSheet(store: IDictionary[str, Decimal])
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


class ReinsuranceRecoveriesClaimsandBenefitsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Claim on the reinsurance company and take the benefits.
    
    ReinsuranceRecoveriesClaimsandBenefitsIncomeStatement(store: IDictionary[str, Decimal])
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


class ReinsuranceRecoveriesofInsuranceLiabilitiesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Income/Expense due to recoveries from reinsurers for insurance liabilities.
    
    ReinsuranceRecoveriesofInsuranceLiabilitiesIncomeStatement(store: IDictionary[str, Decimal])
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


class ReinsuranceRecoveriesofInvestmentContractIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Income/Expense due to recoveries from reinsurers for Investment Contracts.
    
    ReinsuranceRecoveriesofInvestmentContractIncomeStatement(store: IDictionary[str, Decimal])
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


class RentandLandingFeesCostofRevenueIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Costs paid to use the facilities necessary to generate revenue during the accounting PeriodAsByte.
    
    RentandLandingFeesCostofRevenueIncomeStatement(store: IDictionary[str, Decimal])
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


class RentAndLandingFeesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Rent fees are the cost of occupying space during the accounting PeriodAsByte. Landing fees are a change paid to an airport company for
                landing at a particular airport. This item is not available for insurance industry.
    
    RentAndLandingFeesIncomeStatement(store: IDictionary[str, Decimal])
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


class RentExpenseSupplementalIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The sum of all rent expenses incurred by the company for operating leases during the year, it is a supplemental value which would
                be reported outside consolidated statements or consolidated statement's footnotes.
    
    RentExpenseSupplementalIncomeStatement(store: IDictionary[str, Decimal])
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


class ReorganizationOtherCostsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A non-cash adjustment relating to restructuring costs.
    
    ReorganizationOtherCostsCashFlowStatement(store: IDictionary[str, Decimal])
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


class RepaymentinLeaseFinancingCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash outflow to repay lease financing during the PeriodAsByte.
    
    RepaymentinLeaseFinancingCashFlowStatement(store: IDictionary[str, Decimal])
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


class RepaymentOfDebtCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Payments to Settle Long Term Debt plus Payments to Settle Short Term Debt.
    
    RepaymentOfDebtCashFlowStatement(store: IDictionary[str, Decimal])
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


class ReportedNormalizedBasicEPS(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Normalized Basic EPS as reported by the company in the financial statements.
    
    ReportedNormalizedBasicEPS(store: IDictionary[str, Decimal])
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


class ReportedNormalizedDilutedEPS(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Normalized Diluted EPS as reported by the company in the financial statements.
    
    ReportedNormalizedDilutedEPS(store: IDictionary[str, Decimal])
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


class RepurchaseOfCapitalStockCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Payments for Common Stock plus Payments for Preferred Stock.
    
    RepurchaseOfCapitalStockCashFlowStatement(store: IDictionary[str, Decimal])
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


class ResearchAndDevelopmentExpensesSupplementalIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of research and development expenses during the year. It is a supplemental value which would be reported
                outside consolidated statements.
    
    ResearchAndDevelopmentExpensesSupplementalIncomeStatement(store: IDictionary[str, Decimal])
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


class ResearchAndDevelopmentIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of research and development expenses during the year.
    
    ResearchAndDevelopmentIncomeStatement(store: IDictionary[str, Decimal])
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


class RestrictedCashAndCashEquivalentsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The carrying amounts of cash and cash equivalent items which are restricted as to withdrawal or usage. This item is available for
                bank and insurance industries.
    
    RestrictedCashAndCashEquivalentsBalanceSheet(store: IDictionary[str, Decimal])
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


class RestrictedCashAndInvestmentsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash and investments whose use in whole or in part is restricted for the long-term, generally by contractual agreements or
                regulatory requirements. This item is usually only available for bank industry.
    
    RestrictedCashAndInvestmentsBalanceSheet(store: IDictionary[str, Decimal])
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


class RestrictedCashBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The carrying amounts of cash and cash equivalent items, which are restricted as to withdrawal or usage. Restrictions may include
                legally restricted deposits held as compensating balances against short-term borrowing arrangements, contracts entered into with
                others, or entity statements of intention with regard to particular deposits; however, time deposits and short-term certificates of
                deposit are not generally included in legally restricted deposits. Excludes compensating balance arrangements that are not
                agreements, which legally restrict the use of cash amounts shown on the balance sheet. For a classified balance sheet, represents
                the current portion only (the non-current portion has a separate concept); for an unclassified balance sheet represents the entire
                amount. This item is usually not available for bank and insurance industries.
    
    RestrictedCashBalanceSheet(store: IDictionary[str, Decimal])
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


class RestrictedCommonStockBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Shares of stock for which sale is contractually or governmentally restricted for a given period of time. Stock that is acquired through
                an employee stock option plan or other private means may not be transferred. Restricted stock must be traded in compliance with
                special SEC regulations.
    
    RestrictedCommonStockBalanceSheet(store: IDictionary[str, Decimal])
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


class RestrictedInvestmentsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Investments whose use is restricted in whole or in part, generally by contractual agreements or regulatory requirements. This item
                is usually only available for bank industry.
    
    RestrictedInvestmentsBalanceSheet(store: IDictionary[str, Decimal])
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


class RestructuringAndMergernAcquisitionIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Expenses are related to restructuring, merger, or acquisitions. Restructuring expenses are charges associated with the
                consolidation and relocation of operations, disposition or abandonment of operations or productive assets. Merger and acquisition
                expenses are the amount of costs of a business combination including legal, accounting, and other costs that were charged to
                expense during the PeriodAsByte.
    
    RestructuringAndMergernAcquisitionIncomeStatement(store: IDictionary[str, Decimal])
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


class RetainedEarningsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cumulative net income of the company from the date of its inception (or reorganization) to the date of the financial statement
                less the cumulative distributions to shareholders either directly (dividends) or indirectly (treasury stock).
    
    RetainedEarningsBalanceSheet(store: IDictionary[str, Decimal])
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


class RevenueGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's revenue on a percentage basis. Morningstar calculates the growth percentage based on the
                underlying revenue data reported in the Income Statement within the company filings or reports.
    
    RevenueGrowth(store: IDictionary[str, Decimal])
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


class ROA(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Net Income / Average Total Assets
    
    ROA(store: IDictionary[str, Decimal])
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


class ROA5YrAvg(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This is the simple average of the company's ROA over the last 5 years. Return on asset is calculated by dividing a company's annual
                earnings by its average total assets.
    
    ROA5YrAvg(store: IDictionary[str, Decimal])
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


class ROE(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Net Income / Average Total Common Equity
    
    ROE(store: IDictionary[str, Decimal])
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


class ROE5YrAvg(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This is the simple average of the company's ROE over the last 5 years. Return on equity reveals how much profit a company has
                earned in comparison to the total amount of shareholder equity found on the balance sheet.
    
    ROE5YrAvg(store: IDictionary[str, Decimal])
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


class ROIC(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Net Income / (Total Equity + Long-term Debt and Capital Lease Obligation + Short-term Debt and Capital Lease Obligation)
    
    ROIC(store: IDictionary[str, Decimal])
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


class SalariesAndWagesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    All salary, wages, compensation, management fees, and employee benefit expenses.
    
    SalariesAndWagesIncomeStatement(store: IDictionary[str, Decimal])
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


class SaleOfBusinessCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Proceeds received from selling a business including proceeds from a subsidiary, and proceeds from an affiliated company.
    
    SaleOfBusinessCashFlowStatement(store: IDictionary[str, Decimal])
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


class SaleOfIntangiblesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount of capital inflow from the sale of all kinds of intangible assets.
    
    SaleOfIntangiblesCashFlowStatement(store: IDictionary[str, Decimal])
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


class SaleOfInvestmentCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Proceeds received from selling all kind of investments, including both long term and short term.
    
    SaleOfInvestmentCashFlowStatement(store: IDictionary[str, Decimal])
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


class SaleOfInvestmentPropertiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash inflow from sale of investment properties during the accounting PeriodAsByte.
    
    SaleOfInvestmentPropertiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class SaleofJointVentureAssociateCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash inflow from the disposal of joint venture/associates (investment below 50%).
    
    SaleofJointVentureAssociateCashFlowStatement(store: IDictionary[str, Decimal])
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


class SaleOfPPECashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Proceeds from selling any fixed assets such as property, plant and equipment, which also includes retirement of equipment.
    
    SaleOfPPECashFlowStatement(store: IDictionary[str, Decimal])
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


class SaleofSubsidiariesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Cash inflow from the disposal of any subsidiaries.
    
    SaleofSubsidiariesCashFlowStatement(store: IDictionary[str, Decimal])
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


class SalesPerEmployee(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of Revenue to Employees. Morningstar calculates the ratio by using the underlying data reported in the company
                filings or reports:     Revenue / Employee Number.
    
    SalesPerEmployee(store: IDictionary[str, Decimal])
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


class SecuritiesActivitiesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Income/Loss from Securities and Activities
    
    SecuritiesActivitiesIncomeStatement(store: IDictionary[str, Decimal])
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


class SecuritiesAmortizationIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The gradual elimination of a liability, such as a mortgage, in regular payments over a specified period of time. Such payments must
                be sufficient to cover both principal and interest.
    
    SecuritiesAmortizationIncomeStatement(store: IDictionary[str, Decimal])
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


class SecuritiesAndInvestmentsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Asset, often applicable to Banks, which refers to the aggregate amount of all securities and investments.
    
    SecuritiesAndInvestmentsBalanceSheet(store: IDictionary[str, Decimal])
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


class SecuritiesLendingCollateralBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The carrying value as of the balance sheet date of the liabilities collateral securities loaned to other broker-dealers. Borrowers of
                securities generally are required to provide collateral to the lenders of securities, commonly cash but sometimes other securities or
                standby letters of credit, with a value slightly higher than that of the securities borrowed.
    
    SecuritiesLendingCollateralBalanceSheet(store: IDictionary[str, Decimal])
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


class SecuritiesLoanedBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The carrying value as of the balance sheet date of securities loaned to other broker dealers, typically used by such parties to cover
                short sales, secured by cash or other securities furnished by such parties until the borrowing is closed.
    
    SecuritiesLoanedBalanceSheet(store: IDictionary[str, Decimal])
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


class SecurityAgreeToBeResellBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The carrying value of funds outstanding loaned in the form of security resale agreements if the agreement requires the purchaser to
                resell the identical security purchased or a security that meets the definition of "substantially the same" in the case of a dollar roll.
                Also includes purchases of participations in pools of securities that are subject to a resale agreement.
    
    SecurityAgreeToBeResellBalanceSheet(store: IDictionary[str, Decimal])
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


class SecurityBorrowedBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The securities borrowed or on loan, which is the temporary loan of securities by a lender to a borrower in exchange for cash.  This
                item is usually only available for bank industry.
    
    SecurityBorrowedBalanceSheet(store: IDictionary[str, Decimal])
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


class SecurityReference(System.object):
    """
    Definition of the SecurityReference class
    
    SecurityReference()
    """
    def UpdateValues(self, update: QuantConnect.Data.Fundamental.SecurityReference) -> None:
        pass

    CommonShareSubType: str

    ConversionRatio: float

    CurrencyId: str

    DelistingDate: datetime.datetime

    DelistingReason: str

    DepositaryReceiptRatio: float

    ExchangeId: str

    ExchangeSubMarketGlobalId: str

    InvestmentId: str

    IPODate: datetime.datetime

    IPOOfferPrice: float

    IPOOfferPriceRange: str

    IsDepositaryReceipt: bool

    IsDirectInvest: bool

    IsDividendReinvest: bool

    IsPrimaryShare: bool

    MarketDataID: str

    MIC: str

    ParValue: float

    SecuritySymbol: str

    SecurityType: str

    ShareClassDescription: str

    ShareClassStatus: str

    TradingStatus: bool

    Valoren: str



class SecuritySoldNotYetRepurchasedBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represent obligations of the company to deliver the specified security at the contracted price and, thereby, create a liability to
                purchase the security in the market at prevailing prices.
    
    SecuritySoldNotYetRepurchasedBalanceSheet(store: IDictionary[str, Decimal])
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


class SellingAndMarketingExpenseIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate total amount of expenses directly related to the marketing or selling of products or services.
    
    SellingAndMarketingExpenseIncomeStatement(store: IDictionary[str, Decimal])
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


class SellingGeneralAndAdministrationIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate total costs related to selling a firm's product and services, as well as all other general and administrative expenses.
                Selling expenses are those directly related to the company's efforts to generate sales (e.g., sales salaries, commissions,
                advertising, delivery expenses). General and administrative expenses are expenses related to general administration of the
                company's operation (e.g., officers and office salaries, office supplies, telephone, accounting and legal services, and business
                licenses and fees).
    
    SellingGeneralAndAdministrationIncomeStatement(store: IDictionary[str, Decimal])
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


class SeparateAccountAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The fair value of the assets held by the company for the benefit of separate account policyholders.
    
    SeparateAccountAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class SeparateAccountBusinessBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to revenue that is generated that is not part of typical operations.
    
    SeparateAccountBusinessBalanceSheet(store: IDictionary[str, Decimal])
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


class ServiceChargeOnDepositorAccountsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Includes any service charges on following accounts: Demand Deposit; Checking account; Savings account; Deposit in foreign
                offices; ESCROW accounts; Money Market Certificates & Deposit accounts, CDs (Negotiable Certificates of Deposits); NOW
                Accounts (Negotiable Order of Withdrawal); IRAs (Individual Retirement Accounts). This item is usually only available for bank
                industry.
    
    ServiceChargeOnDepositorAccountsIncomeStatement(store: IDictionary[str, Decimal])
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


class ShareIssuedBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The number of authorized shares that is sold to and held by the shareholders of a company, regardless of whether they are insiders,
                institutional investors or the general public. Unlike shares that are held as treasury stock, shares that have been retired are not
                included in this figure. The amount of issued shares can be all or part of the total amount of authorized shares of a corporation.
    
    ShareIssuedBalanceSheet(store: IDictionary[str, Decimal])
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


class ShareofAssociatesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A non-cash adjustment for share of associates' income in respect of operating activities.
    
    ShareofAssociatesCashFlowStatement(store: IDictionary[str, Decimal])
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


class ShortTermDebtIssuanceCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash inflow from a debt initially having maturity due within one year or the normal operating cycle, if longer.
    
    ShortTermDebtIssuanceCashFlowStatement(store: IDictionary[str, Decimal])
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


class ShortTermDebtPaymentsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash outflow for a borrowing having initial term of repayment within one year or the normal operating cycle, if longer.
    
    ShortTermDebtPaymentsCashFlowStatement(store: IDictionary[str, Decimal])
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


class ShortTermInvestmentsAvailableForSaleBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The current assets section of a company's balance sheet that contains the investments that a company holds with the purpose for
                trading.
    
    ShortTermInvestmentsAvailableForSaleBalanceSheet(store: IDictionary[str, Decimal])
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


class ShortTermInvestmentsHeldToMaturityBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The current assets section of a company's balance sheet that contains the investments that a company has made that will expire
                at a fixed date within one year.
    
    ShortTermInvestmentsHeldToMaturityBalanceSheet(store: IDictionary[str, Decimal])
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


class ShortTermInvestmentsTradingBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The current assets section of a company's balance sheet that contains the investments that a company can trade at any moment.
    
    ShortTermInvestmentsTradingBalanceSheet(store: IDictionary[str, Decimal])
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


class SocialSecurityCostsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Benefits paid to the employees in respect of their work.
    
    SocialSecurityCostsIncomeStatement(store: IDictionary[str, Decimal])
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


class SolvencyRatio(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Measure of whether a company's cash flow is sufficient to meet its short-term and long-term debt requirements. The lower this
                ratio is, the greater the probability that the company will be in financial distress. Net Income + Depreciation, Depletion and
                Amortization/ average of annual Total Liabilities over the most recent two periods.
    
    SolvencyRatio(store: IDictionary[str, Decimal])
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


class SpecialIncomeChargesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Earnings or losses attributable to occurrences or actions by the firm that is either infrequent or unusual.
    
    SpecialIncomeChargesIncomeStatement(store: IDictionary[str, Decimal])
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


class StaffCostsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total staff cost which is paid to the employees that is not part of Selling, General, and Administration expense.
    
    StaffCostsIncomeStatement(store: IDictionary[str, Decimal])
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


class StockBasedCompensationCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Value of stock issued during the period as a result of any share-based compensation plan other than an employee stock ownership
                plan (ESOP).
    
    StockBasedCompensationCashFlowStatement(store: IDictionary[str, Decimal])
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


class StockBasedCompensationIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cost to the company for granting stock options to reward employees.
    
    StockBasedCompensationIncomeStatement(store: IDictionary[str, Decimal])
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


class StockholdersEquityBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The residual interest in the assets of the enterprise that remains after deducting its liabilities. Equity is increased by owners'
                investments and by comprehensive income, and it is reduced by distributions to the owners.
    
    StockholdersEquityBalanceSheet(store: IDictionary[str, Decimal])
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


class StockholdersEquityGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the stockholder's equity on a percentage basis. Morningstar calculates the growth percentage based on the residual
                interest in the assets of the enterprise that remains after deducting its liabilities reported in the Balance Sheet within the company
                filings or reports.
    
    StockholdersEquityGrowth(store: IDictionary[str, Decimal])
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


class StockType(System.object):
    """ Helper class for the AssetClassification's StockType field QuantConnect.Data.Fundamental.AssetClassification.StockType """
    AggressiveGrowth: int
    ClassicGrowth: int
    Cyclicals: int
    Distressed: int
    HardAsset: int
    HighYield: int
    SlowGrowth: int
    SpeculativeGrowth: int
    __all__: list


class StyleBox(System.object):
    """
    Helper class for the AssetClassification's StyleBox field QuantConnect.Data.Fundamental.AssetClassification.StyleBox.
                For stocks and stock funds, it classifies securities according to market capitalization and growth and value factor
    """
    LargeCore: int
    LargeGrowth: int
    LargeValue: int
    MidCore: int
    MidGrowth: int
    MidValue: int
    SmallCore: int
    SmallGrowth: int
    SmallValue: int
    __all__: list


class SubordinatedLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The total carrying value of securities loaned to other broker dealers, typically used by such parties to cover short sales, secured by
                cash or other securities furnished by such parties until the borrowing is closed; in a Non-Differentiated Balance Sheet.
    
    SubordinatedLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class TangibleBookValueBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The company's total book value less the value of any intangible assets.
                Methodology: Common Stock Equity minus Goodwill and Other Intangible Assets
    
    TangibleBookValueBalanceSheet(store: IDictionary[str, Decimal])
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


class TaxAssetsTotalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of total tax assets in a Non-Differentiated Balance Sheet, includes Tax Receivables and Deferred Tax Assets.
    
    TaxAssetsTotalBalanceSheet(store: IDictionary[str, Decimal])
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


class TaxEffectOfUnusualItemsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Tax effect of the usual items
    
    TaxEffectOfUnusualItemsIncomeStatement(store: IDictionary[str, Decimal])
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


class TaxesAssetsCurrentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Carrying amount due within one year of the balance sheet date (or one operating cycle, if longer) from tax authorities as of the
                balance sheet date representing refunds of overpayments or recoveries based on agreed-upon resolutions of disputes, and current
                deferred tax assets.
    
    TaxesAssetsCurrentBalanceSheet(store: IDictionary[str, Decimal])
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


class TaxesReceivableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Carrying amount due within one year of the balance sheet date (or one operating cycle, if longer) from tax authorities as of the
                balance sheet date representing refunds of overpayments or recoveries based on agreed-upon resolutions of disputes. This item is
                usually not available for bank industry.
    
    TaxesReceivableBalanceSheet(store: IDictionary[str, Decimal])
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


class TaxesRefundPaidCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total tax paid or received on operating activities.
    
    TaxesRefundPaidCashFlowStatement(store: IDictionary[str, Decimal])
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


class TaxesRefundPaidDirectCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Tax paid/refund related to operating activities, for the direct cash flow.
    
    TaxesRefundPaidDirectCashFlowStatement(store: IDictionary[str, Decimal])
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


class TaxLossCarryforwardBasicEPS(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The earnings attributable to the tax loss carry forward (during the reporting period).
    
    TaxLossCarryforwardBasicEPS(store: IDictionary[str, Decimal])
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


class TaxLossCarryforwardDilutedEPS(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The earnings from any tax loss carry forward (in the reporting period).
    
    TaxLossCarryforwardDilutedEPS(store: IDictionary[str, Decimal])
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


class TaxProvisionIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Include any taxes on income, net of any investment tax credits for the current accounting PeriodAsByte.
    
    TaxProvisionIncomeStatement(store: IDictionary[str, Decimal])
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


class TaxRate(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of tax provision to pretax income. Morningstar calculates the ratio by using the underlying data reported in the
                company filings or reports:   Tax Provision / Pretax Income.
                [Note: Valid only when positive pretax income, and positive tax expense (not tax benefit)]
    
    TaxRate(store: IDictionary[str, Decimal])
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


class TaxRateForCalcsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Tax rate used for Morningstar calculations.
    
    TaxRateForCalcsIncomeStatement(store: IDictionary[str, Decimal])
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


class TotalAdjustmentsforNonCashItemsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of all adjustments back from net income but without real cash outflow or inflow.
    
    TotalAdjustmentsforNonCashItemsCashFlowStatement(store: IDictionary[str, Decimal])
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


class TotalAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of probable future economic benefits obtained or controlled by a particular enterprise as a result of past
                transactions or events.
    
    TotalAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalAssetsGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the total assets on a percentage basis. Morningstar calculates the growth percentage based on the total assets
                reported in the Balance Sheet within the company filings or reports.
    
    TotalAssetsGrowth(store: IDictionary[str, Decimal])
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


class TotalCapitalizationBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Stockholder's Equity plus Long Term Debt.
    
    TotalCapitalizationBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalDebtBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    All borrowings incurred by the company including debt and capital lease obligations.
    
    TotalDebtBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalDebtEquityRatio(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of Total Debt to Common Equity. Morningstar calculates the ratio by using the underlying data reported in the
                Balance Sheet within the company filings or reports: (Current Debt And Current Capital Lease Obligation + Long-Term Debt And
                Long-Term Capital Lease Obligation / Common Equity.   [Note: Common Equity = Total Shareholder's Equity - Preferred Stock]
    
    TotalDebtEquityRatio(store: IDictionary[str, Decimal])
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


class TotalDebtEquityRatioGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's total debt to equity ratio on a percentage basis. Morningstar calculates the growth percentage based
                on the total debt divided by the shareholder's equity reported in the Balance Sheet within the company filings or reports.
    
    TotalDebtEquityRatioGrowth(store: IDictionary[str, Decimal])
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


class TotalDebtInMaturityScheduleBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total Debt in Maturity Schedule is the sum of Debt details above.
    
    TotalDebtInMaturityScheduleBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalDeferredCreditsAndOtherNonCurrentLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Revenue received by a firm but not yet reported as income.  This item is usually only available for utility industry.
    
    TotalDeferredCreditsAndOtherNonCurrentLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalDepositsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A liability account which represents the total amount of funds deposited.
    
    TotalDepositsBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalDividendPaymentofEquitySharesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total amount paid in dividends to equity securities investors.
    
    TotalDividendPaymentofEquitySharesIncomeStatement(store: IDictionary[str, Decimal])
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


class TotalDividendPaymentofNonEquitySharesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total amount paid in dividends to Non-Equity securities investors.
    
    TotalDividendPaymentofNonEquitySharesIncomeStatement(store: IDictionary[str, Decimal])
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


class TotalDividendPerShare(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total Dividend Per Share is cash dividends and special cash dividends paid per share over a certain period of time.
    
    TotalDividendPerShare(store: IDictionary[str, Decimal])
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


class TotalEquityAsReportedBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total Equity as reported by the company, may be the same or not the same as Morningstar's standardized definition.
    
    TotalEquityAsReportedBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalEquityBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total Equity equals Preferred Stock Equity + Common Stock Equity.
    
    TotalEquityBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalEquityGrossMinorityInterestBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Residual interest, including minority interest, that remains in the assets of the enterprise after deducting its liabilities. Equity is
                increased by owners' investments and by comprehensive income, and it is reduced by distributions to the owners.
    
    TotalEquityGrossMinorityInterestBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalExpensesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The sum of operating expense and cost of revenue. If the company does not give the reported number, it will be calculated by
                adding operating expense and cost of revenue.
    
    TotalExpensesIncomeStatement(store: IDictionary[str, Decimal])
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


class TotalFinancialLeaseObligationsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Represents the total amount of long-term capital leases that must be paid within the next accounting period for a Non-
                Differentiated Balance Sheet. Capital lease obligations are contractual obligations that arise from obtaining the use of property or
                equipment via a capital lease contract.
    
    TotalFinancialLeaseObligationsBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalInvestmentsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Asset that refers to the sum of all available for sale securities and other investments often reported on the balance sheet of
                insurance firms.
    
    TotalInvestmentsBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalLiabilitiesAsReportedBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total liabilities as reported by the company, may be the same or not the same as Morningstar's standardized definition.
    
    TotalLiabilitiesAsReportedBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalLiabilitiesGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the total liabilities on a percentage basis. Morningstar calculates the growth percentage based on the total liabilities
                reported in the Balance Sheet within the company filings or reports.
    
    TotalLiabilitiesGrowth(store: IDictionary[str, Decimal])
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


class TotalLiabilitiesNetMinorityInterestBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Probable future sacrifices of economic benefits arising from present obligations of an enterprise to transfer assets or provide
                services to others in the future as a result of past transactions or events, excluding minority interest.
    
    TotalLiabilitiesNetMinorityInterestBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalMoneyMarketInvestmentsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The sum of the money market investments held by a bank's depositors, which are FDIC insured.
    
    TotalMoneyMarketInvestmentsIncomeStatement(store: IDictionary[str, Decimal])
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


class TotalNonCurrentAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Sum of the carrying amounts as of the balance sheet date of all assets that are expected to be realized in cash, sold or consumed
                after one year or beyond the normal operating cycle, if longer.
    
    TotalNonCurrentAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalNonCurrentLiabilitiesNetMinorityInterestBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total obligations, net minority interest, incurred as part of normal operations that is expected to be repaid beyond the following
                twelve months or one business cycle; excludes minority interest.
    
    TotalNonCurrentLiabilitiesNetMinorityInterestBalanceSheet(store: IDictionary[str, Decimal])
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


class TotalOperatingIncomeAsReportedIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Operating profit/loss as reported by the company, may be the same or not the same as Morningstar's standardized definition.
    
    TotalOperatingIncomeAsReportedIncomeStatement(store: IDictionary[str, Decimal])
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


class TotalOtherFinanceCostIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Any other finance cost which is not clearly defined in the Non-Operating section.
    
    TotalOtherFinanceCostIncomeStatement(store: IDictionary[str, Decimal])
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


class TradingAssetsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Trading account assets are bought and held principally for the purpose of selling them in the near term (thus held for only a short
                period of time). Unrealized holding gains and losses for trading securities are included in earnings.
    
    TradingAssetsBalanceSheet(store: IDictionary[str, Decimal])
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


class TradingGainLossIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A broker-dealer or other financial entity may buy and sell securities exclusively for its own account, sometimes referred to as
                proprietary trading. The profit or loss is measured by the difference between the acquisition cost and the selling price or current
                market or fair value. The net gain or loss, includes both realized and unrealized, from trading cash instruments, equities and
                derivative contracts (including commodity contracts) that has been recognized during the accounting period for the broker dealer or
                other financial entity's own account. This item is typically available for bank industry.
    
    TradingGainLossIncomeStatement(store: IDictionary[str, Decimal])
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


class TradingLiabilitiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The carrying amount of liabilities as of the balance sheet date that pertain to principal and customer trading transactions, or which
                may be incurred with the objective of generating a profit from short-term fluctuations in price as part of an entity's market-making,
                hedging and proprietary trading. Examples include short positions in securities, derivatives and commodities, obligations under
                repurchase agreements, and securities borrowed arrangements.
    
    TradingLiabilitiesBalanceSheet(store: IDictionary[str, Decimal])
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


class TradingSecuritiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The total of financial instruments that are bought and held principally for the purpose of selling them in the near term (thus held for
                only a short period of time) or for debt and equity securities formerly categorized as available-for-sale or held-to-maturity which the
                company held as of the date it opted to account for such securities at fair value.
    
    TradingSecuritiesBalanceSheet(store: IDictionary[str, Decimal])
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


class TreasuryBillsandOtherEligibleBillsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Investments backed by the central government, it usually carries less risk than other investments.
    
    TreasuryBillsandOtherEligibleBillsBalanceSheet(store: IDictionary[str, Decimal])
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


class TreasurySharesNumberBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Number of Treasury Shares.
    
    TreasurySharesNumberBalanceSheet(store: IDictionary[str, Decimal])
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


class TreasuryStockBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The portion of shares that a company keeps in their own treasury. Treasury stock may have come from a repurchase or buyback
                from shareholders; or it may have never been issued to the public in the first place. These shares don't pay dividends, have no
                voting rights, and are not included in shares outstanding calculations.
    
    TreasuryStockBalanceSheet(store: IDictionary[str, Decimal])
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


class TrustFeesbyCommissionsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Bank manages funds on behalf of its customers through the operation of various trust accounts. Any fees earned through managing
                those funds are called trust fees, which are recognized when earned. This item is typically available for bank industry.
    
    TrustFeesbyCommissionsIncomeStatement(store: IDictionary[str, Decimal])
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


class UnallocatedSurplusBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount of surplus from insurance contracts which has not been allocated at the balance sheet date. This is represented as a
                liability to policyholders, as it pertains to cumulative income arising from the with-profits business.
    
    UnallocatedSurplusBalanceSheet(store: IDictionary[str, Decimal])
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


class UnbilledReceivablesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Revenues that are not currently billed from the customer under the terms of the contract.  This item is usually only available for
                utility industry.
    
    UnbilledReceivablesBalanceSheet(store: IDictionary[str, Decimal])
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


class UnderwritingExpensesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Also known as Policy Acquisition Costs; and reported by insurance companies.  The cost incurred by an insurer when deciding
                whether to accept or decline a risk; may include meetings with the insureds or brokers, actuarial review of loss history, or physical
                inspections of exposures. Also, expenses deducted from insurance company revenues (including incurred losses and acquisition
                costs) to determine underwriting profit.
    
    UnderwritingExpensesIncomeStatement(store: IDictionary[str, Decimal])
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


class UnearnedIncomeBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Income received but not yet earned, it represents the unearned amount that is netted against the total loan.
    
    UnearnedIncomeBalanceSheet(store: IDictionary[str, Decimal])
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


class UnearnedPremiumsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Carrying amount of premiums written on insurance contracts that have not been earned as of the balance sheet date.
    
    UnearnedPremiumsBalanceSheet(store: IDictionary[str, Decimal])
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


class UnpaidLossAndLossReserveBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Liability amount that reflects claims that are expected based upon statistical projections, but which have not been reported to the
                insurer.
    
    UnpaidLossAndLossReserveBalanceSheet(store: IDictionary[str, Decimal])
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


class UnrealizedGainLossBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A profit or loss that results from holding onto an asset rather than cashing it in and officially taking the profit or loss.
    
    UnrealizedGainLossBalanceSheet(store: IDictionary[str, Decimal])
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


class UnrealizedGainLossOnInvestmentSecuritiesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increases (decreases) in the market value of unsold securities whose gains (losses) were included in earnings.
    
    UnrealizedGainLossOnInvestmentSecuritiesCashFlowStatement(store: IDictionary[str, Decimal])
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


class UnrealizedGainsLossesOnDerivativesCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The gross gains and losses on derivatives. This item is usually only available for insurance industry.
    
    UnrealizedGainsLossesOnDerivativesCashFlowStatement(store: IDictionary[str, Decimal])
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


class ValuationRatios(System.object):
    """
    Definition of the ValuationRatios class
    
    ValuationRatios()
    """
    def UpdateValues(self, update: QuantConnect.Data.Fundamental.ValuationRatios) -> None:
        pass

    ActualForwardDividend: float

    ActualTrailingDividend: float

    BookValuePerShare: float

    BookValueYield: float

    BuyBackYield: float

    CAPERatio: float

    CashReturn: float

    CFOPerShare: float

    CFYield: float

    DivYield5Year: float

    EarningYield: float

    EVtoEBIT: float

    EVToEBIT3YrAvg: float

    EVToEBIT3YrAvgChange: float

    EVToEBITDA: float

    EVToEBITDA10YearGrowth: float

    EVToEBITDA1YearGrowth: float

    EVToEBITDA3YearGrowth: float

    EVToEBITDA3YrAvg: float

    EVToEBITDA3YrAvgChange: float

    EVToEBITDA5YearGrowth: float

    EVtoFCF: float

    EVToFCF10YearGrowth: float

    EVToFCF1YearGrowth: float

    EVToFCF3YearGrowth: float

    EVToFCF3YrAvg: float

    EVToFCF3YrAvgChange: float

    EVToFCF5YearGrowth: float

    EVToForwardEBIT: float

    EVToForwardEBITDA: float

    EVToForwardRevenue: float

    EVtoPreTaxIncome: float

    EVtoRevenue: float

    EVToRevenue10YearGrowth: float

    EVToRevenue1YearGrowth: float

    EVToRevenue3YearGrowth: float

    EVToRevenue3YrAvg: float

    EVToRevenue3YrAvgChange: float

    EVToRevenue5YearGrowth: float

    EVtoTotalAssets: float

    EVToTotalAssets10YearGrowth: float

    EVToTotalAssets1YearGrowth: float

    EVToTotalAssets3YearGrowth: float

    EVToTotalAssets3YrAvg: float

    EVToTotalAssets3YrAvgChange: float

    EVToTotalAssets5YearGrowth: float

    ExpectedDividendGrowthRate: float

    FCFPerShare: float

    FCFRatio: float

    FCFYield: float

    FFOPerShare: float

    FirstYearEstimatedEPSGrowth: float

    ForwardCalculationStyle: str

    ForwardDividend: float

    ForwardDividendYield: float

    ForwardEarningYield: float

    ForwardPERatio: float

    ForwardROA: float

    ForwardROE: float

    NormalizedPEGatio: float

    NormalizedPERatio: float

    PayoutRatio: float

    PBRatio: float

    PBRatio10YearGrowth: float

    PBRatio1YearGrowth: float

    PBRatio3YearGrowth: float

    PBRatio3YrAvg: float

    PBRatio3YrAvgChange: float

    PBRatio5YearGrowth: float

    PCashRatio3YrAvg: float

    PCFRatio: float

    PEGPayback: float

    PEGRatio: float

    PERatio: float

    PERatio10YearAverage: float

    PERatio10YearGrowth: float

    PERatio10YearHigh: float

    PERatio10YearLow: float

    PERatio1YearAverage: float

    PERatio1YearGrowth: float

    PERatio1YearHigh: float

    PERatio1YearLow: float

    PERatio3YearGrowth: float

    PERatio3YrAvg: float

    PERatio3YrAvgChange: float

    PERatio5YearAverage: float

    PERatio5YearGrowth: float

    PERatio5YearHigh: float

    PERatio5YearLow: float

    PFCFRatio10YearGrowth: float

    PFCFRatio1YearGrowth: float

    PFCFRatio3YearGrowth: float

    PFCFRatio3YrAvg: float

    PFCFRatio3YrAvgChange: float

    PFCFRatio5YearGrowth: float

    PriceChange1M: float

    PricetoCashRatio: float

    PricetoEBITDA: float

    PSRatio: float

    PSRatio10YearGrowth: float

    PSRatio1YearGrowth: float

    PSRatio3YearGrowth: float

    PSRatio3YrAvg: float

    PSRatio3YrAvgChange: float

    PSRatio5YearGrowth: float

    RatioPE5YearAverage: float

    SalesPerShare: float

    SalesYield: float

    SecondYearEstimatedEPSGrowth: float

    SustainableGrowthRate: float

    TangibleBookValuePerShare: float

    TangibleBVPerShare3YrAvg: float

    TangibleBVPerShare5YrAvg: float

    TotalAssetPerShare: float

    TotalYield: float

    TrailingCalculationStyle: str

    TrailingDividendYield: float

    TwoYearsForwardEarningYield: float

    TwoYearsForwardPERatio: float

    TwoYrsEVToForwardEBIT: float

    TwoYrsEVToForwardEBITDA: float

    WorkingCapitalPerShare: float

    WorkingCapitalPerShare3YrAvg: float

    WorkingCapitalPerShare5YrAvg: float



class WagesandSalariesIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This is the portion under Staff Costs that represents salary paid to the employees in respect of their work.
    
    WagesandSalariesIncomeStatement(store: IDictionary[str, Decimal])
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


class WaterProductionBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount for a facility and plant that provides water which might include wells, reservoirs, pumping stations, and control
                facilities; and waste water systems which includes the waste treatment and disposal facility and equipment. This item is usually
                only available for utility industry.
    
    WaterProductionBalanceSheet(store: IDictionary[str, Decimal])
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


class WorkingCapitalBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Current Assets minus Current Liabilities.  This item is usually not available for bank and insurance industries.
    
    WorkingCapitalBalanceSheet(store: IDictionary[str, Decimal])
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


class WorkingCapitalTurnoverRatio(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Total revenue / working capital (current assets minus current liabilities)
    
    WorkingCapitalTurnoverRatio(store: IDictionary[str, Decimal])
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


class WorkInProcessBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Work, or goods, in the process of being fabricated or manufactured but not yet completed as finished goods. This item is usually
                available for manufacturing and mining industries.
    
    WorkInProcessBalanceSheet(store: IDictionary[str, Decimal])
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


class WriteOffIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A reduction in the value of an asset or earnings by the amount of an expense or loss.
    
    WriteOffIncomeStatement(store: IDictionary[str, Decimal])
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


