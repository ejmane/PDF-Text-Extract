import PyPDF2
import re

file_name = "Chapter-Questions"

# Opens the correct file
pdfFileObj = open('Econ Master Doc (1).pdf', 'rb')

# Reads the file
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

section_to_page_number = {
'1.1 ': 1, '1.2 ': 63, '1.3 ': 77, 
'2.1 ': 89, '2.2 ': 96, '2.3 ': 115, '2.4 ': 151,
'3.1 ': 180, '3.2 ': 214, '3.3 ': 229,
'4.1 ': 286, '4.2 ': 346, '4.3 ': 357, '4.4 ': 369,
'5.1 ': 395, '5.2 ': 438, '5.3 ': 449,
'6.1 ': 473, '6.2 ': 506, '6.3 ': 523,
'7.1 ': 567, '7.2 ': 579, '7.3 ': 600, '7.4 ': 627,
'8.1 ': 667, '8.2 ': 730,
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
'34.1 ': 2893, '34.2 ': 2919, '34.3 ': 2954, '34.4 ': 2975}

sections = {
1:'1.1 ', 2:'1.2 ', 3:'1.3 ',
4:'2.1 ', 5:'2.2 ', 6:'2.3 ', 7:'2.4 ',
8:'3.1 ', 9:'3.2 ', 10:'3.3 ',
11:'4.1 ', 12:'4.2 ', 13:'4.3 ', 14:'4.4 ',
15:'5.1 ', 16:'5.2 ', 17:'5.3 ',
18:'6.1 ', 19:'6.2 ', 20:'6.3 ',
21:'7.1 ', 22:'7.2 ', 23:'7.3 ', 24:'7.4 ',
25:'8.1 ', 26:'8.2 ', 
27:'9.1 ', 28:'9.2 ', 29:'9.3 ', 30:'9.4 ',
31:'10.1 ', 32:'10.2 ', 33:'10.3 ',
34:'11.1 ', 35:'11.2 ', 36:'11.3 ', 37:'11.4 ',
38:'12.1 ', 39:'12.2 ', 40:'12.3 ',
41:'13.1 ', 42:'13.2 ', 43:'13.3 ',
44:'14.1 ', 45:'14.2 ', 46:'14.3 ',
47:'15.1 ', 48:'15.2 ', 49:'15.3 ', 50:'15.4 ', 51:'15.5 ',
52:'16.1 ', 53:'16.2 ', 54:'16.3 ', 55:'16.4 ', 56:'16.5 ',
57:'17.1 ', 58:'17.2 ', 59:'17.3 ',
60:'18.1 ', 61:'18.2 ', 62:'18.3 ', 63:'18.4 ',
64:'19.1 ', 65:'19.2 ', 
66:'20.1 ', 67:'20.2 ', 68:'20.3 ',
69:'21.1 ', 70:'21.2 ', 71:'21.3 ', 
72:'22.1 ',73:'22.2 ', 74:'22.3 ', 75:'22.4 ', 76:'22.5 ',
77:'23.1 ', 78:'23.2 ', 79:'23.3 ',
80:'24.1 ', 81:'24.2 ', 82:'24.3 ',
83:'25.1 ', 84:'25.2 ', 85:'25.3 ', 86:'25.4 ',
87:'26.1 ', 88:'26.2 ', 89:'26.3 ', 90:'26.4 ',
91:'27.1 ', 92:'27.2 ', 93:'27.3 ', 94:'27.4 ',
95:'28.1 ', 96:'28.2 ', 97:'28.3 ', 98:'28.4 ',
99:'29.1 ', 100:'29.2 ', 101:'29.3 ',
102:'30.1 ', 103:'30.2 ', 104:'30.3 ', 105:'30.4 ',
106:'31.1 ', 107:'31.2 ', 108:'31.3 ', 109:'31.4 ',
110:'32.1 ', 111:'32.2 ',
112:'33.1 ', 113:'33.2 ', 114:'33.3 ',
115:'34.1 ', 116:'34.2 ', 117:'34.3 ', 118:'34.4 '
}

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
        print(str(i) + ")" + Question1)

        # Get option A
        AnswerA = str("A) " + Question.split("A) ")[1].split("B) ")[0].strip())
        AnswerA = ''.join(AnswerA.splitlines())
        print(AnswerA)

        # Get option B
        AnswerB = str("B) " + Question.split("B) ")[1].split("C) ")[0].strip())
        AnswerB= ''.join(AnswerB.splitlines())
        print(AnswerB)

        # Get option C
        AnswerC = str("C) " + Question.split("C) ")[1].split("D) ")[0].strip())
        AnswerC = ''.join(AnswerC.splitlines())
        print(AnswerC)

        # Get get option D
        AnswerD = str("D) " + Question.split("D) ")[1].split("E) ")[0].strip())
        AnswerD = ''.join(AnswerD.splitlines())
        print(AnswerD)

        # Get get option E
        AnswerE = str("E) " + Question.split("E) ")[1].split("Answer: ")[0].strip())
        AnswerE = ''.join(AnswerE.splitlines())
        print(AnswerE)

        # Get the correct answer
        Correct_Answer = Question.split("Answer:")[1].split("Diff")[0].strip()
        Correct_Answer = ''.join(Correct_Answer.splitlines())
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
        Answer_text = ''.join(Answer_text.splitlines())
        print(Answer_text)
        add_to_txt(str(Question1 + AnswerA + AnswerB + AnswerC + AnswerD + AnswerE).strip(), "\t" + Answer_text, file_name)

def get_pages(start, end):
    output = ""
    for i in range(start, end + 1):
        output = str(output) + str(pdfReader.getPage(i).extractText())#.replace("2017 Pearson Education, Inc.", ""))
        output = re.sub(r"\d+Copyright\s.\s+\s*2017 Pearson Education, Inc\.", "", output, flags=re.MULTILINE)
    return output

def get_section_page(number):
    return section_to_page_number[sections[number]]

active_section = 1
def scrape_section():
    section_start = get_section_page(active_section)
    section_end = get_section_page(active_section + 1)
    output = get_pages(section_start, section_end)
    questions = get_questions(90, output)
    #add_to_txt(str(questions), "", file_name)
    #print(output)
    #add_to_txt(output, "", file_name)


scrape_section()