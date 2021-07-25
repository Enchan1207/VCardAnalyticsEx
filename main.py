#
# VCFフォーマット解析
#
import sys
from vcflib.properties.BirthdayProperty import BirthdayProperty
from vcflib.VCardWriter import VCardWriter
from vcflib.properties.FullNameProperty import FullNameProperty
from vcflib.VCard import VCard
from vcflib.properties.NicknameProperty import NicknameProperty
from vcflib.properties.NameProperty import NameProperty

from datetime import datetime

def main(args):
    vcard = VCard()
    vcard.addProperty(FullNameProperty("Steven Paul Jobs")) \
        .addProperty(NameProperty("Steven", "Jobs", "Paul")) \
        .addProperty(NicknameProperty("Jobs", "work")) \
        .addProperty(BirthdayProperty(datetime.now()))

    writer = VCardWriter()
    writer.writeFile("jobs.vcf", vcard)


if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("Ctrl+C")
        exit(0)
