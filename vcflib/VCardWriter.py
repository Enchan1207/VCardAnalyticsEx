#
# vcfライタ
#
from typing import List, Union
from vcflib.PropertyEncoder import PropertyEncoder
from vcflib.VCard import VCard


class VCardWriter():

    def __init__(self) -> None:
        pass

    def writeFile(self, filepath: str, cards: Union[VCard, List[VCard]]):
        """
            VCardをファイルに書き出す.

            Parameters:
            ---
                filepath: str
                保存先ファイルパス. 

                cards: VCard | List[VCard]
                書き込むVCard.複数枚同時格納可能.

        """

        lines = []
        
        if isinstance(cards, VCard):
            lines = self.parseLines(cards)
        elif isinstance(cards, list):
            lines = []
            for card in cards:
                lines.extend(self.parseLines(card))

        with open(filepath, "w") as f:
            f.write("\r\n".join(lines))

    def parseLines(self, card: VCard) -> List[str]:
        """
            VCardをvcfフォーマットに変換する。

            Parameters:
            ---
                card: VCard
                変換対象のVCard.

            Returns: List[str]
            vcfフォーマットに変換されたVCard.
        """

        lines_buffer = []

        # begin!
        lines_buffer.append("BEGIN:VCARD")

        # propertiesを回す
        for prop in card.getProperties():
            encoder = PropertyEncoder()
            enctype = ""
            if prop.name == "PHOTO":
                enctype = "b"
            encoded = str(encoder.encode(prop, enctype)).split("\n")
            lines_buffer.extend(encoded)

        # end!
        lines_buffer.append("END:VCARD")
        lines_buffer.append("")

        return lines_buffer
