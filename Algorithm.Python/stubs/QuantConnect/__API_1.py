import QuantConnect.API
import Newtonsoft.Json.Linq
import Newtonsoft.Json
import typing
import System
import QuantConnect.Packets
import QuantConnect.Api
import QuantConnect
import datetime



class Prices(System.object):
    """
    Prices rest response wrapper

    

    Prices()
    """
    Price: float

    Symbol: QuantConnect.Symbol

    SymbolID: str

    Updated: datetime.datetime


class PricesList(QuantConnect.Api.RestResponse):
    """
    Collection container for a list of prices objects

    

    PricesList()
    """
    Prices: typing.List[QuantConnect.API.Prices]

class SKU(System.object):
    """
    Class for generating a SKU for a node with a given configuration

                Every SKU is made up of 3 variables: 

                - Target environment (L for live, B for Backtest, R for Research)

                - CPU core count

                - Dedicated RAM (GB)

    

    SKU(cores: int, memory: int, target: NodeType)
    """
    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    def __new__(self, cores: int, memory: int, target: QuantConnect.API.NodeType) -> None:
        pass

    Cores: int
    Memory: int
    Target: QuantConnect.API.NodeType

class Split(System.object):
    """
    Split returned from the api

    

    Split()
    """
    Date: datetime.datetime

    ReferencePrice: float

    SplitFactor: float

    Symbol: QuantConnect.Symbol

    SymbolID: str



class SplitList(QuantConnect.Api.RestResponse):
    """
    Collection container for a list of split objects

    

    SplitList()
    """
    Splits: typing.List[QuantConnect.API.Split]



class TradierLiveAlgorithmSettings(QuantConnect.API.BaseLiveAlgorithmSettings):
    """
    Live algorithm settings for trading with Tradier

    

    TradierLiveAlgorithmSettings(accessToken: str, dateIssued: str, refreshToken: str, account: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, accessToken: str, dateIssued: str, refreshToken: str, account: str) -> None:
        pass

    AccessToken: str

    DateIssued: str

    Lifetime: str

    RefreshToken: str
