a = 5
b = 5

string1 = "Five"

import requests
import time

def sumTwo():

    # the base URL
    base_url = 'http://localhost:8000'
    # if you are using the emulator, probably the base_url will be:
    # base_url = 'http://localhost:8000'

    # example username, generated by following https://developers.meethue.com/develop/get-started-2/
    username = 'newdeveloper'
    # if you are using the emulator, the username is:
    # username = 'newdeveloper'

    # lights URL
    lights_url = base_url + '/api/' + username + '/lights/'

    # get the Hue lights (as JSON)
    all_the_lights = requests.get(lights_url).json()

    for i in range(0, 10):

        light2 = "2"
        url_to_call = lights_url + light2 + '/state'
        body = {'on': True, 'effect': 'colorloop'}
        requests.put(url_to_call, json=body)

        for i in range(0, 5):
            time.sleep(1)
            print(5 - i)

        for light in all_the_lights:
            url_to_call = lights_url + light + '/state'
            body = {'on': False}
            requests.put(url_to_call, json=body)

        light3 = "3"
        url_to_call = lights_url + light3 + '/state'
        body = {'on': True, 'effect': 'colorloop'}
        requests.put(url_to_call, json=body)

        for i in range(0, 5):
            time.sleep(1)
            print(5 - i)

        for light in all_the_lights:
            url_to_call = lights_url + light + '/state'
            body = {'on': False}
            requests.put(url_to_call, json=body)
    i+1

    return string1