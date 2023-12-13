import streamlit as st
from github import Github
import os

# Umgebungsvariable für GitHub Token setzen
os.environ['GITHUB_TOKEN'] = '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'

def load_template():
    with open('template.tex', 'r') as file:
        return file.read()

def fill_template(template, data):
    for key, value in data.items():
        template = template.replace(f'{{{key}}}', value)
    return template

def create_tex_file(content, filename='output.tex'):
    with open(filename, 'w') as file:
        file.write(content)

def upload_to_github(filename, content, repo_name, token):
    try:
        g = Github(token)
        repo = g.get_user().get_repo(repo_name)
        all_files = []
        contents = repo.get_contents("")
        while contents:
            file_content = contents.pop(0)
            if file_content.type == "dir":
                contents.extend(repo.get_contents(file_content.path))
            else:
                file = file_content
                all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))

        git_file = filename
        if git_file in all_files:
            contents = repo.get_contents(git_file)
            repo.update_file(contents.path, "Updating file", content, contents.sha, branch="master")
            st.success(f"Datei {filename} erfolgreich aktualisiert!")
        else:
            repo.create_file(git_file, "Creating new file", content, branch="master")
            st.success(f"Datei {filename} erfolgreich erstellt!")
        return True
    except Exception as e:
        st.error(f"Fehler beim Zugriff auf das Repository oder Hochladen: {e}")
        return False

def main():
    st.title("Lebenslauf-Generator")

    # Eingabefelder für persönliche Informationen
    name = st.text_input("Name", "Max Mustermann")
    address = st.text_input("Adresse", "Musterstraße 1")
    mobile = st.text_input("Handynummer", "0123456789")
    email = st.text_input("E-Mail", "max.mustermann@example.com")

    # Eingabefelder für Bildung
    university1 = st.text_input("Universität 1", "Musteruniversität")
    location_us1 = st.text_input("Standort Universität 1", "Musterstadt")
    majorus1 = st.text_input("Studiengang 1", "Musterstudium")
    timeus1 = st.text_input("Zeitraum Universität 1", "2010 - 2014")
    courses1 = st.text_input("Kurse 1", "Musterkurs 1, Musterkurs 2")
    gpa1 = st.text_input("GPA 1", "1.0")
    clubs1 = st.text_input("Clubs 1", "Musterclub 1")

    university2 = st.text_input("Universität 2", "Andere Musteruniversität")
    location_us2 = st.text_input("Standort Universität 2", "Andere Musterstadt")
    majorus2 = st.text_input("Studiengang 2", "Anderes Musterstudium")
    timeus2 = st.text_input("Zeitraum Universität 2", "2014 - 2018")
    courses2 = st.text_input("Kurse 2", "Anderer Musterkurs 1, Anderer Musterkurs 2")
    gpa2 = st.text_input("GPA 2", "1.0")
    clubs2 = st.text_input("Clubs 2", "Anderer Musterclub 1")

    # Eingabefelder für Berufserfahrung
    experience1 = st.text_input("Erfahrung 1", "Musterfirma 1")
    location_e1 = st.text_input("Standort Erfahrung 1", "Musterstadt")
    position1 = st.text_input("Position 1", "Musterposition 1")
    timee1 = st.text_input("Zeitraum Erfahrung 1", "2018 - 2020")
    task11 = st.text_input("Aufgabe 11", "Musterarbeit 1")
    task12 = st.text_input("Aufgabe 12", "Musterarbeit 2")
    task13 = st.text_input("Aufgabe 13", "Musterarbeit 3")

    experience2 = st.text_input("Erfahrung 2", "Musterfirma 2")
    location_e2 = st.text_input("Standort Erfahrung 2", "Andere Musterstadt")
    position2 = st.text_input("Position 2", "Musterposition 2")
    timee2 = st.text_input("Zeitraum Erfahrung 2", "2020 - 2022")
    task21 = st.text_input("Aufgabe 21", "Andere Musterarbeit 1")
    task22 = st.text_input("Aufgabe 22", "Andere Musterarbeit 2")
    task23 = st.text_input("Aufgabe 23", "Andere Musterarbeit 3")

    experience3 = st.text_input("Erfahrung 3", "Musterfirma 3")
    location_e3 = st.text_input("Standort Erfahrung 3", "Dritte Musterstadt")
    position3 = st.text_input("Position 3", "Musterposition 3")
    timee3 = st.text_input("Zeitraum Erfahrung 3", "2022 - Heute")
    task31 = st.text_input("Aufgabe 31", "Dritte Musterarbeit 1")
    task32 = st.text_input("Aufgabe 32", "Dritte Musterarbeit 2")
    task33 = st.text_input("Aufgabe 33", "Dritte Musterarbeit 3")

    # Eingabefelder für außercurriculare Aktivitäten
    extracurricular1 = st.text_input("Außercurriculare Aktivitäten", "Musteraktivität 1")
    additionaleducation1 = st.text_input("Zusätzliche Bildung", "Zusatzkurs 1")
    certificates1 = st.text_input("Zertifikate und Erfolge", "Musterzertifikat 1")

    # Eingabefelder für Skills und Interessen
    languages1 = st.text_input("Sprachen", "Deutsch, Englisch")
    computer1 = st.text_input("Computerkenntnisse", "Musterkenntnisse")
    interests1 = st.text_input("Interessen", "Musterinteresse 1, Musterinteresse 2")

    # Erstellen des gefüllten Templates
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

    if st.button("Lebenslauf erstellen"):
        create_tex_file(filled_template)

    token = os.environ.get('GITHUB_TOKEN')
    repo_name = "Deussaxum/Fixen-des-Generators"
    if st.button("Hochladen auf GitHub"):
        upload_to_github('output.tex', filled_template, repo_name, token)

if __name__ == "__main__":
    main()
