import spacy
import pandas as pd
from spacy.matcher import Matcher

# Load spaCy's pre-trained model
nlp = spacy.load("en_core_web_sm")

# Sample resume text
resume_text = """
Swastika Siddhi Ashok Wagh
Experience:
- Developed scalable applications using Python and Django
- Managed a team of 5 engineers
Education:
- Bachelor of Science in Information Technology from DBATU University
Skills:
- Python, JavaScript, Django, AWS, Data Analysis
"""

# Parse the resume text using spaCy
doc = nlp(resume_text)

# Function to extract named entities for Name and Education
def extract_named_entities(doc):
    name = None
    education = None
    
    # Iterate over the entities to find Name and Education
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text
        elif ent.label_ == "ORG":
            education = ent.text
    return name, education

# Function to extract experience details (in a simplistic way for this example)
def extract_experience(resume_text):
    experience = []
    lines = resume_text.split('\n')
    for line in lines:
        if 'Experience' in line:
            continue  # Skip the title line
        if line.strip():
            experience.append(line.strip())
    return experience

# Function to extract skills (simply looking for keywords in this example)
def extract_skills(resume_text):
    skills_keywords = ['Python', 'JavaScript', 'Django', 'AWS', 'Data Analysis']
    skills = [skill for skill in skills_keywords if skill in resume_text]
    return skills

# Extract parsed data
name, education = extract_named_entities(doc)
experience = extract_experience(resume_text)
skills = extract_skills(resume_text)

# Create a DataFrame to display the output neatly
data = {
    "Field": ["Name", "Education", "Experience", "Skills"],
    "Details": [name, education, "\n".join(experience), ", ".join(skills)]
}

df = pd.DataFrame(data)

# Display the DataFrame as the resume parsing output
print(df)
