from behave import *
from lib.api import REST as rest
import logging

logging.basicConfig(level=logging.DEBUG)
@when(u'request is sent to validate content in posts')
def getContent(context):
    jsonResponse, statusCode = rest.myApiCall("/posts", None, "GET", myNumOfRetries=1)
    assert(statusCode == 0)
    assert(len(jsonResponse) > 0)
    context.jsonResponse = jsonResponse


@then(u'the response keys for all the content is validated successfully')
def validateKeyContent(context):
    listJson = context.jsonResponse
    for key in listJson:
        assert('userId' in dict(key))
        assert('id' in dict(key))
        assert('title' in dict(key))
        assert('body' in dict(key))


@then(u'the response key value for all the content is validated to be not empty successfully')
def validateKeyValueContent(context):
    listJson = context.jsonResponse
    for key in listJson:
        assert (not (dict(key)['userId']) == "")
        assert (not (dict(key)['id']) == "")
        assert (not (dict(key)['title']) == "")
        assert (not (dict(key)['body']) == "")


@then(u'the user must be able to create post')
def getContent(context):
    jsonResponse, statusCode = rest.myApiCall("/posts", None, "POST", myNumOfRetries=1)
    assert(statusCode == 0)
    assert(len(jsonResponse) > 0)


@then(u'delete the post')
def getContent(context):
    jsonResponse, statusCode = rest.myApiCall("/posts/1", None, "DELETE", myNumOfRetries=1)
    assert (statusCode == 0)

