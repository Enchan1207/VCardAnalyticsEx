#
# VCFフォーマット解析
#
import sys
from vcflib.VCardWriter import VCardWriter
from vcflib.properties.FullNameProperty import FullNameProperty
from vcflib.VCard import VCard
from vcflib.properties.NicknameProperty import NicknameProperty
from vcflib.properties.NameProperty import NameProperty

def main(args):
    vcard = VCard()
    vcard.addProperty(FullNameProperty("Steven Paul Jobs")) \
        .addProperty(NameProperty("Steven", "Jobs", "Paul")) \
        .addProperty(NicknameProperty("Jobs", "work"))
    
    writer = VCardWriter()
    writer.writeFile("jobs.vcf", vcard)


if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("Ctrl+C")
        exit(0)
