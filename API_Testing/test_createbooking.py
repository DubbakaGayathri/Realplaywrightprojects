from playwright.sync_api import Playwright,expect

def test_create_booking(playwright:Playwright):
    base_url="https://restful-booker.herokuapp.com"
    request_context=playwright.request.new_context()
    request_body={
                 "firstname": "Sally",
                 "lastname": "Brown",
                 "totalprice": 111,
                 "depositpaid": True,
                 "bookingdates": {
                 "checkin": "2013-02-23",
                 "checkout": "2014-10-23"
                 },
                 "additionalneeds": "Breakfast"
    }
    response = request_context.post(f"{base_url}/booking",data=request_body)

    response_body=response.json()
    print(response_body)

    assert "bookingid" in response_body
    assert "booking" in response_body

    booking=response_body["booking"]
    assert booking["firstname"]=="Sally"
    assert  booking["bookingdates"]["checkin"]=="2013-02-23"




