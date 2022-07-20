# Backlog

## Domain

- A game starts with two players provided with empty game units.  
- Each game unit two 10 x 10 grids, top and bottom.
- The bottom grid is the ocean grid, while the upper grid is the target grid.  
- The columns are marked 1 - 10, while the rows are marked A - J.  

- The players place 5 ships on their grid.
  - Carrier (5 holes)
  - Battleship (4 holes)
  - Cruiser (3 holes)
  - Submarine (3 holes)
  - Destroyer (2 holes)

- Players decide who plays first or a first player is rAndomly selected
- A current player picks a target hole on the grid
- If this was a hit, the game announces so and passes the initiative to opponent
  - A red peg is inserted into the target hole
  - If entire ship was sunk, a red peg marks that the ship was sunk
  - If all the ships have been sunk (all 5 ship indicators have been set), the game ends
- If it was a miss, the initiative is passed to opponent
  - A white peg is inserted into the target hole
  
### Entities

- Battleship Game
  - Player
    - Bot
  - Game Unit
    - Ocean Grid
    - Target Grid
  - Grid
    - Holes (10 x 10)
    - Pegs
      - Red
      - White
  - Sunk Ship Indicator
    - Holes (5)
    - Pegs
      - Red
  - Ships
    - Carrier
    - Battleship
    - Cruiser
    - Submarine
    - Destroyer

### Story telling 1
❌ A game starts with two players provided with empty boards.  Each board two 10 x 10 grids, top And bottom.  The bottom grid is the current player's grid, while the upper grid is the opponents.  The grids represent the ocean.  The columns are marked 1 - 10, while the rows are marked A - J.  

❌ User Story 1:  
__As a__ current player  
__I want__ start up the game  
__So that__ I can see the 2 boards capturing mine And opponents oceans  

❌ UAT 1.1:  
__Given__ a two players  
__And__ the interface is a console  
__When__ the game starts  
__Then__ the 10 x 10 board representing 1st player's ships is printed to the console on bottom-left  
__And__ the 10 x 10 board representing 2nd player's ships are printed to the console on bottom-right  
__And__ the 10 x 10 board representing 1st player's shots are printed to the console on top-left  
__And__ the 10 x 10 board representing 2nd player's shots are printed to the console on top-right


### Story telling 2 ✅
A game starts with two provided with empty game units.  Each game unit has two 10 x 10 grids, top And bottom.  The bottom grid is the current player's ocean grid, while the upper grid is the current player's target grid.  The grids contain columns marked 1 - 10, And rows marked A - J.

#### User Story 2 ✅
__As a__ game player  
__I want__ start the game  
__So that__ I see game unit set up with empty grids  

#### UAT 2.1 ✅
__Given__ a new game
__When__ the game initialises
__Then__ the two game units are set up with grids
__And__ each grid is empty
__And__ each grid is 10 x 10

### Story telling 3 ✅

Both players place 5 ships on their ocean grid.  The ships are:
  - Carrier (5 holes)
  - Battleship (4 holes)
  - Cruiser (3 holes)
  - Submarine (3 holes)
  - Destroyer (2 holes)

#### User Story 3 ✅

__As a__ game player
__I want__ to place ships on my ocean grid
__So that__ I can see my ships

#### UAT 3.1 ✅
Given a player
And the player's grids are set up
When the player places the carrier on their ocean grid
And chooses the position <position>
Then a carrier is placed on the ocean grid
And the carrier is in position <position>
And the carrier has 5 holes

  Examples:
  | position |
  | -------- |
  | A1, A5   |
  | A1, E1   |
  | J5, J9   |

#### UAT 3.2 ✅
Given a player
And the player's grids are set up
When the player places the battleship on their ocean grid
And chooses the position <position>
Then a battleship is placed on the ocean grid
And the battleship is in position <position>
And the battleship has 4 holes

  Examples:
  | position |
  | -------- |
  | A1, A4   |
  | B1, E1   |
  | J5, J8   |

#### UAT 3.3 ✅
Given a player
And the player's grids are set up
When the player places the cruiser on their ocean grid
And chooses the position <position>
Then a cruiser is placed on the ocean grid
And the cruiser is in position <position>
And the cruiser has 3 holes

  Examples:
  | position |
  | -------- |
  | H1, H3   |
  | C1, E1   |
  | J5, J7   |

#### UAT 3.4 ✅
Given a player
And the player's grids are set up
When the player places the submarine on their ocean grid
And chooses the position <position>
Then a submarine is placed on the ocean grid
And the submarine is in position <position>
And the submarine has 3 holes

  Examples:
  | position |
  | -------- |
  | H7, H9   |
  | C2, E2   |
  | J5, J7   |

