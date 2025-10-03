
from datetime import datetime
from flask import Flask, render_template , request
import yaml
# import json

app = Flask(__name__)

# Load profile data from JSON file
# with open("profile.json", "r") as f:
#     profile = json.load(f)

with open("data/profile.yaml", "r") as f:
    profile = yaml.safe_load(f)

#print(profile)

@app.route('/')
def index():

    news_items = [
        {
            "title": "Nouveau projet Data Science",
            "date": "10 octobre 2025",
            "content": "Découvrez notre dernier projet en analyse de données avec Python et Pandas.",
            "link": "/projects/data-science"
        },
        {
            "title": "Atelier MLOps",
            "date": "5 octobre 2025",
            "content": "Rejoignez notre atelier sur le déploiement de modèles avec Docker et Kubernetes.",
            "link": "/projects/mlops"
        },
        {
            "title": "Certification AWS",
            "date": "1er octobre 2025",
            "content": "Nous avons obtenu la certification AWS Solutions Architect !",
            "link": "/projects/aws"
        }
    ]

    return render_template('index.html', news_items=news_items, profile=profile, now=datetime.now())

@app.route('/projects')
def projects():
    return render_template('projects.html', profile=profile, now=datetime.now())

@app.route('/contact')
def contact():
    return render_template('contact.html', profile=profile, now=datetime.now())

@app.route('/search')
def search():
    query = request.args.get('q', '')
    # Implement search logic here (e.g., search in profile data)    
    #return render_template('search.html', profile=profile)
    return f"Search results for: {query}"

@app.route('/data-science')
def data_science():
    return render_template('data_science.html')

@app.route('/mlops')
def mlops():
    return render_template('mlops.html')

@app.route('/aws')
def aws():
    return render_template('aws.html')

@app.route('/news')
def news():
    # Exemple de données dynamiques (remplace par tes vraies données)
    news_items = [
        {
            "title": "Nouveau projet Data Science",
            "date": "10 octobre 2025",
            "content": "Découvrez notre dernier projet en analyse de données avec Python et Pandas.",
            "link": "/projects/data-science"
        },
        {
            "title": "Atelier MLOps",
            "date": "5 octobre 2025",
            "content": "Rejoignez notre atelier sur le déploiement de modèles avec Docker et Kubernetes.",
            "link": "/projects/mlops"
        },
        {
            "title": "Certification AWS",
            "date": "1er octobre 2025",
            "content": "Nous avons obtenu la certification AWS Solutions Architect !",
            "link": "/projects/aws"
        }
    ]
    return render_template('news_feed.html', news_items=news_items, profile=profile, now=datetime.now())

if __name__ == '__main__':
    app.run(debug=True)