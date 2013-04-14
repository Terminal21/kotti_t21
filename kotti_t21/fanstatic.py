from __future__ import absolute_import

from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource
from kotti.fanstatic import base_css

library = Library("kotti_t21", "static")
kotti_t21_css = Resource(library, "style.css", depends=[base_css])
kotti_t21_group = Group([kotti_t21_css])
