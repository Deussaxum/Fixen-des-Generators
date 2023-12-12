import streamlit as st
import requests

def build_pdf(name, address, email, university_name1, university_degree1, university_date1, university_name2, university_degree2, university_date2, research_experience1, research_date1, research_organization1, research_description1, research_experience2, research_date2, research_organization2, research_description2, professional_experience1, professional_date1, professional_organization1, professional_description1, professional_experience2, professional_date2, professional_organization2, professional_description2, awards1, awards2, skills, other_interests):
    # LaTeX template
    latex_template = r"""
    % Welcome to the simple DIS curriculum vitae template!
    % Please delete any sections that do not apply to your past experiences. We do not expect that applicants will have items for all of the sections included here. You can also rename or revise sections to best fit with your personal accomplishments.
    % The final document should not exceed 3 pages

    \documentclass[a4paper,11pt]{article}

    % ... (rest of the LaTeX template, unchanged)

    \begin{document}

    \begin{center}
        {\huge % Your Name} \\ \vspace{0pt}
        \begin{multicols}{2}
        \begin{flushleft}
        \large{% Your Address} \\
        \large{% Additional address information} \\
        \large{% PostalCode City Country} \\
        \end{flushleft}

        \begin{flushright}
        \large{% URL for website you want to link} \\
        \large{% your email address} \\
        \end{flushright}
        \end{multicols}
    \end{center}

    % Education section
    \section{Education}
    \resumeSubHeadingListStart
        \resumeSubheading{% University Name}
        {% Month Year -- Month Year}
        {% degree and major/field of study you are pursuing}
        {% City Country}
        \resumeSubheading{% Other University Name}
        {% Month Year -- Month Year}
        {% degree and major or coursework you pursued}
        {% City Country}
    \resumeSubHeadingListEnd

    % Research Experience section
    \section{Research Experience}
    \resumeSubHeadingListStart
        \resumeSubheading{% Research experience title}
        {% Month Year -- Month Year}
        {% University, Company or Organization}
        {% City, Country}
        \resumeItemListStart
        \small\resumeItem{% very short description of one thing you did}
        \resumeItem{% very short description of another thing you did}
        \resumeItem{% very short description if there was another thing you did}
        \resumeItemListEnd
        \resumeSubheading{% Research experience title}
        {% Month Year -- Month Year}
        {% University, Company or Organization}
        {% City, Country}
        \resumeItemListStart
        \small\resumeItem{% very short description of one thing you did}
        \resumeItem{% very short description of another thing you did}
        \resumeItem{% very short description if there was another thing you did}
        \resumeItemListEnd
    \resumeSubHeadingListEnd

    % Professional Experience section
    \section{Professional Experience}
    \resumeSubHeadingListStart
        \resumeSubheading{% Position title}
        {% Month Year -- Month Year}
        {% University, Company or Organization}
        {% City Country}
        \resumeItemListStart
        \small\resumeItem{% very short description of one thing you did}
        \resumeItem{% very short description of another thing you did}
        \resumeItem{% very short description if there was another thing you did}
        \resumeItemListEnd
        \resumeSubheading{% Another job title}
        {% Month Year -- Month Year}
        {% University, Company or Organization}
        {% City Country}
        \resumeItemListStart
        \small\resumeItem{% very short description of one thing you did}
        \resumeItem{% very short description of another thing you did}
        \resumeItem{% very short description if there was another thing you did}
        \resumeItemListEnd
    \resumeSubHeadingListEnd

    % Awards & Honors section
    \section{Awards \& Honors}
    \resumeSubHeadingListStart
        \resumeSubheading{% Title or brief description of the award}
        {}
        {% University, Sponsor or Organization}
        {% year(s)}
        \resumeSubheading{% Title or brief description of the award}
        {}
        {% University, Sponsor or Organization}
        {% year(s)}
    \resumeSubHeadingListEnd

    % Specialized Skills section
    \section{Specialized Skills}
    \begin{itemize}[leftmargin=0.15in, label={}]
        \small{\item{
            \textbf{Programming Languages}{: Python, Java, C++} \\
            \textbf{Software Tools}{: Microsoft Office, LaTeX} \\
            \textbf{Languages}{: English (native), Spanish (fluent)} \\
        }}
    \end{itemize}

    % Other Interests section
    \section{Other Interests}
    \begin{itemize}[leftmargin=0.15in, label={}]
        \small{\item{
            \textbf{Hobbies}{: Reading, Hiking, Painting} \\
        }}
    \end{itemize}

    \end{document}
    """

    # Fill in the LaTeX template with user data
    filled_template = latex_template.replace('% Your Name', name)
    filled_template = filled_template.replace('% Your Address', address)
    filled_template = filled_template.replace('% your email address', email)
    filled_template = filled_template.replace('% University Name', university_name1)
    filled_template = filled_template.replace('% degree and major/field of study you are pursuing', university_degree1)
    filled_template = filled_template.replace('% Month Year -- Month Year', university_date1)
    filled_template = filled_template.replace('% Other University Name', university_name2)
    filled_template = filled_template.replace('% degree and major or coursework you pursued', university_degree2)
    filled_template = filled_template.replace('% Month Year -- Month Year', university_date2)
    filled_template = filled_template.replace('% Research experience title', research_experience1)
    filled_template = filled_template.replace('% Month Year -- Month Year', research_date1)
    filled_template = filled_template.replace('% University, Company or Organization', research_organization1)
    filled_template = filled_template.replace('% very short description of one thing you did', research_description1)
    filled_template = filled_template.replace('% Research experience title', research_experience2)
    filled_template = filled_template.replace('% Month Year -- Month Year', research_date2)
    filled_template = filled_template.replace('% University, Company or Organization', research_organization2)
    filled_template = filled_template.replace('% very short description of one thing you did', research_description2)
    filled_template = filled_template.replace('% Position title', professional_experience1)
    filled_template = filled_template.replace('% Month Year -- Month Year', professional_date1)
    filled_template = filled_template.replace('% University, Company or Organization', professional_organization1)
    filled_template = filled_template.replace('% very short description of one thing you did', professional_description1)
    filled_template = filled_template.replace('% Position title', professional_experience2)
    filled_template = filled_template.replace('% Month Year -- Month Year', professional_date2)
    filled_template = filled_template.replace('% University, Company or Organization', professional_organization2)
    filled_template = filled_template.replace('% very short description of one thing you did', professional_description2)
    filled_template = filled_template.replace('% Title or brief description of the award', awards1)
    filled_template = filled_template.replace('% Title or brief description of the award', awards2)
    filled_template = filled_template.replace('% Programming Languages', skills)
    filled_template = filled_template.replace('% Hobbies', other_interests)

    # Send filled template to the LaTeX.Online API to generate PDF
    response = requests.post("https://latexonline.cc/compile", data={"text": filled_template})

    # Check if the response was successful
    if response.status_code == 200:
        st.success("CV generated successfully!")
        pdf_content = response.content
        st.write(pdf_content)

