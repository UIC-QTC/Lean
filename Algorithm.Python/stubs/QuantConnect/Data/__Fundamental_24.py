from .__Fundamental_25 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


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
