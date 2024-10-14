# Higher or Lower: Celebrity Follower Count Game

Welcome to the **Higher or Lower** game! 🎉 This fun and engaging Python project challenges you to guess which celebrity has more followers on social media. Are you ready to test your pop culture knowledge?

## Game Overview

In this game, you'll be presented with two celebrity names. Your task is to guess which celebrity has a higher follower count. Each correct guess earns you a point, while an incorrect guess ends the game. 

### Features
- **Multiple Rounds**: Keep guessing until you make a mistake.
- **Scoring System**: Track your score throughout the game.
- **Dynamic Celebrity Data**: Each round features different celebrities, ensuring a unique experience every time you play!

## How to Play

1. Clone or download the repository.
2. Navigate to the folder containing the project files.
3. Run the game script:
   ```bash
   python higherlowerproject.py
   ```
4. Follow the prompts to guess which celebrity has more followers.
5. Enjoy and try to beat your high score!

## Game Data

The game pulls celebrity follower data from a predefined dataset in `game_data.py`. This data includes:
- **Name**: The celebrity's name.
- **Follower Count**: Number of followers they have.
- **Description**: Brief description of who they are.
- **Country**: The country they represent.

### Sample Data:
```python
{
    'name': 'Cristiano Ronaldo',
    'follower_count': 215,
    'description': 'Footballer',
    'country': 'Portugal'
}
```

## Source Code

### `higherlowerproject.py`
This is the main game file where the game logic is implemented. It randomly selects two celebrities and allows the player to guess who has more followers.

### `game_data.py`
This file contains the list of celebrities along with their follower counts, descriptions, and countries. It acts as the database for the game.

```python
import game_data
```

## A Little Joke

Why don't scientists trust atoms?  
Because they make up everything! 😂

## Installation

To play the game, make sure you have Python installed. Then clone this repository and navigate to the folder:

```bash
git clone <repository-url>
cd higher-or-lower-game
```

Run the game with:

```bash
python higherlowerproject.py
```
## Contribution

We encourage contributions to keep the game fresh and up-to-date! 

### Updating Game Data
To update the celebrity follower data:
1. Open the `game_data.py` file.
2. Locate the `data` list at the top of the file.
3. Add new entries or update existing ones in the following format:
   ```python
   {
       'name': 'New Celebrity',
       'follower_count': X,  # Replace X with the actual follower count
       'description': 'Description of the celebrity',
       'country': 'Country of the celebrity'
   }
   ```
4. Save your changes.

No need to modify any other parts of the code; the game will automatically use the updated data.

## Enjoy the Game!

Happy guessing! May your follower-count knowledge guide you to victory! 🌟

*Created with ❤️ by Somanath Nemilidinne*
