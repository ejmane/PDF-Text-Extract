import PyPDF2
import re

file_name = "Chapter-Questions"

# Opens the correct file
pdfFileObj = open('Econ Master Doc (1).pdf', 'rb')

# Reads the file
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Creates a dictionary of the page number for each section
section_to_page_number = {
'1.1 ': 1, '1.2 ': 63, '1.3 ': 77, 
'2.1 ': 89, '2.2 ': 96, '2.3 ': 115, '2.4 ': 151,
'3.1 ': 180, '3.2 ': 214, '3.3 ': 229,
'4.1 ': 286, '4.2 ': 346, '4.3 ': 357, '4.4 ': 369,
'5.1 ': 395, '5.2 ': 438, '5.3 ': 449,
'6.1 ': 473, '6.2 ': 506, '6.3 ': 523, '6A-1 ': 542, '6A-2 ': 547, '6A-3 ': 555, '6A-4 ':558, '6A-5 ': 565, 
'7.1 ': 567, '7.2 ': 579, '7.3 ': 600, '7.4 ': 627,
'8.1 ': 667, '8.2 ': 730, '8A-1 ': 739, '8A-2 ': 743,
'9.1 ': 761, '9.2 ': 764, '9.3 ': 790, '9.4 ': 840,
'10.1 ': 862, '10.2 ': 921, '10.3 ': 926,
'11.1 ': 949, '11.2 ': 964, '11.3 ': 1001, '11.4 ': 1017,
'12.1 ': 1032, '12.2 ': 1082, '12.3 ': 1111,
'13.1 ': 1117, '13.2 ': 1170, '13.3 ': 1178,
'14.1 ': 1202, '14.2 ': 1261, '14.3 ': 1268,
'15.1 ': 1279, '15.2 ': 1283, '15.3 ': 1304, '15.4 ': 1331, '15.5 ': 1337,
'16.1 ': 1350, '16.2 ': 1352, '16.3 ': 1361, '16.4 ': 1416, '16.5 ': 1420,
'17.1 ': 1429, '17.2 ': 1473, '17.3 ': 1512,
'18.1 ': 1517, '18.2 ': 1549, '18.3 ': 1573, '18.4 ': 1594,
'19.1 ': 1595, '19.2 ': 1667,
'20.1 ': 1667, '20.2 ': 1678, '20.3 ': 1720,
'21.1 ': 1746, '21.2 ': 1799, '21.3 ': 1819,
'22.1 ': 1853, '22.2 ': 1864, '22.3 ': 1884, '22.4 ': 1921, '22.5 ': 1945,
'23.1 ': 1947, '23.2 ': 1987, '23.3 ': 2010,
'24.1 ': 2044, '24.2 ': 2080, '24.3 ': 2110,
'25.1 ': 2141, '25.2 ': 2165, '25.3 ': 2220, '25.4 ': 2229,
'26.1 ': 2231, '26.2 ': 2248, '26.3 ': 2270, '26.4 ': 2302,
'27.1 ': 2308, '27.2 ': 2328, '27.3 ': 2346, '27.4 ': 2384,
'28.1 ': 2398, '28.2 ': 2440, '28.3 ': 2462, '28.4 ': 2466,
'29.1 ': 2473, '29.2 ': 2499, '29.3 ': 2539,
'30.1 ': 2559, '30.2 ': 2580, '30.3 ': 2601, '30.4 ': 2631,
'31.1 ': 2640, '31.2 ': 2664, '31.3 ': 2697, '31.4 ': 2713,
'32.1 ': 2722, '32.2 ': 2783,
'33.1 ': 2811, '33.2 ': 2826, '33.3 ': 2879,
'34.1 ': 2893, '34.2 ': 2919, '34.3 ': 2954, '34.4 ': 2975, '35 ': 2997}

