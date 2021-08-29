#
# Propertyクラステスト
#
from unittest import TestCase
from src.vcflib.properties.Property import Property
from termdecorator import termdecorate

class testProperty(TestCase):

    # 単純なインスタンス生成 (unfailable)
    @termdecorate
    def testGenerateInstance(self):
        prop = Property()
        print(prop)

    

