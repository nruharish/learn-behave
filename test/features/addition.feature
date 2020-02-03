Feature: given two numbers add them

  Scenario Outline: Add two numbers
    Given two numbers <number1> and <number2>
    When we add the numbers
    Then we should get <result>

    Examples: Addition
        | number1         | number2 |result |
        | 1 | 2        |3|
        | 0        | 1 | 1|