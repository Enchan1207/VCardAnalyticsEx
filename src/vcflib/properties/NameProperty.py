#
# プロパティ "N" (RFC6350 6.2.2.)
#

from .Property import Property

class NameProperty(Property):

    """
        Class about Property "N" (RFC6350 6.2.2).
        It stores some parameters shown below semi-colon-separated form:

         - Family Names (苗字)
         - Given Names (名前)
         - Additional Names (ミドルネーム, 旧姓)
         - Honorific Prefixes (敬称 (名前の前))
         - Honorific Suffixes (敬称 (名前の後))

        **NOTE** you need keep at least 4 semi-colons
        even if you don't need to define some parameter of those.

    """

    def __init__(self, family_name: str, given_name: str, additional_name: str = "", honorific_prefix: str = "", honorific_suffix: str = "") -> None:
        super().__init__("N", {}, ";".join([family_name, given_name, additional_name, honorific_prefix, honorific_suffix]).encode())

