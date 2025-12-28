# HE Access Assistant (UK)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)

A decision-support web application designed to help asylum seekers and refugees understand potential pathways into UK higher education.

## 🎯 Project Overview

The HE Access Assistant provides guidance on navigating the UK higher education system for individuals with international qualifications. The tool offers approximate mapping to UK education levels and suggests appropriate study pathways.

**Motivation**: This project was inspired by my volunteer work with Aspiring Dreams, where I support asylum seekers and refugees through university applications. I noticed a significant need for accessible guidance on understanding UK education pathways.

## ✨ Key Features

- **Qualification Input System**: Users can input their existing international qualifications and study background
- **UK Level Mapping**: Approximate mapping to likely UK education levels with confidence indicators
- **Pathway Recommendations**: Suggests appropriate routes including:
  - Access to Higher Education Diplomas
  - Foundation Year programs
  - Undergraduate degrees
  - Postgraduate studies
- **Personalized Action Plan**: Automatically generated checklist of next steps
- **Official Guidance**: Clear signposting to official verification services and university admissions teams

## 🛠️ Technology Stack

- **Python 3.8+**: Core programming language
- **Streamlit**: Web application framework for rapid prototyping
- **pandas**: Data manipulation and qualification mapping

## 📋 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/EmmsAdams/he-access-assistant.git
cd he-access-assistant

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## 🔍 How It Works

1. User inputs their educational background and international qualifications
2. System analyzes input against UK education framework
3. Application provides approximate UK level equivalencies with confidence ratings
4. Generates personalized recommendations and actionable next steps
5. Directs users to official verification services for formal assessment

## ⚖️ Ethics & Limitations

**Important Disclaimers:**
- This tool provides **guidance only** and does not constitute legal or official advice
- Qualification recognition is approximate and must be verified with official bodies
- Users are explicitly directed to:
  - [UK ENIC](https://www.enic.org.uk/) for official qualification comparisons
  - Individual university admissions teams for final verification
  - [UCAS](https://www.ucas.com/) for application guidance

This approach ensures users understand the tool's limitations while receiving helpful initial guidance.

## 🚀 Future Enhancements

- Integration with UK ENIC API for real-time verification
- Multi-language support for better accessibility
- Expanded database of international qualification mappings
- University-specific pathway recommendations based on entry requirements
- Mobile-responsive design improvements

## 💡 What I Learned

This project taught me:
- Building user-centered applications that address real community needs
- Implementing ethical design considerations in software development
- Working with Streamlit for rapid web application prototyping
- Data mapping and classification logic
- Importance of clear disclaimers and user guidance

## 👤 About the Developer

This project was independently developed by Emmelyn Adams, a Computer Science student at Northumbria University. It combines my technical skills with my volunteer work at Aspiring Dreams, where I help asylum seekers and refugees navigate university application processes. This is a personal initiative to address a real need I identified in my community work.

**Connect with me:**
- GitHub: [@EmmsAdams](https://github.com/EmmsAdams)
- Email: emmelynadams40@gmail.com
- LinkedIn: [Your LinkedIn Profile]
- Location: Newcastle, UK

## 📄 License

This project is open source and available for educational and community purposes.

## 🤝 Contributing

Feedback and contributions are welcome! If you have suggestions for improvements or find any issues:
1. Open an issue describing your suggestion
2. Fork the repository and create a pull request
3. Contact me directly with feedback

---

**Note**: This application is designed to assist, not replace, professional qualification assessment services. Always verify information with official bodies before making educational decisions.

**Built with ❤️ for the refugee and asylum seeker community**
