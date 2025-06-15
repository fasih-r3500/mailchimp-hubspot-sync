import requests 
import os
import schedule
import time
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
MAILCHIMP_API_KEY = os.getenv("MAILCHIMP_API_KEY")
MAILCHIMP_SERVER = os.getenv("MAILCHIMP_SERVER_PREFIX")
HUBSPOT_TOKEN = os.getenv("HUBSPOT_ACCESS_TOKEN")

# Check if keys are missing
if not MAILCHIMP_API_KEY or not MAILCHIMP_SERVER or not HUBSPOT_TOKEN:
    print("Missing API keys. Please check .env file.")
    exit()

# Define headers
HEADERS = {
    "Authorization": f"Bearer {HUBSPOT_TOKEN}",
    "Content-Type": "application/json"
}

# Fetch campaigns from Mailchimp
def get_campaigns():
    url = f"https://{MAILCHIMP_SERVER}.api.mailchimp.com/3.0/campaigns"
    res = requests.get(url, auth=("anystring", MAILCHIMP_API_KEY))
    data = res.json()
    return [campaign["id"] for campaign in data.get("campaigns", [])]

# Fetch campaign report
def get_campaign_report(campaign_id):
    url = f"https://{MAILCHIMP_SERVER}.api.mailchimp.com/3.0/reports/{campaign_id}"
    res = requests.get(url, auth=("anystring", MAILCHIMP_API_KEY))
    if res.status_code == 200:
        report = res.json()
        return {
            "campaign_name": report.get("campaign_title", "N/A"),
            "emails_sent": report.get("emails_sent", 0),
            "open_rate": round(report["opens"]["open_rate"] * 100, 2),
            "click_rate": round(report["clicks"]["click_rate"] * 100, 2),
            "send_time": report.get("send_time")
        }
    return None

# Push to Hubspot
def push_to_hubspot(data):
    url = "https://api.hubapi.com/crm/v3/objects/campaign_data"  # Replace if using custom object name
    payload = {
        "properties": {
            "campaign_name": data["campaign_name"],
            "emails_sent": str(data["emails_sent"]),
            "open_rate": str(data["open_rate"]),
            "click_rate": str(data["click_rate"]),
            "send_time": data["send_time"]
        }
    }
    res = requests.post(url, headers=HEADERS, json=payload)
    print(f"Pushed '{data['campaign_name']}' to HubSpot: {res.status_code}")


def main():
    campaigns = get_campaigns()
    print(f"Found {len(campaigns)} campaigns.")

    for cid in campaigns:
        report = get_campaign_report(cid)
        if report:
            print(f"\nCampaign: {report['campaign_name']}")
            print(f"  - Emails Sent: {report['emails_sent']}")
            print(f"  - Open Rate: {report['open_rate']}%")
            print(f"  - Click Rate: {report['click_rate']}%")
            push_to_hubspot(report)

if __name__ == "__main__":
    # Scheduler to run once daily at 9 AM
    schedule.every().day.at("09:00").do(main)

    print("Scheduler started. Waiting to run at 09:00 every day...")

    while True:
        schedule.run_pending()
        time.sleep(60)

