#
# vCardオブジェクト
#
from __future__ import annotations

from typing import List

from .properties.Property import Property
from .properties.VersionProperty import VersionProperty


class VCard():

    """
    連絡先カード (vCard) を表すデータクラスです。
    """

    def __init__(self, version: str = "4.0", props: List[Property] = []) -> None:
        """
        インスタンスを生成します。自動でVersionPropertyが追加されます。

        Args:
            props (List[Property]) : 初期状態のプロパティ配列。
        """

        if not issubclass(type(props), list):
            raise ValueError("Invalid argument")

        self.properties: List[Property] = props
        self.add_property(VersionProperty(version))

    def add_property(self, prop: Property, overwrite: bool = False) -> VCard:
        """
        vCardにプロパティを追加します。

        Args:
            prop (Property) : 追加対象のプロパティ。
            overwrite (bool) : Trueを設定するとパラメータを上書きします。

        Raises:
            ValueError : 引数が不正だった場合。
        
        Return:
            VCard
        """

        if not issubclass(type(prop), Property):
            raise ValueError("Invalid argument")

        # 強制上書きの場合は一旦消して
        if overwrite:
            self.remove_property(prop)

        # 追加
        self.properties.append(prop)

        return self

    def remove_property(self, prop: Property):
        """
        引数に渡されたプロパティを削除します。

        Args:
            prop (Property) : 削除対象のプロパティ。

        Raises:
            ValueError : 引数が不正だった場合。
        """

        if not issubclass(type(prop), Property):
            raise ValueError("Invalid argument")

        self.properties = list(filter(lambda p: p != prop, self.properties))

    def is_exists(self, prop: Property) -> bool:
        """
        引数に渡されたプロパティを持っているか返します。

        Args:
            prop (Property) : 対象のプロパティ。

        Returns:
            bool : プロパティを持っていればTrue。

        Raises:
            ValueError : 引数が不正だった場合。
        """

        if not issubclass(type(prop), Property):
            raise ValueError("Invalid argument")

        return len(list(filter(lambda p: p == prop, self.properties))) == 1
