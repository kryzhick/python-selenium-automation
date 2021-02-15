# Created by aleksandrkryzhanovskii at 2/14/21
Feature: Tests for bestsellers functionality

  Scenario: There are 5 bestsellers link
    Given Open Amazon Bestsellers
    Then Verify there are 5 links