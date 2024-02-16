import openai
from openai import OpenAIError


class ChatGpt:
    def __init__(self, api_key, index):
        self.__api_key = api_key
        self.__index = index

    def answer_question(self, clue, question):
        top_titles_index = self.__index.get_top_titles(clue, question)
        request_body = self.__construct_request(clue, question, top_titles_index)
        response_body = self.__send_request(request_body)
        response = self.__decode_response(response_body)
        print(response[0])
        return response[0]

    def get_top_titles(self, clue, question, nr_pages=10):
        top_titles_index = self.__index.get_top_titles(clue, question, nr_pages)
        request_body = self.__construct_request(clue, question, top_titles_index)
        response_body = self.__send_request(request_body)
        response = self.__decode_response(response_body)
        print(response[:10])

    def __construct_request(self, clue, question, titles):
        request = [{"role": "system", "content": "You are a helpful assistant."},
                   {"role": "user", "content": f"clue: {clue} question: {question}"},
                   {"role": "user", "content": "titles form wikipedia pages:"}]
        for title in titles:
            request.append({"role": "user", "content": f"{title}"})
        request.append(
            {"role": "user", "content": "Rerank the titles based on the provided clue and question. Do not write any other text except the title"})
        return request

    def __send_request(self, request_body):
        openai.api_key = self.__api_key
        tries = 0
        while tries < 2:
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=request_body
                )
                return response
            except OpenAIError as e:
                print(f"Error: {e}")
                tries += 1
                print("Retrying connection")

    def __decode_response(self, response_body):
        titles = response_body.choices[0].message['content']
        lines = titles.split('\n')
        response = []
        for line in lines:
            if '. ' in line:
                _, title = line.split('. ', 1)
                response.append(title)
            elif line.strip():
                response.append(line.strip())
        return response
