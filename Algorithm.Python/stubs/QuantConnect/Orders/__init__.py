# encoding: utf-8
# module QuantConnect.Orders calls itself Orders
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import Newtonsoft.Json
import Newtonsoft.Json.Linq
import QuantConnect
import QuantConnect.Algorithm.Framework.Portfolio
import QuantConnect.Interfaces
import QuantConnect.Orders
import QuantConnect.Orders.Fees
import QuantConnect.Orders.Serialization
import QuantConnect.Securities
import System
import System.Threading
import typing

# no functions
# classes

class OrderProperties(System.object, QuantConnect.Interfaces.IOrderProperties):
    """
    Contains additional properties and settings for an order
    
    OrderProperties()
    """
    def Clone(self) -> QuantConnect.Interfaces.IOrderProperties:
        pass

    TimeInForce: QuantConnect.Orders.TimeInForce



class BitfinexOrderProperties(QuantConnect.Orders.OrderProperties, QuantConnect.Interfaces.IOrderProperties):
    """
    Contains additional properties and settings for an order submitted to Bitfinex brokerage
    
    BitfinexOrderProperties()
    """
    def Clone(self) -> QuantConnect.Interfaces.IOrderProperties:
        pass

    Hidden: bool

    PostOnly: bool



class OrderRequest(System.object):
    """ Represents a request to submit, update, or cancel an order """
    def SetResponse(self, response: QuantConnect.Orders.OrderResponse, status: QuantConnect.Orders.OrderRequestStatus) -> None:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        pass

    OrderId: int

    OrderRequestType: QuantConnect.Orders.OrderRequestType

    Response: QuantConnect.Orders.OrderResponse

    Status: QuantConnect.Orders.OrderRequestStatus

    Tag: str

    Time: datetime.datetime



class CancelOrderRequest(QuantConnect.Orders.OrderRequest):
    """
    Defines a request to cancel an order
    
    CancelOrderRequest(time: DateTime, orderId: int, tag: str)
    """
    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    def __new__(self, time: datetime.datetime, orderId: int, tag: str) -> None:
        pass

    OrderRequestType: QuantConnect.Orders.OrderRequestType



class GDAXOrderProperties(QuantConnect.Orders.OrderProperties, QuantConnect.Interfaces.IOrderProperties):
    """
    Contains additional properties and settings for an order submitted to GDAX brokerage
    
    GDAXOrderProperties()
    """
    def Clone(self) -> QuantConnect.Interfaces.IOrderProperties:
        pass

    PostOnly: bool



class InteractiveBrokersOrderProperties(QuantConnect.Orders.OrderProperties, QuantConnect.Interfaces.IOrderProperties):
    """
    Contains additional properties and settings for an order submitted to Interactive Brokers
    
    InteractiveBrokersOrderProperties()
    """
    def Clone(self) -> QuantConnect.Interfaces.IOrderProperties:
        pass

    Account: str

    FaGroup: str

    FaMethod: str

    FaPercentage: int

    FaProfile: str



class Order(System.object):
    """ Order struct for placing new trade """
    def ApplyUpdateOrderRequest(self, request: QuantConnect.Orders.UpdateOrderRequest) -> None:
        pass

    def Clone(self) -> QuantConnect.Orders.Order:
        pass

    @staticmethod
    def CreateOrder(request: QuantConnect.Orders.SubmitOrderRequest) -> QuantConnect.Orders.Order:
        pass

    @staticmethod
    def FromSerialized(serializedOrder: QuantConnect.Orders.Serialization.SerializedOrder) -> QuantConnect.Orders.Order:
        pass

    def GetValue(self, security: QuantConnect.Securities.Security) -> float:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        pass

    AbsoluteQuantity: float

    BrokerId: typing.List[str]

    CanceledTime: typing.Optional[datetime.datetime]

    ContingentId: int

    CreatedTime: datetime.datetime

    Direction: QuantConnect.Orders.OrderDirection

    Id: int

    IsMarketable: bool

    LastFillTime: typing.Optional[datetime.datetime]

    LastUpdateTime: typing.Optional[datetime.datetime]

    OrderSubmissionData: QuantConnect.Orders.OrderSubmissionData

    Price: float

    PriceCurrency: str

    Properties: QuantConnect.Interfaces.IOrderProperties

    Quantity: float

    SecurityType: QuantConnect.SecurityType

    Status: QuantConnect.Orders.OrderStatus

    Symbol: QuantConnect.Symbol

    Tag: str

    Time: datetime.datetime

    TimeInForce: QuantConnect.Orders.TimeInForce

    Type: QuantConnect.Orders.OrderType

    Value: float



