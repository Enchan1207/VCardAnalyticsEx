#
# VCFフォーマット解析
#
import sys
from vcflib.properties.Property import Property
from vcflib.VCardWriter import VCardWriter
from vcflib.properties.FullNameProperty import FullNameProperty
from vcflib.VCard import VCard
from vcflib.properties.NameProperty import NameProperty

from datetime import datetime

def main(args):
    vcard = VCard()
    vcard.addProperty(FullNameProperty("Steven Paul Jobs")) \
        .addProperty(NameProperty("Steven", "Jobs", "Paul")) \
        .addProperty(Property("ADR", {}, "1 Apple Park Way\, Cupertino\, CA".encode()))

    writer = VCardWriter()
    writer.writeFile("jobs.vcf", vcard)


if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("Ctrl+C")
        exit(0)
