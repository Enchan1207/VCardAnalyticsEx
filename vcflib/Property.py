#
# vCardプロパティ
#
from typing import Any, Dict, List, Union
import re, quopri, base64

class Property():

    def __init__(self, name:str="", parameters:Dict[str, str]={}, value:str="") -> None:
        self.name: str = name
        self.parameters: Dict[str, str] = parameters
        self.__value: str = value

    # 生の値(base64などのエンコード処理前の値)を取得
    def getrawvalue(self) -> str:
        encoding = (self.getencoding() or "").lower()

        # エンコーディングによって処理を分ける
        value: str = self.__value
        if encoding == "quoted-printable":
            value = re.sub(r"=+", "=", self.__value) # 改行時の=を捨てる
        if encoding == "base64" or encoding == "b":
            value = re.sub(r" ", "", self.__value) # 空白を捨てる

        return value
    
    # エンコード済みの値を取得
    def getencodedvalue(self) -> Union[str, bytes]:
        encoding = (self.getencoding() or "").lower()
        charset = self.getcharset()
        rawvalue = self.getrawvalue()

        # 適宜デコードして返す
        value: Union[str, bytes] = rawvalue
        if encoding == "quoted-printable":
            value = quopri.decodestring(rawvalue.encode())

            # ENCODINGがquotprtなのにCHARSETが設定されていない -> qpでバイナリを書こうとしている説
            if charset is not None:
                value = value.decode(charset)
        if encoding == "base64" or encoding == "b":
            value = base64.b64decode(rawvalue)

        return value
        
    
    # 値のキャラクタセットを取得
    def getcharset(self) -> Union[str, None]:
        return self.parameters['CHARSET'] if 'CHARSET' in self.parameters else None

    # 値のエンコード方式を取得
    def getencoding(self) -> Union[str, None]:
        return self.parameters['ENCODING'] if 'ENCODING' in self.parameters else None

    # 文字列表現
    def __str__(self) -> str:
        rawvalue = self.getrawvalue()
        return f"vCard Property name:{self.name} params:({self.parameters}) value:{rawvalue[:10]}..."
