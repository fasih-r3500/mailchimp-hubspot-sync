# Mailchimp → HubSpot Campaign Automated Synchronisation

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

- Fetches campaign performance data from Mailchimp — including emails sent, open rates, click-through rates, and send time.

- Syncs structured performance data into HubSpot CRM as custom contact properties for centralized visibility.

- Automates reporting workflows, reducing manual tracking and ensuring your CRM reflects the latest campaign engagement.

By syncing key engagement metrics into HubSpot, marketing teams can segment leads more effectively, prioritize high-engagement contacts, and improve campaign follow-up — leading to smarter targeting and higher conversion rates.



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

I created a sample contact in HubSpot with custom contact properties to simulate synced campaign data from Mailchimp.

This shows how marketing metrics like **emails sent, open rate, click rate, and send time** would appear once synced via the script.

![Screenshot 2025-06-16 at 03-34-53 Summer Promo](https://github.com/user-attachments/assets/6c508564-b509-48f6-ac6f-d11be9446375)

This is the sample JSON payload the script would send to the Hubspot API:
   
      {
        "properties": {
          "campaign_name": "Summer Promo",
          "emails_sent": "4000",
          "open_rate": "38.2",
          "click_rate": "7.1",
          "send_time": "2025-06-10T10:00:00"
        }
      }

