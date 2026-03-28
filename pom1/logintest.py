from pom1.loginpage import logintestpage

def test_login_success(page):
    login_page=logintestpage(page)
    login_page.loginpage("student","Password123")