class LimitOrder(QuantConnect.Orders.Order):
    """
    Limit order type definition
    
    LimitOrder()
    LimitOrder(symbol: Symbol, quantity: Decimal, limitPrice: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
    """
    def ApplyUpdateOrderRequest(self, request: QuantConnect.Orders.UpdateOrderRequest) -> None:
        pass

    def Clone(self) -> QuantConnect.Orders.Order:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, quantity: float, limitPrice: float, time: datetime.datetime, tag: str, properties: QuantConnect.Interfaces.IOrderProperties) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    LimitPrice: float

    Type: QuantConnect.Orders.OrderType



class MarketOnCloseOrder(QuantConnect.Orders.Order):
    """
    Market on close order type - submits a market order on exchange close
    
    MarketOnCloseOrder()
    MarketOnCloseOrder(symbol: Symbol, quantity: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
    """
    def Clone(self) -> QuantConnect.Orders.Order:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, quantity: float, time: datetime.datetime, tag: str, properties: QuantConnect.Interfaces.IOrderProperties) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Type: QuantConnect.Orders.OrderType


    DefaultSubmissionTimeBuffer: TimeSpan


class MarketOnOpenOrder(QuantConnect.Orders.Order):
    """
    Market on Open order type, submits a market order when the exchange opens
    
    MarketOnOpenOrder()
    MarketOnOpenOrder(symbol: Symbol, quantity: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
    """
    def Clone(self) -> QuantConnect.Orders.Order:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, quantity: float, time: datetime.datetime, tag: str, properties: QuantConnect.Interfaces.IOrderProperties) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Type: QuantConnect.Orders.OrderType



class MarketOrder(QuantConnect.Orders.Order):
    """
    Market order type definition
    
    MarketOrder()
    MarketOrder(symbol: Symbol, quantity: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
    """
    def Clone(self) -> QuantConnect.Orders.Order:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, quantity: float, time: datetime.datetime, tag: str, properties: QuantConnect.Interfaces.IOrderProperties) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Type: QuantConnect.Orders.OrderType



class OptionExerciseOrder(QuantConnect.Orders.Order):
    """
    Option exercise order type definition
    
    OptionExerciseOrder()
    OptionExerciseOrder(symbol: Symbol, quantity: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
    """
    def Clone(self) -> QuantConnect.Orders.Order:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, quantity: float, time: datetime.datetime, tag: str, properties: QuantConnect.Interfaces.IOrderProperties) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Type: QuantConnect.Orders.OrderType



