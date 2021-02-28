# Created by aleksandrkryzhanovskii at 2/21/21
Feature: Amazon sing in page

  Scenario: Sing in page can be open from Sing in popup
    Given Open Amazon page
    When Click Sing in from popup
    Then Verify Sing in page opens


  Scenario: Amazon users see sing in button
    Given Open Amazon page
    Then Verify Sing In is clickable
    When Wait for 5 sec
    Then Verify Sing In is clickable
    Then Verify Sing In disappears