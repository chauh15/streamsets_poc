from flask import Flask, render_template, request, jsonify
import os
import yaml
import subprocess
import requests

app = Flask(__name__)
RULES_DIR = 'rules'

# NiFi REST API endpoint
NIFI_API_URL = 'https://127.0.0.1:8443/nifi-api/flow/process-groups/f5f33e58-018d-1000-81a0-d3779ee98fdc/controller-services/f623965c-018d-1000-0436-27b74699a9e3/references'
NIFI_USERNAME = '08a8e122-db91-46fb-bb51-5d52ce46903e'
NIFI_PASSWORD = '0KmYvZZtvWTehLS2bBRESxJrTM8U57zT'

@app.route('/')
def index():
    return render_template('index.html')
    
def trigger_nifi_data_flow():
    headers = {
        'Content-Type': 'application/json'
    }
    
    auth = (NIFI_USERNAME, NIFI_PASSWORD)

    # Customize the payload based on your NiFi setup
    payload = {
        'uri': 'https://127.0.0.1:8443/nifi-api/flow/process-groups/f5f33e58-018d-1000-81a0-d3779ee98fdc/controller-services/f623965c-018d-1000-0436-27b74699a9e3/references',
        'method': 'POST'
    }

    response = requests.post(NIFI_API_URL, json=payload, headers=headers, auth=auth, verify=False)

    if response.status_code == 200:
        print("NiFi data flow triggered successfully.")
    else:
        print(f"Error triggering NiFi data flow: {response.text}")

if __name__ == '__main__':
    trigger_nifi_data_flow()

@app.route('/submit_rule', methods=['POST'])
def submit_rule():
    try:
        rule_name = request.form['rule_name']
        # Get other form fields

        # Save rule to YAML file
        rule_filename = f"{rule_name}_rule.yaml"
        rule_filepath = os.path.join(RULES_DIR, rule_filename)

        rule_data = {
            'rule_name': rule_name,
            # Add other rule attributes
        }
        
        os.makedirs(RULES_DIR, exist_ok=True) # ensure the directory exists

        with open(rule_filepath, 'w') as yaml_file:
            yaml.dump(rule_data, yaml_file, default_flow_style=False)

        # Commit and push to GitHub
        subprocess.run(['git', '-C', 'C:\dev\my_flask_api\streamsets_poc', 'add', RULES_DIR])
        subprocess.run(['git', '-C', 'C:\dev\my_flask_api\streamsets_poc', 'commit', '-m', 'Add new rule'])
        subprocess.run(['git', '-C', 'C:\dev\my_flask_api\streamsets_poc', 'push', 'origin', 'main'])

        #Trigger Nifi data flow
        trigger_nifi_data_flow()

        return jsonify({'message': 'Rule submitted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
