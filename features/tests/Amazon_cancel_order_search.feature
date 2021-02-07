# Created by aleksandrkryzhanovskii at 2/6/21
Feature: Amazon cancel order search test
  # Enter feature description here

  Scenario: User can see Cancel Items or Orders text
    Given Open Amazon help page
    When Input Cancel order into search Help librarty field and hit ENTER
    Then Cancel Items or Orders text is shown
