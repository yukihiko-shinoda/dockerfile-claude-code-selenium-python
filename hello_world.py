from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main():
    """For testing.

    - 2. Getting Started — Selenium Python Bindings 2 documentation
      https://selenium-python.readthedocs.io/getting-started.html
    """
    options = ChromeOptions()
    options.add_argument("--headless")
    driver = Chrome(options=options)
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()


if __name__ == "__main__":
    main()
