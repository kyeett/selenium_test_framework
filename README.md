
# Selenium Test Framework (STFu)

### Resources
[Docker file for python selenium testing](https://github.com/weihanwang/webdriver-python)

[Example test](https://github.com/weihanwang/webdriver-python/blob/master/root/main.py)

### Docker command
Run test
```
docker run -v /c/Users/ewamagn/repo/selenium_tests:/tmp/selenium_tests weihan/webdriver-python python -u /tmp/selenium_tests/example.py
```

Run tests, export screenshots
```
docker run -v /c/Users/ewamagn/repo/selenium_tests/screenshots:/screenshots -v /c/Users/ewamagn/repo/selenium_tests:/tmp/selenium_tests weihan/webdriver-python python -u /tmp/selenium_tests/example.py
```
