# Import the locators file
import sys
sys.path.append(sys.path[0] + "/..")
from pageobject.locators import locators
from pageobject.locators import *

from pageobject.helpers import helpers
from pageobject.helpers import *

@pytest.mark.usefixtures('driver')

class TestYoutubeScraping:
    def exemp_test_scrap_youtube(self, driver) -> list:
        # driver.get("https://www.youtube.com/@hjsblogger/videos")
        driver.get(locators.test_yt_url)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        # Create an instance of ActionChains
        actions = ActionChains(driver)

        # Explicit wait of 10 seconds
        wait = WebDriverWait(driver, 10)

        # Wait for 10 seconds till the Document State is not complete
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

        # Once the page has loaded, scroll to the end of the page to load all the videos
        # Scroll to the end of the page to load all the videos in the channel
        # Reference - https://stackoverflow.com/a/51702698/126105
        # Get scroll height
        start_height = driver.execute_script("return document.documentElement.scrollHeight")
        # print("Height is " + str(start_height))

        # Repeat scrolling until reaching the end of the page
        # Taking cues from my own blog https://www.lambdatest.com/blog/scraping-dynamic-web-pages/
        while True:
            # Scroll to the bottom of the page
            driver.execute_script("window.scrollTo(0, " + str(start_height) + ")")
            # Wait for the content to load
            time.sleep(2)
            scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
            if (scroll_height == start_height):
                # If heights are the same, we reached the end of page
                break
            # print("scroll_height = " + str(scroll_height))
            time.sleep(2)
            start_height = scroll_height

        time.sleep(2)

        elem_contents = driver.find_element(By.XPATH, locators.loc_contains)

        # We have reached end of page, let's count the rows with videos
        elem_video_rows = elem_contents.find_elements(By.CLASS_NAME,
                    locators.loc_rich_renderer)

        # num_videos = driver.find_elements(elem_video_rows)
        # print("Total number of row videos in " + test_url + " are " + str(len(elem_video_rows)))

        # Now that we have the number of rows, let's fetch the details
        # of each video on the respective rows

        meta_data_arr = []
        for video in elem_video_rows:
            #elem_ind_video_rows = video.find_elements(By.CSS_SELECTOR,
                #"#contents .style-scope.ytd-rich-grid-row")

            elem_ind_video_rows = video.find_elements(By.CSS_SELECTOR,
                    locators.loc_grid_row)
            
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
                    elem_5 = video_metadata_1.find_element(By.CSS_SELECTOR,
                        "#meta")
                    
                    elem_6 = elem_5.find_element(By.CSS_SELECTOR,
                        "#video-title")

                    elem_7 = elem_5.find_element(By.CSS_SELECTOR,
                        "#metadata > #metadata-line > span:nth-child(3)")
                    
                    elem_8 = elem_5.find_element(By.CSS_SELECTOR,
                        "#metadata > #metadata-line > span:nth-child(4)")
                    
                    video_title = elem_6.get_attribute('innerText')
                    video_views = elem_7.get_attribute('innerText')
                    video_time = elem_8.get_attribute('innerText')

                    # Create a dictionary of the video meta-data
                    meta_data_dict = {
                        'video title': video_title,
                        'video views': video_views,
                        'video duration': video_time
                    }
                    
                    meta_data_arr.append(meta_data_dict)
        
        # print_scrapped_yt_content(meta_data_arr)
        # for elem_info in meta_data_arr:
        #    print(elem_info)
        helpers.print_scrapped_content(meta_data_arr)

    def test_scrap_youtube(self, driver) -> list:
        meta_data_arr=[]
        driver.get(locators.test_yt_url)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        # Create an instance of ActionChains
        # actions = ActionChains(driver)

        # Explicit wait of 10 seconds
        # wait = WebDriverWait(driver, 10)

        meta_data_arr = helpers.scrap_yt_content(driver)
        helpers.print_scrapped_content(meta_data_arr)