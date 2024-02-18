<!DOCTYPE html>
<html lang="en">
<body>
    <h1>Setup Instructions:</h1>
    In order to compile and run the project, you must install Pycharm and clone the project into your computer.<br>
    For installing the required libraries, the following commands need to be run in the terminal:<br>
 <ul>
    <li><code>pip install whoosh</code></li>
    <li><code>pip install nltk</code></li>
    <li><code>pip install openai</code></li>
 </ul>
    If you have problems using OpenAI API, you should run: <code>openai migrate</code><br>
    From the OpenAI site <a href="https://platform.openai.com/api-keys">https://platform.openai.com/api-keys</a>, generate a key and incorporate it into the <code>Run.py</code> file at line 20.<br>
    Before starting the application, extract the files from "wiki-subset-20140602.tar", select the ones that don't start with a dot and put them into a folder called "dataset" in the root of the project.<br>
    <h1>Run Instructions:</h1>
    To start the app, run the file: <code>Run.py</code>.<br>
    This will open the menu with the following options:<br>
 <ul>
    <li>Option 1: Create index</li>
    <li>Option 2: Answer question with index</li>
    <li>Option 3: Answer question with ChatGpt</li>
    <li>Option 4: Top 10 with index</li>
    <li>Option 5: Top 10 with ChatGpt</li>
    <li>Option 6: Measure & Analyze</li>
    <li>Option 7: Exit</li>
 </ul>
    You need to choose the first option and create the index before being able to run another commands.<br>
    After the index is created, you can run one of the other commands.<br>
    For the 6th option, a dataset is required. You can add this by creating a file called <code>questions.txt</code> in the root of the project. The file format should be as follows:<br>
    <pre>
        question<br>
        clue<br>
        answer<br>
        newline</pre>
 <ul>
    <li>Option 1: Generates the index.</li>
    <li>Option 2: Takes as input the clue and the question and prints, with the use of the index, the title of one of the pages as an answer to the question.</li>
    <li>Option 3: Takes as input the clue and the question and prints, with the use of the CHATGPT API, the title of one of the pages as an answer to the question.</li>
    <li>Option 4: Takes as input the clue and the question and prints, with the use of the index, the first 10 titles as an answer to the question.</li>
    <li>Option 5: Takes as input the clue and the question and prints, with the use of CHATGPT, the first 10 titles as an answer to the question.</li>
    <li>Option 6: Takes as input the file <code>questions.txt</code>, generates answers for those questions, and measures the performances using the correct answers from the file.</li>
    <li>Option 7: Exit.</li>
</body>
</html>

