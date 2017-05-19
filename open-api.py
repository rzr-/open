#! /usr/bin/env python3
import requests, pytest
api_url = "http://kn-ktapp.herokuapp.com/apitest/accounts"

def get_data (id=None):
	url = api_url 
	if id:
		url += "/" + str(id)
	try :
		response = requests.get(url)
	except requests.exceptions.RequestException as e:
		print (e)
	return response

def test_get_data():
    response = get_data()
    assert response.status_code == 200

    response = get_data(12345678)
    assert response.status_code == 200

    response = get_data(12)
    assert response.status_code == 200


accounts_info = get_data()
if accounts_info.status_code == 200:
	print (accounts_info.json())
