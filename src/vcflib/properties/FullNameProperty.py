#
# プロパティ "FN" (RFC6350 6.2.1.)
#

from .Property import Property

class FullNameProperty(Property):

    """
        Class about Property "FN" (RFC6350 6.2.1).
    """

    def __init__(self, full_name: str="") -> None:
        super().__init__("FN", {}, full_name.encode())

