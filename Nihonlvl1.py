import random
import time

class HiraganaGame:
    def __init__(self):
        # Complete hiragana dictionary with romanization
        self.hiragana_dict = {
            # Basic vowels
            'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
            
            # K sounds
            'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
            
            # G sounds
            'が': 'ga', 'ぎ': 'gi', 'ぐ': 'gu', 'げ': 'ge', 'ご': 'go',
            
            # S sounds
            'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
            
            # Z sounds
            'ざ': 'za', 'じ': 'ji', 'ず': 'zu', 'ぜ': 'ze', 'ぞ': 'zo',
            
            # T sounds
            'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
            
            # D sounds
            'だ': 'da', 'ぢ': 'di', 'づ': 'du', 'で': 'de', 'ど': 'do',
            
            # N sounds
            'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
            
            # H sounds
            'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
            
            # B sounds
            'ば': 'ba', 'び': 'bi', 'ぶ': 'bu', 'べ': 'be', 'ぼ': 'bo',
            
            # P sounds
            'ぱ': 'pa', 'ぴ': 'pi', 'ぷ': 'pu', 'ぺ': 'pe', 'ぽ': 'po',
            
            # M sounds
            'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
            
            # Y sounds
            'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
            
            # R sounds
            'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
            
            # W sounds
            'わ': 'wa', 'ゐ': 'wi', 'ゑ': 'we', 'を': 'wo',
            
            # N
            'ん': 'n'
        }
        
        self.score = 0
        self.total_questions = 0
        self.start_time = None
        
    def display_menu(self):
        print("\n" + "="*50)
        print("🗾 HIRAGANA READING GAME 🗾")
        print("="*50)
        print("1. Start Game (All Characters)")
        print("2. Practice Basic Vowels (あいうえお)")
        print("3. Practice K-sounds (かきくけこ)")
        print("4. Practice S-sounds (さしすせそ)")
        print("5. Practice T-sounds (たちつてと)")
        print("6. Practice N-sounds (なにぬねの)")
        print("7. Practice H-sounds (はひふへほ)")
        print("8. Practice M-sounds (まみむめも)")
        print("9. Practice Y-sounds (やゆよ)")
        print("10. Practice R-sounds (らりるれろ)")
        print("11. Practice W-sounds + ん (わをん)")
        print("12. View Statistics")
        print("0. Quit")
        print("="*50)
        
    def get_character_set(self, choice):
        sets = {
            1: list(self.hiragana_dict.keys()),  # All characters
            2: ['あ', 'い', 'う', 'え', 'お'],  # Vowels
            3: ['か', 'き', 'く', 'け', 'こ', 'が', 'ぎ', 'ぐ', 'げ', 'ご'],  # K sounds
            4: ['さ', 'し', 'す', 'せ', 'そ', 'ざ', 'じ', 'ず', 'ぜ', 'ぞ'],  # S sounds
            5: ['た', 'ち', 'つ', 'て', 'と', 'だ', 'ぢ', 'づ', 'で', 'ど'],  # T sounds
            6: ['な', 'に', 'ぬ', 'ね', 'の'],  # N sounds
            7: ['は', 'ひ', 'ふ', 'へ', 'ほ', 'ば', 'び', 'ぶ', 'べ', 'ぼ', 'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ'],  # H sounds
            8: ['ま', 'み', 'む', 'め', 'も'],  # M sounds
            9: ['や', 'ゆ', 'よ'],  # Y sounds
            10: ['ら', 'り', 'る', 'れ', 'ろ'],  # R sounds
            11: ['わ', 'ゐ', 'ゑ', 'を', 'ん']  # W sounds + n
        }
        return sets.get(choice, [])
        
    def play_round(self, character_set, num_questions=10):
        if not character_set:
            print("Invalid selection!")
            return
            
        print(f"\n🎮 Starting game with {len(character_set)} characters!")
        print(f"You'll answer {num_questions} questions.")
        print("Type 'quit' to return to menu, 'hint' for a hint\n")
        
        self.start_time = time.time()
        round_score = 0
        
        for i in range(num_questions):
            hiragana = random.choice(character_set)
            correct_answer = self.hiragana_dict[hiragana]
            
            print(f"\nQuestion {i+1}/{num_questions}")
            print(f"Character: {hiragana}")
            print("(Large font for better visibility)")
            
            user_input = input("Type the romanization: ").strip().lower()
            
            if user_input == 'quit':
                print("Returning to menu...")
                break
            elif user_input == 'hint':
                print(f"💡 Hint: The answer starts with '{correct_answer[0]}'")
                user_input = input("Type the romanization: ").strip().lower()
            
            if user_input == correct_answer:
                print("✅ Correct!")
                round_score += 1
                self.score += 1
            else:
                print(f"❌ Wrong! The correct answer is: {correct_answer}")
            
            self.total_questions += 1
            
            # Show progress
            accuracy = (round_score / (i + 1)) * 100
            print(f"Round progress: {round_score}/{i+1} ({accuracy:.1f}%)")
        
        if self.start_time:
            time_taken = time.time() - self.start_time
            print(f"\n⏱️  Time taken: {time_taken:.1f} seconds")
            print(f"🎯 Round score: {round_score}/{min(i+1, num_questions)}")
            
    def show_statistics(self):
        if self.total_questions == 0:
            print("\n📊 No games played yet!")
            return
            
        accuracy = (self.score / self.total_questions) * 100
        print(f"\n📊 STATISTICS")
        print("="*30)
        print(f"Total Questions: {self.total_questions}")
        print(f"Correct Answers: {self.score}")
        print(f"Accuracy: {accuracy:.1f}%")
        
        if accuracy >= 90:
            print("🏆 Excellent! You're a hiragana master!")
        elif accuracy >= 75:
            print("🥉 Good job! Keep practicing!")
        elif accuracy >= 50:
            print("📚 Not bad! More practice will help!")
        else:
            print("💪 Keep practicing! You'll get there!")
    
    def reset_statistics(self):
        self.score = 0
        self.total_questions = 0
        print("📊 Statistics reset!")
        
    def run(self):
        print("Welcome to the Hiragana Reading Game!")
        print("This game will help you practice reading hiragana characters.")
        
        while True:
            self.display_menu()
            
            try:
                choice = int(input("\nSelect an option (0-12): "))
                
                if choice == 0:
                    print("👋 Thanks for playing! がんばって！(Ganbatte!)")
                    break
                elif choice == 12:
                    self.show_statistics()
                    reset = input("\nReset statistics? (y/n): ").lower()
                    if reset == 'y':
                        self.reset_statistics()
                elif 1 <= choice <= 11:
                    character_set = self.get_character_set(choice)
                    
                    # Ask for number of questions
                    try:
                        num_q = input(f"\nHow many questions? (default: 10): ").strip()
                        num_questions = int(num_q) if num_q else 10
                        num_questions = max(1, min(50, num_questions))  # Limit between 1-50
                    except ValueError:
                        num_questions = 10
                    
                    self.play_round(character_set, num_questions)
                else:
                    print("❌ Invalid choice! Please select 0-12.")
                    
            except ValueError:
                print("❌ Please enter a valid number!")
            except KeyboardInterrupt:
                print("\n👋 Thanks for playing!")
                break

def main():
    game = HiraganaGame()
    game.run()

if __name__ == "__main__":
    main()