import streamlit as st
from github import Github
import os

# Umgebungsvariable für GitHub Token setzen (ersetzen Sie 'Ihr_Persönlicher_Token' mit Ihrem tatsächlichen Token)
os.environ['GITHUB_TOKEN'] = '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'

# Funktionen
def load_template():
    with open('template.tex', 'r') as file:
        return file.read()

def fill_template(template, data):
    for key, value in data.items():
        template = template.replace(key, value)
    return template

def create_tex_file(content, filename='output.tex'):
    with open(filename, 'w') as file:
        file.write(content)

def upload_to_github(filename, content, repo_name, token):
    g = Github(token)
    repo = g.get_user().get_repo(repo_name)
    try:
        repo.create_file(filename, "CV update", content)
        return True
    except Exception as e:
        print(f"Fehler beim Hochladen: {e}")
        return False

# Streamlit Benutzeroberfläche
def main():
    st.title("Lebenslauf-Generator")

    # Eingabefelder für persönliche Informationen
    name = st.text_input("Name")
    address = st.text_input("Adresse")
    mobile = st.text_input("Handynummer")
    email = st.text_input("E-Mail")

    # Eingabefelder für Bildung
    university1 = st.text_input("Universität 1")
    location_us1 = st.text_input("Standort Universität 1")
    majorus1 = st.text_input("Studiengang 1")
    timeus1 = st.text_input("Zeitraum Universität 1")
    courses1 = st.text_input("Kurse 1")
    gpa1 = st.text_input("GPA 1")
    clubs1 = st.text_input("Clubs 1")

    university2 = st.text_input("Universität 2")
    location_us2 = st.text_input("Standort Universität 2")
    majorus2 = st.text_input("Studiengang 2")
    timeus2 = st.text_input("Zeitraum Universität 2")
    courses2 = st.text_input("Kurse 2")
    gpa2 = st.text_input("GPA 2")
    clubs2 = st.text_input("Clubs 2")

    # Eingabefelder für Berufserfahrung
    experience1 = st.text_input("Erfahrung 1")
    location_e1 = st.text_input("Standort Erfahrung 1")
    position1 = st.text_input("Position 1")
    timee1 = st.text_input("Zeitraum Erfahrung 1")
    task11 = st.text_input("Aufgabe 11")
    task12 = st.text_input("Aufgabe 12")
    task13 = st.text_input("Aufgabe 13")

    experience2 = st.text_input("Erfahrung 2")
    location_e2 = st.text_input("Standort Erfahrung 2")
    position2 = st.text_input("Position 2")
    timee2 = st.text_input("Zeitraum Erfahrung 2")
    task21 = st.text_input("Aufgabe 21")
    task22 = st.text_input("Aufgabe 22")
    task23 = st.text_input("Aufgabe 23")

    experience3 = st.text_input("Erfahrung 3")
    location_e3 = st.text_input("Standort Erfahrung 3")
    position3 = st.text_input("Position 3")
    timee3 = st.text_input("Zeitraum Erfahrung 3")
    task31 = st.text_input("Aufgabe 31")
    task32 = st.text_input("Aufgabe 32")
    task33 = st.text_input("Aufgabe 33")

    # Eingabefelder für außercurriculare Aktivitäten
    extracurricular1 = st.text_input("Außercurriculare Aktivitäten")
    additionaleducation1 = st.text_input("Zusätzliche Bildung")
    certificates1 = st.text_input("Zertifikate und Erfolge")

    # Eingabefelder für Skills und Interessen
    languages1 = st.text_input("Sprachen")
    computer1 = st.text_input("Computerkenntnisse")
    interests1 = st.text_input("Interessen")

    # Erstellen des Lebenslauf-Dokuments
    if st.button("Lebenslauf erstellen"):
        template = load_template()
        user_data = {
            "name": name,
            "address": address,
            "mobile": mobile,
            "email": email,
            "university1": university1,
            "location_us1": location_us1,
            "majorus1": majorus1,
            "timeus1": timeus1,
            "courses1": courses1,
            "gpa1": gpa1,
            "clubs1": clubs1,
            "university2": university2,
            "location_us2": location_us2,
            "majorus2": majorus2,
            "timeus2": timeus2,
            "courses2": courses2,
            "gpa2": gpa2,
            "clubs2": clubs2,
            "experience1": experience1,
            "location_e1": location_e1,
            "position1": position1,
            "timee1": timee1,
            "task11": task11,
            "task12": task12,
            "task13": task13,
            "experience2": experience2,
            "location_e2": location_e2,
            "position2": position2,
            "timee2": timee2,
            "task21": task21,
            "task22": task22,
            "task23": task23,
            "experience3": experience3,
            "location_e3": location_e3,
            "position3": position3,
            "timee3": timee3,
            "task31": task31,
            "task32": task32,
            "task33": task33,
            "extracurricular1": extracurricular1,
            "additionaleducation1": additionaleducation1,
            "certificates1": certificates1,
            "languages1": languages1,
            "computer1": computer1,
            "interests1": interests1
        }
        filled_template = fill_template(template, user_data)
        create_tex_file(filled_template)

        # Hochladen auf GitHub
        token = os.environ.get('GITHUB_TOKEN')  # Liest das Token aus der Umgebungsvariable
        repo_name = "deussaxum/Fixen-des-Generators"  # Ihr GitHub Benutzername und Repository-Name
        if st.button("Hochladen auf GitHub"):
            success = upload_to_github('output.tex', filled_template, repo_name, token)
            if success:
                st.success("Erfolgreich auf GitHub hochgeladen!")
            else:
                st.error("Fehler beim Hochladen auf GitHub.")

if __name__ == "__main__":
    main()
