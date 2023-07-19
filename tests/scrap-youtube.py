from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# Replaced with Explicit Waits
import time

# Import the locators file
import sys
sys.path.append(sys.path[0] + "/..")
from pageobject.locators import locators

def scrap_youtube(test_url) -> list:
    options = ChromeOptions()

    # Refer https://www.selenium.dev/blog/2023/headless-is-going-away/ for the new way
    # to trigger browser in headless mode

    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    driver.get(test_url)

    # Commented once the tests are executed in non-headless mode
    driver.maximize_window()

    # Create an instance of ActionChains
    actions = ActionChains(driver)

    # Explicit wait of 10 seconds
    wait = WebDriverWait(driver, 10)

    # wait.Until(d => ((IJavaScriptExecutor)d).ExecuteScript("return document.readyState").Equals("complete"));
    # Wait for 10 seconds till the Document State is not complete
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
 

    # Once the page has loaded, scroll to the end of the page to load all the videos
    # Scroll to the end of the page to load all the videos in the channel
    # Reference - https://stackoverflow.com/a/51702698/126105
    # Get scroll height
    start_height = driver.execute_script("return document.documentElement.scrollHeight")
    print("Height is " + str(start_height))

    meta_data_arr = []

    # Repeat scrolling until reaching the end of the page
    while True:
        # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, " + str(start_height) + ")")
        time.sleep(2)  # Wait for the content to load
        scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
        if (scroll_height == start_height):
            # If heights are the same, we reached the end of page
            print("End of page reached")
            break
        # print("scroll_height = " + str(scroll_height))
        time.sleep(2)
        start_height = scroll_height

    time.sleep(2)

    elem_contents = driver.find_element(By.XPATH, "//*[@id='contents']")

    # We have reached end of page, let's count the rows with videos
    elem_video_rows = elem_contents.find_elements(By.CLASS_NAME,
            "style-scope.ytd-rich-grid-renderer")
    # num_videos = driver.find_elements(elem_video_rows)
    # print("Total number of row videos in " + test_url + " are " + str(len(elem_video_rows)))

    # Now that we have the number of rows, let's fetch the details
    # of each video on the respective rows

    meta_data_arr = []
    for video in elem_video_rows:
        #elem_ind_video_rows = video.find_elements(By.CSS_SELECTOR,
            #"#contents .style-scope.ytd-rich-grid-row")

        elem_ind_video_rows = video.find_elements(By.CSS_SELECTOR,
            "ytd-rich-item-renderer.style-scope.ytd-rich-grid-row")
        
        # print("Individual Rows = " + str(len(elem_ind_video_rows)))

        for video_metadata in elem_ind_video_rows:
            elem_1 = video_metadata.find_element(By.CSS_SELECTOR,
                "#content .style-scope.ytd-rich-item-renderer")
            # print("elem_1" + str(elem_1))
            
            elem_2 = elem_1.find_element(By.CSS_SELECTOR,
                "ytd-rich-grid-media.style-scope.ytd-rich-item-renderer")
            
            # elem_3 = elem_2.find_element(By.CSS_SELECTOR,
            #    "#dismissible .style-scope.ytd-rich-grid-media")
            
            elem_4 = elem_2.find_elements(By.CSS_SELECTOR,
                "#dismissible > #details")
            
            for video_metadata_1 in elem_4:
                # elem_5 = elem_4.find_element(By.XPATH,
                #    "//*[@id='meta']")

                elem_5 = video_metadata_1.find_element(By.CSS_SELECTOR,
                    "#meta")
                
                elem_6 = elem_5.find_element(By.CSS_SELECTOR,
                    "#video-title")

                elem_7 = elem_5.find_element(By.CSS_SELECTOR,
                    "#metadata > #metadata-line > span:nth-child(3)")
                
                elem_8 = elem_5.find_element(By.CSS_SELECTOR,
                    "#metadata > #metadata-line > span:nth-child(4)")
                
                video_title = elem_6.get_attribute('innerText')
                # print(video_title)

                video_views = elem_7.get_attribute('innerText')
                # print(video_views)

                video_time = elem_8.get_attribute('innerText')
                # print(video_time)

                # Create a dictionary of the video meta-data
                meta_data_dict = {
                    'video title': video_title,
                    'video views': video_views,
                    'video duration': video_time
                }
                
                meta_data_arr.append(meta_data_dict)

    driver.quit()
    return meta_data_arr

def main():
    # meta_data_arr = scrap_youtube("https://www.youtube.com/@hjsblogger/videos")
    meta_data_arr = scrap_youtube("https://www.youtube.com/@lambdatest/videos")
    # Print array elements on new lines
    for elem_info in meta_data_arr:
        print(elem_info)

if __name__ == '__main__':
    main()