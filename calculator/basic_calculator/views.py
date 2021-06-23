from django.http import HttpResponse
from django.views import View
import json


# AUTH_TOKEN will be used to store our authentication token that is required to be passed at request time as a header Auth-Token
AUTH_TOKEN = "JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF"


# This is a small function that will comapre the passed token to the app token and perform evaluation
def authenticate(token):
    if token == AUTH_TOKEN:
        return True
    else:
        return False


# The view can be tested with (optional)
# curl -X GET -d '{"num01":"2", "num02":"2"}' http://127.0.0.1:8000/basic_calculator/add/
# curl -X GET -H "Auth-Token: JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF" -d '{"num01":"2", "num02":"2"}' http://127.0.0.1:8000/basic_calculator/add/
# We will define a class based view AddView
class AddView(View):
    # We define a post method
    def post(self, request, *args, **kwargs):
        # We check for the token in the Authorization Header and if it matches then all is goo and we can continue
        if not authenticate(request.headers['Authorization']):
            return HttpResponse(status=403)

        # within the method we will extract num01 and num02 from the request, conver them to json, so we can easily extract the values and convert them to floats
        num01 = float(request.POST['num01'])
        num02 = float(request.POST['num02'])

        # In the end num01 and num02 will be added as floats and the result will be returned as a HttpResponse.
        return HttpResponse(num01+num01)

        #return HttpResponse(num01 + num02)

    # Within the the class a get method will be written
    def get(self, request):
        # Here we will check what the return value of our authenticate function is and if it is False the response will be 403 Forbidden

        print(request.headers)

        if not authenticate(request.headers['Auth-Token']):
            return HttpResponse(status=403)

        # within the method we will extract num01 and num02 from the request, conver them to json, so we can easily extract the values and convert them to floats
        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])

        print("Num01", num01)

        # In the end num01 and num02 will be added as floats and the result will be returned as a HttpResponse.
        return HttpResponse(num01 + num02)


# The view can be tested with (optional)
# curl -X GET -d '{"num01":"2", "num02":"2"}' http://127.0.0.1:8000/basic_calculator/sub/
# curl -X GET -H "Auth-Token: JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF" -d '{"num01":"2", "num02":"2"}' http://127.0.0.1:8000/basic_calculator/sub/
# SubViw will be defined a class based view
class SubView(View):
    # We define a post method
    def post(self, request, *args, **kwargs):
        # We check for the token in the Authorization Header and if it matches then all is goo and we can continue
        if not authenticate(request.headers['Authorization']):
            return HttpResponse(status=403)

        # within the method we will extract num01 and num02 from the request, conver them to json, so we can easily extract the values and convert them to floats

        num01 = float(request.POST['num01'])
        num02 = float(request.POST['num02'])

        # instead of adding number we will proceed to subtract numbers and then return the result as an HttpResponse.
        return HttpResponse(num01 - num01)

    # Within the class a get method will be defined
    def get(self, request):
        # Here we will check what the return value of our authenticate function is and if it is False the response will be 403 Forbidden
        if not authenticate(request.headers['Auth-Token']):
            return HttpResponse(status=403)

        # Here we will repeat the extraction process from the previous class AddView
        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])

        # instead of adding number we will proceed to subtract numbers and then return the result as an HttpResponse.
        return HttpResponse(num01 - num02)


# The view can be tested with (optional)
# curl -X GET -d '{"num01":"2", "num02":"2"}' http://127.0.0.1:8000/basic_calculator/div/
# curl -X GET -H "Auth-Token: JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF" -d '{"num01":"2", "num02":"2"}' http://127.0.0.1:8000/basic_calculator/div/
# Class based view DivView will be defined
class DivView(View):
    # We define a post method
    def post(self, request, *args, **kwargs):
        # We check for the token in the Authorization Header and if it matches then all is goo and we can continue
        if not authenticate(request.headers['Authorization']):
            return HttpResponse(status=403)

        # within the method we will extract num01 and num02 from the request, conver them to json, so we can easily extract the values and convert them to floats
        num01 = float(request.POST['num01'])
        num02 = float(request.POST['num02'])

        # We will need to do an extra check here stating that num02 cannot be 0 as you cannot divide by 0, so only if num02 is not a zero can we perform the division
        if num02 == 0.0:
            return HttpResponse("Cannot divide by 0")
        else:
            return HttpResponse(num01 / num02)

    # In the class a get method will be defined
    def get(self, request):
        # Here we will check what the return value of our authenticate function is and if it is False the response will be 403 Forbidden
        if not authenticate(request.headers['Auth-Token']):
            return HttpResponse(status=403)

        # The same data extraction process will be repeated for num01 and num02
        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])

        # We will need to do an extra check here stating that num02 cannot be 0 as you cannot divide by 0, so only if num02 is not a zero can we perform the division
        if num02 == 0.0:
            return HttpResponse("Cannot divide by 0")
        else:
            return HttpResponse(num01 / num02)


# The view can be tested with (optional)
# curl -X GET -d '{"num01":"2", "num02":"2"}' http://127.0.0.1:8000/basic_calculator/multi/
# curl -X GET -H "Auth-Token: JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF" -d '{"num01":"2", "num02":"2"}' http://127.0.0.1:8000/basic_calculator/multi/
# Class based view MultiView will be defined
class MultiView(View):
    # We define a post method
    def post(self, request, *args, **kwargs):
        # We check for the token in the Authorization Header and if it matches then all is goo and we can continue
        if not authenticate(request.headers['Authorization']):
            return HttpResponse(status=403)

        # The same data extraction process will be repeated for num01 and num02
        num01 = float(request.POST['num01'])
        num02 = float(request.POST['num02'])

        # No need to perform the same checks as with the division, we can simply proceed to multiply the two numbers
        return HttpResponse(num01 * num01)

    # Get method within the class will be defined
    def get(self, request):
        # Here we will check what the return value of our authenticate function is and if it is False the response will be 403 Forbidden
        if not authenticate(request.headers['Auth-Token']):
            return HttpResponse(status=403)

        # The same data extraction process will be repeated for num01 and num02
        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])

        # No need to perform the same checks as with the division, we can simply proceed to multiply the two numbers
        return HttpResponse(num01 * num02)
