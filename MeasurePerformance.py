import time

from tqdm import tqdm


class Request:
    def __init__(self, question, clue, answer):
        self.question = question
        self.clue = clue
        self.answer = answer


class MeasurePerformance:
    def __init__(self, dataset_path, index, chat_gpt):
        self.__dataset_path = dataset_path
        self.__dataset = self.__get_dataset()
        self.__index = index
        self.__chat_gpt = chat_gpt

    def __get_results_chat(self):
        total_nr_questions = len(self.__dataset)
        correct_answers = 0
        incorrect_answers = 0
        mrr = 0
        with tqdm(total=total_nr_questions) as pbar:
            for request in self.__dataset:
                result = self.__chat_gpt.get_top_titles(request.clue, request.question)
                if result[0] == request.answer:
                    correct_answers += 1
                else:
                    incorrect_answers += 1
                if request.answer in result:
                    mrr += 1 / (result.index(request.answer) + 1)
                time.sleep(0.1)
                pbar.update(1)
        precision_at_one = correct_answers / total_nr_questions
        mean_reciprocal_rank = mrr / total_nr_questions
        print(f"ChatGpt P@1: {precision_at_one}")
        print(f"ChatGpt MRR: {mean_reciprocal_rank}")

    def __get_results_index(self):
        total_nr_questions = len(self.__dataset)
        correct_answers = 0
        incorrect_answers = 0
        mrr = 0
        with tqdm(total=total_nr_questions) as pbar:
            for request in self.__dataset:
                result = self.__index.get_top_titles(request.clue, request.question)
                if result[0] == request.answer:
                    correct_answers += 1
                else:
                    incorrect_answers += 1
                if request.answer in result:
                    mrr += 1 / (result.index(request.answer) + 1)
                time.sleep(0.1)
                pbar.update(1)

        precision_at_one = correct_answers / total_nr_questions
        mean_reciprocal_rank = mrr / total_nr_questions
        print(f"Index P@1: {precision_at_one}")
        print(f"Index MRR: {mean_reciprocal_rank}")

    def print_results(self):
        self.__get_results_index()
        # self.__get_results_chat()

    def __get_dataset(self):
        with open(self.__dataset_path, "r", encoding="utf-8") as file:
            content = file.readlines()

        questions = content[::4]
        clues = content[1::4]
        answers = content[2::4]
        dataset = []

        for i in range(len(questions)):
            request = Request(questions[i].strip(), clues[i].strip(), answers[i].strip())
            dataset.append(request)

        return dataset
