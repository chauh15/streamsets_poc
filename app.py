from flask import Flask, render_template, request, jsonify
import os
import yaml
import subprocess

app = Flask(__name__)
RULES_DIR = 'rules'

@app.route('/')
def index():
    return render_template('index.html')

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

        with open(rule_filepath, 'w') as yaml_file:
            yaml.dump(rule_data, yaml_file, default_flow_style=False)

        # Commit and push to GitHub
        subprocess.run(['git', '-C', '/path/to/your/repo', 'add', RULES_DIR])
        subprocess.run(['git', '-C', '/path/to/your/repo', 'commit', '-m', 'Add new rule'])
        subprocess.run(['git', '-C', '/path/to/your/repo', 'push', 'origin', 'master'])

        return jsonify({'message': 'Rule submitted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
