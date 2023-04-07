# PDF-Text-Extract
Extracts Questions and answers from a multiple choice pdf

"Extracting Text From PDFs.py" asks the user for the amount of pages to load
and number of questions to output, then extracts the questions. The pages
loaded need to have one the question following the one inputed.

"Get Section names & pages.py" loads the pages one chapters one at a time
and grabs the sections within the chapters along with the pages.

"Get Question from sections.py" Takes the sections and page numbers and gets 
the number of questions in the chapter. Then extracts the questions in each
section and saves them to "Chapter-Questions.txt" seperated by section
