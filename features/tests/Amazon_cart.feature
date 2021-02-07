# Created by aleksandrkryzhanovskii at 2/6/21
Feature: Amazon cart is empty test
  # Enter feature description here

  Scenario: Users cart is empty
    Given Open Amazon page
    When Click on cart icon
    Then Cart is empty