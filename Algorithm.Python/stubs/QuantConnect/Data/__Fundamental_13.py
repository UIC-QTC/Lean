from .__Fundamental_14 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


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
