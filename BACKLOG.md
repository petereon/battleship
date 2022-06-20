# Backlog

## Domain

- A game starts with two players provided with empty game units.  
- Each game unit two 10 x 10 grids, top and bottom.
- The bottom grid is the ocean grid, while the upper grid is the target grid.  
- The columns are marked 1 - 10, while the rows are marked A - J.  

- The players place 5 ships on their grid.
  - Carrier (5 squares)
  - Battleship (4 squares)
  - Cruiser (3 squares)
  - Submarine (3 squares)
  - Destroyer (2 squares)

- Players decide who plays first or a first player is randomly selected
- A current player picks a target hole on the grid
- If this was a hit, the game announces so and passes the initiative to opponent
  - A red peg is inserted into the target hole
  - If entire ship was sunk, a red peg marks that the ship was sunk
  - If all the ships have been sunk (all 5 ship indicators have been set), the game ends
- If it was a miss, the initiative is passed to opponent
  
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
❌ A game starts with two players provided with empty boards.  Each board two 10 x 10 grids, top and bottom.  The bottom grid is the current player's grid, while the upper grid is the opponents.  The grids represent the ocean.  The columns are marked 1 - 10, while the rows are marked A - J.  

❌ User Story 1:  
__As a__ current player  
__I want__ start up the game  
__So that__ I can see the 2 boards capturing mine and opponents oceans  

❌ UAT 1.1:  
__GIVEN__ a two players  
__AND__ the interface is a console  
__WHEN__ the game starts  
__THEN__ the 10 x 10 board representing 1st player's ships is printed to the console on bottom-left  
__AND__ the 10 x 10 board representing 2nd player's ships are printed to the console on bottom-right  
__AND__ the 10 x 10 board representing 1st player's shots are printed to the console on top-left  
__AND__ the 10 x 10 board representing 2nd player's shots are printed to the console on top-right


### Story telling 2
A game starts with two provided with empty game units.  Each game unit has two 10 x 10 grids, top and bottom.  The bottom grid is the current player's ocean grid, while the upper grid is the current player's target grid.  The grids contain columns marked 1 - 10, and rows marked A - J.

#### User Story 2
__As a__ game player  
__I want__ start the game  
__So that__ I see game unit set up with empty grids  

#### UAT 2.1
__GIVEN__ a new game
__WHEN__ the game initialises
__THEN__ the two game units are set up with grids
__AND__ each grid is empty
__AND__ each grid is 10 x 10

TODO:

- [ ] Snyk into CI pipeline  
