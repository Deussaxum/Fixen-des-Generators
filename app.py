import streamlit as st
import requests
from base64 import b64encode

# Streamlit-Anwendungsoberfläche
st.title('Simple LaTeX Editor')

# Benutzereingabe
name = st.text_input('Geben Sie Ihren Namen ein')

# GitHub-Repository-Informationen
github_repo = 'Ihr_GitHub_Benutzername/Ihr_Repository'
path = 'pfad/zu/example.tex'
github_token = st.text_input("Enter your GitHub token", type="password")

# Funktion zum Hochladen der Datei auf GitHub
def upload_to_github(name, repo, path, token):
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    headers = {'Authorization': f'token {token}'}

    # LaTeX-Inhalt mit Benutzereingaben
    content = f"""
    \\documentclass{{article}}
    \\begin{{document}}
    Hello, \\textbf{{{name}}}!
    \\end{{document}}
    """

    data = {
        "message": "Update LaTeX file",
        "content": b64encode(content.encode()).decode(),
    }

    response = requests.put(url, json=data, headers=headers)
    return response.status_code == 201

# Knopf zum Aktualisieren der LaTeX-Datei
if st.button('Aktualisieren und in Overleaf öffnen'):
    if upload_to_github(name, github_repo, path, github_token):
        st.success('LaTeX-Datei erfolgreich aktualisiert.')
        # Overleaf-Link bereitstellen
        overleaf_url = f'https://www.overleaf.com/github/{github_repo}'
        st.markdown(f'[Open in Overleaf]({overleaf_url})')
    else:
        st.error('Fehler beim Hochladen der Datei.')

