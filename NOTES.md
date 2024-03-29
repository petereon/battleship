# Battleship kata

Participants:
- Peter Vyboch
- Gearoid O'Treasaigh

## 1st Pomodoro
~ 2 hrs

- ✅ setup the initial story, US and UAT

### Story telling
A game starts with two players provided with empty boards.  Each board two 10 x 10 grids, top and bottom.  The bottom grid is the current player's grid, while the upper grid is the opponents.  The grids represent the ocean.  The columns are marked 1 - 10, while the rows are marked A - J.  

User Story 1:  
__As a__ current player  
__I want__ start up the game  
__So that__ I can see the 2 boards capturing mine and opponents oceans  

UAT 1.1:  
__GIVEN__ a two players  
__AND__ the interface is a console  
__WHEN__ the game starts  
__THEN__ the 10 x 10 board representing 1st player's ships is printed to the console on bottom-left  
__AND__ the 10 x 10 board representing 2nd player's ships are printed to the console on bottom-right  
__AND__ the 10 x 10 board representing 1st player's shots are printed to the console on top-left  
__AND__ the 10 x 10 board representing 2nd player's shots are printed to the console on top-right

## 2nd Pomodoro
Driver: G  
Navigator: Petko  

- 🚧 Implement scaffolding for new game
- ⚠ commit
- 

## 3rd Pomodoro

Driver: Petko
Navigator: G

- 🚧 Test out the formatter utility
- ⚠ commit
- ⚠ Implement the functionality for the BDD test
- ⚠ commit

## 4th Pomodoro

Driver: Petko
Navigator: G

- 🚧 Update the formatter to handle the four boards
- ⚠ commit
- ⚠ Implement the UAT tests for the four boards
- ⚠ commit

## 5th Pomodoro

Driver: G
Navigator: Petko

- ✅ Update the formatter to handle the four boards
- ⚠ Implement the UAT tests for the four boards

## 6th Pomodoro

Driver: Petko
Navigator: G

- ✅ Rename everything that mentions battleship to battleship
- ✅ commit
- ✅ Update steps files to have given, when, then in the function names
- ✅ commit
- ✅ Replace own_board with ocean_grid
- ✅ Replace shots_board with target_grid
- ✅ commit
- 🚧 Implement @then tests in the steps file
- ⚠ commit

## 7th Pomodoro

Mob programming

- ✅ Figure out way to mock the table placement


## 8th Pomodoro

Driver: G
Navigator: Petko

- ✅ Figure out how to put a table within a table from the game object
- ⚠ Fixture for Player 1 Shots for Grid

## 9th Pomodoro

Driver: Petko
Navigator: G

- 🚧 Create print function for the table (drive by unit tests)

## 10th Pomodoro

Driver: Petko
Navigator: G

- 🚧: update the feature for the new game
- ⚠ commit
- ⚠ create tests for the format function of the entire game
- ⚠ commit

## 11th Pomodoro

Mob programming

- ✅ Write BDD tests for UAT 2.1
- ✅ commit

## 12th Pomodoro

Mob programming

- 🚧 Write unit tests for UAT 2.1
- ⚠ commit
- ⚠ Write the implementation for the UAT 2.1
- ⚠ commit

## 13th Pomodoro

- ✅ Write unit tests for UAT 2.1
- ✅ commit

## 14th Pomodoro

- ✅ Write more of the backlog

## 15th Pomodoro

Driver: G
Navigator: Petko

- ✅ Implement passing BDD test stubs
- ✅ Provide actual implementation of BDD tests
- ⚠ Drill down to unit tests

## 16th Pomodoro

Driver: Petko
Navigator: G

- 🚧 Drill down to unit tests for UAT 3.1
- ⚠ commit
- ⚠ write the functionality for UAT 3.1
- ⚠ commit

## 17th Pomodoro

Driver & Navigator: G  

- ✅ continue with the unit tests for UAT 3.1
- ✅ commit

## 18th Pomodoro

Mob Programming  

- ✅ Set up Terraform

## 19th Pomodoro

Driver & Navigator: G  

- 🚧 work on UAT 3.2
- ⚠ commit

## 20th Pomodoro

Driver & Navigator: G

- ✅ refactor bdd tests to support multiple types of vessels
- ✅ commit
- ✅ refactor use of carrier to ENUM
- ✅ commit
- ⚠ write the bdd tests for UAT 3.2
- ⚠ commit
- ⚠ write the unit test for UAT 3.2
- ⚠ commit

