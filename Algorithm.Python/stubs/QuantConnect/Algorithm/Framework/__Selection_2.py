from .__Selection_3 import *
import typing
import System.Collections.Generic
import System
import QuantConnect.Securities
import QuantConnect.Scheduling
import QuantConnect.Interfaces
import QuantConnect.Data.UniverseSelection
import QuantConnect.Data
import QuantConnect.Algorithm.Framework.Selection
import QuantConnect.Algorithm
import QuantConnect
import Python.Runtime
import NodaTime
import datetime

class NullUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel, QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel):
    """
    Provides a null implementation of QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel

    

    NullUniverseSelectionModel()
    """
    def CreateUniverses(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.List[QuantConnect.Data.UniverseSelection.Universe]:
        pass


class OpenInterestFutureUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.FutureUniverseSelectionModel, QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel):
    """
    Selects contracts in a futures universe, sorted by open interest.  This allows the selection to identifiy current

                    active contract.

    

    OpenInterestFutureUniverseSelectionModel(algorithm: IAlgorithm, futureChainSymbolSelector: Func[DateTime, IEnumerable[Symbol]], chainContractsLookupLimit: Nullable[int], resultsLimit: Nullable[int])
    """
    def FilterByOpenInterest(self, contracts: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.Symbol, QuantConnect.Securities.SecurityExchangeHours]) -> typing.List[QuantConnect.Symbol]:
        pass

    @staticmethod # known case of __new__
    def __new__(self, algorithm: QuantConnect.Interfaces.IAlgorithm, futureChainSymbolSelector: typing.Callable[[datetime.datetime], typing.List[QuantConnect.Symbol]], chainContractsLookupLimit: typing.Optional[int], resultsLimit: typing.Optional[int]) -> None:
        pass


class OptionUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel, QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel that subscribes to option chains

    

    OptionUniverseSelectionModel(refreshInterval: TimeSpan, optionChainSymbolSelector: Func[DateTime, IEnumerable[Symbol]])

    OptionUniverseSelectionModel(refreshInterval: TimeSpan, optionChainSymbolSelector: Func[DateTime, IEnumerable[Symbol]], universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)

    OptionUniverseSelectionModel(refreshInterval: TimeSpan, optionChainSymbolSelector: Func[DateTime, IEnumerable[Symbol]], universeSettings: UniverseSettings)
    """
    def CreateUniverses(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.List[QuantConnect.Data.UniverseSelection.Universe]:
        pass

    def GetNextRefreshTimeUtc(self) -> datetime.datetime:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, refreshInterval: datetime.timedelta, optionChainSymbolSelector: typing.Callable[[datetime.datetime], typing.List[QuantConnect.Symbol]]) -> None:
        pass

    @typing.overload
    def __new__(self, refreshInterval: datetime.timedelta, optionChainSymbolSelector: typing.Callable[[datetime.datetime], typing.List[QuantConnect.Symbol]], universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, securityInitializer: QuantConnect.Securities.ISecurityInitializer) -> None:
        pass

    @typing.overload
    def __new__(self, refreshInterval: datetime.timedelta, optionChainSymbolSelector: typing.Callable[[datetime.datetime], typing.List[QuantConnect.Symbol]], universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        pass

    def __new__(self, *args) -> None:
        pass


class QC500UniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.FundamentalUniverseSelectionModel, QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel):
    """
    Defines the QC500 universe as a universe selection model for framework algorithm

                For details: https://github.com/QuantConnect/Lean/pull/1663

    

    QC500UniverseSelectionModel()

    QC500UniverseSelectionModel(universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)
    """
    def SelectCoarse(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, coarse: typing.List[QuantConnect.Data.UniverseSelection.CoarseFundamental]) -> typing.List[QuantConnect.Symbol]:
        pass

    def SelectFine(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, fine: typing.List[QuantConnect.Data.Fundamental.FineFundamental]) -> typing.List[QuantConnect.Symbol]:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings, securityInitializer: QuantConnect.Securities.ISecurityInitializer) -> None:
        pass

    def __new__(self, *args) -> None:
        pass


class ScheduledUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel, QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel):
    """
    Defines a universe selection model that invokes a selector function on a specific scheduled given by an QuantConnect.Scheduling.IDateRule and an QuantConnect.Scheduling.ITimeRule

    

    ScheduledUniverseSelectionModel(dateRule: IDateRule, timeRule: ITimeRule, selector: Func[DateTime, IEnumerable[Symbol]], settings: UniverseSettings, initializer: ISecurityInitializer)

    ScheduledUniverseSelectionModel(timeZone: DateTimeZone, dateRule: IDateRule, timeRule: ITimeRule, selector: Func[DateTime, IEnumerable[Symbol]], settings: UniverseSettings, initializer: ISecurityInitializer)

    ScheduledUniverseSelectionModel(dateRule: IDateRule, timeRule: ITimeRule, selector: PyObject, settings: UniverseSettings, initializer: ISecurityInitializer)

    ScheduledUniverseSelectionModel(timeZone: DateTimeZone, dateRule: IDateRule, timeRule: ITimeRule, selector: PyObject, settings: UniverseSettings, initializer: ISecurityInitializer)
    """
    def CreateUniverses(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.List[QuantConnect.Data.UniverseSelection.Universe]:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, selector: typing.Callable[[datetime.datetime], typing.List[QuantConnect.Symbol]], settings: QuantConnect.Data.UniverseSelection.UniverseSettings, initializer: QuantConnect.Securities.ISecurityInitializer) -> None:
        pass

    @typing.overload
    def __new__(self, timeZone: NodaTime.DateTimeZone, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, selector: typing.Callable[[datetime.datetime], typing.List[QuantConnect.Symbol]], settings: QuantConnect.Data.UniverseSelection.UniverseSettings, initializer: QuantConnect.Securities.ISecurityInitializer) -> None:
        pass

    @typing.overload
    def __new__(self, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, selector: Python.Runtime.PyObject, settings: QuantConnect.Data.UniverseSelection.UniverseSettings, initializer: QuantConnect.Securities.ISecurityInitializer) -> None:
        pass

    @typing.overload
    def __new__(self, timeZone: NodaTime.DateTimeZone, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, selector: Python.Runtime.PyObject, settings: QuantConnect.Data.UniverseSelection.UniverseSettings, initializer: QuantConnect.Securities.ISecurityInitializer) -> None:
        pass

    def __new__(self, *args) -> None:
        pass


class SP500SectorsETFUniverse(QuantConnect.Algorithm.Framework.Selection.InceptionDateUniverseSelectionModel, QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel):
    """
    Universe Selection Model that adds the following SP500 Sectors ETFs at their inception date

                1998-12-22   XLB   Materials Select Sector SPDR ETF

                1998-12-22   XLE   Energy Select Sector SPDR Fund

                1998-12-22   XLF   Financial Select Sector SPDR Fund

                1998-12-22   XLI   Industrial Select Sector SPDR Fund

                1998-12-22   XLK   Technology Select Sector SPDR Fund

                1998-12-22   XLP   Consumer Staples Select Sector SPDR Fund

                1998-12-22   XLU   Utilities Select Sector SPDR Fund

                1998-12-22   XLV   Health Care Select Sector SPDR Fund

                1998-12-22   XLY   Consumer Discretionary Select Sector SPDR Fund

    

    SP500SectorsETFUniverse()
    """

class TechnologyETFUniverse(QuantConnect.Algorithm.Framework.Selection.InceptionDateUniverseSelectionModel, QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel):
    """
    Universe Selection Model that adds the following Technology ETFs at their inception date

                1998-12-22   XLK    Technology Select Sector SPDR Fund

                1999-03-10   QQQ    Invesco QQQ

                2001-07-13   SOXX   iShares PHLX Semiconductor ETF

                2001-07-13   IGV    iShares Expanded Tech-Software Sector ETF

                2004-01-30   VGT    Vanguard Information Technology ETF

                2006-04-25   QTEC   First Trust NASDAQ 100 Technology

                2006-06-23   FDN    First Trust Dow Jones Internet Index

                2007-05-10   FXL    First Trust Technology AlphaDEX Fund

                2008-12-17   TECL   Direxion Daily Technology Bull 3X Shares

                2008-12-17   TECS   Direxion Daily Technology Bear 3X Shares

                2010-03-11   SOXL   Direxion Daily Semiconductor Bull 3x Shares

                2010-03-11   SOXS   Direxion Daily Semiconductor Bear 3x Shares

                2011-07-06   SKYY   First Trust ISE Cloud Computing Index Fund

                2011-12-21   SMH    VanEck Vectors Semiconductor ETF

                2013-08-01   KWEB   KraneShares CSI China Internet ETF

                2013-10-24   FTEC   Fidelity MSCI Information Technology Index ETF

    

    TechnologyETFUniverse()
    """
