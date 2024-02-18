import os
import re
import shutil
import time

import nltk
from tqdm import tqdm
from whoosh import index
from whoosh.qparser import QueryParser
from whoosh.query import Or


class Index:
    def __init__(self, input_path, schema, stop_words_language, output_path):
        self.__input_path = input_path
        self.__schema = schema
        self.__text_processor = TextProcessor(stop_words_language)
        self.__output_path = output_path
        self.__query_parser = None
        self.__index = None
        try:
            if os.path.exists(self.__output_path):
                self.__index = index.open_dir(self.__output_path)
                self.__query_parser = QueryParser("content", schema=self.__schema)
        finally:
            print("Please create an index before any other action.")

    def create(self):
        self.__create_index_dir()  # create directory for index
        our_index = index.create_in(self.__output_path, self.__schema)  # create index object
        with our_index.writer() as file_writer:  # create writer
            with tqdm(total=80) as pbar:
                for file_name in os.listdir(self.__input_path):
                    file_path = os.path.join(self.__input_path, file_name)
                    titles_information = self.__get_data(file_path)
                    for title_information in titles_information:
                        file_writer.add_document(title=title_information[0], content=title_information[1])
                    time.sleep(0.1)
                    pbar.update(1)
        our_index.close()

    def answer_question(self, clue, question):
        if self.__index is None:
            print("An index does not exist. Please create one before any other action.")
            return
        query = Or(self.__parse_information(clue) + self.__parse_information(question))

        with self.__index.searcher() as searcher:
            results = searcher.search(query)
            top_page = results[0]["title"]
            print(f"Top page: {top_page}")
            return top_page

    def get_top_titles(self, clue, question, nr_pages=10):
        if self.__index is None:
            print("An index does not exist. Please create one before any other action.")
            return
        query = Or(self.__parse_information(clue) + self.__parse_information(question))

        with self.__index.searcher() as searcher:
            results = searcher.search(query)
            return [page["title"] for page in results[:nr_pages]]

    def __parse_information(self, information):
        tokens = self.__text_processor.process_content_answer(information)
        parsed_tokens = []
        for token in tokens:
            parsed_tokens.append(self.__query_parser.parse(token))
        return parsed_tokens

    def __create_index_dir(self):
        if os.path.exists(self.__output_path):
            shutil.rmtree(self.__output_path)
        os.makedirs(self.__output_path)

    def __get_data(self, file_path):
        pages_titles, pages_information = [], []
        with open(file_path, 'r', encoding="utf-8") as file:
            file_content = file.read()
        pages_titles += re.findall(r'\n*\[\[(.*?)\]\]\n',
                                   file_content)  # get all titles that are on a new line , starting with [[ and ending with ]]
        pages_information += re.split(r'\n*\[\[(.*?)\]\]\n', file_content)[
                             ::2]  # split file by title and get only the content
        pages_information.pop(0)
        processed_information = self.__process_information(pages_information)
        titles_information = []
        for i in range(len(processed_information)):
            titles_information.append([pages_titles[i], processed_information[i]])
        return titles_information

    def __process_information(self, pages_information):
        processed_information = []
        for page_info in pages_information:
            processed_information.append(self.__text_processor.process_content(page_info))
        return processed_information


class TextProcessor:
    def __init__(self, stop_words_language):
        self.__porter_stemmer = nltk.PorterStemmer()
        self.__stop_words = nltk.corpus.stopwords.words(stop_words_language)

    def tokenize(self, text):
        return nltk.word_tokenize(text)

    def post_process(self, tokens):
        stemmed_tokens = []
        for word in tokens:
            if word.isalnum() and word.lower() not in self.__stop_words:
                stemmed_tokens.append(self.__porter_stemmer.stem(word))
        return stemmed_tokens

    def process_content(self, content):
        tokens = self.tokenize(content)
        stemmed_tokens = self.post_process(tokens)
        return " ".join([token for token in stemmed_tokens])

    def process_content_answer(self, content):
        tokens = self.tokenize(content)
        return self.post_process(tokens)
