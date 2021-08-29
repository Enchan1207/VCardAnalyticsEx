#
# プロパティ "PHOTO" (RFC6350 6.2.4.)
#

from typing import Dict, List, Union
from .Property import Property


class PhotoProperty(Property):

    """
        Class about Property "PHOTO" (RFC6350 6.2.4).
        It can define image source from url or data-uri-scheme.
    """

    def __init__(self, image_uri: Union[str, None] = None, filepath: Union[str, None] = None, enctype: str = "Base64") -> None:
        
        # TODO: ファイルパス読めるように
        content = image_uri or ""

        super().__init__("PHOTO", {"ENCODING": enctype}, content.encode())
