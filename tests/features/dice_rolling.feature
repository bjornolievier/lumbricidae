Feature: Dice Rolling
  As a player
  I want to roll dice
  So that I can try to claim tiles

  Scenario: Roll initial dice
    Given a new game with 2 players
    When player 1 starts their turn
    And they roll 8 dice
    Then they should get 8 dice results
    And all results should be valid dice faces