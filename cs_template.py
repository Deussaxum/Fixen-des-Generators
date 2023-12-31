import streamlit as st
import subprocess

def build_latex_code(name, address, phone, email, university1, locationus1, majorus1, timeus1, courses1, gpa1, clubs1, university2, locationus2, majorus2, timeus2, courses2, gpa2, clubs2, experience1, locatione1, position1, timee1, task11, task12, experience2, locatione2, position2, timee2, task21, task22, extracurricular1, additionaleducation1, certificates1, languages1, projectname1, planguage1, pfunction1, timep1, taskp11, taskp12, planguage2, pfunction2, timep2, taskp21, taskp22, technologies1):
    latex_code = fr"""
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
    \textbf{{{university1}}} \hfill \textbf{{{locationus1}}} \\[-3ex]
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
        \item {majorus1} \hfill \color[HTML]{{1C033C}} {timeus1}
    \end{{itemize}}
    \begin{{itemize}}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
        \item Courses: {courses1}
        \item GPA: {gpa1}
        \item {clubs1}
    \end{{itemize}}
    \textbf{{{university2}}} \hfill \textbf{{{locationus2}}} \\[-3ex]
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
        \item {majorus2} \hfill \color[HTML]{{1C033C}} {timeus2}
    \end{{itemize}}
    \begin{{itemize}}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
        \item Courses: {courses2}
        \item GPA: {gpa2}
        \item {clubs2}
    \end{{itemize}}
    \section{{PROFESSIONAL EXPERIENCE}}
    \textbf{{{experience1}}} \hfill \textbf{{{locatione1}}} \\[-3ex]
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
        \item \textit{{{position1}}} \hfill \color[HTML]{{1C033C}} {timee1}
    \end{{itemize}}
    \begin{{itemize}}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
        \item {task11}
        \item {task12}
    \end{{itemize}}
    \textbf{{{experience2}}} \hfill \textbf{{{locatione2}}} \\[-3ex]
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
        \item \textit{{{position2}}} \hfill \color[HTML]{{1C033C}} {timee2}
    \end{{itemize}}
    \begin{{itemize}}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
        \item {task21}
        \item {task22}
    \end{{itemize}}
    \section{{PROJECTS}}
    \textbf{{{projectname1}}} \hfill \textbf{{{planguage1}}} \\[-3ex]
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
    \item \textit{{{pfunction1}}} \hfill \color[HTML]{{1C033C}} {timep1}
    \end{{itemize}}
    \begin{{itemize}}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
        \item {taskp11}
        \item {taskp12}
    \end{{itemize}}
    \textbf{{{projectname2}}} \hfill \textbf{{{planguage2}}} \\[-3ex]
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
    \item \textit{{{pfunction2}}} \hfill \color[HTML]{{1C033C}} {timep2}
    \end{{itemize}}
    \begin{{itemize}}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
        \item {taskp21}
        \item {taskp22}
    \end{{itemize}}
    \section{{EXTRACURRICULAR ACTIVITIES / ENGAGEMENT}}
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
        \item Extracurricular: {extracurricular1}
        \item Additional Education: {additionaleducation1}
        \item Certificate & Achievements: {certificates1}
    \end{{itemize}}
    \section{{SKILLS}}
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
        \item Languages: {languages1}
        \item Technologies / Tools:: {technologies1}
    \end{{itemize}}
    \end{{document}}
    """
    return latex_code

st.write("# CV Creator")
st.write("Enter your information:")

name = st.text_input("Name", "Your Name")
address = st.text_input("Address", "Your Address")
phone = st.text_input("Phone", "Your Phone")
email = st.text_input("Email", "your.email@example.com")

# Education Inputs
university1 = st.text_input("University 1", "University Name")
locationus1 = st.text_input("Location of University 1", "Location")
majorus1 = st.text_input("Major at University 1", "Major")
timeus1 = st.text_input("Time at University 1", "Time Period")
courses1 = st.text_input("Courses at University 1", "Courses")
gpa1 = st.text_input("GPA at University 1", "GPA")
clubs1 = st.text_input("Clubs at University 1", "Clubs")

