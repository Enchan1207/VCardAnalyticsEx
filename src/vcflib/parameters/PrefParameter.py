#
# 優先(PREF)パラメータ
#
from .Parameter import Parameter

class PrefParameter(Parameter):

    """
    プロパティが同一の名前を持つ他のプロパティと比較して優先されることを示すパラメータです。
    (RFC6350 5.3.)

    **NOTE** `type=PREF` とは異なります。
    """

    def __init__(self, priority_level: int) -> None:
        """
        優先度レベルを設定してインスタンスを生成します。

        Args:
            priority_level (int) : 優先度。値は0~100の間である必要があります。

        Raises:
            ValueError : 不正な引数が与えられた場合。
        """

        if type(priority_level) is not int:
            raise ValueError("Invalid argument")

        if priority_level < 0 or priority_level > 100:
            raise ValueError("priority out of range")

        super().__init__("pref", f"{priority_level}")