class OrderDirection(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Direction of the order
    
    enum OrderDirection, values: Buy (0), Hold (2), Sell (1)
    """
    value__: int
    Buy: OrderDirection
    Hold: OrderDirection
    Sell: OrderDirection


class OrderError(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Specifies the possible error states during presubmission checks
    
    enum OrderError, values: CanNotUpdateFilledOrder (-8), GeneralError (-7), InsufficientCapital (-4), MarketClosed (-3), MaxOrdersExceeded (-5), NoData (-2), None (0), TimestampError (-6), ZeroQuantity (-1)
    """
    value__: int
    CanNotUpdateFilledOrder: OrderError
    GeneralError: OrderError
    InsufficientCapital: OrderError
    MarketClosed: OrderError
    MaxOrdersExceeded: OrderError
    NoData: OrderError
    None: OrderError
    TimestampError: OrderError
    ZeroQuantity: OrderError


class OrderEvent(System.object):
    """
    Order Event - Messaging class signifying a change in an order state and record the change in the user's algorithm portfolio
    
    OrderEvent()
    OrderEvent(orderId: int, symbol: Symbol, utcTime: DateTime, status: OrderStatus, direction: OrderDirection, fillPrice: Decimal, fillQuantity: Decimal, orderFee: OrderFee, message: str)
    OrderEvent(order: Order, utcTime: DateTime, orderFee: OrderFee, message: str)
    """
    def Clone(self) -> QuantConnect.Orders.OrderEvent:
        pass

    @staticmethod
    def FromSerialized(serializedOrderEvent: QuantConnect.Orders.Serialization.SerializedOrderEvent) -> QuantConnect.Orders.OrderEvent:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, orderId: int, symbol: QuantConnect.Symbol, utcTime: datetime.datetime, status: QuantConnect.Orders.OrderStatus, direction: QuantConnect.Orders.OrderDirection, fillPrice: float, fillQuantity: float, orderFee: QuantConnect.Orders.Fees.OrderFee, message: str) -> None:
        pass

    @typing.overload
    def __new__(self, order: QuantConnect.Orders.Order, utcTime: datetime.datetime, orderFee: QuantConnect.Orders.Fees.OrderFee, message: str) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    AbsoluteFillQuantity: float

    Direction: QuantConnect.Orders.OrderDirection

    FillPrice: float

    FillPriceCurrency: str

    FillQuantity: float

    Id: int

    IsAssignment: bool

    LimitPrice: typing.Optional[float]

    Message: str

    OrderFee: QuantConnect.Orders.Fees.OrderFee

    OrderId: int

    Quantity: float

    Status: QuantConnect.Orders.OrderStatus

    StopPrice: typing.Optional[float]

    Symbol: QuantConnect.Symbol

    UtcTime: datetime.datetime



class OrderExtensions(System.object):
    """ Provides extension methods for the QuantConnect.Orders.Order class and for the QuantConnect.Orders.OrderStatus enumeration """
    @staticmethod
    def IsClosed(status: QuantConnect.Orders.OrderStatus) -> bool:
        pass

    @staticmethod
    def IsFill(status: QuantConnect.Orders.OrderStatus) -> bool:
        pass

    @staticmethod
    def IsLimitOrder(orderType: QuantConnect.Orders.OrderType) -> bool:
        pass

    @staticmethod
    def IsOpen(status: QuantConnect.Orders.OrderStatus) -> bool:
        pass

    @staticmethod
    def IsStopOrder(orderType: QuantConnect.Orders.OrderType) -> bool:
        pass

    __all__: list


