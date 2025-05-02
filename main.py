# main.py
from tkinter import Tk
from quiz_data import quiz_questions, correct_answers
from quiz_logic import QuizLogic
from quiz_gui import QuizGUI

def main():
    root = Tk()
    quiz = QuizLogic(quiz_questions, correct_answers)
    app = QuizGUI(root, quiz)
    root.mainloop()

if __name__ == "__main__":
    main()