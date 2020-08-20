from .__Fundamental_53 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


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
