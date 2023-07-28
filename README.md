# Web Scraping with Selenium Python and Beautiful Soup

<img width="1000" height="500" alt="Bulb" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/f178de16-2749-4997-9fe7-348a46e45835">

<div align="center"><a href="https://scrape-it.cloud/assets/blog_img/web-scraping-with-python.png">Image Credit</a></div>
<br/>

In this 'Web Scraping with Python' repo, we have covered the following usecases:

* <b>Web Scraping using Selenium PyUnit</b>
* <b>Web Scraping using Selenium Pytest</b>
* <b>Web Scraping of dynamic website using Beautiful Soup and Selenium</b>

The following websites are used for the purpose of demoing web scraping:

* [LambdaTest YouTube Channel](https://www.youtube.com/@lambdatest/videos)
* [LambdaTest E-commerce Playground](https://ecommerce-playground.lambdatest.io/)
* [Scraping Club Infinite Scroll Website](https://scrapingclub.com/exercise/list_infinite_scroll/)

<img width="20" height="20" alt="Bulb" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/52f062e0-239e-4131-bde5-5bb8cb218d7b">As mentioned online, scraping public web data from YouTube is legal as long as you don't go after information that is not available to the general public. However, there might be cases where the YouTube scraping might throw errors (or exceptions) when scraping is done on the Cloud Selenium Grid.

## Pre-requisites for test execution

**Step 1**

Create a virtual environment by triggering the *virtualenv venv* command on the terminal

```bash
virtualenv venv
```
<img width="1418" alt="VirtualEnvironment" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/c714a0a9-aaf6-43ee-9bdc-cc6e8dd83134">

**Step 2**

Navigate the newly created virtual environment by triggering the *source venv/bin/activate* command on the terminal

```bash
source venv/bin/activate
```

Follow steps(3) and (4) for performing web scraping on LambdaTest Cloud Grid:

**Step 3**

Procure the LambdaTest User Name and Access Key by navigating to [LambdaTest Account Page](https://accounts.lambdatest.com/security). You might need to create an an account on LambdaTest since it is used for running tests (or scraping) on the cloud Grid.

<img width="1288" alt="LambdaTestAccount" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/fedbd2b8-73c3-4358-b162-01cf52b652b8">

**Step 4**

Add the LambdaTest User Name and Access Key in the *Makefile* that is located in the parent directory. Once done, save the Makefile.

![MakeFileChange](https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/55613de8-87e9-4cb3-8098-91f5edbd316f)

## Dependency/Package Installation

Run the *make install* command on the terminal to install the desired packages (or dependencies) - Pytest, Selenium, Beautiful Soup, etc.

```bash
make install
```
<img width="1404" alt="Make-Install" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/4df933da-22b1-4bea-94a2-1f90c602ee5f">

<img width="1404" alt="Make-Install-2" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/a671572f-c995-4261-9905-c96682e4219b">

With this, all the dependencies and environment variables are set. We are all set for web scraping with the desired frameworks (i.e. Pyunit, Pytest, and Beautiful Soup)

## Web Scraping using Selenium PyUnit (Local Execution)

The following websites are used for demonstration:

* [LambdaTest YouTube Channel](https://www.youtube.com/@lambdatest/videos)
* [LambdaTest E-commerce Playground](https://ecommerce-playground.lambdatest.io/)

Follow the below mentioned steps to perform scraping on local machine:

**Step 1**

Set *EXEC_PLATFORM* environment variable to *local*. Trigger the command *export EXEC_PLATFORM=local* on the terminal.

<img width="1043" alt="Make-Local" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/bd8772c8-b73c-4e71-b24d-e49101f38b20">

**Step 2**

Trigger the command *make clean* to clean the remove _pycache_ folder(s) and .pyc files

<img width="710" alt="Make-Clean" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/39178f69-187a-4b74-ac8a-7c45409e2457">

**Step 3**

The Chrome browser is invoked in the Headless Mode. It is recommended to install Chrome on your machine before you proceed to Step(3)

**Step 4**

Trigger the *make scrap-using-pyunit* command on the terminal to scrap content from the above mentioned websites

<img width="1404" alt="Pyunit-Scraping-1" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/5ca5fd6b-4491-4568-a838-6cacaab634a7">

<img width="1404" alt="Pyunit-Scraping-2" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/e66f1160-e860-4a04-8fc1-0bb3cc40b05e">

As seen above, the content from LambdaTest YouTube channel and LambdaTest e-commerce playground are scrapped successfully!

## Web Scraping using Selenium Pytest (Local Execution)

The following websites are used for demonstration:

* [LambdaTest YouTube Channel](https://www.youtube.com/@lambdatest/videos)
* [LambdaTest E-commerce Playground](https://ecommerce-playground.lambdatest.io/)

Follow the below mentioned steps to perform scraping on local machine:

**Step 1**

Set *EXEC_PLATFORM* environment variable to *local*. Trigger the command *export EXEC_PLATFORM=local* on the terminal.

<img width="1043" alt="Make-Local" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/bd8772c8-b73c-4e71-b24d-e49101f38b20">

**Step 2**

The Chrome browser is invoked in the Headless Mode. It is recommended to install Chrome on your machine before you proceed to Step(4)

**Step 3**

Trigger the command *make clean* to clean the remove _pycache_ folder(s) and .pyc files

<img width="710" alt="Make-Clean" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/39178f69-187a-4b74-ac8a-7c45409e2457">

**Step 4**

Trigger the *make scrap-using-pytest* command on the terminal to scrap content from the above mentioned websites

<img width="1405" alt="Pytest-scraping-1" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/7e38f482-2612-41d1-b03f-83986ab78104">

<img width="1405" alt="Pytest-scraping-2" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/3ea0734c-190b-43ef-827b-14e5eb463af9">

## Web Scraping using Beautiful Soup

Beautiful Soup is a Python library that is majorly used for screen-scraping (or web scraping). More information about the library is available on [Beautiful Soup HomePage](https://www.crummy.com/software/BeautifulSoup/)

The Beautiful Soup (bs4) library is already installed as a part of *pre-requisite steps*. Hence, it is safe to proceed with the scraping with Beautiful Soup. *[Scraping Club Infinite Scroll Website]*(https://scrapingclub.com/exercise/list_infinite_scroll/)) has infinite scrolling pages and Selenium is used to scroll to the end of the page so that all the items on the page can be scraped using the said libraries.

The following websites are used for demonstration:

* [LambdaTest E-commerce Playground](https://ecommerce-playground.lambdatest.io/)
* [Scraping Club Infinite Scroll Website](https://scrapingclub.com/exercise/list_infinite_scroll/))

Follow the below mentioned steps to perform web scraping using Beautiful Soup(bs4):

**Step 1**

Set *EXEC_PLATFORM* environment variable to *local*. Trigger the command *export EXEC_PLATFORM=local* on the terminal.

<img width="1043" alt="Make-Local" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/bd8772c8-b73c-4e71-b24d-e49101f38b20">

**Step 2**

Trigger the *make scrap-using-beautiful-soup* command on the terminal to scrap content from the above mentioned websites

<img width="1402" alt="scraping-bs4-1" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/7308b93b-1420-4d99-bb01-9d73c25bdf13">

<img width="1402" alt="scraping-bs4-2" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/f028573a-ff50-4fd5-9914-e003cde8e355">

<img width="1402" alt="scraping-bs4-3" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/ea93a7eb-e814-4f6a-93ff-8db6ed31cc41">

<img width="1413" alt="scraping-bs4-4" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/bda90673-f477-4b57-8a6c-b44530ed06f5">

<img width="1413" alt="scraping-bs4-5" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/f6a70ef5-1c2c-4dc8-a284-3de0cdc5ea80">

As seen from the above screenshots, content on Pages (1) thru' (5) on *LambdaTest E-Commerce Playground](https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=57) are successfully displayed on the console.

<img width="1413" alt="infinite-1" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/4cc3eef1-ec31-467a-9747-ba811f793c7e">

<img width="1097" alt="infinite-2" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/f6f8f28d-c96f-425f-8e9c-f068620c9a7a">

Also, all the 60 items on [Scraping Club Infinite Scroll Website](https://scrapingclub.com/exercise/list_infinite_scroll/) are scraped without any issues.

## Web Scraping using Selenium Cloud Grid and Python

<b>Note</b>: As mentioned earlier, there could be cases where YouTube Scraping might fail on cloud grid (particularly when there are a number of attempts to scrape the content). Since cookies and other settings are cleared (or sanitized) after every test session, YouTube might take genuine web scraping as a Bot Attack! In such cases, you might across the following page where cookie consent has to be given by clicking on "Accept all" button.

<img width="1407" alt="Accept-All" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/38c7e399-c4d6-4961-b95b-077d83a9ab74">

You can find more information about this insightful [Stack Overflow thread](https://stackoverflow.com/questions/66902404/selenium-python-click-agree-to-youtube-cookie)

Since we are using LambdaTest Selenium Grid for test execution, it is recommended to create an acccount on [LambdaTest](https://www.lambdatest.com/?fp_ref=himanshu15) before proceeding with the test execution. Procure the LambdaTest User Name and Access Key by navigating to [LambdaTest Account Page](https://accounts.lambdatest.com/security).

<img width="1288" alt="LambdaTestAccount" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/fedbd2b8-73c3-4358-b162-01cf52b652b8">

### Web Scraping using Selenium Pyunit (Cloud Execution)

The following websites are used for demonstration:

* [LambdaTest YouTube Channel](https://www.youtube.com/@lambdatest/videos)
* [LambdaTest E-commerce Playground](https://ecommerce-playground.lambdatest.io/)

Follow the below mentioned steps to perform scraping on LambdaTest cloud grid:

**Step 1**

Set *EXEC_PLATFORM* environment variable to *cloud*. Trigger the command *export EXEC_PLATFORM=cloud* on the terminal.

<img width="1396" alt="Terminal" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/63fa7c81-b69d-4e37-b1e2-39d6b2dd3b01">

**Step 2**

Trigger the command *make clean* to clean the remove _pycache_ folder(s) and .pyc files

<img width="710" alt="Make-Clean" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/39178f69-187a-4b74-ac8a-7c45409e2457">

**Step 3**

Trigger the *make scrap-using-pyunit* command on the terminal to scrap content from the above mentioned websites

<img width="1410" alt="Pyunit-cloud-1" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/96a5f5dd-2ea5-4621-81ad-461f6f94abeb">

<img width="1410" alt="Pyunit-cloud-2" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/b916ca1e-8d48-4280-9474-823d5df01f3a">

<img width="1410" alt="Pyunit-cloud-3" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/e4487f07-81e3-474c-93c6-43c6249df30d">


As seen above, the content from LambdaTest YouTube channel and LambdaTest e-commerce playground are scrapped successfully! You can find the status of test execution in the [LambdaTest Automation Dashboard](https://automation.lambdatest.com/build).

<img width="1422" alt="Pyunit-LambdaTest-Status-1" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/058ec7d3-a955-4e95-8b02-7da984cf83b8">

<img width="1422" alt="Pyunit-LambdaTest-Status-2" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/cb97da79-7307-4e75-8616-01333dea5538">

As seen above, the status of test execution is "Completed". Since the browser is instantiated in the *Headless* mode, the video recording is not available on the dashboard.

### Web Scraping using Selenium Pytest (Cloud Execution)

The following websites are used for demonstration:

* [LambdaTest YouTube Channel](https://www.youtube.com/@lambdatest/videos)
* [LambdaTest E-commerce Playground](https://ecommerce-playground.lambdatest.io/)

Follow the below mentioned steps to perform scraping on LambdaTest cloud grid:

**Step 1**

Set *EXEC_PLATFORM* environment variable to *cloud*. Trigger the command *export EXEC_PLATFORM=cloud* on the terminal.

<img width="1396" alt="Terminal" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/63fa7c81-b69d-4e37-b1e2-39d6b2dd3b01">

**Step 2**

Trigger the command *make clean* to clean the remove _pycache_ folder(s) and .pyc files

<img width="710" alt="Make-Clean" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/39178f69-187a-4b74-ac8a-7c45409e2457">

**Step 3**

Trigger the *make scrap-using-pytest* command on the terminal to scrap content from the above mentioned websites

<img width="1410" alt="Pytest-cloud-1" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/7dca2fbd-b1d7-413b-9a3c-c428f43076bc">

<img width="1410" alt="Pytest-cloud-2" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/1df0c382-b110-4f3b-8b0f-e532bdaf399b">

<img width="1410" alt="Pytest-cloud-3" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/f2f5541b-892e-4248-9755-8592bc7ce886">

As seen above, the content from LambdaTest YouTube channel and LambdaTest e-commerce playground are scrapped successfully! You can find the status of test execution in the [LambdaTest Automation Dashboard](https://automation.lambdatest.com/build).

<img width="1422" alt="Pytest-LambdaTest-Status-1" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/1d8d1a7a-21e4-4367-a720-319cb986aab3">

<img width="1429" alt="Pytest-LambdaTest-Status-2" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/40e5f38a-1b4b-4250-9118-7538b0b02e71">

As seen above, the status of test execution is "Completed". Since the browser is instantiated in the *Headless* mode, the video recording is not available on the dashboard.

## Have feedback or need assistance?
Feel free to fork the repo and contribute to make it better! Email to [himanshu[dot]sheth[at]gmail[dot]com](mailto:himanshu.sheth@gmail.com) for any queries or ping me on the following social media sites:

<b>LinkedIn</b>: [@hjsblogger](https://linkedin.com/in/hjsblogger)<br/>
<b>Twitter</b>: [@hjsblogger](https://www.twitter.com/hjsblogger)