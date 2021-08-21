# Bitly url shorterer

This code creates shortlink from your long url or counts clicks to your shortlink using [https://app.bitly.com](https://app.bitly.com).

## Requirements

Python 3.9

requests==2.26.0

python_dotenv==0.19.0

### How to install

* Python3 should be already installed.

* Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
* Be registered on the [https://app.bitly.com](https://app.bitly.com).

* Generate your [access token](https://app.bitly.com/Bl8f4PtdN5s/bitlinks/3zfABbf?actions=accountMain&actions=profile&actions=accessToken). Put it in file `.env` to folder with script like this:
```
TOKEN=fa9dac58dbced9a28458e2e409fnk0038a6e83ef
```
* Run the script in a terminal
```console
python3 bitlinks.py link
```
### Example


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).#