university2 = st.text_input("University 2", "Second University Name")
locationus2 = st.text_input("Location of University 2", "Location")
majorus2 = st.text_input("Major at University 2", "Major")
timeus2 = st.text_input("Time at University 2", "Time Period")
courses2 = st.text_input("Courses at University 2", "Courses")
gpa2 = st.text_input("GPA at University 2", "GPA")
clubs2 = st.text_input("Clubs at University 2", "Clubs")

# Professional Experience Inputs
experience1 = st.text_input("First Experience", "Company/Organization")
locatione1 = st.text_input("Location of First Experience", "Location")
position1 = st.text_input("Position at First Experience", "Position")
timee1 = st.text_input("Time Period at First Experience", "Time Period")
task11 = st.text_input("Task 1 at First Experience", "Task")
task12 = st.text_input("Task 2 at First Experience", "Task")

experience2 = st.text_input("Second Experience", "Second Company/Organization")
locatione2 = st.text_input("Location of Second Experience", "Location")
position2 = st.text_input("Position at Second Experience", "Position")
timee2 = st.text_input("Time Period at Second Experience", "Time Period")
task21 = st.text_input("Task 1 at Second Experience", "Task")
task22 = st.text_input("Task 2 at Second Experience", "Task")

#Programming Projects
projectname1 = st.text_input("Programming Project 1", "Search AI")
planguage1 = st.text_input("Programming tools used in the project", "Python, Java Script, SQL Server, HTML")
pfunction1 = st.text_input("Projects function", "Web Scraper for daily search")
timep1 = st.text_input("Time of the Project", "05/2022 - 08/2022")
taskp11 = st.text_input(" Task done during integration 1", "Finetuned a ChatGPT API")
taskp12 = st.text_input("Task done during integration 2", "Designed a Website with HTML")

projectname2 = st.text_input("Programming Project 2", "Picturest")
planguage2 = st.text_input("Programming tools used in the project", "C++, Java Script, Git")
pfunction2 = st.text_input("Projects function", "Picture upscaler")
timep2 = st.text_input("Time of the Project", "09/2021 - 12/2021")
taskp21 = st.text_input(" Task done during integration 1", "Selecting and implementing a suitable upscaling method, such as bicubic interpolation")
taskp22 = st.text_input("Task done during integration 2", "Used JavaScript to create interactive components in the user interface")
# Extracurricular Activities
extracurricular1 = st.text_input("Extracurricular Activities", "Activities")

# Additional Education and Certificates
additionaleducation1 = st.text_input("Additional Education", "Courses or Training")
certificates1 = st.text_input("Certificates and Achievements", "Certificates")

# Skills and Interests
languages1 = st.text_input("Programming Languages", "Python, PHP, C++, SQL, HTML, JavaScript")
technologies1 = st.text_input("Technologies / Tools", "Flask, Django, Git, Linux, Docker")


# Compile LaTeX Button
if st.button("Generate LaTeX"):
    latex_code = build_latex_code(name, address, phone, email, university1, locationus1, majorus1, timeus1, courses1, gpa1, clubs1, university2, locationus2, majorus2, timeus2, courses2, gpa2, clubs2, experience1, locatione1, position1, timee1, task11, task12, experience2, locatione2, position2, timee2, task21, task22, extracurricular1, additionaleducation1, certificates1, languages1, projectname1, planguage1, pfunction1, timep1, taskp11, taskp12, planguage2, pfunction2, timep2, taskp21, taskp22, technologies1)
    st.text_area("Generated LaTeX Code:", latex_code, height=300)
    
    st.markdown("### How to Create a Pdf with this LaTeX Code")
    st.markdown("""
    - Copy the entire LaTeX code above.
    - Visit [Overleaf](https://www.overleaf.com/project) and create a new project.te that you will need to create a free account if you don't already have one.
    - In the project settings, set the compiler to either XeLaTeX or LuaTeX.
    - Paste the copied code on the left side of the Overleaf editor.
    - Compile the document to generate a PDF.
    - Download the PDF from Overleaf once it's compiled.
    """)

