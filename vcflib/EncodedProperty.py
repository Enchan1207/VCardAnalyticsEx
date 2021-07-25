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
        # パラメータを文字列に変換する 基本はkey=value、ただし配列の場合はkey=valueを繰り返す(つまり同じkeyが重複する)
        params_encoded = []
        for key in self.params.keys():
            value = self.params[key]
            if type(value) == list:
                for val in value:
                    params_encoded.append(f"{key}={val}")
            else:
                params_encoded.append(f"{key}={value}")
        property_string = f"{';'.join([self.name, *params_encoded])}:{self.value}"
        return property_string
