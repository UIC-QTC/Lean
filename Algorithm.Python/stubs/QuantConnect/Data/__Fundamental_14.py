from .__Fundamental_15 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


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
