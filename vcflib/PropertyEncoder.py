#
# Propertyエンコーダ
#
from typing import Dict, Union
from vcflib.EncodedProperty import EncodedProperty
from vcflib.Property import Property
import base64
import quopri


class PropertyEncoder():

    def __init__(self) -> None:
        pass

    def encode(self, property: Property, enctype: Union[str, None] = None) -> EncodedProperty:
        """
            vcflib.PropertyをエンコードしてEncodedPropertyを生成する.

            Parameters
            ---
            property: vcflib.Property
                エンコード対象のプロパティ.

            enctype: str|None
                エンコード形式.大文字小文字は区別しない.
                'b' または 'base64' -> Base64
                'quoted-printable' -> quoted printable
                None -> 引数charsetに従いbytesにエンコード

            Returns: EncodedProperty
            ---
            vcfフォーマットでエンコードされたプロパティ.
        """

        # Propertyから情報を持ってきて
        name = property.name
        params = property.parameters
        value = property.value

        # 適宜エンコード
        value_encoded = value

        enctype = (enctype or "").lower()
        print(enctype)
        if enctype in ['b', 'base64']:
            value_encoded = base64.encodebytes(value)
            params['ENCODING'] = "BASE64"
        if enctype in ['quoted-printable']:
            value_encoded = quopri.encodestring(value)
            params['ENCODING'] = "QUOTED-PRINTABLE"

        # EncodedPropertyを生成して返す
        property_encoded = EncodedProperty(name, params, value_encoded.decode())
        return property_encoded
