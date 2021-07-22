#
# VCFフォーマット解析
#
import sys
from vcflib.VCardFileReader import VCardFileReader

def main(args):
    reader = VCardFileReader()
    filename = "resources/v2_1.vcf"
    cards = reader.parseFile(filename)

    card = cards[0]


if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("Ctrl+C")
        exit(0)
