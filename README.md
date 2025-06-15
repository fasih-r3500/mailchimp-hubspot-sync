# Mailchimp → HubSpot Campaign Sync

This script automates the syncing of email campaign performance data from Mailchimp to HubSpot CRM using their APIs. It enables better client reporting, lead segmentation, and marketing automation.

# Setup

1. Clone the project and create a `.env` file:
   
        .env:
       
        MAILCHIMP_API_KEY=mailchimp-api-key
       
        MAILCHIMP_SERVER_PREFIX=usX
       
        HUBSPOT_ACCESS_TOKEN=hubspot-access-token

2. Create a virtual environment:
   
        python3 -m venv venv
       
        source venv/bin/activate
       
        pip install -r requirements.txt

3. Run the script:

       python sync.py

# Features

    Fetches latest campaign data from Mailchimp

    Extracts open/click rates and sends stats

    Pushes structured data into HubSpot CRM

# API Notes

    Mailchimp:

        /campaigns

        /reports/{id}

        Auth: Basic (anystring, API_KEY)

    HubSpot:

        /crm/v3/objects/{custom_type}

        Auth: Bearer Token

# Demo Output

Sample Output:

    Found 3 campaigns.

    Campaign: Summer Promo
      - Emails Sent: 4000
      - Open Rate: 38.2%
      - Click Rate: 7.1%
    Pushed 'Summer Promo' to HubSpot: 201

A sample contact was created in HubSpot to simulate synced campaign data from Mailchimp.

This shows how marketing metrics like **email volume, open rate, click rate, and send time** would appear once synced via the script.

![Alt text](<Screenshot 2025-06-16 at 02-54-06 Demo Campaign.png>)
