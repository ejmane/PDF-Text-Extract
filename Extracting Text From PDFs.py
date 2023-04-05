import PyPDF2
file_name = "Answer_bank"
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

def get_pages(page_end):
    output = ""
    for i in range(1, page_end + 1):
        output = output + pdfReader.getPage(i).extractText().replace(str(i + 1) + "Copyright © 2017 Pearson Education, Inc.", "")
    return output

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



pdfFileObj = open('Econ Master Doc (1).pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pages_to_get = int(input("Input how many pages you want to collect: "))
# Choose the number of pages to get
# Need to get the page with the question after the one you want
# So if you want Question 2 you need the page with Question 3 too.


Questions_to_get_to = int(input("Enter how many questions you would like to get: "))
# Chose the number of questions to get
# Need to have one question after the one you want, so ensure there are one too many on the pages
# So if you want question 2 make sure question 3 is on the same page

output = get_pages(pages_to_get)
get_questions(Questions_to_get_to, output)

#You are a professor preparing a university student for their EC140 final exam. You are going to give the student a multiple-choice economics question with 5 possible answers (a, b, c, d, e) and you tell them why they are correct or why they are wrong. Wait until the user responds before presenting a new question
