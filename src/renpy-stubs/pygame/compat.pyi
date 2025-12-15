from _typeshed import Incomplete

__all__ = [
    "geterror",
    "long_",
    "xrange_",
    "ord_",
    "unichr_",
    "unicode_",
    "raw_input_",
    "as_bytes",
    "as_unicode",
    "file_type",
]

file_type: Incomplete

def geterror(): ...

long_ = long
long_ = int
xrange_ = xrange
xrange_ = range

def ord_(o): ...

unichr_ = unichr
unichr_ = chr
unicode_ = unicode
unicode_ = str
bytes_ = bytes
bytes_ = str
raw_input_ = raw_input
raw_input_ = input

def as_bytes(string): ...
def as_unicode(rstring): ...

next_ = next
imap_ = map
