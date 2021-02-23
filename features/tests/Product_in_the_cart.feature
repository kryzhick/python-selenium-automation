# Created by aleksandrkryzhanovskii at 2/20/21
Feature: User can add the product to the cart

  Scenario: User can add the product to the cart
    Given Open Amazon page
    When Input LOL doll into Amazon search field
    And Click on first result product
    And Add first result product into the cart
    Then Varify cart has 1 item