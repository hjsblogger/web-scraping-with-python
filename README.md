In this 'Web Scraping with Python' repo, we have covered the following usecases:

* <b>Web Scraping using Selenium PyUnit</b>
* <b>Web Scraping using Selenium Pytest</b>
* <b>Web Scraping of dynamic website using Beautiful Soup and Selenium</b>

The following websites are used for the purpose of demoing web scraping:

* [LambdaTest YouTube Channel](https://www.youtube.com/@lambdatest/videos)
* [LambdaTest E-commerce Playground](https://ecommerce-playground.lambdatest.io/)
* [Scraping Club Infinite Scroll Website](https://scrapingclub.com/exercise/list_infinite_scroll/))

<img width="20" height="20" alt="Bulb" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/52f062e0-239e-4131-bde5-5bb8cb218d7b">As mentioned online, scraping public web data from YouTube is legal as long as you don't go after information that is not available to the general public. However, there might be cases where the YouTube scraping might throw errors (or exceptions) when scraping is done on the Cloud Selenium Grid.

In such cases, recommendation is to perform web scraping on local machine.

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

Procure the LambdaTest User Name and Access Key by navigating to [LambdaTest Account Page](https://accounts.lambdatest.com/security). You might need to create an an account on LambdaTest since it is used for running tests (or scraping) on the cloud Grid

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

## Web Scraping using Selenium PyUnit (Cloud Execution)

<b>Note</b>: As mentioned earlier, there could be cases where YouTube Scraping might fail on cloud grid (particularly when there are a number of attempts to scrape the content). However, it works flawlessly on local machine.