# Creates a dictionary of the index number and the sections so that it can be iterated through a for loop
sections = {
1:'1.1 ', 2:'1.2 ', 3:'1.3 ',
4:'2.1 ', 5:'2.2 ', 6:'2.3 ', 7:'2.4 ',
8:'3.1 ', 9:'3.2 ', 10:'3.3 ',
11:'4.1 ', 12:'4.2 ', 13:'4.3 ', 14:'4.4 ',
15:'5.1 ', 16:'5.2 ', 17:'5.3 ',
18:'6.1 ', 19:'6.2 ', 20:'6.3 ',
21:'6A-1 ', 22:'6A-2 ', 23:'6A-3 ', 24:'6A-4 ', 25:'6A-5 ',
26:'7.1 ',27:'7.2 ',28:'7.3 ',29:'7.4 ',
30:'8.1 ',31:'8.2 ',32:'8A-1 ', 33:'8A-2 ',
34:'9.1 ',35:'9.2 ',36:'9.3 ',37:'9.4 ',
38:'10.1 ',39:'10.2 ',40:'10.3 ',
41:'11.1 ',42:'11.2 ',43:'11.3 ',44:'11.4 ',
45:'12.1 ',46:'12.2 ',47:'12.3 ',
48:'13.1 ',49:'13.2 ',50:'13.3 ',
51:'14.1 ',52:'14.2 ',53:'14.3 ',
54:'15.1 ',55:'15.2 ',56:'15.3 ',57:'15.4 ',58:'15.5 ',
59:'16.1 ',60:'16.2 ',61:'16.3 ',62:'16.4 ',63:'16.5 ',
64:'17.1 ',65:'17.2 ',66:'17.3 ',
67:'18.1 ',68:'18.2 ',69:'18.3 ',70:'18.4 ',
71:'19.1 ',72:'19.2 ',
73:'20.1 ',74:'20.2 ',75:'20.3 ',
76:'21.1 ',77:'21.2 ',78:'21.3 ',
79:'22.1 ',80:'22.2 ',81:'22.3 ',82:'22.4 ',83:'22.5 ',
84:'23.1 ',85:'23.2 ',86:'23.3 ',
87:'24.1 ',88:'24.2 ',89:'24.3 ',
90:'25.1 ',91:'25.2 ',92:'25.3 ',93:'25.4 ',
94:'26.1 ',95:'26.2 ',96:'26.3 ',97:'26.4 ',
98:'27.1 ',99:'27.2 ',100:'27.3 ',101:'27.4 ',
102:'28.1 ',103:'28.2 ',104:'28.3 ',105:'28.4 ',
106:'29.1 ',107:'29.2 ',108:'29.3 ',
109:'30.1 ',110:'30.2 ',111:'30.3 ',112:'30.4 ',
113:'31.1 ',114:'31.2 ',115:'31.3 ',116:'31.4 ',
117:'32.1 ',118:'32.2 ',
119:'33.1 ',120:'33.2 ',121:'33.3 ',
122:'34.1 ',123:'34.2 ',124:'34.3 ',125:'34.4 ', 126: '35 '}

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

# get_pages takes the start and end page numbers and outputs the text from those pages
def get_pages(start, end):
    output = ""
    for i in range(start, end + 1):
        output = str(output) + str(pdfReader.getPage(i).extractText())
        output = re.sub(r"\d+Copyright\s.\s+\s*2017 Pearson Education, Inc\.", "", output, flags=re.MULTILINE)
    return output

# Get section page takes the index number for the sections and outputs the section page numbers
def get_section_page(number):
    return section_to_page_number[sections[number]]

# Question count takes the output and counts the number of questions in the section (output)
def question_count(output):
    # Filters out the answers and extra part from questions
    filtered_lines = [line for line in output.split('\n') if ' A) ' not in line and ' B) ' not in line and ' C) ' not in line and ' D) ' not in line and ' E) ' not in line and 'Answer: ' not in line and 'Diff' not in line]
    output = '\n'.join(filtered_lines)
    i = 1
    # Loops through the output and counts the number of questions
    while(True):
        if str(str(i) + ")") in output:
            i += 1
        else:
            return i-1

