import PyPDF2

# Opens the correct file
pdfFileObj = open('Econ Master Doc (1).pdf', 'rb')

# Reads the file
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


# chapter_dictionary is chapter: page number
chapter_dictionary = {
    1:1, 
    2:89, 
    3:180,
    4:286,
    5:395,
    6:473,
    7:567,
    8:667,
    9:762,
    10:862,
    11:949,
    12:1032,
    13:1117,
    14:1202,
    15:1279,
    16:1350,
    17:1429,
    18:1517,
    19:1595,
    20:1667,
    21:1746,
    22:1853,
    23:1947,
    24:2044,
    25:2141,
    26:2231,
    27:2308,
    28:2398,
    29:2473,
    30:2559,
    31:2640,
    32:2722,
    33:2811,
    34:2893,
    35:2997,
}


file_name = "Answer_bank2"

# Adds input1 and input 2 to file_name
def add_to_txt(input, input2, file_name):
    # Open the file in append & read mode ('a+')
    with open(file_name + ".txt", "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(input)
        file_object.write("\t" + input2)

# Sets ouput to the pages from start to end
def get_pages(start, end):
    output = ""
    for i in range(start, end + 1):
        output = output + pdfReader.getPage(i).extractText().replace("2017 Pearson Education, Inc.", "\n" + str("PAGE NUMBER:" + str(i)) + " ***" + str(i + 1) + " on doc***" + " ================" + "\n")
    return output

# Gets the questions from the output and output them in format for excel
def get_questions(question_end, output):
    for i in range(1, question_end + 1): 
        if i == 1:
            Question = output.split(str(i + 1) + ")")[0]
        else:
            Question = str(i) + ")" +output.split(str(i) + ")")[1].split(str(i+1)+")")[0]
        print("======================================== Question", i)
        
        # Get the question
        Question1 = Question.split(str(i) + ")")[1].split("A)")[0].strip()
        Question1 = ''.join(Question1.splitlines())
        print(str(i) + ")", Question1)

        # Get option A
        AnswerA = str("A) " + Question.split("A)")[1].split("B)")[0].strip())
        print(AnswerA)

        # Get option B
        AnswerB = str("B) " + Question.split("B)")[1].split("C)")[0].strip())
        print(AnswerB)

        # Get option C
        AnswerC = str("C) " + Question.split("C)")[1].split("D)")[0].strip())
        print(AnswerC)

        # Get get option D
        AnswerD = str("D) " + Question.split("D)")[1].split("E)")[0].strip())
        print(AnswerD)

        # Get get option E
        AnswerE = str("E) " + Question.split("E)")[1].split("Answer: ")[0].strip())
        print(AnswerE)

        # Get the correct answer
        Correct_Answer = Question.split("Answer:")[1].split("Diff")[0].strip()
        print("Correct answer is:", str(Correct_Answer))

        # Get the correct answer ad the option
        if Correct_Answer == "A":
            Answer_text = AnswerA
        elif Correct_Answer == "B":
            Answer_text = AnswerB
        elif Correct_Answer == "C":
            Answer_text = AnswerC
        elif Correct_Answer == "D":
            Answer_text = AnswerD
        elif Correct_Answer == "E":
            Answer_text = AnswerE
        print(Answer_text)
        add_to_txt(str(Question1 + AnswerA + AnswerB + AnswerC + AnswerD + AnswerE), Answer_text, file_name)

# Removes all the answers from the output
def remove_questions(text):
    filtered_lines = [line for line in text.split('\n') if ')' not in line and 'Topic: ' not in line and 'Learning Obj.:' not in line]
    return'\n'.join(filtered_lines)

    #filtered_lines = [line for line in text.split('\n') if ')' not in line]
    #result = '\n'.join(filtered_lines)
    #return result

# Return true if a section is in the chapter and false otherwise
def check_if_in_section(section_to_check, restricted_output):
    if str(section_to_check) in restricted_output:
        return True
    else:
        return False

#takes in a chapter and returns a list of sections in that chapter
def sections_in_chapter(chapter, restricted_output):
    i = 1
    sections_in_chapter = []
    while(True):
        if check_if_in_section(str(chapter) + "." + str(i) + " ", restricted_output):
            sections_in_chapter.append(str(chapter) + "." + str(i) + " ")
            i += 1
        else:
            return sections_in_chapter
            break

#takes in a list of sections and returns a list with the pages for each section
def get_section_pages(sections, restricted_output):
    pages = {}
    for i in sections:
        pages[i] = int(restricted_output.split(str(i))[1].split("PAGE NUMBER:")[1].split(" *")[0].strip())
        #print(pages)
    return pages


def return_section_pages(chapter_to_get):
    # Prompts the user to input the chapter they want
    #chapter_to_get = int(input("Input the chapter you want: "))

    # The page the requested chapter starts on (The start for output)
    start_of_chapter = int(chapter_dictionary[chapter_to_get]-1)

    # The page the requested chapter ends on (The end for output)
    end_of_chapter = int(chapter_dictionary[chapter_to_get + 1])

    # Sets output to the pages from start to end
    output = get_pages(start_of_chapter, end_of_chapter)

    # Removes all the answers from the output (For getting section pages)
    restricted_output = remove_questions(output)

    add_to_txt(output, "", file_name)
    
    return get_section_pages(sections_in_chapter(chapter_to_get, restricted_output), restricted_output)


    

for i in range(1, 35):
    print((return_section_pages(i)))

#chapter_to_get = int(input("Input the chapter you want: "))
#print(return_section_pages(chapter_to_get))