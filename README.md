

## Stone, Paper, Scissors Game in Python

This project is a simple and interactive Stone, Paper, Scissors game developed using Python. The game allows users to play against the computer, which generates random choices, providing an engaging experience.

### Features

- **User Input Prompt**: The game starts by asking the user if they want to play.
- **Random Computer Choice**: The computer randomly selects between "stone," "paper," and "scissors" using Python's `random` module.
- **Continuous Gameplay**: The game runs in a loop, allowing the user to play multiple rounds until they choose to exit.
- **Winner Determination**: After each round, the game checks and announces the winner based on standard Stone, Paper, Scissors rules.
- **User-Friendly Interface**: Simple text-based interaction makes the game easy to play and understand.

### Implementation Details

1. **Random Module**: Used to generate the computer's choice. This ensures that each game is unpredictable and fair.
    ```python
    import random
    ```

2. **User Input**: The game prompts the user to choose "stone," "paper," or "scissors" and validates the input to ensure it's correct.
    ```python
    user_choice = input("Enter your choice (stone, paper, scissors): ")
    ```

3. **Game Loop**: The game uses a loop to allow the user to play multiple rounds without restarting the program.
    ```python
    while True:
        # Game logic here
        if option==0:
            
    ```

4. **Winner Determination Logic**: The game checks the user's choice against the computer's choice to determine the winner.
    ```python
    if user_choice == computer_choice:
        print(" !!..... match draw.......!!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("congratulations..... You Win...!!")
    else:
        print(" Oo No Computer Win......!\n")
    ```

### Example Gameplay

```
welcome to stone,paper, Scissors python game
0 for game start and 1 for game quite:0
game start......!
"0 for stone, 1 for paper, 2 for scissors
choose your option :0
you choose: stone
Computer chose: scissors
congratulations..... You Win...!
```

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to improve the game.
