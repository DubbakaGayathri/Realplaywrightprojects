from playwright.sync_api import Playwright

def test_getreq(playwright:Playwright):
    base_url="https://restful-booker.herokuapp.com"
    request_context=playwright.request.new_context()
    response=request_context.get(f"{base_url}/booking/1979")
    assert response.ok
    assert response.status==200
    response_body=response.json()
    print(response_body)