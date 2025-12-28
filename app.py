"""
HE Access Assistant (UK)
A web application to help asylum seekers and refugees navigate UK higher education pathways
Developer: Emmelyn Adams
"""

import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="HE Access Assistant (UK)",
    page_icon="🎓",
    layout="wide"
)

# Qualification mapping data
QUALIFICATION_LEVELS = {
    "Primary School (up to age 11-12)": 1,
    "Lower Secondary School (ages 12-15)": 2,
    "Upper Secondary School/High School Certificate": 3,
    "Technical/Vocational Diploma": 3,
    "Higher Secondary/Pre-University (A-Level equivalent)": 3,
    "Foundation/Access Course": 3,
    "Bachelor's Degree (3-4 years)": 6,
    "Master's Degree": 7,
    "Doctoral Degree (PhD)": 8,
    "No formal qualifications": 0
}

# UK pathway recommendations
def get_uk_equivalent(level):
    """Map international qualification level to UK equivalent"""
    if level == 0:
        return "Entry Level", "Limited formal education"
    elif level == 1:
        return "UK Entry Level / Level 1", "Primary education equivalent"
    elif level == 2:
        return "UK Level 1-2 (GCSE equivalent)", "Lower secondary education"
    elif level == 3:
        return "UK Level 3 (A-Level equivalent)", "Upper secondary/college level"
    elif level >= 6:
        return "UK Level 6+ (Degree level)", "Higher education qualification"
    else:
        return "UK Level 2-3", "Secondary/college level"

def recommend_pathway(level, age, english_level):
    """Recommend appropriate UK education pathway"""
    pathways = []
    
    if level == 0 or level == 1:
        pathways.append({
            "pathway": "English for Speakers of Other Languages (ESOL)",
            "duration": "Varies (3-12 months)",
            "description": "Essential first step to improve English language skills",
            "next_steps": "After completing ESOL, consider Skills Bootcamps or Access to HE"
        })
        pathways.append({
            "pathway": "Functional Skills (English & Maths)",
            "duration": "3-6 months",
            "description": "Build fundamental skills needed for further study",
            "next_steps": "Progress to Level 2 qualifications or Access to HE"
        })
    
    if level <= 2:
        pathways.append({
            "pathway": "Access to Higher Education Diploma",
            "duration": "1 year (full-time) or 2 years (part-time)",
            "description": "Specifically designed for adults returning to education. No formal qualifications required.",
            "next_steps": "Direct entry to undergraduate degree programmes"
        })
        pathways.append({
            "pathway": "Skills Bootcamps",
            "duration": "12-16 weeks",
            "description": "Free, flexible training in digital, technical and green skills",
            "next_steps": "Employment or further study"
        })
    
    if level == 3:
        pathways.append({
            "pathway": "Foundation Year (Year 0) + Undergraduate Degree",
            "duration": "4 years total",
            "description": "Foundation year prepares you for degree-level study",
            "next_steps": "Progress to full undergraduate degree"
        })
        pathways.append({
            "pathway": "Direct Entry to Undergraduate Degree",
            "duration": "3-4 years",
            "description": "Apply directly to university with A-Level equivalent qualifications",
            "next_steps": "Complete bachelor's degree, then employment or postgraduate study"
        })
    
    if level >= 6:
        pathways.append({
            "pathway": "Postgraduate Taught Masters",
            "duration": "1 year (full-time) or 2 years (part-time)",
            "description": "Advanced study with existing bachelor's degree",
            "next_steps": "Professional career or PhD study"
        })
        pathways.append({
            "pathway": "Postgraduate Research (PhD)",
            "duration": "3-4 years",
            "description": "Original research leading to doctoral qualification",
            "next_steps": "Academic or research career"
        })
    
    # Filter based on English level
    if english_level == "Beginner (learning basic words and phrases)":
        pathways.insert(0, {
            "pathway": "ESOL - Priority Recommendation",
            "duration": "6-12 months",
            "description": "Focus on English language acquisition before other studies",
            "next_steps": "Re-assess education pathways after achieving B1/B2 English level"
        })
    
    return pathways

