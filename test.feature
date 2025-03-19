Feature: Shopping Cart Functionality  

  Scenario: Adding a product to the cart  
    Given I am on the login page  
    When I log in with valid credentials  
    And I add a product to the cart  
    Then the button should change to "Remove"  
    And the cart badge should show "1"