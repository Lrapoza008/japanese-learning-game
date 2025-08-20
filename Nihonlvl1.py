import tkinter as tk
from tkinter import messagebox
import random
import time

class HiraganaGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hiragana Reading Game")
        self.root.geometry("600x400")
        
        # Hiragana dictionary
        self.hiragana_dict = {
            'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
            'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
            'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
            'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
            'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
            'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
            'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
            'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
            'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
            'わ': 'wa', 'を': 'wo', 'ん': 'n'
        }
        
        self.character_set = list(self.hiragana_dict.keys())
        self.current_character = None
        self.score = 0
        self.total_questions = 0
        self.start_time = None
        
        # GUI Elements
        self.create_widgets()
    
    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Hiragana Reading Game", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)
        
        # Hiragana Character Display
        self.character_label = tk.Label(self.root, text="", font=("Arial", 50, "bold"), fg="blue")
        self.character_label.pack(pady=20)
        
        # Input Field
        self.input_field = tk.Entry(self.root, font=("Arial", 16))
        self.input_field.pack(pady=10)
        self.input_field.bind("<Return>", self.check_answer)  # Bind Enter key to submit
        
        # Buttons
        self.submit_button = tk.Button(self.root, text="Submit", font=("Arial", 14), command=self.check_answer)
        self.submit_button.pack(pady=5)
        
        self.hint_button = tk.Button(self.root, text="Hint", font=("Arial", 14), command=self.show_hint)
        self.hint_button.pack(pady=5)
        
        self.start_button = tk.Button(self.root, text="Start Game", font=("Arial", 14), command=self.start_game)
        self.start_button.pack(pady=5)
        
        self.quit_button = tk.Button(self.root, text="Quit", font=("Arial", 14), command=self.root.quit)
        self.quit_button.pack(pady=5)
        
        # Score Label
        self.score_label = tk.Label(self.root, text="Score: 0", font=("Arial", 14))
        self.score_label.pack(pady=10)
    
    def start_game(self):
        self.score = 0
        self.total_questions = 0
        self.start_time = time.time()
        self.next_question()
    
    def next_question(self):
        self.current_character = random.choice(self.character_set)
        self.character_label.config(text=self.current_character)
        self.input_field.delete(0, tk.END)
    
    def check_answer(self, event=None):
        user_input = self.input_field.get().strip().lower()
        correct_answer = self.hiragana_dict[self.current_character]
        
        if user_input == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", f"✅ Correct! The answer is: {correct_answer}")
        else:
            messagebox.showerror("Wrong!", f"❌ Wrong! The correct answer is: {correct_answer}")
        
        self.total_questions += 1
        self.update_score()
        self.next_question()
    
    def show_hint(self):
        correct_answer = self.hiragana_dict[self.current_character]
        hint = f"The answer starts with '{correct_answer[0]}'"
        messagebox.showinfo("Hint", hint)
    
    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}/{self.total_questions}")
    
    def end_game(self):
        time_taken = time.time() - self.start_time
        accuracy = (self.score / self.total_questions) * 100 if self.total_questions > 0 else 0
        messagebox.showinfo("Game Over", f"Time: {time_taken:.1f}s\nScore: {self.score}/{self.total_questions}\nAccuracy: {accuracy:.1f}%")
        self.root.quit()

def main():
    root = tk.Tk()
    game = HiraganaGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()