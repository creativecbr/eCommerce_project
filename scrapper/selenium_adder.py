from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

adm_site = 'https://3.209.82.53/admubrokeit/index.php/sell/catalog/products'

# ENTER LOGIN AND PASSWORD
presta_mail = "sklep.ubrokeit@gmail.com"
presta_password = "Biznes123$"

# CHOOSE FILE
fileToSend = 'D:\\Studia\\sem5\\be\\scrapper\\serwis_xiaomi.csv'

# SET 
WHAT_KIND_OF_IMPORT = "Produkt"

browser  = webdriver.Chrome(ChromeDriverManager().install())
browser.get(adm_site)
browser.maximize_window()

#fill 
browser.find_element_by_name("email").send_keys(presta_mail)
browser.find_element_by_name("passwd").send_keys(presta_password)
#submit
browser.find_element_by_id("submit_login").click()

#find products
wait = WebDriverWait(browser, 10)
men_menu = wait.until(ec.visibility_of_element_located((By.ID, "subtab-AdminCatalog")))
browser.find_element_by_id("subtab-AdminCatalog").click()
time.sleep(1)
browser.find_element_by_link_text("Produkty").click()

#find import
wait = WebDriverWait(browser, 10)
men_menu = wait.until(ec.visibility_of_element_located((By.ID, "catalog-tools-button")))
browser.find_element_by_id("catalog-tools-button").click()
time.sleep(1)
browser.find_element_by_id("desc-product-import").click()

#set dropdown
wait = WebDriverWait(browser, 10)
men_menu = wait.until(ec.visibility_of_element_located((By.XPATH, "//select[@name='entity']")))

if WHAT_KIND_OF_IMPORT == "Produkt":    
    browser.find_element_by_xpath("//select[@name='entity']/option[text()='Produkty']").click()
if WHAT_KIND_OF_IMPORT == "Kategorie":    
    browser.find_element_by_xpath("//select[@name='entity']/option[text()='Kategorie']").click()
if WHAT_KIND_OF_IMPORT == "Kombinacje":    
    browser.find_element_by_xpath("//select[@name='entity']/option[text()='Kombinacje']").click()
#set file
browser.find_element_by_id("file").send_keys(fileToSend)
#submit
wait = WebDriverWait(browser, 10)
men_menu = wait.until(ec.visibility_of_element_located((By.XPATH, "//p[@class='alert-text js-import-file']")))
browser.find_element_by_name("submitImportFile").click()

#start importing
wait = WebDriverWait(browser, 10)
men_menu = wait.until(ec.visibility_of_element_located((By.XPATH, "//select[@id='valueImportMatchs']")))
browser.find_element_by_xpath("//select[@id='valueImportMatchs']/option[text()='produkty2']").click()
browser.find_element_by_id("loadImportMatchs").click()
time.sleep(2)
browser.find_element_by_id("import").click()
