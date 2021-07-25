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
            name = prop.name
            value = prop.value
            try:
                value_decoded = prop.value.decode()
                if name.startswith("X-PHONETIC"):
                    value_decoded = jaconv.h2z(value_decoded)
            except UnicodeDecodeError:
                value_decoded = f"(binary: {len(value)} bytes)"
            
            print(f"{name}:{value_decoded}")
        
        print()


if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("Ctrl+C")
        exit(0)
