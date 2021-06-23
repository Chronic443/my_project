# We will import Client module so that we can set up our connection
from django.test import Client
# We will import reverse so that we can get the url to our views
from django.urls import reverse


# Define a test for our add endpoint
def test_add():
    # use client to create a connection
    client = Client()
    # from client use post method and get the url with reverse method by giving it a view name.
    # Pass parameters to it num01 and num02 and provide them with values
    # Set HTTP_AUTHORIZATION header to our token
    response = client.post(reverse(viewname='add'),
                           {'num01': '2', 'num02': '2'},
                           HTTP_AUTHORIZATION='JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF')

    # assert that the return values from the endpoint comply with the expected values that we define
    # you can perform multiple asserts and test out for various things.
    assert response.status_code == 200 and float(response.content) == 4


# Define a test for our sub endpoint
def test_sub():
    # use client to create a connection
    client = Client()
    # from client use post method and get the url with reverse method by giving it a view name.
    # Pass parameters to it num01 and num02 and provide them with values
    # Set HTTP_AUTHORIZATION header to our token
    response = client.post(reverse(viewname='sub'),
                           {'num01': '2', 'num02': '2'},
                           HTTP_AUTHORIZATION='JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF')

    # assert that the return values from the endpoint comply with the expected values that we define
    # you can perform multiple asserts and test out for various things.
    assert response.status_code == 200 and float(response.content) == 0


# Define a test for our div endpoint
def test_div():
    # use client to create a connection
    client = Client()
    # from client use post method and get the url with reverse method by giving it a view name.
    # Pass parameters to it num01 and num02 and provide them with values
    # Set HTTP_AUTHORIZATION header to our token
    response = client.post(reverse(viewname='div'),
                           {'num01': '2', 'num02': '2'},
                           HTTP_AUTHORIZATION='JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF')

    # assert that the return values from the endpoint comply with the expected values that we define
    # you can perform multiple asserts and test out for various things.
    assert response.status_code == 200 and float(response.content) == 1


# Define a test for our multi endpoint
def test_multi():
    # use client to create a connection
    client = Client()
    # from client use post method and get the url with reverse method by giving it a view name.
    # Pass parameters to it num01 and num02 and provide them with values
    # Set HTTP_AUTHORIZATION header to our token
    response = client.post(reverse(viewname='multi'),
                           {'num01': '2', 'num02': '2'},
                           HTTP_AUTHORIZATION='JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF')

    # assert that the return values from the endpoint comply with the expected values that we define
    # you can perform multiple asserts and test out for various things.
    assert response.status_code == 200 and float(response.content) == 4
