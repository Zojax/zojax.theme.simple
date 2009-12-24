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
from zope import interface
from zojax.pageelement.interfaces import IPageElement
from zojax.layoutform.interfaces import ILayoutFormLayer

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('zojax.theme.simple')

MENUITEM_SEPARATOR = '__separator__'


class ISkinLayer(interface.Interface):
    """ zojax layer """

class ISkin(ISkinLayer, ILayoutFormLayer):
    """ zojax Skin """

class IPageHeaders(IPageElement):
    """ page headers """
