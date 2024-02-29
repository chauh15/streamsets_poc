import requests

# NiFi REST API endpoint
NIFI_API_URL = 'http://localhost:8080/nifi-api/flow/process-groups/{processGroupId}/controller-services/{controllerServiceId}/references'
NIFI_API_TOKEN = 'your_nifi_api_token'

def trigger_nifi_data_flow():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {NIFI_API_TOKEN}'
    }

    # Customize the payload based on your NiFi setup
    payload = {
        'uri': 'http://localhost:8080/nifi-api/flow/process-groups/{processGroupId}/controller-services/{controllerServiceId}/references',
        'method': 'POST'
    }

    response = requests.post(NIFI_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        print("NiFi data flow triggered successfully.")
    else:
        print(f"Error triggering NiFi data flow: {response.text}")

if __name__ == '__main__':
    trigger_nifi_data_flow()
