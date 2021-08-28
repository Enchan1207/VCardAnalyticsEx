#
# VCFフォーマット解析
#
from os import nice
import sys, jaconv
import vcflib

def main(args):
    # ファイル読み込み
    filepath = args[1] if len(args) > 1 else "resources/yasuhiko.vcf"
    cards = vcflib.VCardReader().parseFile(filepath)
    newcards = []

    for card in cards:
        # 新しいカードを作り、
        newcard = vcflib.VCard(version="4.0", properties=[])

        # 既存のプロパティを流し込む
        for prop in card.getProperties():
            newcard.addProperty(prop)

        # ふりがなは全角にして上書き
        phonetic_prop = card.getPropertyByName("X-PHONETIC-FIRST-NAME")
        if phonetic_prop is not None:
            phonetic_name = jaconv.h2z(phonetic_prop.value.decode())
            phonetic_new_prop = vcflib.Property("X-PHONETIC-LAST-NAME", {"CHARSET": "UTF-8"}, phonetic_name.encode())
            newcard.addProperty(phonetic_new_prop, True)
        newcard.removePropertyByName("X-PHONETIC-FIRST-NAME")

        # X-GROUP-MEMBERSHIPはORGに変換 (めんどくさいため)
        group_prop = card.getPropertyByName("X-GROUP-MEMBERSHIP")
        if group_prop is not None:
            group_name = jaconv.h2z(group_prop.value.decode())
            group_new_prop = vcflib.Property("ORG", {}, group_name.encode())
            newcard.addProperty(group_new_prop, True)
        newcard.removePropertyByName("X-GROUP-MEMBERSHIP")

        newcards.append(newcard)

    writer = vcflib.VCardWriter()
    writer.writeFile(f"{filepath}_.vcf", newcards)

if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("Ctrl+C")
        exit(0)
