#
# VCFフォーマット解析
#
import sys, jaconv
from vcflib.PropertyEncoder import PropertyEncoder
from vcflib.VCardFileReader import VCardFileReader

def main(args):
    reader = VCardFileReader()
    filename = args[1] if len(args) > 1 else "resources/v2_1.vcf"
    cards = reader.parseFile(filename)

    for card in cards:
        for prop in card.properties:
            encoder = PropertyEncoder()
            enctype = ""
            if prop.name == "PHOTO":
                enctype = "b"
            print(encoder.encode(prop, enctype))
        
        print()


if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("Ctrl+C")
        exit(0)
