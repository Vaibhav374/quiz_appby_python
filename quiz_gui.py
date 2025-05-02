# quiz_gui.py
from tkinter import *

class QuizGUI:
    def __init__(self, root, quiz_logic):
        self.root = root
        self.quiz = quiz_logic
        self.setup_gui()
        
    def setup_gui(self):
        self.root.title("Python Quiz App")
        self.root.geometry("850x520")
        
        self.user_answer = StringVar()
        self.user_answer.set('None')
        
        # Header
        Label(self.root, text="Quiz App", 
              font="calibre 40 bold",
              relief=SUNKEN, background="cyan").pack(pady=10)
        
        # Start button
        self.start_button = Button(self.root, text="Start Quiz",
                                 command=self.start_quiz, 
                                 font="calibre 17 bold")
        self.start_button.pack(pady=20)
        
        # Question frame
        self.question_frame = Frame(self.root)
        self.question_frame.pack(fill=BOTH, expand=True)
        
        # Next button
        self.next_button = Button(self.root, text="Next Question",
                                 command=self.next_question,
                                 font="calibre 17 bold")
        
        # Score display
        self.score_var = StringVar()
        Label(self.root, textvariable=self.score_var, 
             font="calibre 14 bold").pack(side=BOTTOM, pady=10)
    
    def start_quiz(self):
        self.start_button.forget()
        self.next_button.pack()
        self.show_question()
    
    def show_question(self):
        self.clear_frame()
        question_text, options = self.quiz.get_current_question()
        
        Label(self.question_frame, text=question_text, 
             font="calibre 12 normal").pack(pady=10)
        
        for option in options:
            Radiobutton(self.question_frame, text=option,
                       variable=self.user_answer,
                       value=option).pack(anchor='w', padx=20)
    
    def next_question(self):
        self.quiz.check_answer(self.user_answer.get())
        self.user_answer.set('None')
        self.score_var.set(f"Score: {self.quiz.get_score()}")
        
        if self.quiz.next_question():
            self.show_question()
        else:
            self.show_results()
    
    def show_results(self):
        self.clear_frame()
        self.next_button.forget()
        Label(self.question_frame, 
             text=f"Final Score: {self.quiz.get_score()}/{len(self.quiz.questions)}",
             font="calibre 25 bold").pack(pady=50)
    
    def clear_frame(self):
        for widget in self.question_frame.winfo_children():
            widget.destroy()