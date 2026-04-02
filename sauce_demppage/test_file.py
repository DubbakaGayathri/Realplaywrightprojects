from sauce_demppage.loginpage import loginpage
from sauce_demppage.homepage import homepage

def test_login(page):
    login_page=loginpage(page)
    home_page=homepage(page)
    login_page.login_test("standard_user","secret_sauce")
    home_page.all_products_count()
    home_page.all_products_names()
    home_page.add_product("Sauce Labs Bike Light")
    home_page.click_cart()
    home_page.open_menu()
    home_page.logout()


