import random;

def init_game():
    cards = ['A', 'B', 'C', 'D', 'E', 'F'] * 2;
    random.shuffle(cards);
    return cards, [None] * len(cards);

def display_board(board):
    print(" ".join(card if card is not None else '*' for card in board));

def get_valid_choice(board):
    while True:
        try:
            choice = int(input("Choose a card (0-11): "));
            if choice < 0 or choice >= len(board) or board[choice] is not None:
                raise ValueError;
            return choice;
        except ValueError:
            print("Invalid choice. Please enter a valid number between 0 and 11 and select a hidden card.");

def play_game():
    cards, board = init_game();
    revealed = 0;

    while revealed < len(cards):
        display_board(board);

        first_choice = get_valid_choice(board);
        board[first_choice] = cards[first_choice];
        display_board(board);

        second_choice = get_valid_choice(board);
        board[second_choice] = cards[second_choice];
        display_board(board);

        if cards[first_choice] == cards[second_choice]:
            print("Match found!");
            revealed += 2;
        else:
            print("No match. Try again.");
            board[first_choice] = board[second_choice] = None;
        print();

    print("All pairs found! You won the game!");

    if input("Play again? (Y/N): ").strip().upper() == 'Y':
        play_game();
    else:
        print("Thanks for playing!");

if __name__ == "__main__":
    play_game();
