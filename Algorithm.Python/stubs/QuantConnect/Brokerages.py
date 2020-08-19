# encoding: utf-8
# module QuantConnect.Brokerages calls itself Brokerages
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import QuantConnect
import QuantConnect.Brokerages
import QuantConnect.Data.Market
import QuantConnect.Interfaces
import QuantConnect.Orders
import QuantConnect.Orders.Fees
import QuantConnect.Orders.Fills
import QuantConnect.Orders.Slippage
import QuantConnect.Packets
import QuantConnect.Securities
import System.Collections.Generic
import typing

# no functions
# classes

class DefaultBrokerageModel(System.object, QuantConnect.Brokerages.IBrokerageModel):
    """
    Provides a default implementation of QuantConnect.Brokerages.IBrokerageModel that allows all orders and uses
                the default transaction models
    
    DefaultBrokerageModel(accountType: AccountType)
    """
    def ApplySplit(self, tickets: typing.List[QuantConnect.Orders.OrderTicket], split: QuantConnect.Data.Market.Split) -> None:
        pass

    def CanExecuteOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> bool:
        pass

    def CanSubmitOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> bool:
        pass

    def CanUpdateOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> bool:
        pass

    @typing.overload
    def GetBuyingPowerModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.IBuyingPowerModel:
        pass

    @typing.overload
    def GetBuyingPowerModel(self, security: QuantConnect.Securities.Security, accountType: QuantConnect.AccountType) -> QuantConnect.Securities.IBuyingPowerModel:
        pass

    def GetBuyingPowerModel(self, *args) -> QuantConnect.Securities.IBuyingPowerModel:
        pass

    def GetFeeModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        pass

    def GetFillModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fills.IFillModel:
        pass

    def GetLeverage(self, security: QuantConnect.Securities.Security) -> float:
        pass

    @typing.overload
    def GetSettlementModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.ISettlementModel:
        pass

    @typing.overload
    def GetSettlementModel(self, security: QuantConnect.Securities.Security, accountType: QuantConnect.AccountType) -> QuantConnect.Securities.ISettlementModel:
        pass

    def GetSettlementModel(self, *args) -> QuantConnect.Securities.ISettlementModel:
        pass

    def GetSlippageModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Slippage.ISlippageModel:
        pass

    @staticmethod # known case of __new__
    def __new__(self, accountType: QuantConnect.AccountType) -> None:
        pass

    AccountType: QuantConnect.AccountType

    DefaultMarkets: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]

    RequiredFreeBuyingPowerPercent: float


    DefaultMarketMap: ReadOnlyDictionary[SecurityType, str]


class AlpacaBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel, QuantConnect.Brokerages.IBrokerageModel):
    """
    Alpaca Brokerage Model Implementation for Back Testing.
    
    AlpacaBrokerageModel(orderProvider: IOrderProvider, accountType: AccountType)
    """
    def CanSubmitOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> bool:
        pass

    def GetFeeModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        pass

    def GetFillModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fills.IFillModel:
        pass

    def GetSlippageModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Slippage.ISlippageModel:
        pass

    @staticmethod # known case of __new__
    def __new__(self, orderProvider: QuantConnect.Securities.IOrderProvider, accountType: QuantConnect.AccountType) -> None:
        pass

    DefaultMarkets: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]


    DefaultMarketMap: ReadOnlyDictionary[SecurityType, str]


class AlphaStreamsBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel, QuantConnect.Brokerages.IBrokerageModel):
    """
    Provides properties specific to Alpha Streams
    
    AlphaStreamsBrokerageModel(accountType: AccountType)
    """
    def GetFeeModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        pass

    def GetLeverage(self, security: QuantConnect.Securities.Security) -> float:
        pass

    @typing.overload
    def GetSettlementModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.ISettlementModel:
        pass

    @typing.overload
    def GetSettlementModel(self, security: QuantConnect.Securities.Security, accountType: QuantConnect.AccountType) -> QuantConnect.Securities.ISettlementModel:
        pass

    def GetSettlementModel(self, *args) -> QuantConnect.Securities.ISettlementModel:
        pass

    def GetSlippageModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Slippage.ISlippageModel:
        pass

    @staticmethod # known case of __new__
    def __new__(self, accountType: QuantConnect.AccountType) -> None:
        pass


class BitfinexBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel, QuantConnect.Brokerages.IBrokerageModel):
    """
    Provides Bitfinex specific properties
    
    BitfinexBrokerageModel(accountType: AccountType)
    """
    @typing.overload
    def GetBuyingPowerModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.IBuyingPowerModel:
        pass

    @typing.overload
    def GetBuyingPowerModel(self, security: QuantConnect.Securities.Security, accountType: QuantConnect.AccountType) -> QuantConnect.Securities.IBuyingPowerModel:
        pass

    def GetBuyingPowerModel(self, *args) -> QuantConnect.Securities.IBuyingPowerModel:
        pass

    def GetFeeModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        pass

    def GetLeverage(self, security: QuantConnect.Securities.Security) -> float:
        pass

    @staticmethod # known case of __new__
    def __new__(self, accountType: QuantConnect.AccountType) -> None:
        pass

    DefaultMarkets: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]



class BrokerageFactoryAttribute(System.Attribute, System.Runtime.InteropServices._Attribute):
    """
    Represents the brokerage factory type required to load a data queue handler
    
    BrokerageFactoryAttribute(type: Type)
    """
    @staticmethod # known case of __new__
    def __new__(self, type: type) -> None:
        pass

    Type: type



class BrokerageMessageEvent(System.object):
    """
    Represents a message received from a brokerage
    
    BrokerageMessageEvent(type: BrokerageMessageType, code: int, message: str)
    BrokerageMessageEvent(type: BrokerageMessageType, code: str, message: str)
    """
    @staticmethod
    def Disconnected(message: str) -> QuantConnect.Brokerages.BrokerageMessageEvent:
        pass

    @staticmethod
    def Reconnected(message: str) -> QuantConnect.Brokerages.BrokerageMessageEvent:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, type: QuantConnect.Brokerages.BrokerageMessageType, code: int, message: str) -> None:
        pass

    @typing.overload
    def __new__(self, type: QuantConnect.Brokerages.BrokerageMessageType, code: str, message: str) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Code: str

    Message: str

    Type: QuantConnect.Brokerages.BrokerageMessageType



class BrokerageMessageType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Specifies the type of message received from an IBrokerage implementation
    
    enum BrokerageMessageType, values: Disconnect (4), Error (2), Information (0), Reconnect (3), Warning (1)
    """
    value__: int
    Disconnect: BrokerageMessageType
    Error: BrokerageMessageType
    Information: BrokerageMessageType
    Reconnect: BrokerageMessageType
    Warning: BrokerageMessageType


class BrokerageModel(System.object):
    """ Provides factory method for creating an QuantConnect.Brokerages.IBrokerageModel from the QuantConnect.Brokerages.BrokerageName enum """
    @staticmethod
    def Create(orderProvider: QuantConnect.Securities.IOrderProvider, brokerage: QuantConnect.Brokerages.BrokerageName, accountType: QuantConnect.AccountType) -> QuantConnect.Brokerages.IBrokerageModel:
        pass

    __all__: list


class BrokerageName(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Specifices what transaction model and submit/execution rules to use
    
    enum BrokerageName, values: Alpaca (13), AlphaStreams (14), Bitfinex (5), Default (0), FxcmBrokerage (4), GDAX (12), InteractiveBrokersBrokerage (1), OandaBrokerage (3), QuantConnectBrokerage (0), TradierBrokerage (2)
    """
    value__: int
    Alpaca: BrokerageName
    AlphaStreams: BrokerageName
    Bitfinex: BrokerageName
    Default: BrokerageName
    FxcmBrokerage: BrokerageName
    GDAX: BrokerageName
    InteractiveBrokersBrokerage: BrokerageName
    OandaBrokerage: BrokerageName
    QuantConnectBrokerage: BrokerageName
    TradierBrokerage: BrokerageName


