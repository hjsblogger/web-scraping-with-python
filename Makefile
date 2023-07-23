# Define variables
PYTHON := python3
PYTEST := pytest
PIP := pip3
PROJECT_NAME := web scraping using Python

.PHONY: install
install:
	$(PIP) install -r requirements.txt
	@echo "Set env vars LT_USERNAME & LT_ACCESS_KEY"
    # Procure Username and AccessKey from https://accounts.lambdatest.com/security
    export LT_USERNAME=himanshuj
    export LT_ACCESS_KEY=Ia1MiqNfc

.PHONY: test
test:
    export NODE_ENV = test


.PHONY: test
scrap-using-pyunit:
	- echo $(EXEC_PLATFORM)
	- $(PYTHON) tests/pyunit/test_ecommerce_scraping.py
	- $(PYTHON) tests/pyunit/test_yt_scraping.py

scrap-using-pytest:
	- echo $(EXEC_PLATFORM)
	- $(PYTEST) --verbose --capture=no tests/pytest/test_ecommerce_scraping.py
	- $(PYTEST) --verbose --capture=no tests/pytest/test_yt_scraping.py

.PHONY: clean
clean:
    # This helped: https://gist.github.com/hbsdev/a17deea814bc10197285
	find . | grep -E "(__pycache__|\.pyc$$)" | xargs rm -rf
	@echo "Clean Succeded"

.PHONY: distclean
distclean: clean
	rm -rf venv

.PHONY: help
help:
	@echo ""
	@echo "install - Install project dependencies"
	@echo "clean - Clean up temp files"
	@echo "scrap-using-pyunit - Web Scraping using Pyunit"
	@echo "scrap-using-pytest - Web Scraping using Pytest"