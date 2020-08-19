# encoding: utf-8
# module QuantConnect.Orders.TimeInForces calls itself TimeInForces
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import QuantConnect.Orders
import QuantConnect.Securities
import System
import typing

# no functions
# classes

class DayTimeInForce(QuantConnect.Orders.TimeInForce, QuantConnect.Interfaces.ITimeInForceHandler):
    """
    Day Time In Force - order expires at market close
    
    DayTimeInForce()
    """
    def IsFillValid(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, fill: QuantConnect.Orders.OrderEvent) -> bool:
        pass

    def IsOrderExpired(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> bool:
        pass


class GoodTilCanceledTimeInForce(QuantConnect.Orders.TimeInForce, QuantConnect.Interfaces.ITimeInForceHandler):
    """
    Good Til Canceled Time In Force - order does never expires
    
    GoodTilCanceledTimeInForce()
    """
    def IsFillValid(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, fill: QuantConnect.Orders.OrderEvent) -> bool:
        pass

    def IsOrderExpired(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> bool:
        pass


class GoodTilDateTimeInForce(QuantConnect.Orders.TimeInForce, QuantConnect.Interfaces.ITimeInForceHandler):
    """
    Good Til Date Time In Force - order expires and will be cancelled on a fixed date/time
    
    GoodTilDateTimeInForce(expiry: DateTime)
    """
    def GetForexOrderExpiryDateTime(self, order: QuantConnect.Orders.Order) -> datetime.datetime:
        pass

    def IsFillValid(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, fill: QuantConnect.Orders.OrderEvent) -> bool:
        pass

    def IsOrderExpired(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> bool:
        pass

    @staticmethod # known case of __new__
    def __new__(self, expiry: datetime.datetime) -> None:
        pass

    Expiry: datetime.datetime



