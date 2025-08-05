# main.py
import requests
from dotenv import load_dotenv
import os
from vonage_jwt import JwtClient

load_dotenv()

API_URL = "https://api-eu.vonage.com/v0.1/identity-insights"
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
DEFAULT_HOURS = int(os.getenv("DEFAULT_HOURS"))
application_id = os.getenv("VONAGE_APPLICATION_ID")
private_key_path = os.getenv("VONAGE_PRIVATE_KEY_PATH")

jwt_client = JwtClient(application_id, private_key_path)

def check_sim_swap(phone_number, hours):

    jwt_token = jwt_client.generate_application_jwt()

    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "phone_number": phone_number,
        "purpose": "FraudPreventionAndDetection",
        "insights": {
            "format": {},
            "sim_swap": {
                "period": hours
            }
        }
    }

    print(f"\n🔍 Checking SIM swap status for {phone_number}...")
    res = requests.post(API_URL, headers=headers, json=payload)

    if res.status_code != 200:
        print("❌ Error:", res.status_code, res.text)
        return

    data = res.json()

    sim_swap_info = data.get("insights", {}).get("sim_swap", {})
    status_code = sim_swap_info.get("status", {}).get("code")

    if status_code != "OK":
        print(f"\n⚠️ SIM Swap check failed. Status: {status_code}")
        print("   Message:", sim_swap_info.get("status", {}).get("message"))
        return

    swapped = sim_swap_info.get("swapped")
    swap_time = sim_swap_info.get("latest_sim_swap_at")

    print(f"\n🔒 SIM Swap Results:")
    print(f"   SIM Swapped: {'❌ Yes' if swapped else '✅ No'}")
    print(f"   Last SIM Swap: {swap_time if swap_time else 'None detected'}")

if __name__ == "__main__":
    print("=== Vonage Identity Insights - SIM Swap Checker ===")
    phone = input(f"Enter phone number [Default: {PHONE_NUMBER}]: ").strip() or PHONE_NUMBER
    hours = input(f"How many hours ago to check for? [Default: {DEFAULT_HOURS}]: ").strip() or DEFAULT_HOURS
    hours = int(hours)
    check_sim_swap(phone, hours)
