# Created by Fazila Banu
Feature: Contains feature making posts for the specified service

  @GET_POSTS @TC_POSTS_01
  Scenario:Request for validating the ai response in posts
    When request is sent to validate content in posts
    Then the response keys for all the content is validated successfully

  @GET_POSTS @TC_POSTS_02
  Scenario:Request for retrieving contents in post
    When request is sent to validate content in posts
    Then the response key value for all the content is validated to be not empty successfully

  @GET_POSTS @TC_POSTS_03 @TC_COMMENT_03
  Scenario:Request for retrieving contents in post
    When request is sent to validate content in posts
    Then delete the post

