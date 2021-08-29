#
# Parameterクラステスト
#
from src.vcflib.parameters.TypeParameter import TypeParameter
from src.vcflib.parameters.PrefParameter import PrefParameter
from unittest import TestCase
from termdecorator import termdecorate

class testParameter(TestCase):

    # 単純なインスタンス生成 (unfailable)
    @termdecorate
    def testGenerateInstance(self):
        pref_param = PrefParameter(100)
        print(pref_param)
        type_param = TypeParameter(["WORK", "PREF"])
        print(type_param)


    