# Scrape section takes the active section and scrapes the questions and answers
def scrape_section(active_section):
    # Get the start and end page numbers for the section
    section_start = get_section_page(active_section)
    section_end = get_section_page(active_section + 1)

    # Sets the output to the text from the section
    output = get_pages(section_start, section_end)

    # Removes spillover from previous section and ensures the first question is 1)
    output = "1) " + output.split(sections[active_section], 1)[1].split("1) ", 1)[1]

    # Corrects error in spreadsheet
    if sections[active_section] == "22.1 ":
        output = output.replace("Cthrough", "C) through")
    
    # Gets the list of questions
    question_list = output_to_list(output, question_count(output))

    # Outputs the questions to Chapter-questions.txt in the correct format
    output_questions(question_list, sections[active_section])

# Output_to_list takes the output and question count and returns a list of questions
def output_to_list(output, question_count):
    questions = []
    # Splits the output into a list of questions
    for i in range(question_count + 1):
        questions.append(output.split("User2: ")[i])
    return questions

# output_questions takes the question, possible answers, correct answer, and adds prints them to Chapter-questions.txt
def output_questions(questions, section):
    for i in range(len(questions) - 1):
        answer = {}
        # Gets the question from questions[i] and prints it + stores it in question
        question = questions[i].split(str(i + 1) + ") ", 1)[1].split("A) ")[0]
        question = ''.join(question.splitlines())
        print(question)

        # Gets the answer from questions[i] and prints it + stores it in answer["A"]
        answer["A"] = "A) " + questions[i].split("A) ", 1)[1].split("B) ", 1)[0]
        answer["A"] = ''.join(answer["A"].splitlines())
        print(answer["A"])

        # Gets the answer from questions[i] and prints it + stores it in answer["B"]
        answer["B"] = "B) " + questions[i].split("B) ", 1)[1].split("C) ", 1)[0]
        answer["B"] = ''.join(answer["B"].splitlines())
        print(answer["B"])

        # Gets the answer from questions[i] and prints it + stores it in answer["C"]
        answer["C"] = "C) " + questions[i].split("C) ", 1)[1].split("D) ", 1)[0]
        answer["C"] = ''.join(answer["C"].splitlines())
        print(answer["C"])

        # Gets the answer from questions[i] and prints it + stores it in answer["D"]
        answer["D"] = "D) " + questions[i].split("D) ", 1)[1].split("E) ", 1)[0]
        answer["D"] = ''.join(answer["D"].splitlines())
        print(answer["D"])

        # Gets the answer from questions[i] and prints it + stores it in answer["E"]
        try:
            answer["E"] = "E) " + questions[i].split("E) ", 1)[1].split("Answer: ", 1)[0]
            answer["E"] = ''.join(answer["E"].splitlines())
            print(answer["E"])
        except:
            answer["E"] = ""
            print("E) " + answer["E"])

        # Gets the correct answer from questions[i] and prints it + stores it in correct_answer
        correct_letter = str(questions[i].split("Answer: ", 1)[1].split("Diff: ", 1)[0]).strip()
        correct_letter = ''.join(correct_letter.splitlines())
        correct_letter = correct_letter[:1]
        correct_answer = answer[correct_letter]
        print("Correct Answer: " + correct_answer + "\n")
        
        # Adds the question, answers, and correct answer to Chapter-questions.txt
        add_to_txt(str(question + answer["A"] + answer["B"] + answer["C"] + answer["D"] + answer["E"]).strip(), "\t" + correct_answer + "\t" + section, file_name)

# Loops through the sections and scrapes the questions and answers
for i in range(1, len(sections)):
    add_to_txt("\n" + "Section: " + str(sections[i]) + "\n", "", file_name)
    scrape_section(i)
