from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def verify_alert_lgpd(browser):
    return len(browser.find_elements_by_tag_name('app-lgpd-tou')) >= 1


def accept_lgpd(browser, alert_lgpd_are_available=False):
    if not alert_lgpd_are_available:
        return f"There is no lgpd terms alert"
    else:
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable \
                ((By.XPATH, "//button[@type='button'][text()=' Concordo e Aceito ']"))).click()
        return f"Lgpd terms were accepted"


def get_list_of_certificates(browser):
    #  browser.find_elements(By.XPATH, "//img[]")
    return [_.get_attribute("alt") for _ in browser.find_elements \
            (By.XPATH, "//img[@class='course-image']")]


def verify_if_element_is_in_the_list(list_of_images, element='text'):
    if element in list_of_images:
        return f"{element} is in the list"
    return f"{element} is not in the list"


if __name__ == '__main__':
    page_url = 'https://fpftech.com/principal'
    browser = webdriver.Chrome(ChromeDriverManager().install())    
    browser.get(page_url)

    print(accept_lgpd(browser, alert_lgpd_are_available=verify_alert_lgpd(browser)))
    print(verify_if_element_is_in_the_list(get_list_of_certificates(browser), "CSM"))

