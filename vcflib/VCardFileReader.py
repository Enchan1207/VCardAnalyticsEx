#
# vcfリーダ
#
from typing import Any, Dict, List
from vcflib.Property import Property
from vcflib.VCard import VCard
import re

class VCardFileReader():
    
    def __init__(self) -> None:
        pass

    def parseLines(self, lines: List[str]) ->List[VCard]:
        parsed_cards_raw = [self.__parse_properties(card) for card in self.__parse_cards(lines)]
        cards = [VCard([Property(prop[0], prop[1], prop[2]) for prop in card_raw]) for card_raw in parsed_cards_raw]
        return cards
    
    def parseFile(self, filepath: str) -> List[VCard]:
        with open(filepath, "r") as f:
            lines = f.readlines()
        return self.parseLines(lines)

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
    def __parse_properties(self, lines: List[str]) -> List[Any]:
        properties = []
        
        # プロパティバッファ
        current_property_name = "" # 最後に検出されたプロパティの名称
        current_property_params: Dict[str, str] = {} # 最後に検出されたプロパティの付帯情報
        current_property_value = "" # 最後に検出されたプロパティの値

        is_property_detected = False # プロパティを検出しているか?

        for line in lines:

            # プロパティを含む場合は、
            if re.search(r"[^\\]:", line):
                # 現時点で何らかのプロパティを検出していればそれを保存する
                if is_property_detected:
                    properties.append([current_property_name, current_property_params, current_property_value])

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
    def __parse_parameters(self, params) -> Dict[str, str]:
        parameters = {}

        def parse_param(info):
            key, value = info.split('=')[0], info.split('=')[1:]
            
            if len(value) == 0:
                return {"type": key}

            return {key: "".join(value)}

        property_params_raw = list(map(parse_param, params))
        for param in property_params_raw:
            parameters.update(param)

        return parameters
