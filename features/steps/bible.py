import time

import docx
from behave import *

import oR
from Selenium_Operations.Element_Operations import Element_Operations

use_step_matcher("parse")


# @given(u'User navigated to Bible')
# def step_impl(context):
#     context.ele_ops = Element_Operations(context.driver)
#     chapter = 1
#     verse = 1
#     book = "mark"
#     book_name = "Mark"
#     doc = docx.Document()
#     while chapter <= 3:
#         context.ele_ops.get_url("https://www.biblehub.com/" + book + "/" + str(chapter) + "-" + str(verse) + ".htm")
#         context.ele_ops.maximize_window()
#         # frame = context.ele_ops.find_element(oR.bible_frame__XPATH)
#         # context.ele_ops.switch_to_frame(frame)
#         # context.ele_ops.switch_to_default_content()
#         verses_text_list = context.ele_ops.get_text_from_multiple_elements(oR.bible_text_verse__XPATH)
#         verses_text_list.insert(0, str(chapter) + ":" + str(verse))
#         doc.add_paragraph([ele_text + " " for ele_text in verses_text_list])
#         doc.save("E://auto_frameworks//Behave_python//features//steps//mark.docx")
#         verse += 1

