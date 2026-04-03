import json

from playwright.sync_api import Playwright,expect

def test_create_usingjson(playwright:Playwright):
    base_url="https://restful-booker.herokuapp.com"
    request_context=playwright.request.new_context()
    file=open("testdata/create_booking.json","r")
    request_body=json.load(file)
    response=request_context.post(f"{base_url}/booking",data=request_body)
    assert response.ok
    assert response.status==200
    response_body=response.json()
    print(response_body)
    assert "bookingid" in response_body
    assert "booking" in response_body
    booking=response_body["booking"]
    assert booking["lastname"]=="Brown"
