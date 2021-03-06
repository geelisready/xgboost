# coding: utf-8
# pylint: disable= invalid-name,  unused-import
"""For compatibility"""

from __future__ import absolute_import

import sys


PY3 = (sys.version_info[0] == 3)

if PY3:
    # pylint: disable=invalid-name, redefined-builtin
    STRING_TYPES = str,

    def py_str(x):
        """convert c string back to python string"""
        return x.decode('utf-8')
else:
    # pylint: disable=invalid-name
    STRING_TYPES = basestring,

    def py_str(x):
        """convert c string back to python string"""
        return x

try:
    import cPickle as pickle   # noqa
except ImportError:
    import pickle              # noqa


# pandas
try:
    from pandas import DataFrame
    PANDAS_INSTALLED = True
except ImportError:

    class DataFrame(object):
        """ dummy for pandas.DataFrame """
        pass

    PANDAS_INSTALLED = False

# sklearn
try:
    from sklearn.base import BaseEstimator
    from sklearn.base import RegressorMixin, ClassifierMixin
    from sklearn.preprocessing import LabelEncoder                # noqa
    try:
        from sklearn.model_selection import KFold, StratifiedKFold
    except ImportError:
        from sklearn.cross_validation import KFold, StratifiedKFold
    
    SKLEARN_INSTALLED = True

    XGBModelBase = BaseEstimator
    XGBRegressorBase = RegressorMixin
    XGBClassifierBase = ClassifierMixin

    XGBKFold = KFold
    XGBStratifiedKFold = StratifiedKFold
    XGBLabelEncoder = LabelEncoder
except ImportError:
    SKLEARN_INSTALLED = False

    # used for compatiblity without sklearn
    XGBModelBase = object
    XGBClassifierBase = object
    XGBRegressorBase = object

    XGBKFold = None
    XGBStratifiedKFold = None
    XGBLabelEncoder = None
