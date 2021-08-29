#
# プロパティ "FN" (RFC6350 6.2.1.)
#
from typing import Optional
from .Property import Property


class FullNameProperty(Property):

    """
    プロパティ "FN" (RFC6350 6.2.1) を扱うデータクラス。
    FNプロパティは連絡先のフルネームに関する情報を提供します。
    値は一つで、セミコロンによる区切りはありません。
    """

    def __init__(self, full_name: str, encoding: Optional[str] = None) -> None:
        """
        インスタンスを生成します。

        Args:
            full_name (str) : フルネームを表す文字列。
            encoding (Optional[str]) : 文字列のエンコーディング。デフォルトではUTF-8が使用されます。

        Raises:
            ValueError : 不正な引数が渡された場合。
            UnicodeEncodeError : プロパティ値のエンコードに失敗した場合。
        """

        if type(full_name) is not str:
            raise ValueError("Invalid argument")

        enc = encoding or "UTF-8"
        name_encoded = full_name.encode(enc)

        super().__init__("FN", {}, name_encoded)