## 21st Pomodoro

Driver & Navigator: G

- ✅ write the bdd tests for UAT 3.2
- ✅ commit
- 🚧 write the unit test for UAT 3.2
- ⚠ commit

## 22nd Pomodoro

Driver & Navigator: G

- ✅ write the unit tests and basic code for UAT 3.2
- ✅ commit
- ✅ write the bdd tests for UAT 3.3
- ✅ commit
- 🚧 write the unit tests for UAT 3.3
- ⚠ commit

## 23rd Pomodoro

Driver & Navigator: G

- ✅ write the unit tests for UAT 3.3
- ✅ commit
- ✅ write the bdd tests for UAT 3.4
- ✅ commit
- ✅ write the unit tests for UAT 3.4
- ✅ commit
- ✅ write the bdd tests for UAT 3.5
- ✅ commit
- ✅ write the unit tests for UAT 3.5
- ✅ commit
- ✅ write UAT 3.6 in the backlog for the negative case

## 24th Pomodoro

Driver & Navigator: G

- ✅ write the bdd tests for UAT 3.6
- ✅ commit
- 🚧 write the unit tests for UAT 3.6
- ⚠ commit

## 25th Pomodoro

Driver & Navigator: G

- 🚧 write the unit tests for UAT 3.6
- ⚠ commit

## 26th Pomodoro

Driver: G
Navigator: Petko

- 🚧 write the unit tests for UAT 3.6
- ⚠ commit

## 27th Pomodoro

Driver: Petko
Navigator: G

- ✅ Refactor `place_vessel`
- ✅ commit
- ⚠ Write the backlog of scenarios that we need to complete for the logic

## 28th Pomodoro

Driver: G  
Navigator: Petko  

- 🚧 Write the backlog of scenarios that we need to complete for the logic


## 29th Pomodoro

Mob Programming  

- 🚧 Write the backlog of UATs that we need to complete for the logic
- ⚠ Fix the uncovered lines

## 30th Pomodoro

Driver: G  
Navigator: Petko 

- 🚧 Features for the UAT 4.1
- ⚠ commit

## 31st Pomodoro

Driver: Petko  
Navigator: G  

- ✅ Implement the unit tests for the UAT 4.1
- ✅ commit

## 32nd Pomodoro

Driver: G  
Navigator: Petko 

- ✅ Implement the BDD tests for the UAT 5.1
- ✅ commit

## 33rd Pomodoro

Driver: Petko
Navigator: G

- 🚧 Implement the unit tests for the UAT 5.1
- ⚠ commit

## 34th Pomodoro

Driver: Petko
Navigator: G

- ✅ Implement the unit tests for the UAT 5.1
- ✅ commit

## 35th Pomodoro

Driver: G
Navigator: Petko

- ✅ Implement the BDD tests for the UAT 6.1
- ✅ commit

## 36th Pomodoro

Driver: Petko
Navigator: G

- 🚧 Implement the unit tests for the UAT 6.1
- ✅ commit

## 37th Pomodoro

Driver: G
Navigator: Petko

- ✅ Implement the unit tests for the UAT 6.1
- ✅ commit
- ✅ Implement the BDD tests for the UAT 6.2
- ✅ commit

## 38th Pomodoro

Driver: Petko  
Navigator: G   

- ✅ Implement the unit tests for UAT 6.2
- ✅ commit
- ✅ Implement the BDD tests for UAT 7.1
- ✅ commit

## 39th Pomodoro 

Driver: G
Navigator: Petko

- ✅ Implement BDD test for UAT 8.1.1
- ✅ commit

## 40th Pomodoro

Driver: Petko
Navigator: G

- 🚧 Implement unit tests for UAT 8.1.1
- ⚠ commit

## 41th Pomodoro

Driver: G
Navigator: Petko

- 🚧 Implement unit tests for UAT 8.1.1
- ⚠ commit

## 42nd Pomodoro

Driver: Petko
Navigator: G

- ✅ Implement unit tests for UAT 8.1.1
- ✅ commit
- 🚧 Implement BDD tests for UAT 8.2.1
- ⚠ commit

## 43rd Pomodoro 

Driver: G
Navigator: Petko 

