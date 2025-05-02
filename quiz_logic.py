# quiz_logic.py
class QuizLogic:
    def __init__(self, questions, answers):
        self.questions = questions
        self.answers = answers
        self.current_question_index = 0
        self.score = 0
        
    def check_answer(self, user_answer):
        if user_answer and user_answer != 'None':
            if user_answer == self.answers[self.current_question_index]:
                self.score += 1
                return True
        return False
    
    def next_question(self):
        if self.has_more_questions():
            self.current_question_index += 1
            return True
        return False
    
    def get_current_question(self):
        if self.has_more_questions():
            question_text = list(self.questions.keys())[self.current_question_index]
            options = self.questions[question_text]
            return question_text, options
        return None, None
    
    def has_more_questions(self):
        return self.current_question_index < len(self.questions)
    
    def get_score(self):
        return self.score