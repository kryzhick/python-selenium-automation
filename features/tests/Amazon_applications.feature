# Created by aleksandrkryzhanovskii at 2/27/21
Feature: Amazon Applications

  Scenario: User can open and close Amazon Applications
    Given Open Amazon T&C page
    When Store the original window
    And Click on Amazon Applications link
    And Switch to newly opened window
    Then Verify Amazon page is opened
    And Verify User can close new window and switch back to original