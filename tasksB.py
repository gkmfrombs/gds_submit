# /// script 
# requires-python = ">=3.13"
# dependencies = [
#     "gitpython",
#     "requests",
#     "duckdb"
# ]    

import os

# import git

def B12(filepath):
    if filepath.startswith('/data'):
        
        # raise PermissionError("Access outside /data is not allowed.")
        # print("Access outside /data is not allowed.")
        return True
    else:
        return False

# B3: Fetch Data from an API
def B3(url, save_path):
    if not B12(save_path):
        return "Error: Access outside /data is not allowed."
    import requests
    response = requests.get(url)
    with open(save_path, 'w') as file:
        file.write(response.text)
    return f"B3 Completed: Data fetched from {url} and saved to {save_path}"

# B4: Clone a Git Repo and Make a Commit
# def clone_git_repo(repo_url, commit_message):
#     repo_name = repo_url.split('/')[-1].split('.')[0]
#     repo = git.Repo.clone_from(repo_url, repo_name)
#     with open(f"{repo_name}/README.md", 'a') as f:
#         f.write("\nUpdated by script")
#     repo.git.add(update=True)
#     repo.index.commit(commit_message)
#     return f"B4 Completed: Cloned and committed to {repo_name}"

# B5: Run SQL Query
def B5(db_path, query, output_filename):
    if not B12(db_path):
        return "Error: Access outside /data is not allowed."
    import sqlite3, duckdb
    conn = sqlite3.connect(db_path) if db_path.endswith('.db') else duckdb.connect(db_path)
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    conn.close()
    with open(output_filename, 'w') as file:
        file.write(str(result))
    return result

# B6: Web Scraping
def B6(url, output_filename):
    import requests
    result = requests.get(url).text
    with open(output_filename, 'w') as file:
        file.write(str(result))

# B7: Image Processing
def B7(image_path, output_path, resize=None ,compress=None,quality: int = 85, size: tuple = (800, 600)):
    from PIL import Image
    if not B12(image_path):
        return "Error: Access outside /data is not allowed."
    if not B12(output_path):
        return "Error: Access outside /data is not allowed."    
    img = Image.open(image_path)
    if compress:
        img = img.convert('RGB')
        img.save(output_path, optimize=True, quality=quality)
    elif resize:
        img = img.resize(resize)
        img.save(output_path)
    return f"B7 Completed: Image {compress or resize}ed and saved to {output_path}"


# B8: Audio Transcription
def B8(audio_path, output_path):
    import speech_recognition as sr
    if not B12(audio_path):
        return "Error: Access outside /data is not allowed."
    r= sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)
    text = r.recognize_google(audio)
    with open(output_path, 'w') as file:
        file.write(text)
    return f"B8 Completed: Audio transcribed to {output_path}"

# B9: Markdown to HTML Conversion
def B9(md_path, output_path):
    import markdown
    if not B12(md_path):
        return "Error: Access outside /data is not allowed."
    if not B12(output_path):
        return "Error: Access outside /data is not allowed."
    with open(md_path, 'r') as file:
        html = markdown.markdown(file.read())
    with open(output_path, 'w') as file:
        file.write(html)

# B10: API Endpoint for CSV Filtering
# from flask import Flask, request, jsonify
# app = Flask(__name__)
# @app.route('/filter_csv', methods=['POST'])
# def filter_csv():
#     import pandas as pd
#     data = request.json
#     csv_path, filter_column, filter_value = data['csv_path'], data['filter_column'], data['filter_value']
#     B12(csv_path)
#     df = pd.read_csv(csv_path)
#     filtered = df[df[filter_column] == filter_value]
#     return jsonify(filtered.to_dict(orient='records'))