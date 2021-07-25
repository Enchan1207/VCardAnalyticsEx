#
# エンコードされたプロパティ
#

from typing import Dict, List, Union

class EncodedProperty():

    def __init__(self, name: str, params: Dict[str, Union[str, List[str]]], value: str) -> None:
        self.name = name
        self.params = params
        self.value = value

        self.__enctype = str(self.params['ENCODING']) if 'ENCODING' in self.params else None
        self.__charset = str(self.params['CHARSET']) if 'CHARSET' in self.params else None

    # 値のキャラクタセットを取得
    def getcharset(self) -> Union[str, None]:
        return self.__charset

    # 値のエンコード方式を取得
    def getencoding(self) -> Union[str, None]:
        return self.__enctype

    def __str__(self) -> str:
        # TODO: 74文字制限をなんとかする (普通に改行挟むだけだとquopriが壊れる)
        params_encoded = [f"{key}={self.params[key]}" for key in self.params.keys()]
        property_string = f"{';'.join([self.name, *params_encoded])}:{self.value}"
        return property_string
