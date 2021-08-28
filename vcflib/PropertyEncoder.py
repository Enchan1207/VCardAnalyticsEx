#
# Propertyエンコーダ
#
from typing import Dict, Union
from vcflib.properties.EncodedProperty import EncodedProperty
from vcflib.properties.Property import Property
import base64
import quopri


class PropertyEncoder():

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

        # エンコード情報を消す(Encoderの指定と異なってしまうのを防ぐため)
        if 'ENCODING' in params:
            del params['ENCODING']

        # 適宜エンコード
        enctype = (enctype or "").lower()
        if enctype in ['b', 'base64']:
            value_encoded = base64.encodebytes(value).decode().replace("\n", "\n ")
            params['ENCODING'] = "BASE64"
        if enctype in ['q', 'quoted-printable']:
            value_encoded = quopri.encodestring(value).decode()
            params['ENCODING'] = "QUOTED-PRINTABLE"
        if enctype == "":
            value_encoded = value.decode()

        # EncodedPropertyを生成して返す
        property_encoded = EncodedProperty(name, params, value_encoded)
        return property_encoded