- ✅ Implement BDD tests for UAT 8.2.1
- ✅ commit
- ✅  Implement unit tests for UAT 8.2.1
- ✅ commit
- ✅ Implement functionality for UAT 8.2.1
- ✅ commit
- 🚧 Implement BDD tests for UAT 8.2.2
- ⚠ commit

## 44th Pomodoro

Driver: Petko
Navigator: G

- ✅ Implement unit tests for UAT 8.2.2
- ✅ commit
- 🚧 Implement unit tests for UAT 8.2.2
- ⚠ commit
- ⚠ Implement the functionality for UAT 8.2.2
- ⚠ commit

## 45th Pomodoro 

Driver: G
Navigator: Petko

- 🚧 Implement unit tests for UAT 8.2.2
- ⚠ commit
- ⚠ Implement the functionality for UAT 8.2.2
- ⚠ commit

## 46th Pomodoro

Driver: Petko
Navigator: G

- 🚧 Implement unit tests for UAT 8.2.2
- ⚠ commit

## 47th Pomodoro

Driver: G  
Navigator: Petko  

- 🚧 Implement unit tests for UAT 8.2.2
- ⚠ commit

## 48th Pomodoro 

Driver: Petko  
Navigator: G  

- ✅ Implement unit tests for UAT 8.2.2
- ✅ commit
- 🚧 move the sunk vessel to the player

## 49th Pomodoro

Driver: G  
Navigator: Petko  

- 🚧 Implement BDD tests for UAT 9.1
- ⚠ commit

## 50th Pomodoro

Driver: Petko  
Navigator: G  

- ✅ Implement BDD tests for UAT 9.1
- ✅ commit
- 🚧 Implement unit tests for UAT 9.1
- ⚠ commit

## 51th Pomodoro

Driver: Petko  
Navigator: G  

- 🚧 Implement unit tests for UAT 9.1
- ⚠ commit

## 52th Pomodoro

Driver: G
Navigator: Petko

- ✅ Implement unit tests for UAT 9.1
- ✅ commit
- 🚧  Implement BDD tests for UAT 10.1
- ⚠  commit

## 53rd Pomodoro

Driver: Petko  
Navigator: G  

- ✅ refactor the code sunk vessel check and update
- ✅ commit
- ✅  Implement BDD tests for UAT 10.1
- ✅  commit
- ⚠  Implement unit tests for UAT 10.1
- ⚠  commit

## 54th Pomodoro

Driver: G  
Navigator: Petko   

- 🚧 Implement unit tests for UAT 10.1
- 🚧 commit

# 55th Pomodoro

Driver: Petko    
Navigator: G    

- ❌ Implement unit tests for UAT 10.1
- 🚧 Handling the current shot being None
- ⚠ Integrate the get current shot into check sunk vessel status
- ⚠ commit

# 56th Pomodoro

Driver: G  
Navigator: Petko  

- ✅ Handling the current shot being None
- ✅ Integrate the get current shot into check sunk vessel status
- ✅ commit
- 🚧 Implement unit tests for UAT 10.1
- ⚠ commit

## 57th Pomodoro

Driver: Petko  
Navigator: G  

- 🚧 Implement unit tests for UAT 10.1
- ⚠ commit

## 58th Pomodoro

Driver: G  
Navigator: Petko  

- 🚧 Implement unit tests for UAT 10.1
- ⚠ commit

## 59th Pomodoro

Driver: Petko  
Navigator: G  

- ✅ Implement unit tests for UAT 10.1
  - ✅ working on tests for placing the peg as part of take turn
- ✅ commit

## 60th Pomodoro

Driver: Petko  
Navigator: G  

- 🚧 Write out the backlog for bot vs bot API
- ⚠ commit
- ⚠ Implement BDD tests for UAT 11.1

## 71st Pomodoro

Driver & Navigator: G

- ✅ Write the BDD test for the health check endpoint UAT 11.1
- ✅ commit
- ✅ Write unit tests for the health check endpoint UAT 11.1
- ✅ commit
- ✅ Implement the health endpoint
- ✅ commit

# 72nd - 76th

Driver & Navigator: G  

- ✅ Investigate why gitlint is complaining - it's due to the fact that poetry doesn't support gitlint and it's actually installed using pip
- 🚧 Investigate why the health endpoint is not running on https://goo9cf.deta.dev/heatlh
  - Enabled visor
  - Deployed the app to https://6tkmo4.deta.dev/health where I can see it is working
  - Next step is to look at the visor logs as to what the error is.
