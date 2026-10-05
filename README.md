# 🌱 AgriGuardians

### AI-Powered Crop Disease Detection and Management Platform

AgriGuardians is an AI-powered crop-health platform designed for the early detection and management of crop diseases and pest-related risks. The platform allows farmers and agricultural extension workers to upload crop leaf images and receive AI-based disease predictions with confidence scores.

The system combines deep-learning-based image classification with AI-generated agricultural advisory to transform disease detection into actionable crop-management guidance.

---

## 🎯 Problem Statement

**SIH Problem Statement ID: 26131**

**Early detection and management of crop diseases and pest infestations**

AgriGuardians aims to support early identification of crop diseases through image-based artificial intelligence and provide users with useful management guidance for faster intervention.

---

## 🚀 Key Features

- 🌿 AI-based crop disease detection
- 📷 Crop leaf image upload
- 🧠 Deep-learning disease classification
- 📊 Prediction confidence score
- 🤖 Gemini AI-powered disease advisory
- 👤 User authentication
- 🔐 Secure login and signup
- 🖼️ User profile management
- 📜 Prediction history
- 🌱 Crop-health focused dashboard
- 📱 Responsive web interface
- 💾 Database-backed prediction history

---

## 🧠 AI/ML Model

The platform uses a trained deep-learning model built using **TensorFlow/Keras** for crop disease classification.

The trained model is stored using **Git Large File Storage (Git LFS)** because of its large file size.

```text
Model:
crop_disease_model.keras



🏗️ System Architecture
                 ┌──────────────────────┐
                 │      User/Farmer     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Web Interface      │
                 │ HTML / CSS / JS       │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Django Backend       │
                 │ Django REST APIs     │
                 └──────────┬───────────┘
                            │
                  ┌─────────┴─────────┐
                  ▼                   ▼
        ┌─────────────────┐   ┌─────────────────┐
        │ TensorFlow/Keras│   │ Gemini AI       │
        │ Disease Model   │   │ Advisory        │
        └────────┬────────┘   └────────┬────────┘
                 │                     │
                 └──────────┬──────────┘
                            ▼
                 ┌──────────────────────┐
                 │ Prediction Result    │
                 │ + Advisory           │
                 └──────────────────────┘


🛠️ Technology Stack

Frontend
- HTML5
- CSS3
- JavaScript
- Responsive UI
Backend
- Python
- Django
- Django REST Framework
Artificial Intelligence
- TensorFlow
- Keras
- Deep Learning
- Image Classification
Generative AI
- Google Gemini API
Database
- SQLite (development)
Version Control
- Git
- GitHub
- Git LFS

📁 Project Structure
AgriGuardians/
│
├── backend/
│   ├── backend/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── base/
│   │   ├── ml_models/
│   │   │   └── crop_disease_model.keras
│   │   ├── templates/
│   │   ├── views.py
│   │   ├── api_views.py
│   │   ├── models.py
│   │   ├── forms.py
│   │   ├── urls.py
│   │   └── utils.py
│   │
│   ├── static/
│   ├── templates/
│   └── manage.py
│
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Installation

1. Clone the repository
	git clone https://github.com/BALU-216/AgriGuardians.git
	cd AgriGuardians

2. Create a virtual environment
	python -m venv venv
3. Activate the virtual environment
	venv\Scripts\activate
4. Install dependencies
	pip install -r requirements.txt
5. Configure environment variables
Create a .env file inside:
	backend/backend/
Add:
	GEMINI_API_KEY=your_gemini_api_key
	DJANGO_SECRET_KEY=your_django_secret_key
Never commit the .env file to GitHub.
▶️ Run the Application

Navigate to the backend:
cd backend

Run migrations:
python manage.py migrate

Start the development server:
python manage.py runserver

Open:
http://127.0.0.1:8000/

🔬 Disease Detection Workflow

Upload Crop Leaf Image
          ↓
Django Backend
          ↓
Image Processing
          ↓
Trained Keras Model
          ↓
Disease Prediction
          ↓
Confidence Score
          ↓
Gemini AI Advisory
          ↓
Management Guidance
          ↓
Prediction History

🤖 AI Advisory
After disease detection, Gemini AI is used to generate disease-specific advisory information.
The advisory can help users understand:
- Identified disease
- Possible causes
- Recommended management practices
- Preventive measures
- Crop-care guidance

🔮 Future Enhancements
AgriGuardians is designed to evolve into a broader intelligent crop-health platform.
Potential future enhancements include:
- 🌦️ Weather-based disease risk prediction
- 🐛 Pest monitoring and pest-trap integration
- 📍 Geospatial disease hotspots
- 📡 IoT and field-sensor integration
- 🌾 Field-level crop monitoring
- 🗣️ Multilingual agricultural advisory
- 👨‍🌾 Expert validation
- 🔔 Early disease and pest alerts
- 📈 Crop-health trend analysis
- 📱 Mobile application


🎯 Expected Impact
AgriGuardians aims to:
- Enable earlier crop disease detection
- Support faster agricultural decision-making
- Reduce avoidable crop losses
- Provide accessible AI-assisted crop-health guidance
- Support farmers and agricultural extension workers
- Encourage preventive and targeted crop management


🔐 Security
Sensitive configuration such as API keys and secret keys should be stored using environment variables.
The following should not be committed to the repository:
.env
db.sqlite3
media/
venv/
__pycache__/



📄 License
This project is intended for academic, educational, and innovation purposes.

### 2. Save it.

Then in PowerShell:

```powershell
cd C:\Github_Push\AgriGuardians
git add README.md
git commit -m "Add project README"
git push