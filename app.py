import streamlit as st
import requests

# Funktion zur Extraktion von Informationen aus der API-Antwort
def extract_info(jsondata):
    extracted_info = {
        'full_name': jsondata.get('full_name', ''),
        'city': jsondata.get('city', ''),
        'state': jsondata.get('state', ''),
        'country': jsondata.get('country', ''),
        'education': jsondata.get('education', []),
        'experiences': jsondata.get('experiences', []),
        'volunteer_work': jsondata.get('volunteer_work', []),
        'certifications': jsondata.get('certifications', []),
        'languages': jsondata.get('languages', []),
        'interests': jsondata.get('interests', [])
    }
    return extracted_info

# Funktion zum Abrufen von Informationen
def retrieve_info(linkedin_profile_url):
    api_key = '_EIqMpWEbOnJLoQvNFz1CQ'
    headers = {'Authorization': 'Bearer ' + api_key}
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    params = {'linkedin_profile_url': linkedin_profile_url}
    response = requests.get(api_endpoint, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return extract_info(data)
    else:
        st.error(f"Profilinformationen konnten nicht abgerufen werden: HTTP {response.status_code}")
        return {}

# Funktion zum Erstellen des LaTeX-Codes
def build_latex_code(name, address, phone, email, university1, locationus1, majorus1, timeus1, courses1, gpa1, clubs1, university2, locationus2, majorus2, timeus2, courses2, gpa2, clubs2, experience1, locatione1, position1, timee1, task11, task12, task13, experience2, locatione2, position2, timee2, task21, task22, task23, experience3, locatione3, position3, timee3, task31, task32, task33, extracurricular1, additionaleducation1, certificates1, languages1, computer1, interests1):
    # LaTeX-Code-Vorlage hier einfügen
    latex_code = f"""
    % Hier kommt Ihr LaTeX-Code
    \documentclass[a4paper,8pt]{{article}}
    ...
    """
    return latex_code

# Streamlit-App-Layout
st.title("CV Generator 📃")

# Tab-System
tab_titles = ["Consulting 🧮", "Finance 📈", "Corporate 🏢", "Start-Up 🚀", "IT 🖥", "Academic 📚"]
tabs = st.tabs(tab_titles)

for tab in tabs:
    with tab:
        # Layout für jede Tab-Seite
        linkedin_profile_url = st.text_input('LinkedIn-Profil-URL eingeben', key=f'linkedin_url_{tab.index}')
        if st.button('LinkedIn-Daten abrufen', key=f'retrieve_data_{tab.index}'):
            linkedin_data = retrieve_info(linkedin_profile_url) or {}

        # Eingabefelder für Benutzerdaten
        name = st.text_input("Name", value=linkedin_data.get('full_name', ''), key=f'name_{tab.index}')
        address = st.text_input("Adresse", key=f'address_{tab.index}')
        phone = st.text_input("Telefonnummer", key=f'phone_{tab.index}')
        email = st.text_input("E-Mail", key=f'email_{tab.index}')

        # Weitere Eingabefelder
        university1 = st.text_input("Universität 1", key=f'university1_{tab.index}')
        locationus1 = st.text_input("Standort der Universität 1", key=f'locationus1_{tab.index}')
        majorus1 = st.text_input("Studiengang an der Universität 1", key=f'majorus1_{tab.index}')
        timeus1 = st.text_input("Zeitraum an der Universität 1", key=f'timeus1_{tab.index}')
        courses1 = st.text_input("Kurse an der Universität 1", key=f'courses1_{tab.index}')
        gpa1 = st.text_input("GPA an der Universität 1", key=f'gpa1_{tab.index}')
        clubs1 = st.text_input("Clubs an der Universität 1", key=f'clubs1_{tab.index}')

        university2 = st.text_input("Universität 2", key=f'university2_{tab.index}')
        locationus2 = st.text_input("Standort der Universität 2", key=f'locationus2_{tab.index}')
        majorus2 = st.text_input("Studiengang an der Universität 2", key=f'majorus2_{tab.index}')
        timeus2 = st.text_input("Zeitraum an der Universität 2", key=f'timeus2_{tab.index}')
        courses2 = st.text_input("Kurse an der Universität 2", key=f'courses2_{tab.index}')
        gpa2 = st.text_input("GPA an der Universität 2", key=f'gpa2_{tab.index}')
        clubs2 = st.text_input("Clubs an der Universität 2", key=f'clubs2_{tab.index}')

        experience1 = st.text_input("Erste Berufserfahrung", key=f'experience1_{tab.index}')
        locatione1 = st.text_input("Standort der ersten Berufserfahrung", key=f'locatione1_{tab.index}')
        position1 = st.text_input("Position bei der ersten Berufserfahrung", key=f'position1_{tab.index}')
        timee1 = st.text_input("Zeitraum bei der ersten Berufserfahrung", key=f'timee1_{tab.index}')
        task11 = st.text_input("Aufgabe 1 bei der ersten Berufserfahrung", key=f'task11_{tab.index}')
        task12 = st.text_input("Aufgabe 2 bei der ersten Berufserfahrung", key=f'task12_{tab.index}')
        task13 = st.text_input("Aufgabe 3 bei der ersten Berufserfahrung", key=f'task13_{tab.index}')

        experience2 = st.text_input("Zweite Berufserfahrung", key=f'experience2_{tab.index}')
        locatione2 = st.text_input("Standort der zweiten Berufserfahrung", key=f'locatione2_{tab.index}')
        position2 = st.text_input("Position bei der zweiten Berufserfahrung", key=f'position2_{tab.index}')
        timee2 = st.text_input("Zeitraum bei der zweiten Berufserfahrung", key=f'timee2_{tab.index}')
        task21 = st.text_input("Aufgabe 1 bei der zweiten Berufserfahrung", key=f'task21_{tab.index}')
        task22 = st.text_input("Aufgabe 2 bei der zweiten Berufserfahrung", key=f'task22_{tab.index}')
        task23 = st.text_input("Aufgabe 3 bei der zweiten Berufserfahrung", key=f'task23_{tab.index}')

        experience3 = st.text_input("Dritte Berufserfahrung", key=f'experience3_{tab.index}')
        locatione3 = st.text_input("Standort der dritten Berufserfahrung", key=f'locatione3_{tab.index}')
        position3 = st.text_input("Position bei der dritten Berufserfahrung", key=f'position3_{tab.index}')
        timee3 = st.text_input("Zeitraum bei der dritten Berufserfahrung", key=f'timee3_{tab.index}')
        task31 = st.text_input("Aufgabe 1 bei der dritten Berufserfahrung", key=f'task31_{tab.index}')
        task32 = st.text_input("Aufgabe 2 bei der dritten Berufserfahrung", key=f'task32_{tab.index}')
        task33 = st.text_input("Aufgabe 3 bei der dritten Berufserfahrung", key=f'task33_{tab.index}')

        extracurricular1 = st.text_input("Außerschulische Aktivitäten", key=f'extracurricular1_{tab.index}')
        additionaleducation1 = st.text_input("Zusätzliche Bildung", key=f'additionaleducation1_{tab.index}')
        certificates1 = st.text_input("Zertifikate und Erfolge", key=f'certificates1_{tab.index}')
        languages1 = st.text_input("Sprachen", key=f'languages1_{tab.index}')
        computer1 = st.text_input("Computerkenntnisse", key=f'computer1_{tab.index}')
        interests1 = st.text_input("Interessen", key=f'interests1_{tab.index}')

        # LaTeX-Code generieren und anzeigen
        if st.button("CV erstellen", key=f'generate_cv_{tab.index}'):
            latex_code = build_latex_code(name, address, phone, email, university1, ...)
            st.text_area("Generierter LaTeX-Code", latex_code, height=300)
