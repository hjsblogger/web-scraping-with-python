from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Replaced with Explicit Waits
# import time

# Import the locators file
import sys
sys.path.append(sys.path[0] + "/..")
from pageobject.locators import locators

def scrap_ecommerce(test_url) -> list:
    options = ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get(test_url)

    #This will be commented once the tests are executed in non-headless mode
    driver.maximize_window()

    # Create an instance of ActionChains
    actions = ActionChains(driver)

    # Explicitly wait for an element to be visible
    wait = WebDriverWait(driver, 10)

    # 
    element = wait.until(EC.visibility_of_element_located((By.XPATH,
            locators.shopcategory)))

    # element = driver.find_element(By.XPATH, "//a[contains(.,'Shop by Category')]")

    # Perform a series of actions using ActionChains
    actions.move_to_element(element).click().perform()

    # element_category = driver.find_element(By.XPATH, "//span[contains(.,'Phone, Tablets & Ipod')]")
    element_category = wait.until(EC.visibility_of_element_located((By.XPATH,
            locators.phonecategory)))

    # Perform a series of actions using ActionChains
    actions.move_to_element(element_category).click().perform()
    
    # Better to wait till the respective element is visible
    nested_elements = wait.until(EC.visibility_of_element_located((By.XPATH,
        "//div[@id='entry_212391']//div[@id='entry_212408']//div[@class='row']")))
    
    
    actual_items = nested_elements.find_elements(By.CLASS_NAME,
            "product-layout.product-grid.no-desc.col-xl-4.col-lg-4.col-md-4.col-sm-6.col-6")

    count = len(actual_items)
    print("Number of elements found:" + str(count) + ".\n")

    meta_data_arr = []
    for ind_elem_props in actual_items:
        # nested_img_elem = ind_elem_props.find_element(By.CSS_SELECTOR,
        #    "div.product-thumb > div.product-thumb-top > div.image")
        
        ################ Product Image Link ################
        # item_image = nested_img_elem.find_element(By.XPATH,
        #    "//*[contains(@id, 'mz-product-grid-image')]")

        nested_prodname_elem = ind_elem_props.find_element(By.CSS_SELECTOR,
            "div.product-thumb > div.caption")
        
        ################ Product Name ################
        nested_title_elem = nested_prodname_elem.find_element(By.CSS_SELECTOR,
                ".title .text-ellipsis-2")
        
        ################ Price #######################
        nested_price_elem = nested_prodname_elem.find_element(By.CSS_SELECTOR,
                ".price .price-new")

        # Create a dictionary of the meta-data of the items on e-commerce store
        meta_data_dict = {
            'product image': nested_title_elem.get_attribute('href'),
            'product name': nested_title_elem.text,
            'product price': nested_price_elem.text
        }
        
        meta_data_arr.append(meta_data_dict)

    driver.quit()
    return meta_data_arr

def main():
    meta_data_arr = scrap_ecommerce("https://ecommerce-playground.lambdatest.io/")

    # Print array elements on new lines
    for elem_info in meta_data_arr:
        print(elem_info)

if __name__ == '__main__':
    main()