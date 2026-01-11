# Selenium Automation – Demo Booking Application

## Project Overview
This repository contains automated UI tests for a public demo booking application using Selenium WebDriver with Python.  
The project was created for hands-on learning, focusing on real-world automation challenges rather than idealized scenarios.

## Application Under Test
- Base URL: https://automationintesting.online/
- Environment: Public demo (non-production)

## Tools & Technologies
- Python 3.14.0
- Selenium WebDriver 4.38.0
- BDD-style feature files (Gherkin syntax)
- Chrome WebDriver
- PyCharm IDE

## Test Scope
The automation covers the following areas:
- Page navigation and UI rendering
- Room listing interactions
- Booking-related UI flows
- Element visibility and interaction validation

## Automation Approach
The tests follow a BDD-style structure where feature files describe user behavior, and Python step definitions implement Selenium interactions.


## Prerequisites
- Python 3.8 or higher
- Chrome browser installed
- ChromeDriver (compatible with your Chrome version)

## Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/Lurese/automation.git
cd automation
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run all tests**
```bash
behave
```
 **Run specific feature**
```bash
behave features/availability.feature
behave features/contact.feature

## Project Structure
```
├── features/          # BDD feature files
├── steps/             # Step definitions
├── pages/             # Page object 
├── utils/             # Helper functions
└── requirements.txt   # Python dependencies
```

## Known Issues
Some UI elements on the rooms page exhibit inconsistent responsiveness during automation. Multiple interaction strategies (explicit waits, JavaScript executors, action chains) have been attempted. This is documented as part of the learning process.

## Key Learnings
- Handling dynamic content loading in Selenium
- Implementing wait strategies for stable automation
- Structuring BDD tests for maintainability
- Debugging unresponsive UI element interactions

## Future Enhancements
- Add reporting functionality
- Expand test coverage
- Implement cross-browser testing
- Add CI/CD integration

## Contributing
Feedback and suggestions are welcome, particularly on handling the documented UI interaction challenges.

## License
This project is for educational purposes.

---
**Note:** This is a practice project for learning test automation. The application under test is a publicly available demo site.
