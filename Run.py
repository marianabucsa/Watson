from whoosh.fields import Schema, TEXT

from ChatGpt import ChatGpt
from Index import Index
from MeasurePerformance import MeasurePerformance


class App:
    def __init__(self):
        self.dataset_path = r'C:\Users\Katy\Desktop\Master\Watson\dataset'
        self.index_path = 'index'
        self.schema = Schema(
            title=TEXT(stored=True),
            content=TEXT(stored=True),
        )
        self.language = 'english'

    def run(self):
        index = Index(self.dataset_path, self.schema, self.language, self.index_path)
        chat = ChatGpt("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", index)
        measure = MeasurePerformance("questions.txt", index, chat)
        while True:
            print("Menu:")
            print("1. Create index")
            print("2. Answer question with index")
            print("3. Answer question with ChatGpt")
            print("4. Top 10 with index")
            print("5. Top 10 with ChatGpt")
            print("6. Measure & Analyze")
            print("7. Exit")
            choice = input("Give a number :  ")
            if choice == "1":
                # index.create()
                break
            elif choice == "2":
                clue = input("Give clue: ")
                question = input("Give question: ")
                index.answer_question(clue, question)
            elif choice == "3":
                clue = input("Give clue: ")
                question = input("Give question: ")
                chat.answer_question(clue, question)
            elif choice == "4":
                clue = input("Give clue: ")
                question = input("Give question: ")
                print(index.get_top_titles(clue, question))
            elif choice == "5":
                clue = input("Give clue: ")
                question = input("Give question: ")
                print(chat.get_top_titles(clue, question))
            elif choice == "6":
                measure.print_results()
            elif choice == "7":
                break
            else:
                print("Invalid entry")
        return


if __name__ == "__main__":
    app = App()
    app.run()
