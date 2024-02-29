import requests

# NiFi REST API endpoint
NIFI_API_URL = 'http://localhost:8080/nifi-api/flow/process-groups/f5f33e58-018d-1000-81a0-d3779ee98fdc/controller-services/f623965c-018d-1000-0436-27b74699a9e3/references'
NIFI_USERNAME = '08a8e122-db91-46fb-bb51-5d52ce46903e'
NIFI_PASSWORD = '0KmYvZZtvWTehLS2bBRESxJrTM8U57zT'

def trigger_nifi_data_flow():
    headers = {
        'Content-Type': 'application/json'
    }
    
    auth = (NIFI_USERNAME, NIFI_PASSWORD)

    # Customize the payload based on your NiFi setup
    payload = {
        'uri': 'http://localhost:8080/nifi-api/flow/process-groups/f5f33e58-018d-1000-81a0-d3779ee98fdc/controller-services/f623965c-018d-1000-0436-27b74699a9e3/references',
        'method': 'POST'
    }

    response = requests.post(NIFI_API_URL, json=payload, headers=headers, auth=auth)

    if response.status_code == 200:
        print("NiFi data flow triggered successfully.")
    else:
        print(f"Error triggering NiFi data flow: {response.text}")

if __name__ == '__main__':
    trigger_nifi_data_flow()
