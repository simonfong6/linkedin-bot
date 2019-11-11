# linkedin-bot
LinkedIn bot to view someone's page for the sole purpose of triggering a view notification.

# Installation
## Requires Python 3
```
pip3 install -r requirements.txt
```

## Chrome Webdriver
Get the Chrome Driver for your Chrome version [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).


### Put chromedriver in PATH
I put it in `/usr/local/bin/`.

```
Simons-MacBook-Pro:linkedin-bot simon$ which chromedriver
/usr/local/bin/chromedriver
```

# Running the program
```
python3 bot.py --email '{Your LinkedIn Email}' --password '{Your LinkedIn Password}'
```

## Example
```
python3 bot.py --email 'simonfong6@gmail.com' --password 'password123'
```

# Helpful Documents
[Python Selenium](https://selenium-python.readthedocs.io/)