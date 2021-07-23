#
# VCFフォーマット解析
#
import sys
from vcflib.VCardFileReader import VCardFileReader

def main(args):
    reader = VCardFileReader()
    filename = "resources/v2_1.vcf"
    cards = reader.parseFile(filename)

    for card in cards:
        print("\n".join(list(map(lambda prop: str(prop), card.properties))))
        print()


if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("Ctrl+C")
        exit(0)