class DefaultBrokerageMessageHandler(System.object, QuantConnect.Brokerages.IBrokerageMessageHandler):
    """
    Provides a default implementation o QuantConnect.Brokerages.IBrokerageMessageHandler that will forward
                messages as follows:
                Information -> IResultHandler.Debug
                Warning     -> IResultHandler.Error && IApi.SendUserEmail
                Error       -> IResultHandler.Error && IAlgorithm.RunTimeError
    
    DefaultBrokerageMessageHandler(algorithm: IAlgorithm, job: AlgorithmNodePacket, api: IApi, initialDelay: Nullable[TimeSpan], openThreshold: Nullable[TimeSpan])
    """
    def Handle(self, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, api: QuantConnect.Interfaces.IApi, initialDelay: typing.Optional[datetime.timedelta], openThreshold: typing.Optional[datetime.timedelta]) -> None:
        pass


class DowngradeErrorCodeToWarningBrokerageMessageHandler(System.object, QuantConnect.Brokerages.IBrokerageMessageHandler):
    """
    Provides an implementation of QuantConnect.Brokerages.IBrokerageMessageHandler that converts specified error codes into warnings
    
    DowngradeErrorCodeToWarningBrokerageMessageHandler(brokerageMessageHandler: IBrokerageMessageHandler, errorCodesToIgnore: Array[str])
    """
    def Handle(self, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, brokerageMessageHandler: QuantConnect.Brokerages.IBrokerageMessageHandler, errorCodesToIgnore: typing.List[str]) -> None:
        pass


class FxcmBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel, QuantConnect.Brokerages.IBrokerageModel):
    """
    Provides FXCM specific properties
    
    FxcmBrokerageModel(accountType: AccountType)
    """
    def CanSubmitOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> bool:
        pass

    def CanUpdateOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> bool:
        pass

    def GetFeeModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        pass

    def GetFillModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fills.IFillModel:
        pass

    @typing.overload
    def GetSettlementModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.ISettlementModel:
        pass

    @typing.overload
    def GetSettlementModel(self, security: QuantConnect.Securities.Security, accountType: QuantConnect.AccountType) -> QuantConnect.Securities.ISettlementModel:
        pass

    def GetSettlementModel(self, *args) -> QuantConnect.Securities.ISettlementModel:
        pass

    def GetSlippageModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Slippage.ISlippageModel:
        pass

    @staticmethod # known case of __new__
    def __new__(self, accountType: QuantConnect.AccountType) -> None:
        pass

    DefaultMarkets: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]


    DefaultMarketMap: ReadOnlyDictionary[SecurityType, str]


class GDAXBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel, QuantConnect.Brokerages.IBrokerageModel):
    """
    Provides GDAX specific properties
    
    GDAXBrokerageModel(accountType: AccountType)
    """
    def CanSubmitOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> bool:
        pass

    def CanUpdateOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> bool:
        pass

    @typing.overload
    def GetBuyingPowerModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.IBuyingPowerModel:
        pass

    @typing.overload
    def GetBuyingPowerModel(self, security: QuantConnect.Securities.Security, accountType: QuantConnect.AccountType) -> QuantConnect.Securities.IBuyingPowerModel:
        pass

    def GetBuyingPowerModel(self, *args) -> QuantConnect.Securities.IBuyingPowerModel:
        pass

    def GetFeeModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        pass

    def GetFillModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fills.IFillModel:
        pass

    def GetLeverage(self, security: QuantConnect.Securities.Security) -> float:
        pass

    @staticmethod # known case of __new__
    def __new__(self, accountType: QuantConnect.AccountType) -> None:
        pass


