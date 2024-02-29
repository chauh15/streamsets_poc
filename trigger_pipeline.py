import requests

# StreamSets REST API endpoint and token
STREAMSETS_API_URL = 'http://localhost:18630/rest/v1/pipeline/start'
STREAMSETS_API_TOKEN = 'your_api_token'

def trigger_streamsets_pipeline(pipeline_name):
    headers = {'Content-Type': 'application/json', 'X-Requested-By': 'SDC', 'Authorization': f'Bearer {STREAMSETS_API_TOKEN}'}
    payload = {'pipeline': pipeline_name}

    response = requests.post(STREAMSETS_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        print(f"Pipeline '{pipeline_name}' triggered successfully.")
    else:
        print(f"Error triggering pipeline: {response.text}")

if __name__ == '__main__':
    # Replace 'your_pipeline_name' with the actual name of your StreamSets pipeline
    trigger_streamsets_pipeline('your_pipeline_name')
