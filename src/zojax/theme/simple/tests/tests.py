##############################################################################
#
# Copyright (c) 2008 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
import os.path
import unittest, doctest
from pkg_resources import get_distribution
from zope import interface
from zope.app.testing import setup
from zope.app.testing.functional import ZCMLLayer
from zope.app.testing.functional import FunctionalDocFileSuite
from zope.app.rotterdam import Rotterdam

from zojax.filefield import testing
from zojax.theme.simple.interfaces import ISkinLayer
from zojax.layoutform.interfaces import ILayoutFormLayer

if get_distribution('ZODB3').version <= '3.9.0a4':
    ZCMLLayer = testing.ZCMLLayer
    FunctionalDocFileSuite = testing.FunctionalBlobDocFileSuite


class IDefaultSkin(ILayoutFormLayer, Rotterdam):
    """ skin """

skinLayer = testing.ZCMLLayer(
    os.path.join(os.path.split(__file__)[0], 'ftesting.zcml'),
    __name__, 'skinLayer', allow_teardown=True)


def test_suite():
    tests = FunctionalDocFileSuite(
        "tests.txt",
        optionflags=doctest.ELLIPSIS|doctest.NORMALIZE_WHITESPACE)
    tests.layer = skinLayer

    columns = FunctionalDocFileSuite(
        "columns.txt",
        optionflags=doctest.ELLIPSIS|doctest.NORMALIZE_WHITESPACE)
    columns.layer = skinLayer

    exceptions = FunctionalDocFileSuite(
        "exceptions.txt",
        optionflags=doctest.ELLIPSIS|doctest.NORMALIZE_WHITESPACE)
    exceptions.layer = skinLayer

    return unittest.TestSuite((tests, columns, exceptions,))
