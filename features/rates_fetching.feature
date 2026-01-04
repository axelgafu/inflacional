Feature: Banxico API Rates Integration
  As an analyst
  I want the report to show the actual target interest rate from Banxico
  So that the report contains official information

  Scenario: Successfully fetching the target interest rate
    Given the application is in test mode
    And mock data for series "TI52" exists with value "11.25" for date "2023-12-01"
    When I fetch the target rate for "2023-12-01"
    Then the result should be "11.25"
