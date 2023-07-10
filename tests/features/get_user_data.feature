@automated
Feature: User - Fetch user data
  As a user
  I will send GET request to Req Res API
  I want to be able to see the expected response

  Background:
    Given I set Req Res API URL to $BASE_URL

  @smoke
  Scenario: Get all user data
    Given I set Req Res API GET route to "users" for all users
    When I set Content-Type as "application/json" in Headers
    And I send a GET HTTP request
    Then I expect HTTP response code to be "200" for GET
    Then I expect response body of GET to be non-empty
    And I expect response body to contain all user data

  @smoke
  Scenario: Get a single user data
    Given I set Req Res API GET route to "users/{id}" for single user
    When I set Content-Type as "application/json" in Headers
    And I send a GET HTTP request
    Then I expect HTTP response code to be "200" for GET
    Then I expect response body of GET to be non-empty
    And I expect response body to contain a single user data
