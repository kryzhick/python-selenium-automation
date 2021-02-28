# Created by aleksandrkryzhanovskii at 2/27/21
Feature: Test for 404 page

  Scenario: Amazon 404 page opens blog in another window
    Given Open Amazon B07BJKRR25 page
    When Store original window
    And Click to open blog
    And Switch to the newly opened window
    Then User can close new window and switch back to original