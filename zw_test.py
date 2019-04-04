from docx import Document
from collections import OrderedDict
import re
import pdb

def detect_chinese(stringA):
    chinese_characters = []
    for character in stringA:
        if character > u'\u4e00' and character < u'\u9fff':
            chinese_characters.append(character)
    return chinese_characters

def load_dict(filename):
    document = Document(filename)
    chinese_dict = OrderedDict()
    for num, para in enumerate(document.paragraphs):
        # pdb.set_trace()
        if para == "":
            continue
        chinese, ipa = re.split('\s+',para.text.strip())
        chinese_dict[chinese]=ipa
    return chinese_dict
def chinese_to_ipa(chinese_list, chinese_dict):
    ipa_list = []
    for chinese_char in chinese_list:
        try:
            ipa = chinese_dict[chinese_char]
            ipa_list.append(ipa)
        except KeyError:
            print("not found {}".format(chinese_char))
    return ipa_list
if __name__ == '__main__':
    chinese_dict=load_dict('./dict.docx')
    chinese_sentence = input('Enter your name:')
    chinese_list = detect_chinese(chinese_sentence)
    # print(chinese_list)
    ipa_list = chinese_to_ipa(chinese_list,chinese_dict)
    print(ipa_list)