# -*- coding: utf-8 -*-
# @Time : 2022/10/14 14:47
# @Author : Wang Hai
# @Email : nicewanghai@163.com
# @Code Specification : PEP8
# @File : trans.py
# @Project : NJX
from translate import Translator
translator = Translator(from_lang="chinese",to_lang="english")
translation = translator.translate("你吃了吗？")
print(translation)
translator2 = Translator(from_lang="english",to_lang="chinese")
translation = translator2.translate("Did you eat？")
print(translation)

