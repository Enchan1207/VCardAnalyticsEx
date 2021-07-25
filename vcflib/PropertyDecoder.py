#
# Propertyデコーダ
#

from typing import Union
from vcflib.EncodedProperty import EncodedProperty
from vcflib.Property import Property
import re, quopri, base64

class PropertyDecoder():

    def __init__(self) -> None:
        pass

    def decode(self, encoded: EncodedProperty) -> Property:
        """
            vcflib.EncodedPropertyからvcflib.Propertyを生成する。

            Parameters
            ---
            encoded: EncodedProperty
                デコード対象のEncodedProperty.

            Returns: vcflib.Property
            ---
            EncodedPropertyからデコードされたPropertyインスタンス.

            Raises:
            ---
            ValueError
                引数に渡されたEncodedPropertyが不正だった場合.
        """
        
        name = encoded.name
        params = encoded.params
        encoding = (encoded.getencoding() or "").lower()
        value_encoded = encoded.value

        # デコードに失敗しないようにゴミを取り除く
        value_encoded = value_encoded.replace("\n", "")
        value_decoded = value_encoded.encode()
        if encoding in ['quoted-printable']:
            value_encoded = re.sub(r"=+", "=", value_encoded) # 改行時の=を捨てる
            value_decoded = quopri.decodestring(value_encoded.encode())
        if encoding in ['b', 'base64']:
            value_encoded = re.sub(r" ", "", value_encoded) # 空白を捨てる
            value_decoded = base64.decodebytes(value_encoded.encode())

        # Propertyを生成
        # TODO: FactoryかなんかでPhotoProperty(仮), NameProperty(仮)などに分岐できるようにする
        prop = Property(name, params, value_decoded)
        return prop

        