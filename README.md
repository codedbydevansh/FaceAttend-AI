# FaceAttend-AI

> Automated attendance tracking using facial recognition and Streamlit.

![GitHub stars](https://img.shields.io/github/stars/codedbydevansh/FaceAttend-AI?style=for-the-badge&logo=github) ![GitHub forks](https://img.shields.io/github/forks/codedbydevansh/FaceAttend-AI?style=for-the-badge&logo=github) ![GitHub issues](https://img.shields.io/github/issues/codedbydevansh/FaceAttend-AI?style=for-the-badge&logo=github) ![Last commit](https://img.shields.io/github/last-commit/codedbydevansh/FaceAttend-AI?style=for-the-badge&logo=github) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📑 Table of Contents

- [Description](#description)
- [Key Features](#key-features)
- [Use Cases](#use-cases)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Key Dependencies](#key-dependencies)
- [Project Structure](#project-structure)
- [Development Setup](#development-setup)
- [Contributors](#contributors)
- [Contributing](#contributing)

## 📝 Description

FaceAttend-AI is an automated attendance management platform designed to replace manual roll calls with facial recognition. Utilizing Python, the application allows users to create and manage groups, register participants, and automate attendance logging through image capture or uploads. The system aims to streamline the tracking process to make recording attendance faster and less prone to manual errors.

## ✨ Key Features

- **🔐 Role-Based Screen Routing** — Dynamically directs users to teacher, student, or home screens based on active Streamlit session state logins.
- **📝 Automated Participant Enrollment** — Streamlines participant registration using built-in auto-enrollment dialog components.
- **📊 Data Manipulation Capabilities** — Processes, stores, and structures attendance logs efficiently utilizing NumPy and Pandas.
- **💻 Streamlit Web Interface** — Provides an interactive web frontend built natively in Python for direct participant and group management.

## 🎯 Use Cases

- Teachers looking to automate student tracking through an interactive web-based interface.
- Developers seeking to deploy a local, Python-based facial attendance registration system using Streamlit.

## 🛠️ Tech Stack

- 🐍 **Python**

**Notable libraries:** NumPy, Pandas

## ⚡ Quick Start

```bash

# 1. Clone the repository
git clone https://github.com/codedbydevansh/FaceAttend-AI.git

# 2. Create & activate a virtualenv
python -m venv venv && source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

#4. Running Localhost
python app.py
```


## 📦 Key Dependencies

```
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

## 📁 Project Structure

```
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

## 🛠️ Development Setup

### Python
1. Install Python (v3.10+ recommended)
2. `python -m venv venv && source venv/bin/activate`  (Windows: `venv\Scripts\activate`)
3. `pip install -r requirements.txt`

## 👥 Contributors

Thanks to everyone who has contributed to this project:

<p align="left">
<a href="https://github.com/codedbydevansh" title="codedbydevansh"><img src="https://avatars.githubusercontent.com/u/155902353?v=4&s=64" width="64" height="64" alt="codedbydevansh" style="border-radius:50%" /></a>
</p>

[See the full list of contributors →](https://github.com/codedbydevansh/FaceAttend-AI/graphs/contributors)

## 👥 Contributing

Contributions are welcome! Here's the standard flow:

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/codedbydevansh/FaceAttend-AI.git`
3. **Branch**: `git checkout -b feature/your-feature`
4. **Commit**: `git commit -m 'feat: add some feature'`
5. **Push**: `git push origin feature/your-feature`