if __name__ == "__main__":
    st.title("Curriculum Vitae Generator")
    st.write("Fill in the fields below to generate your CV in LaTeX.")

    name = st.text_input("Your Name")
    address = st.text_area("Address")
    email = st.text_input("Email Address")
    university_name1 = st.text_input("University Name (1)")
    university_degree1 = st.text_input("Degree and Major (1)")
    university_date1 = st.text_input("Date (1) e.g., Month Year -- Month Year (University 1)")
    university_name2 = st.text_input("University Name (2)")
    university_degree2 = st.text_input("Degree and Major (2)")
    university_date2 = st.text_input("Date (2) e.g., Month Year -- Month Year (University 2)")
    research_experience1 = st.text_input("Research Experience Title (1)")
    research_date1 = st.text_input("Date (1) e.g., Month Year -- Month Year (Research 1)")
    research_organization1 = st.text_input("University, Company or Organization (1)")
    research_description1 = st.text_area("Description (1)")
    research_experience2 = st.text_input("Research Experience Title (2)")
    research_date2 = st.text_input("Date (2) e.g., Month Year -- Month Year (Research 2)")
    research_organization2 = st.text_input("University, Company or Organization (2)")
    research_description2 = st.text_area("Description (2)")
    professional_experience1 = st.text_input("Position Title (1)")
    professional_date1 = st.text_input("Date (1) e.g., Month Year -- Month Year (Professional 1)")
    professional_organization1 = st.text_input("University, Company or Organization (1)")
    professional_description1 = st.text_area("Description (1)")
    professional_experience2 = st.text_input("Position Title (2)")
    professional_date2 = st.text_input("Date (2) e.g., Month Year -- Month Year (Professional 2)")
    professional_organization2 = st.text_input("University, Company or Organization (2)")
    professional_description2 = st.text_area("Description (2)")
    awards1 = st.text_input("Awards & Honors (1)")
    awards2 = st.text_input("Awards & Honors (2)")
    skills = st.text_area("Specialized Skills (List programming languages, software tools, languages, etc.)")
    other_interests = st.text_area("Other Interests (Hobbies, etc.)")

    if st.button("Generate CV"):
        if not name or not address or not email:
            st.error("Please fill in your name, address, and email address.")
        else:
            build_pdf(name, address, email, university_name1, university_degree1, university_date1, university_name2, university_degree2, university_date2, research_experience1, research_date1, research_organization1, research_description1, research_experience2, research_date2, research_organization2, research_description2, professional_experience1, professional_date1, professional_organization1, professional_description1, professional_experience2, professional_date2, professional_organization2, professional_description2, awards1, awards2, skills, other_interests)