def generate_checklist(level, pathways):
    """Generate personalized action checklist"""
    checklist = []
    
    # Universal first steps
    checklist.extend([
        "📧 Register with local colleges offering ESOL and Access courses",
        "🌐 Create account on UCAS (Universities and Colleges Admissions Service) website",
        "📄 Get official UK ENIC Statement of Comparability for your qualifications"
    ])
    
    # Level-specific steps
    if level <= 2:
        checklist.extend([
            "📚 Enquire about Access to Higher Education Diplomas at local colleges",
            "💰 Check eligibility for Advanced Learner Loan (fee support)",
            "🤝 Contact refugee support organizations for education guidance"
        ])
    
    if level >= 3:
        checklist.extend([
            "🎓 Research universities with refugee scholarship programmes",
            "💷 Investigate student finance options (fees may be covered after 3 years UK residency)",
            "📝 Prepare personal statement highlighting your experience and goals"
        ])
    
    checklist.extend([
        "🔍 Verify settlement status/immigration requirements with universities",
        "💼 Look for part-time work or volunteering to build UK experience",
        "🏛️ Contact university widening participation teams for additional support"
    ])
    
    return checklist

# App header
st.title("🎓 HE Access Assistant (UK)")
st.markdown("*Supporting asylum seekers and refugees to navigate UK higher education pathways*")

st.markdown("---")

# Important disclaimer at the top
st.warning("""
⚠️ **Important Disclaimer**

This tool provides **guidance only** and does not constitute legal or official advice. 
All qualification assessments are approximate and must be verified with:
- [UK ENIC](https://www.enic.org.uk/) for official qualification recognition
- Individual university admissions teams
- [UCAS](https://www.ucas.com/) for application support

This guidance is a starting point to help you understand potential pathways.
""")

st.markdown("---")

# Input section
st.header("📋 Tell Us About Your Background")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Educational Background")
    
    highest_qualification = st.selectbox(
        "What is your highest level of education?",
        options=list(QUALIFICATION_LEVELS.keys()),
        help="Select the option that best matches your educational background"
    )
    
    years_since_study = st.slider(
        "How many years since you completed this qualification?",
        min_value=0,
        max_value=30,
        value=5,
        help="This helps us understand if you might need additional preparation"
    )
    
    country_of_study = st.text_input(
        "In which country did you complete your education?",
        placeholder="e.g., Syria, Afghanistan, Iran",
        help="Helps identify if UK ENIC can compare your qualifications"
    )

with col2:
    st.subheader("Current Situation")
    
    age = st.number_input(
        "Your age",
        min_value=16,
        max_value=100,
        value=25,
        help="Some programmes have age-specific support"
    )
    
    english_level = st.select_slider(
        "English language level (self-assessment)",
        options=[
            "Beginner (learning basic words and phrases)",
            "Elementary (can have simple conversations)",
            "Intermediate (can communicate in most situations)",
            "Upper Intermediate (confident in most contexts)",
            "Advanced (fluent, university-ready)"
        ],
        value="Intermediate (can communicate in most situations)"
    )
    
    residence_status = st.selectbox(
        "Immigration/residence status",
        options=[
            "Asylum seeker (application pending)",
            "Refugee status granted",
            "Humanitarian protection",
            "Indefinite Leave to Remain",
            "Other/Prefer not to say"
        ],
        help="This may affect funding eligibility"
    )

# Study preferences
st.subheader("🎯 Your Study Goals")

col3, col4 = st.columns(2)

with col3:
    subject_interest = st.multiselect(
        "Subject areas of interest",
        options=[
            "Business & Management",
            "Computing & Technology",
            "Engineering",
            "Health & Social Care",
            "Law",
            "Arts & Humanities",
            "Sciences",
            "Education",
            "Other"
        ],
        help="Select all that apply"
    )

with col4:
    study_mode = st.radio(
        "Preferred study mode",
        options=[
            "Full-time",
            "Part-time",
            "Flexible/Distance learning"
        ]
    )

# Generate recommendations button
st.markdown("---")