class OrderField(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Specifies an order field that does not apply to all order types
    
    enum OrderField, values: LimitPrice (0), StopPrice (1)
    """
    value__: int
    LimitPrice: OrderField
    StopPrice: OrderField


class OrderJsonConverter(Newtonsoft.Json.JsonConverter):
    """
    Provides an implementation of Newtonsoft.Json.JsonConverter that can deserialize Orders
    
    OrderJsonConverter()
    """
    def CanConvert(self, objectType: type) -> bool:
        pass

    @staticmethod
    def CreateOrderFromJObject(jObject: Newtonsoft.Json.Linq.JObject) -> QuantConnect.Orders.Order:
        pass

    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: type, existingValue: object, serializer: Newtonsoft.Json.JsonSerializer) -> object:
        pass

    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: object, serializer: Newtonsoft.Json.JsonSerializer) -> None:
        pass

    CanWrite: bool



class OrderRequestStatus(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Specifies the status of a request
    
    enum OrderRequestStatus, values: Error (3), Processed (2), Processing (1), Unprocessed (0)
    """
    value__: int
    Error: OrderRequestStatus
    Processed: OrderRequestStatus
    Processing: OrderRequestStatus
    Unprocessed: OrderRequestStatus


class OrderRequestType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Specifies the type of QuantConnect.Orders.OrderRequest
    
    enum OrderRequestType, values: Cancel (2), Submit (0), Update (1)
    """
    value__: int
    Cancel: OrderRequestType
    Submit: OrderRequestType
    Update: OrderRequestType


class OrderResponse(System.object):
    """
    Represents a response to an QuantConnect.Orders.OrderRequest. See QuantConnect.Orders.OrderRequest.Response property for
                a specific request's response value
    """
    @staticmethod
    def Error(request: QuantConnect.Orders.OrderRequest, errorCode: QuantConnect.Orders.OrderResponseErrorCode, errorMessage: str) -> QuantConnect.Orders.OrderResponse:
        pass

    @staticmethod
    def InvalidStatus(request: QuantConnect.Orders.OrderRequest, order: QuantConnect.Orders.Order) -> QuantConnect.Orders.OrderResponse:
        pass

    @staticmethod
    def Success(request: QuantConnect.Orders.OrderRequest) -> QuantConnect.Orders.OrderResponse:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod
    def UnableToFindOrder(request: QuantConnect.Orders.OrderRequest) -> QuantConnect.Orders.OrderResponse:
        pass

    @staticmethod
    def WarmingUp(request: QuantConnect.Orders.OrderRequest) -> QuantConnect.Orders.OrderResponse:
        pass

    @staticmethod
    def ZeroQuantity(request: QuantConnect.Orders.OrderRequest) -> QuantConnect.Orders.OrderResponse:
        pass

    ErrorCode: QuantConnect.Orders.OrderResponseErrorCode

    ErrorMessage: str

    IsError: bool

    IsProcessed: bool

    IsSuccess: bool

    OrderId: int


    Unprocessed: OrderResponse


class OrderResponseErrorCode(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Error detail code
    
    enum OrderResponseErrorCode, values: AlgorithmWarmingUp (-24), BrokerageFailedToCancelOrder (-8), BrokerageFailedToSubmitOrder (-5), BrokerageFailedToUpdateOrder (-6), BrokerageHandlerRefusedToUpdateOrder (-7), BrokerageModelRefusedToSubmitOrder (-4), BrokerageModelRefusedToUpdateOrder (-25), ConversionRateZero (-27), ExceededMaximumOrders (-20), ExchangeNotOpen (-15), ForexBaseAndQuoteCurrenciesRequired (-17), ForexConversionRateZero (-18), InsufficientBuyingPower (-3), InvalidOrderStatus (-9), InvalidRequest (-22), MarketOnCloseOrderTooLate (-21), MissingSecurity (-14), None (0), NonExercisableSecurity (-29), NonTradableSecurity (-28), OrderAlreadyExists (-2), OrderQuantityLessThanLoteSize (-30), OrderQuantityZero (-11), PreOrderChecksError (-13), ProcessingError (-1), QuoteCurrencyRequired (-26), RequestCanceled (-23), SecurityHasNoData (-19), SecurityPriceZero (-16), UnableToFindOrder (-10), UnsupportedRequestType (-12)
    """
    value__: int
    AlgorithmWarmingUp: OrderResponseErrorCode
    BrokerageFailedToCancelOrder: OrderResponseErrorCode
    BrokerageFailedToSubmitOrder: OrderResponseErrorCode
    BrokerageFailedToUpdateOrder: OrderResponseErrorCode
    BrokerageHandlerRefusedToUpdateOrder: OrderResponseErrorCode
    BrokerageModelRefusedToSubmitOrder: OrderResponseErrorCode
    BrokerageModelRefusedToUpdateOrder: OrderResponseErrorCode
    ConversionRateZero: OrderResponseErrorCode
    ExceededMaximumOrders: OrderResponseErrorCode
    ExchangeNotOpen: OrderResponseErrorCode
    ForexBaseAndQuoteCurrenciesRequired: OrderResponseErrorCode
    ForexConversionRateZero: OrderResponseErrorCode
    InsufficientBuyingPower: OrderResponseErrorCode
    InvalidOrderStatus: OrderResponseErrorCode
    InvalidRequest: OrderResponseErrorCode
    MarketOnCloseOrderTooLate: OrderResponseErrorCode
    MissingSecurity: OrderResponseErrorCode
    None: OrderResponseErrorCode
    NonExercisableSecurity: OrderResponseErrorCode
    NonTradableSecurity: OrderResponseErrorCode
    OrderAlreadyExists: OrderResponseErrorCode
    OrderQuantityLessThanLoteSize: OrderResponseErrorCode
    OrderQuantityZero: OrderResponseErrorCode
    PreOrderChecksError: OrderResponseErrorCode
    ProcessingError: OrderResponseErrorCode
    QuoteCurrencyRequired: OrderResponseErrorCode
    RequestCanceled: OrderResponseErrorCode
    SecurityHasNoData: OrderResponseErrorCode
    SecurityPriceZero: OrderResponseErrorCode
    UnableToFindOrder: OrderResponseErrorCode
    UnsupportedRequestType: OrderResponseErrorCode


class OrderSizing(System.object):
    """ Provides methods for computing a maximum order size. """
    @staticmethod
    def AdjustByLotSize(security: QuantConnect.Securities.Security, quantity: float) -> float:
        pass

    @staticmethod
    def GetOrderSizeForMaximumValue(security: QuantConnect.Securities.Security, maximumOrderValueInAccountCurrency: float, desiredOrderSize: float) -> float:
        pass

    @staticmethod
    def GetOrderSizeForPercentVolume(security: QuantConnect.Securities.Security, maximumPercentCurrentVolume: float, desiredOrderSize: float) -> float:
        pass

    @staticmethod
    def GetUnorderedQuantity(algorithm: QuantConnect.Interfaces.IAlgorithm, target: QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget) -> float:
        pass

    __all__: list


class OrderStatus(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Fill status of the order class.
    
    enum OrderStatus, values: Canceled (5), CancelPending (8), Filled (3), Invalid (7), New (0), None (6), PartiallyFilled (2), Submitted (1), UpdateSubmitted (9)
    """
    value__: int
    Canceled: OrderStatus
    CancelPending: OrderStatus
    Filled: OrderStatus
    Invalid: OrderStatus
    New: OrderStatus
    None: OrderStatus
    PartiallyFilled: OrderStatus
    Submitted: OrderStatus
    UpdateSubmitted: OrderStatus


class OrderSubmissionData(System.object):
    """
    The purpose of this class is to store time and price information
                available at the time an order was submitted.
    
    OrderSubmissionData(bidPrice: Decimal, askPrice: Decimal, lastPrice: Decimal)
    """
    def Clone(self) -> QuantConnect.Orders.OrderSubmissionData:
        pass

    @staticmethod # known case of __new__
    def __new__(self, bidPrice: float, askPrice: float, lastPrice: float) -> None:
        pass

    AskPrice: float

    BidPrice: float

    LastPrice: float



class OrderTicket(System.object):
    """
    Provides a single reference to an order for the algorithm to maintain. As the order gets
                updated this ticket will also get updated
    
    OrderTicket(transactionManager: SecurityTransactionManager, submitRequest: SubmitOrderRequest)
    """
    def Cancel(self, tag: str) -> QuantConnect.Orders.OrderResponse:
        pass

    def Get(self, field: QuantConnect.Orders.OrderField) -> float:
        pass

    def GetMostRecentOrderRequest(self) -> QuantConnect.Orders.OrderRequest:
        pass

    def GetMostRecentOrderResponse(self) -> QuantConnect.Orders.OrderResponse:
        pass

    @staticmethod
    def InvalidCancelOrderId(transactionManager: QuantConnect.Securities.SecurityTransactionManager, request: QuantConnect.Orders.CancelOrderRequest) -> QuantConnect.Orders.OrderTicket:
        pass

    @staticmethod
    def InvalidSubmitRequest(transactionManager: QuantConnect.Securities.SecurityTransactionManager, request: QuantConnect.Orders.SubmitOrderRequest, response: QuantConnect.Orders.OrderResponse) -> QuantConnect.Orders.OrderTicket:
        pass

    @staticmethod
    def InvalidUpdateOrderId(transactionManager: QuantConnect.Securities.SecurityTransactionManager, request: QuantConnect.Orders.UpdateOrderRequest) -> QuantConnect.Orders.OrderTicket:
        pass

    @staticmethod
    def InvalidWarmingUp(transactionManager: QuantConnect.Securities.SecurityTransactionManager, submit: QuantConnect.Orders.SubmitOrderRequest) -> QuantConnect.Orders.OrderTicket:
        pass

    def ToString(self) -> str:
        pass

    def Update(self, fields: QuantConnect.Orders.UpdateOrderFields) -> QuantConnect.Orders.OrderResponse:
        pass

    def UpdateLimitPrice(self, limitPrice: float, tag: str) -> QuantConnect.Orders.OrderResponse:
        pass

    def UpdateQuantity(self, quantity: float, tag: str) -> QuantConnect.Orders.OrderResponse:
        pass

    def UpdateStopPrice(self, stopPrice: float, tag: str) -> QuantConnect.Orders.OrderResponse:
        pass

    def UpdateTag(self, tag: str) -> QuantConnect.Orders.OrderResponse:
        pass

    @staticmethod # known case of __new__
    def __new__(self, transactionManager: QuantConnect.Securities.SecurityTransactionManager, submitRequest: QuantConnect.Orders.SubmitOrderRequest) -> None:
        pass

    AverageFillPrice: float

    CancelRequest: QuantConnect.Orders.CancelOrderRequest

    HasOrder: bool

    OrderClosed: System.Threading.WaitHandle

    OrderEvents: typing.List[QuantConnect.Orders.OrderEvent]

    OrderId: int

    OrderSet: System.Threading.WaitHandle

    OrderType: QuantConnect.Orders.OrderType

    Quantity: float

    QuantityFilled: float

    SecurityType: QuantConnect.SecurityType

    Status: QuantConnect.Orders.OrderStatus

    SubmitRequest: QuantConnect.Orders.SubmitOrderRequest

    Symbol: QuantConnect.Symbol

    Tag: str

    Time: datetime.datetime

    UpdateRequests: typing.List[QuantConnect.Orders.UpdateOrderRequest]



class OrderType(System.Enum, System.IComparable, System.IFormattable, System.IConvertible):
    """
    Type of the order: market, limit or stop
    
    enum OrderType, values: Limit (1), Market (0), MarketOnClose (5), MarketOnOpen (4), OptionExercise (6), StopLimit (3), StopMarket (2)
    """
    value__: int
    Limit: OrderType
    Market: OrderType
    MarketOnClose: OrderType
    MarketOnOpen: OrderType
    OptionExercise: OrderType
    StopLimit: OrderType
    StopMarket: OrderType


class StopLimitOrder(QuantConnect.Orders.Order):
    """
    Stop Market Order Type Definition
    
    StopLimitOrder()
    StopLimitOrder(symbol: Symbol, quantity: Decimal, stopPrice: Decimal, limitPrice: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
    """
    def ApplyUpdateOrderRequest(self, request: QuantConnect.Orders.UpdateOrderRequest) -> None:
        pass

    def Clone(self) -> QuantConnect.Orders.Order:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, quantity: float, stopPrice: float, limitPrice: float, time: datetime.datetime, tag: str, properties: QuantConnect.Interfaces.IOrderProperties) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    LimitPrice: float

    StopPrice: float

    StopTriggered: bool

    Type: QuantConnect.Orders.OrderType



class StopMarketOrder(QuantConnect.Orders.Order):
    """
    Stop Market Order Type Definition
    
    StopMarketOrder()
    StopMarketOrder(symbol: Symbol, quantity: Decimal, stopPrice: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
    """
    def ApplyUpdateOrderRequest(self, request: QuantConnect.Orders.UpdateOrderRequest) -> None:
        pass

    def Clone(self) -> QuantConnect.Orders.Order:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, quantity: float, stopPrice: float, time: datetime.datetime, tag: str, properties: QuantConnect.Interfaces.IOrderProperties) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Type: QuantConnect.Orders.OrderType

    StopPrice: float


class SubmitOrderRequest(QuantConnect.Orders.OrderRequest):
    """
    Defines a request to submit a new order
    
    SubmitOrderRequest(orderType: OrderType, securityType: SecurityType, symbol: Symbol, quantity: Decimal, stopPrice: Decimal, limitPrice: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
    """
    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    def __new__(self, orderType: QuantConnect.Orders.OrderType, securityType: QuantConnect.SecurityType, symbol: QuantConnect.Symbol, quantity: float, stopPrice: float, limitPrice: float, time: datetime.datetime, tag: str, properties: QuantConnect.Interfaces.IOrderProperties) -> None:
        pass

    LimitPrice: float

    OrderProperties: QuantConnect.Interfaces.IOrderProperties

    OrderRequestType: QuantConnect.Orders.OrderRequestType

    OrderType: QuantConnect.Orders.OrderType

    Quantity: float

    SecurityType: QuantConnect.SecurityType

    StopPrice: float

    Symbol: QuantConnect.Symbol



class TimeInForce(System.object, QuantConnect.Interfaces.ITimeInForceHandler):
    """ Time In Force - defines the length of time over which an order will continue working before it is canceled """
    @staticmethod
    def GoodTilDate(expiry: datetime.datetime) -> QuantConnect.Orders.TimeInForce:
        pass

    def IsFillValid(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, fill: QuantConnect.Orders.OrderEvent) -> bool:
        pass

    def IsOrderExpired(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> bool:
        pass

    Day: DayTimeInForce
    GoodTilCanceled: GoodTilCanceledTimeInForce


class TimeInForceJsonConverter(Newtonsoft.Json.JsonConverter):
    """
    Provides an implementation of Newtonsoft.Json.JsonConverter that can deserialize TimeInForce objects
    
    TimeInForceJsonConverter()
    """
    def CanConvert(self, objectType: type) -> bool:
        pass

    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: type, existingValue: object, serializer: Newtonsoft.Json.JsonSerializer) -> object:
        pass

    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: object, serializer: Newtonsoft.Json.JsonSerializer) -> None:
        pass

    CanWrite: bool



class UpdateOrderFields(System.object):
    """
    Specifies the data in an order to be updated
    
    UpdateOrderFields()
    """
    LimitPrice: typing.Optional[float]

    Quantity: typing.Optional[float]

    StopPrice: typing.Optional[float]

    Tag: str



class UpdateOrderRequest(QuantConnect.Orders.OrderRequest):
    """
    Defines a request to update an order's values
    
    UpdateOrderRequest(time: DateTime, orderId: int, fields: UpdateOrderFields)
    """
    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    def __new__(self, time: datetime.datetime, orderId: int, fields: QuantConnect.Orders.UpdateOrderFields) -> None:
        pass

    LimitPrice: typing.Optional[float]

    OrderRequestType: QuantConnect.Orders.OrderRequestType

    Quantity: typing.Optional[float]

    StopPrice: typing.Optional[float]



# variables with complex values

