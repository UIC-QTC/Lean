from .__Fundamental_61 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


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
