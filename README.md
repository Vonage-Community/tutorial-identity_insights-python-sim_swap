# Prevent SIM Swap Fraud in Python With the Identity Insights API
A python script that allows you to check if a phone number has been involved in a SIM swap fraud.

> You can find full step-by-step instructions on the [Vonage Developer Blog](#). (Not published yet)

## Prerequisites 
1. [Python 3.6 or higher installed on your machine.](https://www.python.org/downloads/) Python 3.6 or higher is installed on your machine. 
2. [Vonage Developer Account](https://developer.vonage.com/sign-up)
3. A Vonage Application with the Network Registry Playground enabled.

## Instructions
1. Clone this repo
2. Setup a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies:
```
pip install vonage python-dotenv
```
3. Rename the `.env.example` file to `.env`, and add your `VONAGE_APPLICATION_ID`.
4. Add your `private.key` file in the root of the project directory.
5. Run your Python scriopt:
```
python main.py
```
