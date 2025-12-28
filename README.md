# HE Access Assistant (UK)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)

This web application helps asylum seekers and refugees understand their options for entering UK higher education.

## Project Overview

The HE Access Assistant offers guidance for those with international qualifications trying to navigate the UK higher education system. The tool maps qualifications to UK education levels and suggests possible study routes.

**Motivation**: My volunteer work with Aspiring Dreams inspired this project. I help asylum seekers and refugees with university applications. I realized there is a strong need for accessible advice on UK education pathways.

## Key Features

- **Qualification Input System**: Users can enter their international qualifications and educational history.
- **UK Level Mapping**: Provides approximate mapping to UK education levels along with confidence indicators.
- **Pathway Recommendations**: Offers suggestions for routes such as:
  - Access to Higher Education Diplomas
  - Foundation Year programs
  - Undergraduate degrees
  - Postgraduate studies
- **Personalized Action Plan**: Automatically creates a checklist of next steps.
- **Official Guidance**: Clearly directs users to verification services and university admissions teams.

## Technology Stack

- **Python 3.8+**: The main programming language.
- **Streamlit**: A framework for building web applications quickly.
- **pandas**: Used for data manipulation and qualification mapping.

## Installation & Setup

```bash
# Clone the repository
git clone https://github.com/EmmsAdams/he-access-assistant.git
cd he-access-assistant

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## How It Works

1. Users enter their educational background and international qualifications.
2. The system compares this input to the UK education framework.
3. The application shows approximate UK level equivalencies with confidence ratings.
4. It generates personalized recommendations and next steps.
5. Users are directed to official verification services for formal assessment.

## Ethics & Limitations

**Important Disclaimers:**
- This tool provides guidance only and does not serve as legal or official advice.
- Qualification recognition is approximate and should be verified with official organizations.
- Users are directed to:
  - [UK ENIC](https://www.enic.org.uk/) for official qualification comparisons.
  - Individual university admissions teams for final verification.
  - [UCAS](https://www.ucas.com/) for application guidance.

This approach helps users understand the tool's limitations while offering useful initial guidance.

## Future Enhancements

- Integration with the UK ENIC API for real-time verification.
- Multi-language support for greater accessibility.
- A wider database of international qualification mappings.
- University-specific pathway recommendations based on entry requirements.
- Improved mobile-responsive design.

## What I Learned

This project taught me:
- How to build user-centered applications that meet community needs.
- The importance of ethical design in software development.
- How to use Streamlit for quick web application prototyping.
- Data mapping and classification logic.
- The need for clear disclaimers and user guidance.

## About the Developer

This project was developed by Emmelyn Adams, a Computer Science student at Northumbria University. It combines my technical skills with my volunteer experience at Aspiring Dreams, where I assist asylum seekers and refugees with university applications. This initiative addresses a real need I noticed in my community work.

**Connect with me:**
- GitHub: [@EmmsAdams](https://github.com/EmmsAdams)
- Email: emmelynadams40@gmail.com
- LinkedIn: [Your LinkedIn Profile]
- Location: Newcastle, UK

## License

This project is open source and available for educational and community use.

## Contributing

Feedback and contributions are welcome! If you have suggestions or find any issues:
1. Open an issue to describe your suggestion.
2. Fork the repository and create a pull request.
3. Contact me directly with feedback.

---

**Note**: This application aims to assist, not replace, professional qualification assessment services. Always verify information with official organizations before making educational decisions. 

**Built with care for the refugee and asylum seeker community.**
