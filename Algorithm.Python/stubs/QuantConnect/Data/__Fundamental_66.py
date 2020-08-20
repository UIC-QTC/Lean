from .__Fundamental_67 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


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
