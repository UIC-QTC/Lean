# encoding: utf-8
# module QuantConnect.Algorithm.Framework calls itself Framework
# from QuantConnect.Algorithm, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null, QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import QuantConnect.Algorithm
import QuantConnect.Data.UniverseSelection
import typing

# no functions
# classes

class INotifiedSecurityChanges:
    """ Types implementing this interface will be called when the algorithm's set of securities changes """
    def OnSecuritiesChanged(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        pass


# variables with complex values

