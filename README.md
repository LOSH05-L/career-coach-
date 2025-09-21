# Career & Skills Advisor

A GenAI-powered career guidance chatbot designed for students in Tier 2/3 India. Built entirely using free-tier tools, it delivers personalized career paths, skill recommendations, and local job suggestions—all through a simple, multilingual chat interface.

---

## Problem Statement

Students in underserved regions often lack access to career mentors, guidance counselors, or reliable platforms. Language barriers, limited digital literacy, and lack of exposure to job markets make it difficult for them to make informed career decisions. This solution aims to bridge that gap using conversational AI.

---

## Solution Overview

Career & Skills Advisor is a browser-based chatbot that uses Google Cloud’s Gemini model to provide personalized career advice. Users can ask questions in English, Telugu, or Hindi and receive tailored guidance, including:

- Career paths based on education and interests  
- Required skills and free online courses  
- Local job suggestions and skill gap analysis  

The interface mimics WhatsApp-style chat, making it intuitive and accessible even for first-time users. No app download or login is required.

---

## Technologies Used

**GenAI Integration**
- Gemini via Vertex AI (Google Cloud): Generates personalized career advice
- Google Cloud Translation API (optional): Enables multilingual support

**Frontend**
- Streamlit (Python): Browser-based chat interface

**Backend and Logic**
- Python: Manages prompt construction, API communication, and response formatting
- Google Cloud SDK + gcloud CLI: Used for authentication and project configuration

**Data Layer**
- Static JSON files (`jobs.json`, `skills.json`): Store job roles and skill mappings
- Optional: Google Sheets or Firebase for dynamic data storage

**Deployment**
- Streamlit Cloud or local server: Hosts the application
- GitHub: Version control and hackathon submission

---

## Architecture

