# Created by Fazila Banu
Feature: Contains feature of user creation, making posts and comments for the specified service

  @POST_USERS @TC_USER_01
  Scenario:Request for validating the user creation in service
    When user is created in the service
    Then the response of the user created is validated

  @POST_COMMENT @TC_COMMENT_01
  Scenario:Request for validating the user creation in service
    When user is created in the service
    Then the user must be able to create a comment on the post

