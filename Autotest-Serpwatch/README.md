# Autotest-Serpwatch


please install all libraries from this file requirements.txt
use this  -  " pip install -r requirements.txt"

in file test_website.py - i am checking our website - serpwatch.io 
1)serpchecker  
2) chat)

in file test_aplication.py - I am testing our app (dev.serpwatch.io)
1) registration


This test wrote with OOP, that's why please note that locators, pages (on the website or app), 
main logic (conftest and base_page)  and end to end tests have different pages.

used the framework PYTEST


When the test crashes, the test do screenshot

for start :
        pytest -s -v --tb=short --browser_name=firefox test_website.py
        pytest -s -v --tb=short --browser_name=chrome --language=en test_website.py
        pytest -s -v --tb=short  test_website.py
        pytest -s -v --tb=short -m green  test_website.py
        
        pytest -s -v --tb=short  test_application.py
        pytest -s -v --tb=short -m green test_application.py


    по умолчанию броузер 'chrome' и язык 'en'
        pytest -s -v --tb=line 