if st.button("🔍 Generate Pathway Recommendations", type="primary"):
    
    # Calculate qualification level
    qual_level = QUALIFICATION_LEVELS[highest_qualification]
    
    # Get UK equivalent
    uk_equivalent, description = get_uk_equivalent(qual_level)
    
    # Generate recommendations
    pathways = recommend_pathway(qual_level, age, english_level)
    
    # Generate checklist
    checklist = generate_checklist(qual_level, pathways)
    
    # Display results
    st.markdown("---")
    st.header("📊 Your Personalized Guidance")
    
    # Qualification assessment
    st.subheader("🎓 Qualification Assessment")
    
    col5, col6 = st.columns(2)
    
    with col5:
        st.metric("Your Qualification Level", qual_level)
        st.caption(highest_qualification)
    
    with col6:
        st.metric("Approximate UK Equivalent", uk_equivalent)
        st.caption(description)
    
    # Confidence indicator
    if years_since_study <= 5 and country_of_study:
        confidence = "High"
        confidence_color = "green"
    elif years_since_study <= 10:
        confidence = "Medium"
        confidence_color = "orange"
    else:
        confidence = "Lower"
        confidence_color = "red"
    
    st.info(f"""
    **Assessment Confidence Level:** :{confidence_color}[{confidence}]
    
    This is an approximate assessment. For official recognition, you must obtain a UK ENIC Statement of Comparability.
    """)
    
    st.markdown("---")
    
    # Recommended pathways
    st.subheader("🛤️ Recommended Education Pathways")
    
    for i, pathway in enumerate(pathways, 1):
        with st.expander(f"**Option {i}: {pathway['pathway']}**", expanded=(i==1)):
            st.write(f"**Duration:** {pathway['duration']}")
            st.write(f"**Description:** {pathway['description']}")
            st.write(f"**Next Steps:** {pathway['next_steps']}")
    
    st.markdown("---")
    
    # Personalized checklist
    st.subheader("✅ Your Next Steps Checklist")
    
    st.write("Here are the actions you should take:")
    
    for item in checklist:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    # Important resources
    st.subheader("🔗 Essential Resources")
    
    resources_col1, resources_col2 = st.columns(2)
    
    with resources_col1:
        st.markdown("""
        **Official Verification Services:**
        - [UK ENIC](https://www.enic.org.uk/) - Qualification comparison service
        - [UCAS](https://www.ucas.com/) - University applications
        - [GOV.UK Student Finance](https://www.gov.uk/student-finance) - Funding information
        """)
    
    with resources_col2:
        st.markdown("""
        **Support Organizations:**
        - [Refugee Council](https://www.refugeecouncil.org.uk/) - Education support
        - [STAR Network](https://www.star-network.org.uk/) - Student refugee support
        - [Access HE](https://www.accesstohe.ac.uk/) - Access courses directory
        """)
    
    st.markdown("---")
    
    # Funding information
    st.subheader("💰 Funding & Financial Support")
    
    if residence_status == "Refugee status granted":
        st.success("""
        ✅ **Good News!** With refugee status, you may be eligible for:
        - Home fee status (lower tuition fees)
        - Student loans for tuition and living costs
        - University refugee scholarships
        - Council of Europe Development Bank loans
        """)
    elif residence_status == "Asylum seeker (application pending)":
        st.info("""
        ℹ️ As an asylum seeker, funding options may be limited, but you can:
        - Apply for refugee-specific scholarships
        - Look for hardship funds at universities
        - Consider part-time study with part-time work
        - Access free courses through local colleges
        """)
    else:
        st.info("""
        ℹ️ Funding eligibility depends on your specific immigration status. Contact:
        - University student finance teams directly
        - UKCISA (UK Council for International Student Affairs)
        - Your support organization for detailed advice
        """)
    
    # Download option
    st.markdown("---")
    st.info("💡 **Tip:** Take a screenshot of this guidance for your records, or note down the key recommendations.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p><strong>HE Access Assistant (UK)</strong></p>
    <p>Developed by Emmelyn Adams | Computer Science Student, Northumbria University</p>
    <p>Inspired by volunteer work with Aspiring Dreams supporting refugees and asylum seekers</p>
    <p><em>Built with ❤️ for the refugee and asylum seeker community</em></p>
    <p>⚠️ Remember: This tool provides guidance only. Always verify information with official sources.</p>
</div>
""", unsafe_allow_html=True)
