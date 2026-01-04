Feature: Environment Switching
  As a developer
  I want to switch between production and test environments
  So that I can run deterministic tests or real reports safely

  Scenario: Default to production mode
    Given the environment variable "INFLACIONAL_ENV" is not set
    When I request the API provider
    Then the provider should be an instance of "RealSIEProvider"

  Scenario: Switch to test mode
    Given the environment variable "INFLACIONAL_ENV" is set to "test"
    When I request the API provider
    Then the provider should be an instance of "MockSIEProvider"
