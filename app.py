import streamlit as st
import requests
from string import Template
import tempfile


# Streamlit-Benutzeroberfläche
st.title("CV-Generator")

# Persönliche Informationen
st.header("Personal Information")
name = st.text_input("Name")
address = st.text_input("Adresse")
phone = st.text_input("Telefonnummer")
email = st.text_input("E-Mail")

# Education
st.header("Education")
university1 = st.text_input("Universität/Schule 1")
locationus1 = st.text_input("Standort 1")
majorus1 = st.text_input("Studiengang 1")
timeus1 = st.text_input("Zeitraum 1")
courses1 = st.text_input("Kurse 1")
gpa1 = st.text_input("GPA 1")
clubs1 = st.text_input("Clubs/Aktivitäten 1")

university2 = st.text_input("Universität/Schule 2", "")
locationus2 = st.text_input("Standort 2", "")
majorus2 = st.text_input("Studiengang 2", "")
timeus2 = st.text_input("Zeitraum 2", "")
courses2 = st.text_input("Kurse 2", "")
gpa2 = st.text_input("GPA 2", "")
clubs2 = st.text_input("Clubs/Aktivitäten 2", "")

# Professional Experience
st.header("Professional Experience")
experience1 = st.text_input("Erfahrung 1")
locatione1 = st.text_input("Standort Erfahrung 1")
position1 = st.text_input("Position 1")
timee1 = st.text_input("Zeitraum Erfahrung 1")
task11 = st.text_area("Aufgaben 1", key='task11', height=100)
task12 = st.text_area("Aufgaben 2", key='task12', height=100)
task13 = st.text_area("Aufgaben 3", key='task13', height=100)

experience2 = st.text_input("Erfahrung 2", "")
locatione2 = st.text_input("Standort Erfahrung 2", "")
position2 = st.text_input("Position 2", "")
timee2 = st.text_input("Zeitraum Erfahrung 2", "")
task21 = st.text_area("Aufgaben 1", key='task21', height=100)
task22 = st.text_area("Aufgaben 2", key='task22', height=100)
task23 = st.text_area("Aufgaben 3", key='task23', height=100)

experience3 = st.text_input("Erfahrung 3", "")
locatione3 = st.text_input("Standort Erfahrung 3", "")
position3 = st.text_input("Position 3", "")
timee3 = st.text_input("Zeitraum Erfahrung 3", "")
task31 = st.text_area("Aufgaben 1", key='task31', height=100)
task32 = st.text_area("Aufgaben 2", key='task32', height=100)
task33 = st.text_area("Aufgaben 3", key='task33', height=100)

# Extracurricular Activities / Engagement
st.header("Extracurricular Activities / Engagement")
extracurricular1 = st.text_input("Extrakurrikulare Aktivitäten")
additionaleducation1 = st.text_input("Zusätzliche Bildung")
certificates1 = st.text_input("Zertifikate und Errungenschaften")

# Skills & Interest
st.header("Skills & Interest")
languages1 = st.text_input("Sprachen")
computer1 = st.text_input("Computerkenntnisse")
interests1 = st.text_input("Interessen")

# Button zum Erstellen des CVs
if st.button("CV Erstellen"):
    # URL der LaTeX-Vorlage im GitHub-Repository
    url = "https://raw.githubusercontent.com/Deussaxum/Fixen-des-Generators/main/template_finance.tex"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            latex_template_string = response.text
        else:
            st.error("Vorlage konnte nicht geladen werden.")
            st.stop()
    except Exception as e:
        st.error(f"Fehler beim Laden der Vorlage: {e}")
        st.stop()

    try:
        # Erstellen des Template-Objekts und Formatierung des LaTeX-Templates
        latex_template = Template(latex_template_string)
        latex_filled = latex_template.safe_substitute(
            # ... [Ihre Platzhalter und Werte wie zuvor] ...
        )

        # Erstellen einer temporären Datei und Schreiben des LaTeX-Codes
        with tempfile.NamedTemporaryFile(delete=False, suffix=".tex", mode='w+') as tmpfile:
            tmpfile.write(latex_filled)
            tmpfile.seek(0)
            st.text_area("Vorschau des LaTeX-Dokuments", tmpfile.read(), height=300)

        # Optional: Senden des Inhalts an die API
        # ... [Ihr Code zur Kommunikation mit der API] ...

    except KeyError as key_err:
        st.error(f"Fehler bei der Formatierung: Unbekannter Platzhalter {key_err}")
        st.stop()
    except Exception as format_err:
        st.error(f"Fehler bei der Formatierung: {format_err}")
        st.stop()