#### UAT 3.5 ✅
Given a player
And the player's grids are set up
When the player places the destroyer on their ocean grid
And chooses the position <position>
Then a destroyer is placed on the ocean grid
And the destroyer is in position <position>
And the destroyer has 2 holes

  Examples:
  | position |
  | -------- |
  | H7, H8   |
  | D2, E2   |
  | J5, J6   |


#### UAT 3.6 ✅
Given a player
And the player's grids are set up
When the player places the destroyer on their ocean grid
And chooses the position <position>
Then the player receives an error message
And there is no change to their ocean grid

  Examples:
  | H H, H 8   |
  | A 4, C 5   |
  | A 7, A 10  |
  | D 2, bl ah |
  | J 10, J 12 |

#### Story telling 4 ✅
After the vessels have all been placed on the game units.  The game player makes a move by choosing a target hole on their target grid.

### User Story 4 ✅
__As a__ a game player  
__I want__ choose a hole on a target grid  
__So that__ so that I can make a target shot  

#### UAT 4.1 ✅
Given my target grid  
When I choose the hole on my target grid  
Then I know if it's available  

#### UAT 4.2 ✅
Given my target grid  
When I choose the hole off my target grid  
Then I know it's unavailable

#### Storytelling 5 ✅
After the shot was made.  The game announces if the shot was a hit or a miss.

### User Story 5 ✅
__As a__ a game player  
__I want__ the game to announce the shot status  
__So that__ I know that it is a hit or a miss  

#### UAT 5.1 ✅
Given I have taken a shot at the hole <hole>
And the opponent's ocean grid
When the game checks the shot status  
Then the status is <status>

  Examples:  
  | hole | status |  
  | A1   | hit    |  
  | A1   | miss   |  
  | J5   | hit    |  

#### Storytelling 6 ✅
After the shot was announced as being a hit.  The game places a red peg on the shot position on both the target grid and the ocean grid.

### User Story 6 ✅
__As a__ a game player
__I want__ the game to place a red peg on the shot position on both the target grid and the ocean grid
__So that__ I know that it was a hit

#### UAT 6.1 ✅
Given I have took my shot
And it was a hit
And my target grid
When the game places the peg on my target grid
Then the color of the peg is red

#### UAT 6.2 ✅
Given I have took my shot
And it was a hit
And opponent's ocean grid
When the game places the peg on opponent's ocean grid
Then the color of the peg is red

#### Storytelling 7 🚧
After the shot was announced as being a miss.  The game places a white peg on the shot position on the target grid.

### User Story 7 🚧
__As a__ a game player
__I want__ the game to place a white peg on the shot position on the target grid
__So that__ I know that it was a miss

#### UAT 7.1 🚧
Given I have took my shot  
And it was a miss  
And my target grid  
When the game places the peg on my target grid  
Then the color of the peg is white  

#### Storytelling 8 ⚠
After a red peg was placed.  The game announces that the player has sunk a ship and indicate it.

### User Story 8.1 ⚠
__As a__ a game player  
__I want__ the game to announce that the I have sunk the ship 
__So that__ I know that the ship has been sunk  

#### UAT 8.1.1 ⚠
Given I have sunk a ship
When the game checks the sunk ship status
Then the game announces that the ship has been sunk

### User Story 8.2 ⚠
__As a__ a game player  
__I want__ the game to indicate that the I have sunk a ship 
__So that__ I know how many ships I have sunk

#### UAT 8.2.1 ⚠
Given I have an empty target grid  
And an empty sunk ship indicator  
When the game starts  
Then it contains 5 empty holes  

#### UAT 8.2.2 ⚠
Given I have sunk a ship
When the game checks the sunk ship status
Then the game adds a red peg to the sunk ship indicator

#### Storytelling 9 ⚠
After each move has been made.  The game passes the initiative to the opponent.

### User Story 9 ⚠
__As a__ a game player  
__I want__ the game to pass the initiative to the opponent  
__So that__ they can make a move  

#### UAT 9.1 ⚠
Given my target grid <my target grid>  
And opponent's target grid <opponent target grid>  
When I take the shot  
Then the game does not end  
And the opponent can take the shot  

#### Storytelling 10 ⚠
After all of the opponent's 5 ships have been sunk. Then the game declares me as a winner.

### User Story 10 ⚠
__As a__ a game player  
__I want__ the game to declare me as a winner when I've sunk all of the opponent's 5 ships  
__So that__ I know that I won  

#### UAT 10.1 ⚠
Given I have sunk all of the opponent's 5 ships
When the game checks the sunk ship status
Then the game announces that I won
