import time

import docx
from behave import *

import oR
from Selenium_Operations.Element_Operations import Element_Operations

use_step_matcher("parse")


@given(u'User navigated to Bible and write data')
def step_impl(context):
    verse = 1
    chapter = 1
    while chapter <= 16:
        context.ele_ops = Element_Operations(context.driver)
        verse_str = str(verse)
        chapter_str = str(chapter)
        context.ele_ops.get_url("https://www.biblehub.com/mark/"+chapter_str+"-"+verse_str+".htm")
        context.ele_ops.maximize_window()
        bible_frame = context.ele_ops.find_element(oR.bible_frame__XPATH)
        context.ele_ops.switch_to_frame(bible_frame)
        # context.ele_ops.select_by_visible_text(oR.bible_Menu_1_dropdown__XPATH, "Gen")
        try:
            context.ele_ops.select_by_visible_text(oR.bible_Menu_2_dropdown__XPATH, str(chapter_str+":"+verse_str))
        except:
            verse = 1
            verse -= 1
            chapter += 1
        # context.ele_ops.click(oR.bible_Hebrew__XPATH)
        context.ele_ops.switch_to_default_content()
        # context.ele_ops.find_elements(oR.bible_text_verse__XPATH)
        verse_text = context.ele_ops.get_text_from_multiple_elements(oR.bible_text_verse__XPATH)
        verse_text.insert(0, chapter_str+":"+verse_str)
        mydoc = docx.Document("E://auto_frameworks//Behave_python//features//steps//mark.docx")
        mydoc.add_paragraph([ele+" " for ele in verse_text])
        mydoc.save("E://auto_frameworks//Behave_python//features//steps//mark.docx")
        verse += 1


