
SETUP:
 - In order to compile and run the project, you must install Pycharm and to clone the project into your computer
 - For installing the required libraries, the following commands need to be run in the terminal:
       - pip install whoosh
       - pip install nltk
       - pip install openai
   !! IF you have problems using openai API you should run: openai migrate !!
 - From the openai site https://platform.openai.com/api-keys, generate a key and incorporated in the Run.py file at line 20
 - Before starting the applications, extract the files from "wiki-subset-20140602.tar", select the ones who don't start with dot :) and put them into a folder called "dataset" in the root of the project

RUN:
 - To start the app, run the file: Run.py
 - This will open the menu with the following options:
   1. Create index
   2. Answer question with index
   3. Answer question with ChatGpt
   4. Top 10 with index
   5. Top 10 with ChatGpt
   6. Measure & Analyze
   7. Exit
- You need to choose the first option and create the index before being able to run another commands
- After the index is created, you can run one of the other commands
- For the 6th options, a dataset in required. You can add this by creating a file called "questions.txt" in the root of the project. The file format should look be as followers:
    question
    clue
    answer
    newline

Option 1: Generates the index
Option 2: Takes as input the clue and the question and prints, with the use of the index, the title of one of the pages as an answer to the question 
Option 3: Takes as input the clue and the question and prints, with the use of the CHATGPT API, the title of one of the pages as an answer to the question 
Option 4: Takes as input the clue and the question and prints, with the use of the index, the first 10 titles as an answer to the question 
Option 5: Takes as input the clue and the question and prints, with the use of the CHATGPT, the first 10 titles as an answer to the question 
Option 6: Takes as input the file "questions.txt", generates answers for those questions and measures the performances using the correct answers from the file
Option 7: Exit
