from flask import Flask, render_template
import yaml
# import json

app = Flask(__name__)

# Load profile data from JSON file
# with open("profile.json", "r") as f:
#     profile = json.load(f)

with open("data/profile.yaml", "r") as f:
    profile = yaml.safe_load(f)

print(profile)

@app.route('/')
def index():
    return render_template('index.html', profile=profile)

@app.route('/projects')
def projects():
    return render_template('projects.html', profile=profile)

@app.route('/contact')
def contact():
    return render_template('contact.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)