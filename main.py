#
# VCFフォーマット解析
#
from os import write
import sys, jaconv
from vcflib.VCardWriter import VCardWriter
from vcflib.PropertyEncoder import PropertyEncoder
from vcflib.VCardReader import VCardReader

def main(args):
    reader = VCardReader()
    filename = args[1] if len(args) > 1 else "resources/v2_1.vcf"
    cards = reader.parseFile(filename)

    writer = VCardWriter()
    writer.writeFile("test.vcf", cards)


if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("Ctrl+C")
        exit(0)
