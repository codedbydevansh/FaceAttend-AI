# FaceAttend-AI

> Automated attendance tracking using facial recognition and Streamlit.

![GitHub stars](https://img.shields.io/github/stars/codedbydevansh/FaceAttend-AI?style=for-the-badge&logo=github) ![GitHub forks](https://img.shields.io/github/forks/codedbydevansh/FaceAttend-AI?style=for-the-badge&logo=github) ![GitHub issues](https://img.shields.io/github/issues/codedbydevansh/FaceAttend-AI?style=for-the-badge&logo=github) ![Last commit](https://img.shields.io/github/last-commit/codedbydevansh/FaceAttend-AI?style=for-the-badge&logo=github) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 📑 Table of Contents

- [Description](#-description)
- [Key Features](#-key-features)
- [Use Cases](#-use-cases)
- [Tech Stack & Key Dependencies](#-tech-stack--key-dependencies)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Contributors](#-contributors)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📝 Description

FaceAttend-AI is an automated attendance management platform designed to replace manual roll calls with facial recognition. Utilizing Python, the application allows users to create and manage groups, register participants, and automate attendance logging through image capture or uploads. The system aims to streamline the tracking process to make recording attendance faster and less prone to manual errors.

## ✨ Key Features

* **🔐 Role-Based Screen Routing** — Dynamically directs users to teacher, student, or home screens based on active Streamlit session state logins.
* **📝 Automated Participant Enrollment** — Streamlines participant registration using built-in auto-enrollment dialog components.
* **📊 Data Manipulation Capabilities** — Processes, stores, and structures attendance logs efficiently utilizing NumPy and Pandas.
* **💻 Streamlit Web Interface** — Provides an interactive web frontend built natively in Python for direct participant and group management.

## 🎯 Use Cases

* **Teachers** looking to automate student tracking through an interactive web-based interface.
* **Developers** seeking to deploy a local, Python-based facial attendance registration system using Streamlit.

## 🛠️ Tech Stack & Key Dependencies

### 🤖 Artificial Intelligence & Machine Learning
- Face Recognition
- Voice Recognition
- Speaker Verification
- Machine Learning
- Computer Vision

### 🐍 Programming Language
- Python

### 👁️ Computer Vision
- OpenCV
- Face Recognition Library
- Dlib

### 🎙️ Speech & Audio Processing
- Resemblyzer
- Librosa

### 📊 Data Science & Machine Learning
- NumPy
- Pandas
- Scikit-Learn

### 🖼️ Image Processing
- Pillow (PIL)

### 🗄️ Database & Security
- Supabase
- Bcrypt

### 📱 QR Code Generation
- Segno

### 🌐 Web Application Framework
- Streamlit

### 🔧 Development Tools
- Git
- GitHub
- Visual Studio Code

---

## 📦 Core Dependencies

| Category | Technologies |
|-----------|--------------|
| Programming Language | Python |
| Frontend | Streamlit |
| Computer Vision | OpenCV, Dlib, Face Recognition |
| Speech Recognition | Resemblyzer, Librosa |
| Machine Learning | Scikit-Learn |
| Data Processing | NumPy, Pandas |
| Database | Supabase |
| Security | Bcrypt |
| Image Processing | Pillow |
| QR Generation | Segno |
| Version Control | Git, GitHub |

---

## 🏗️ Architecture Overview

```text
FaceAttend AI
│
├── Frontend
│   └── Streamlit
│
├── AI Engine
│   ├── Face Recognition
│   ├── Voice Recognition
│   └── Speaker Verification
│
├── Data Processing
│   ├── NumPy
│   ├── Pandas
│   └── Scikit-Learn
│
├── Database
│   └── Supabase
│
├── Security
│   └── Bcrypt
│
└── Utilities
    ├── Segno (QR Codes)
    └── Pillow (Image Processing)
```

### Key Dependencies
```text
streamlit: latest
numpy: latest
pandas: latest
scikit-learn: latest
dlib-bin: latest
git: +https://github.com/ageitgey/face_recognition_models
setuptools: 70.0.0
supabase: latest
bcrypt: latest
segno: latest
pillow: latest
librosa: latest
resemblyzer: latest
```

## ⚡ Getting Started

### Prerequisites
- Python 3.10 or higher installed on your system.

### Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/codedbydevansh/FaceAttend-AI.git
   cd FaceAttend-AI
   ```

2. **Create & activate a virtual environment:**
   - **macOS/Linux:**
     ```bash
     python -m venv venv && source venv/bin/activate
     ```
   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Configuration
<!-- TODO: Add specific environment variables or local configs here if required by src/database/config.py -->
Before running the application, ensure you have set up your database configurations (such as Supabase credentials) as required by `src/database/config.py`.

## 💻 Usage

To run the Streamlit local server, execute:

```bash
python app.py
```

Once the server starts, navigate to the local URL provided in your terminal (usually `http://localhost:8501`) to access the web application.

<!-- TODO: Add a brief overview of how to register/login or take attendance once the app is open -->

## 📁 Project Structure

```text
.
├── app.py
├── requirements.txt
└── src
    ├── components
    │   ├── dialog_add_photo.py
    │   ├── dialog_attendance_results.py
    │   ├── dialog_auto_enroll.py
    │   ├── dialog_create_subject.py
    │   ├── dialog_enroll.py
    │   ├── dialog_share_subject.py
    │   ├── dialog_voice_attendance.py
    │   ├── footer.py
    │   ├── header.py
    │   └── subject_card.py
    ├── database
    │   ├── config.py
    │   └── db.py
    ├── pipeline
    │   ├── face_pipeline.py
    │   └── voice_pipeline.py
    ├── screens
    │   ├── home_screen.py
    │   ├── student_screen.py
    │   └── teacher_screen.py
    └── ui
        └── base_layout.py
```

## 👥 Contributors

Thanks to everyone who has contributed to this project:

<p align="left">
<a href="https://github.com/codedbydevansh" title="codedbydevansh"><img src="https://avatars.githubusercontent.com/u/155902353?v=4&s=64" width="64" height="64" alt="codedbydevansh" style="border-radius:50%" /></a>
</p>

[See the full list of contributors →](https://github.com/codedbydevansh/FaceAttend-AI/graphs/contributors)

## 🤝 Contributing

Contributions are welcome! Here is the standard workflow to contribute to FaceAttend-AI:

1. **Fork** the repository
2. **Clone** your fork:
   ```bash
   git clone https://github.com/codedbydevansh/FaceAttend-AI.git
   ```
3. **Create a Branch** for your feature:
   ```bash
   git checkout -b feature/your-feature
   ```
4. **Commit** your changes with clear, descriptive commit messages:
   ```bash
   git commit -m 'feat: add some feature'
   ```
5. **Push** to your fork:
   ```bash
   git push origin feature/your-feature
   ```
6. Open a **Pull Request** on GitHub.

## 📄 License
<!-- TODO: Add project license details here (e.g. MIT, Apache 2.0) -->
This project's licensing details are currently pending. Please refer to the repository owner for more information.