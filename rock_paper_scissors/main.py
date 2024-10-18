import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def get_player_choice(self):
        choice = input("Enter rock, paper, or scissors: ").lower()
        while choice not in self.choices:
            print("Invalid choice. Try again.")
            choice = input("Enter rock, paper, or scissors: ").lower()
        return choice

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            return "You win!"
        else:
            return "You lose!"

    def play(self):
        while True:
            player_choice = self.get_player_choice()
            computer_choice = self.get_computer_choice()

            print(f"\nYou chose: {player_choice}")
            print(f"Computer chose: {computer_choice}")

            result = self.determine_winner(player_choice, computer_choice)
            print(result)

            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thanks for playing!")
                break


if __name__ == "__main__":
    print("Welcome to Rock Paper Scissors!")
    game = RockPaperScissors()  # Create an instance of the game
    game.play()  # Start the game

