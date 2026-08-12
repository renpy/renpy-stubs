from _frozen_importlib import BuiltinImporter as BuiltinImporter
from collections import OrderedDict as OrderedDict

all_properties: dict[str, list[str]]
prefix_priority: dict[str, int]
prefix_alts: dict[str, list[str]]
prefix_search: dict[str, list[str]]
proxy_properties: dict[str, frozenset[str]]
