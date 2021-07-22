#
# vCardプロパティ
#
from typing import Any, Dict, List
import re, quopri, base64

class Property():

    def __init__(self, name:str="", parameters:Dict[str, str]={}, value:str="") -> None:
        self.name: str = name
        self.parameters: Dict[str, str] = parameters
        self.__value: str = value

    # 値はエンコードされてたりいろいろしてめんどくさいのでgetvalueで吸収させる
    def getvalue(self) -> str:
        encoding = self.getencoding().lower()

        # エンコーディングによって処理を分ける
        value: str = self.__value
        if encoding == "quoted-printable":
            value = re.sub(r"=+", "=", self.__value) # 改行時の=を捨てる
        if encoding == "base64" or encoding == "b":
            value = re.sub(r" ", "", self.__value) # 空白を捨てる

        return value
    
    # 値のキャラクタセットを取得
    def getcharset(self) -> str:
        return self.parameters['CHARSET'] if 'CHARSET' in self.parameters else "UTF-8"

    # 値のエンコード方式を取得
    def getencoding(self) -> str:
        return self.parameters['ENCODING'] if 'ENCODING' in self.parameters else ""
