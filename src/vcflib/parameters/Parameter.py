#
# プロパティパラメータ
#

from __future__ import annotations

from typing import List, Union


class Parameter():

    """
    プロパティへの付加情報を管理するデータクラスです。
    """

    def __init__(self, name: str, value: Union[List[str], str]) -> None:
        """
        名前と値をもとにパラメータを生成します。

        Args:
            name (str) : パラメータの名称。
            value (Union[List[str], str]) : パラメータ値。複数の値を持つ場合があります。

        Raises:
            ValueError : 不正な引数が渡された場合。
        """

        if type(name) is not str or not type(value) in [str, list]:
            raise ValueError("Invalid Argument")

        self.name: str = name
        self.value: Union[List[str], str] = value

    def str_representation(self) -> str:
        """
        パラメータの文字列表現を返します。
        """
        value_str = ','.join(self.value) if type(self.value) is list else self.value
        return f"{self.name}={value_str}"

    def __str__(self) -> str:
        return self.str_representation()
