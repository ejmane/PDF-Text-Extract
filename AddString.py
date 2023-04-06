import re
chapter_to_get = 1#input("Input the chapter you want: ")
output = "asdfjas;lfjals1.1lkasjdf;lajsfl;k1.2lkasjdf;lajs 1.2asfdsafkjaslfj1.3lsajfl;kjasdl;fj1.4"

def remove_questions(text):
    filtered_lines = [line for line in text.split('\n') if ')' not in line]
    result = '\n'.join(filtered_lines)
    return result

def check_section(section_to_check):
    if str(section_to_check) in output:
        return True
    else:
        return False

def section_check(chapter):
    i = 1
    sections_in_chapter = []
    while(True):
        if check_section(str(chapter) + "." + str(i)):
            sections_in_chapter.append(str(chapter) + "." + str(i))
            i += 1
        else:
            return sections_in_chapter
            break

section_dictionary = {}
section_dictionary[1] = 12




#text = """This is line 1
#This is line 2 with a )
#This is line 3"""

text = """ Skill:  Recall
 Learning Obj.:  2-1 Distinguish between positive and normative statements.
 User2:  Qualitative
 3) Which is the best description of positive statements? Positive statements
 A) have been verified by appeal to factual evidence.
 B) form the basis of all normative arguments.
 C) are falsifiable in principle by appeal to factual evidence.
 D) are seldom employed in social sciences like economics.
 E) have no place in economics because economics deals only with value judgments.
 Answer:  C
 Diff: 2
 Topic:  2.1. positive and normative statements
 Skill:  Recall
 Learning Obj.:  2-1 Distinguish between positive and normative statements.
 User2:  Qualitative
  91Copyright � """



print(remove_questions(text))