import requests

#BaseURL declaration
baseUrl = "https://jsonplaceholder.typicode.com"
debug = False


class REST(object):

    # Class Initialization
    def __init__(self):
        pass

    # REST Method calls
    def myApiCall(myUrl, myParams, myMethod, myNumOfRetries=1):

        """ Makes a RESTful API call and returns a tuple of JSON payload and HTTP response code
        Keyword arguments:
            myUrl (string)          -- Url path with / included
            myParams (JSON)         -- POST command parameters or None.  Parameters must be in JSON format
            myMethod (string)       -- POST, GET, PUT, DELETE
            myNumOfRetries (string) -- Number of time the API to retry
        """

        # Build the full URL
        myURL = baseUrl + myUrl

        # Variable Initialization
        retryCount = 0
        timeout = 600
        while True:
            # Execute the required method
            # headers is excluded
            if myMethod == 'POST':
                r = requests.post(myURL, data=myParams,  timeout=timeout)
            elif myMethod == 'GET':
                r = requests.get(myURL, params=myParams, timeout=timeout)
            elif myMethod == 'PUT':
                r = requests.put(myURL, data=myParams, timeout=timeout)
            elif myMethod == 'DELETE':
                r = requests.delete(myURL, params=myParams,  timeout=timeout)

            #debug
            if debug:
                print('API Call: ' + myMethod + ' ' + myURL, end=', ')
                print('params:' + str(myParams))
                if r.text != '':
                    print('RESPONSE: {}'.format(r.json()))
                print("STATUS CODE: {}".format(r.status_code))

            #response validation
            if r.text != '':
                jsonResponse = r.json()
            else:
                jsonResponse = ''

            statusCode = r.status_code

            if statusCode in [200, 201, 202, 204]:
                statusCode = 0
                break
            else:
                retryCount += 1
                if retryCount > myNumOfRetries:
                    jsonResponse = None
                    break

        return jsonResponse, statusCode


if __name__ == '__main__':
    pass


