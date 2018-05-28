
def assert_status_code(self, status):
    if status == 200 or status == 201 or status == 202:
        print "Test Passed - Successfull " + str(status)
    elif status == 400 or status == 401 or status == 402 or status == 403 or status == 404:
        print "Test Failed - client error " + str(status) 
    elif status == 500 or status == 501 or status == 502:
        print "Test Failed - Server error " + str(status)