class IBrokerageMessageHandler:
    """
    Provides an plugin point to allow algorithms to directly handle the messages
                that come from their brokerage
    """
    def Handle(self, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> None:
        pass


class IBrokerageModel:
    """ Models brokerage transactions, fees, and order """
    def ApplySplit(self, tickets: typing.List[QuantConnect.Orders.OrderTicket], split: QuantConnect.Data.Market.Split) -> None:
        pass

    def CanExecuteOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> bool:
        pass

    def CanSubmitOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> bool:
        pass

    def CanUpdateOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> bool:
        pass

    @typing.overload
    def GetBuyingPowerModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.IBuyingPowerModel:
        pass

    @typing.overload
    def GetBuyingPowerModel(self, security: QuantConnect.Securities.Security, accountType: QuantConnect.AccountType) -> QuantConnect.Securities.IBuyingPowerModel:
        pass

    def GetBuyingPowerModel(self, *args) -> QuantConnect.Securities.IBuyingPowerModel:
        pass

    def GetFeeModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        pass

    def GetFillModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fills.IFillModel:
        pass

    def GetLeverage(self, security: QuantConnect.Securities.Security) -> float:
        pass

    @typing.overload
    def GetSettlementModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.ISettlementModel:
        pass

    @typing.overload
    def GetSettlementModel(self, security: QuantConnect.Securities.Security, accountType: QuantConnect.AccountType) -> QuantConnect.Securities.ISettlementModel:
        pass

    def GetSettlementModel(self, *args) -> QuantConnect.Securities.ISettlementModel:
        pass

    def GetSlippageModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Slippage.ISlippageModel:
        pass

    AccountType: QuantConnect.AccountType

    DefaultMarkets: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]

    RequiredFreeBuyingPowerPercent: float



class InteractiveBrokersBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel, QuantConnect.Brokerages.IBrokerageModel):
    """
    Provides properties specific to interactive brokers
    
    InteractiveBrokersBrokerageModel(accountType: AccountType)
    """
    def CanExecuteOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> bool:
        pass

    def CanSubmitOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> bool:
        pass

    def CanUpdateOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> bool:
        pass

    def GetFeeModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        pass

    @staticmethod # known case of __new__
    def __new__(self, accountType: QuantConnect.AccountType) -> None:
        pass

    DefaultMarkets: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]


    DefaultMarketMap: ReadOnlyDictionary[SecurityType, str]


class OandaBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel, QuantConnect.Brokerages.IBrokerageModel):
    """
    Oanda Brokerage Model Implementation for Back Testing.
    
    OandaBrokerageModel(accountType: AccountType)
    """
    def CanSubmitOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> bool:
        pass

    def GetFeeModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        pass

    def GetFillModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fills.IFillModel:
        pass

    @typing.overload
    def GetSettlementModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.ISettlementModel:
        pass

    @typing.overload
    def GetSettlementModel(self, security: QuantConnect.Securities.Security, accountType: QuantConnect.AccountType) -> QuantConnect.Securities.ISettlementModel:
        pass

    def GetSettlementModel(self, *args) -> QuantConnect.Securities.ISettlementModel:
        pass

    def GetSlippageModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Slippage.ISlippageModel:
        pass

    @staticmethod # known case of __new__
    def __new__(self, accountType: QuantConnect.AccountType) -> None:
        pass

    DefaultMarkets: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]


    DefaultMarketMap: ReadOnlyDictionary[SecurityType, str]


class TradierBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel, QuantConnect.Brokerages.IBrokerageModel):
    """
    Provides tradier specific properties
    
    TradierBrokerageModel(accountType: AccountType)
    """
    def ApplySplit(self, tickets: typing.List[QuantConnect.Orders.OrderTicket], split: QuantConnect.Data.Market.Split) -> None:
        pass

    def CanExecuteOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> bool:
        pass

    def CanSubmitOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> bool:
        pass

    def CanUpdateOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> bool:
        pass

    def GetFeeModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        pass

    def GetFillModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fills.IFillModel:
        pass

    def GetSlippageModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Slippage.ISlippageModel:
        pass

    @staticmethod # known case of __new__
    def __new__(self, accountType: QuantConnect.AccountType) -> None:
        pass


