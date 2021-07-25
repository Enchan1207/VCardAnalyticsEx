#
# プロパティ "BDAY" (RFC6350 6.2.5.)
#

from vcflib.properties.Property import Property

from datetime import datetime

class BirthdayProperty(Property):

    """
        Class about Property "BDAY" (RFC6350 6.2.5).
    """

    def __init__(self, date: datetime) -> None:
        super().__init__("BDAY", {}, f"{date:%Y-%m-%d}".encode())

