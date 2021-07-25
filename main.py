#
# VCFフォーマット解析
#
import sys, jaconv
import vcflib

def main(args):
    # ファイル読み込み
    filepath = args[1] if len(args) > 1 else "resources/v2_1.vcf"
    cards = vcflib.VCardReader().parseFile(filepath)
    newcards = []

    for card in cards:
        # 新しいカードを作り、
        newcard = vcflib.VCard()

        # 既存のプロパティを流し込む
        for prop in card.getProperties():
            newcard.addProperty(prop)

        # ふりがなは全角にして上書き
        phonetic_name = jaconv.h2z(card.getPropertyByName("X-PHONETIC-FIRST-NAME").value.decode())
        phonetic_prop = vcflib.Property("X-PHONETIC-FIRST-NAME", {}, phonetic_name.encode())
        newcard.addProperty(phonetic_prop, True)

        newcards.append(newcard)

    writer = vcflib.VCardWriter()
    writer.writeFile(f"{filepath}_.vcf", newcards)
    


if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("Ctrl+C")
        exit(0)
