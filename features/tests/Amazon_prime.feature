# Created by aleksandrkryzhanovskii at 2/13/21
Feature: Amazon Prime tests

  Scenario: Amazon Prime displays 8 benefit boxes
    Given Open Amazon Prime page
    Then Verify 8 benefit boxes are displayed