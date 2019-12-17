from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from urllib import response, request
from urllib.error import URLError, HTTPError

url = 'http://127.0.0.1:8000/login/'

def test_login(url):
    """
    Test Login with mockup username and password to see if the application 
    recognizes the wrong data input and stays in the login page.
    """
    username = "test"
    password = "hello12345"

    browser = webdriver.Chrome(executable_path='/Users/pawariswongsalung/Downloads/chromedriver')
    browser.get(url)

    username_field = browser.find_elements_by_id('id_username')
    pw_field = browser.find_elements_by_id('id_password')
    
    print("Username Field Element: ")
    print(username_field)

    print("Password Field Element: ")
    print(pw_field)

    username_field[0].send_keys(username)
    username_field[0].send_keys(Keys.RETURN)
    pw_field[0].send_keys(password)
    pw_field[0].send_keys(Keys.RETURN)

    print("The current url is still at login page because username and password is incorrect.")
    print(browser.current_url)
    browser.quit()


if __name__ == "__main__":
    test_login(url)