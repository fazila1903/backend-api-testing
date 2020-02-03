from behave import *
from lib.api import REST as rest
import logging
import json
import os


logging.basicConfig(level=logging.DEBUG)
@when(u'user is created in the service')
def postUser(context):
    path = (os.path.dirname(os.path.abspath(__file__)))
    with open(path+'/lib/userCreation.json') as f:
        data = json.load(f)
        context.data = data
    jsonResponse, statusCode = rest.myApiCall( "/users", data, "POST", myNumOfRetries=1)
    context.statusCode = statusCode


@then(u'the response of the user created is validated')
def validateUser(context):
    statusCode = context.statusCode
    assert (statusCode == 0)


@then(u'the user must be able to create a comment on the post')
def createComment(context):
    path = (os.path.dirname(os.path.abspath(__file__)))
    with open(path+'/lib/commentCreation.json') as f:
        data = json.load(f)
        context.data = data
    jsonResponse, statusCode = rest.myApiCall( "/posts/1", data, "POST", myNumOfRetries=1)
    print(statusCode)


#Examples

@when('u "{user}" is created in the service')
def step_impl(context, user):
    pass


@then('u the user must be able to create "{post}"')
def step_impl(context, post):
    pass


@then('u "{comment}" on the "{post}" created')
def step_impl(context, comment, post):
    pass

