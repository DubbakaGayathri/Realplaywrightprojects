from pom.logintest import loginpage

def test_successlogin(page):
    login_page=loginpage(page)
    login_page.test_login("tomsmith", "SuperSecretPassword!")