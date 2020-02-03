# Created by Fazila Banu
Feature: Contains feature of user creation, making posts and comments for the specified service


# This is an example scenario for a complete journey
# Cannot be executed as it is a fake server


@POST_COMMENT @TC_COMMENT_02
Scenario Outline:Request for validating the user creation in service
  When "<user>" is created in the service
  Then the user must be able to create "<post>"
  And "<comment>" on the "<post>" created

  Examples:
    | user  | post  | comment  |
    | user1 | post1 | comment1 |
    | user2 | post2 | comment2 |

