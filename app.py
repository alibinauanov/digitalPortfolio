from pathlib import Path

import streamlit as st
from PIL import Image

# Path settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Alibi Nauanov - Resume.pdf"
profile_pic = current_dir / "assets" / "meCircle.png"

# General settings
PAGE_TITLE = "Digital CV | Alibi Nauanov"
PAGE_ICON = ":wave:"
NAME = "Alibi Nauanov"
DESCRIPTION = """
Software Engineer, utilizing technical skills to create inventive solutions and contribute to the success of software applications.
"""
EMAIL = "alibi.nauanov@nyu.edu"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/alibinauanov/",
    "GitHub": "https://github.com/alibinauanov",
    "Instagram": "https://www.instagram.com/alibinauan/",
    "LeetCode": "https://leetcode.com/an3502/"
}
PROJECTS = {
    "🏆 Movix - Sophisticated movie database": "https://github.com/alibinauanov/movie-app",
    "🏆 Article Summarizer AI": "https://github.com/alibinauanov/article-summarizer-ai",
    "🏆 Weather App - Get a weather app to view the present weather conditions": "incredible-moonbeam-340408.netlify.app",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Load CSS, PDF, & Profile Pic
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# Hero section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.markdown(f"<h1 style='text-decoration:none;'>{NAME}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-decoration:none;'>{DESCRIPTION}</p>", unsafe_allow_html=True)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.markdown(f"<p style='text-decoration:none;'>📫 {EMAIL}</p>", unsafe_allow_html=True)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].markdown(
        f"<a style='text-decoration:none;' href='{link}'>{platform}</a>",
        unsafe_allow_html=True
    )


# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skills")
st.write(
    """
- 👩‍💻 Programming Languages: Python, Java, JavaScript, Typescript, C
- 👩‍💻 Frameworks: React.js, Vue.js, Next.js, Vite.js, Node.js, p5.js, Django, Express.js, MySQL, Firebase, Redux, Pandas, NumPy, Babel, Webpack, NuxtJS, Yarn
- 👩‍💻 Developer Tools: Git, Figma, Linux, Docker, AWS, Google Cloud Platforms, VS Code, Eclipse
"""
)

# --- Other Skills & Awards ---
st.write('\n')
st.subheader("Other Skills & Awards")
st.write(
    """
- 👩‍💻 All: UI/UX Design, Mobile Development
- 🎤 Languages: English(Fluent), Chinese(Intermediate), Kazakh(Native), Russian(Native)
- 🏆 Awards: International Association of Students in Economics and Business(AIESEC) case-competition 1st Place Fall 2022, AIESEC case-competition 3rd Place Spring 2022
"""
)

# --- Education ---
st.write('\n')
st.subheader("Education")
st.write(
    """
🏛 New York University - Bachelor of Science in Computer Science
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work Experience")
st.write("---")

# --- JOB 1
st.write("🚧", "**Full-Stack Development Intern | METANA**")
st.write("July 2023 - August 2023")
st.write(
    """
- ► Developed Python pipelines to streamline data processing and machine learning tasks, contributing to the API's creation and integration.
- ► Set up servers and APIs for configuration and deployment purposes for successful production
- ► Built the front-end components using JavaScript and Bubble for web development
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Front-end Development & UI UX Design Intern | Shoptaki**")
st.write("September 2022 - July 2023")
st.write(
    """
- ► Designed the user interface of Dashboard, Settings, Profile, SmartID, and Analytics pages as an MVP
- ► Developed the Front-end part with React.JS
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Full-Stack Development Summer Bootcamp | nFactorial Incubator**")
st.write("June 2022 - August 2022")
st.write(
    """
- ► Developed the website with React.js and write the Back-end in JS, Node.js, Lifecycle, Client-server, HTTP, API, Local Storage, MongoDB, and Express.js.
- ► One of the 180 participants selected from 4000+ applicants.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Business Development Intern | Grantly.Academy**")
st.write("February 2022 - April 2022")
st.write(
    """
- ► Spearheaded server management for amoCRM (Enterprise-focused web-hosted CRM for lead and sales management, from initial contact to completed sales)
- ► Resolved critical server crash issues and database errors, resulting in enhanced sales office efficiency of 20%
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")