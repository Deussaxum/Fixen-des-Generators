import streamlit as st
import requests

# Funktion zur Extraktion von Informationen aus der API-Antwort
def extract_info(jsondata):
    keys = ['full_name', 'city', 'state', 'country', 'education', 'experiences', 'volunteer_work', 'certifications', 'languages', 'interests']
    return {key: jsondata.get(key, [] if key != 'full_name' else '') for key in keys}

# Funktion zum Abrufen von Informationen
def retrieve_info(linkedin_profile_url):
    api_key = '_EIqMpWEbOnJLoQvNFz1CQ'
    headers = {'Authorization': 'Bearer ' + api_key}
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    params = {'linkedin_profile_url': linkedin_profile_url}
    response = requests.get(api_endpoint, params=params, headers=headers)
    if response.status_code == 200:
        return extract_info(response.json())
    else:
        st.error(f"Profilinformationen konnten nicht abgerufen werden: HTTP {response.status_code}")
        return None

# Funktion zum Erstellen des LaTeX-Codes
def build_latex_code(**kwargs):
    # LaTeX-Code-Vorlage hier einfügen
     latex_code = r"""
    % Hier kommt Ihr LaTeX-Code
    \documentclass[a4paper,8pt]{{article}}
    \usepackage{{parskip}}
    \usepackage{{hologo}}
    \usepackage{{fontspec}}
    \RequirePackage{{color}}
    \RequirePackage{{graphicx}}
    \usepackage[usenames,dvipsnames]{{xcolor}}
    \usepackage[scale=0.9, top=.4in, bottom=.4in]{{geometry}}
    \usepackage{{enumitem}}
    \usepackage{{tabularx}}
    \usepackage{{enumitem}}
    \newcolumntype{{C}}{{>{{\centering\arraybackslash}}X}} 
    \usepackage{{supertabular}}
    \usepackage{{tabularx}}
    \newlength{{\fullcollw}}
    \setlength{{\fullcollw}}{{0.42\textwidth}}
    \usepackage{{titlesec}}             
    \usepackage{{multicol}}
    \usepackage{{multirow}}
    \titleformat{{\section}}{{\Large\scshape\raggedright}}{{}}{{0em}}{{}}[\titlerule]
    \titlespacing{{\section}}{{0pt}}{{2pt}}{{2pt}}
    \usepackage[style=authoryear,sorting=ynt, maxbibnames=2]{{biblatex}}
    \usepackage[unicode, draft=false]{{hyperref}}
    \color[HTML]{{110223}}
    \addbibresource{{citations.bib}}
    \setlength\bibitemsep{{1em}}
    \usepackage{{fontawesome5}}
    \usepackage[normalem]{{ulem}}
    \setmainfont{{Arial}}
    \begin{{document}}
    \pagestyle{{empty}}
    \begin{{tabularx}}{{\linewidth}}{{@{{}} C @{{}}}}
    \color[HTML]{{1C033C}} \Huge\textbf{{{name}}} \\[6pt]
    \textcolor[HTML]{{1C033C}} Address: {address} \\
    \textcolor[HTML]{{1C033C}} Mobile: {phone} \\
    \textcolor[HTML]{{1C033C}} Email: {email}
    \end{{tabularx}}
    \section{{EDUCATION}}
    \textbf{{{university1}}} \hfill \textbf{{{locationus1}}} \\
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
        \item {majorus1} \hfill \color[HTML]{{1C033C}} {timeus1}
    \end{{itemize}}
    \begin{{itemize}}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
        \item Courses: {courses1}
        \item GPA: {gpa1}
        \item {clubs1}
    \end{{itemize}}
    \textbf{{{university2}}} \hfill \textbf{{{locationus2}}} \\
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
        \item {majorus2} \hfill \color[HTML]{{1C033C}} {timeus2}
    \end{{itemize}}
    \begin{{itemize}}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
        \item Courses: {courses2}
        \item GPA: {gpa2}
        \item {clubs2}
    \end{{itemize}}
    \section{{PROFESSIONAL EXPERIENCE}}
    \textbf{{{experience1}}} \hfill \textbf{{{locatione1}}} \\
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
        \item \textit{{{position1}}} \hfill \color[HTML]{{1C033C}} {timee1}
    \end{{itemize}}
    \begin{{itemize}}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
        \item {task11}
        \item {task12}
        \item {task13}
    \end{{itemize}}
    \textbf{{{experience2}}} \hfill \textbf{{{locatione2}}} \\
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
        \item \textit{{{position2}}} \hfill \color[HTML]{{1C033C}} {timee2}
    \end{{itemize}}
    \begin{{itemize}}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
        \item {task21}
        \item {task22}
        \item {task23}
    \end{{itemize}}
    \textbf{{{experience3}}} \hfill \textbf{{{locatione3}}} \\
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
        \item \textit{{{position3}}} \hfill \color[HTML]{{1C033C}} {timee3}
    \end{{itemize}}
    \begin{{itemize}}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
        \item {task31}
        \item {task32}
        \item {task33}
    \end{{itemize}}
    \section{{EXTRACURRICULAR ACTIVITIES / ENGAGEMENT}}
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
        \item Extracurricular: {extracurricular1}
        \item Additional Education: {additionaleducation1}
        \item Certificate & Achievements: {certificates1}
    \end{{itemize}}
    \section{{SKILLS /& INTEREST}}
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
        \item Languages: {languages1}
        \item Computer: {computer1}
        \item Interests: {interests1}
    \end{{itemize}}
    \end{{document}}
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
        linkedin_data = {}
        if st.button('LinkedIn-Daten abrufen', key=f'retrieve_data_{tab.index}'):
            linkedin_data = retrieve_info(linkedin_profile_url) or {}

        # Eingabefelder für Benutzerdaten
        form = st.form(key=f'form_{tab.index}')
        name = form.text_input("Name", value=linkedin_data.get('full_name', ''))
        address = form.text_input("Adresse")
        phone = form.text_input("Telefonnummer")
        email = form.text_input("E-Mail")

        # Weitere Eingabefelder (vereinfacht für Demonstration)
        # Fügen Sie hier weitere Felder nach Bedarf hinzu...

        # LaTeX-Code generieren und anzeigen
        if form.form_submit_button("CV erstellen"):
            latex_code = build_latex_code(name=name, address=address, phone=phone, email=email)
            st.text_area("Generierter LaTeX-Code", latex_code, height=300)
