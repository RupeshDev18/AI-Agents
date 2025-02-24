import requests
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sqlite3
import smtplib
from email.mime.text import MIMEText
# Step 1: Fetch projects 
def fetch_projects(query):
    response = requests.get(f"https://api.example.com/jobs?q={query}")
    return response.json()
# Step 2: Extract keywords
nlp = spacy.load("en_core_web_sm")
def extract_keywords(description):
    doc = nlp(description)
    return [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
# Step 3: Filter projects
def filter_projects(projects, required_skills, excluded_skills):
    filtered = []
    for project in projects:
        keywords = extract_keywords(project["description"])
        if all(skill in keywords for skill in required_skills) and \
           not any(skill in keywords for skill in excluded_skills):
            filtered.append(project)
    return filtered
# Step 4: Rank projects
def rank_projects(projects, query):
    descriptions = [project["description"] for project in projects]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(descriptions + [query])
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    ranked_indices = similarity_scores.argsort()[0][::-1]
    return [projects[i] for i in ranked_indices]
# Step 5: Save to database
def save_to_db(projects):
    conn = sqlite3.connect("projects.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS projects (title TEXT, description TEXT, budget INTEGER)")
    for project in projects:
        cursor.execute("INSERT INTO projects VALUES (?, ?, ?)",
                       (project["title"], project["description"], project["budget"]))
    conn.commit()
    conn.close()
# Step 6: Send email alert
def send_email(subject, body, to_email):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "your_email@example.com"
    msg["To"] = to_email
    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.login("your_email@example.com", "your_password")
        server.sendmail("your_email@example.com", [to_email], msg.as_string())
# Main Function
if __name__ == "__main__":
    projects = fetch_projects("Python")
    filtered = filter_projects(projects, ["Python", "Flask"], ["React Native"])
    ranked = rank_projects(filtered, "Python API development")
    save_to_db(ranked)
    send_email("New Projects Found", str(ranked), "your_email@example.com")
