#
# vcfリーダ
#
from typing import Any, Dict, List, Tuple, Union
from vcflib.PropertyDecoder import PropertyDecoder
from vcflib.properties.EncodedProperty import EncodedProperty
from vcflib.properties.Property import Property
from vcflib.VCard import VCard
import re

class VCardReader():
    
    def __init__(self) -> None:
        pass

    # vcfフォーマット文字列からVCardを生成する
    def parse_lines(self, vcfstring: str) ->List[VCard]:
        # 改行で分割して
        lines = vcfstring.split("\n")

        # カード単位でパース
        cards: List[VCard] = []
        cards_raw = self.__parse_cards(lines)
        for card in cards_raw:
            # エンコード済みのプロパティを取得、EncodedPropertyに変換
            encoded_properties = [EncodedProperty(name, params, value) for (name, params, value) in self.__parse_properties(card)]

            # デコードしてVCardを生成
            decoder = PropertyDecoder()
            cards.append(VCard(prop=[decoder.decode(prop) for prop in encoded_properties]))
        
        return cards
    
    def parse_file(self, filepath: str) -> List[VCard]:
        with open(filepath, "r") as f:
            lines = f.readlines()
        return self.parse_lines("".join(lines))

    # 複数のvCard形式のstring配列をカード単位で分割
    def __parse_cards(self, lines:List[str]) -> List[List[str]]:
        cards = []
        card_buffer = []
        in_card_data_row = False
        for line in lines:
            if in_card_data_row:
                card_buffer.append(line)
                
            if line.startswith("BEGIN:VCARD"):
                in_card_data_row = True

            if line.startswith("END:VCARD"):
                in_card_data_row = False
                cards.append(card_buffer)
                card_buffer = []
        return cards

    # vCard形式のstring配列をパース(AAA;BBB=CCC:DDDを["AAA", {'BBB': 'CCC'}, "DDD"]に変換)
    def __parse_properties(self, lines: List[str]) -> List[Tuple[str, Dict[str, Union[str, List[str]]], str]]:
        properties = []
        
        # プロパティバッファ
        current_property_name = "" # 最後に検出されたプロパティの名称
        current_property_params: Dict[str, Union[str, List[str]]] = {} # 最後に検出されたプロパティの付帯情報
        current_property_value = "" # 最後に検出されたプロパティの値

        is_property_detected = False # プロパティを検出しているか?

        for line in lines:

            # プロパティを含む場合は、
            if re.search(r"[^\\]:", line):
                # 現時点で何らかのプロパティを検出していればそれを保存する
                if is_property_detected:
                    properties.append((current_property_name, current_property_params, current_property_value))

                    # バッファ初期化
                    current_property_value = ""
                    current_property_name = ""
                    current_property_params = {}
                    is_property_detected = False

                # 検出したプロパティの情報をパースしてバッファに積む
                property_field = line[:line.index(":")]
                current_property_name = property_field.split(";")[0]
                property_params_raw = property_field.split(";")[1:]
                current_property_params = self.__parse_parameters(property_params_raw)
                
                is_property_detected = True
            
            # プロパティを含まない場合でも、それ以前でプロパティを検出していた場合はプロパティ値と判断しバッファに追加
            if is_property_detected:
                # コロンより後を読むことに注意 (一行の中でプロパティ名とプロパティ値が共存することは普通にあり得るため)
                if line.find(":") >= 0:
                    current_property_value += line[line.index(":")+1:]
                else:
                    current_property_value += line
                
                # 改行を飛ばす
                current_property_value = current_property_value.replace("\r\n", "").replace("\n", "")

        return properties

    # パラメータ解析(AAA=BBB;CCC=DDDを{'AAA': 'BBB', 'CCC': 'DDD'}に変換)
    def __parse_parameters(self, params) -> Dict[str, Union[str, List[str]]]:
        parameters:Dict[str, Union[str, List[str]]] = {}

        def parse_param(info):
            key, value = info.split('=')[0], info.split('=')[1:]
            
            # key-valueのvalueにあたる値がない(type=VOICEのような形式でなく PREF; など)場合
            if len(value) == 0:
                return {"type": key}

            return {key: "".join(value)}

        property_params_raw = list(map(parse_param, params))
        for param in property_params_raw:
            key = list(param.keys())[0]

            # typeキーに関しては無条件で配列に変換
            if key == "type":
                current = list(parameters["type"]) if "type" in parameters else []
                current.append(param[key])
                parameters["type"] = current
            else:
                parameters.update(param)

        return parameters
