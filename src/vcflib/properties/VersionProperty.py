#
# プロパティ "VERSION" (RFC6350 6.7.9)
#

from vcflib.properties.Property import Property

class VersionProperty(Property):

    """
        Class about Property "VERSION" (RFC6350 6.7.9).
        It's value should be "4.0", but user can define any value.
    """

    def __init__(self, version: str="4.0") -> None:
        super().__init__("VERSION", {}, version.encode())

