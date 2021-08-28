#
# サンプル vCardの生成
#
from vcflib.properties.EmailAddressProperty import EmailAddressProperty
from vcflib.properties.PhoneNumberProperty import PhoneNumberProperty
from vcflib.properties.FullNameProperty import FullNameProperty
import vcflib

vcard = vcflib.VCard()

vcard.addProperty(FullNameProperty("Steve Jobs"))
    # .addProperty(PhoneNumberProperty("000-0000-1234", ['PREF', 'HOME'])) \
    # .addProperty(PhoneNumberProperty("000-0000-5678", ['PREF', 'WORK'])) \
    # .addProperty(EmailAddressProperty("info@apple.com", ['PREF']))

print(vcard)

