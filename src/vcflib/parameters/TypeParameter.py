#
# プロパティタイプパラメータ
#
from typing import List, Union
from .Parameter import Parameter

class TypeParameter(Parameter):
    
    """
    プロパティの付加情報を示すパラメータです。
    (RFC6350 5.6.)
    """

    def __init__(self, values: Union[List[str], str]) -> None:
        """
        タイプ値を指定してパラメータを生成します。

        Args:
            values (Union[List[str], str]) : 指定するタイプの値。詳細はRFCを参照してください。

        Raises:
            ValueError : 不正な引数が与えられた場合。
        """

        _values = values if type(values) is list else [values]
        super().__init__("type", ','.join(_values))
