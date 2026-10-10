# 📸 SnapClass – AI Attendance System

> Face + voice based smart attendance for classrooms. Take attendance in one snap, with no roll calls and no proxy attendance.

🔗 **Live Demo:** <https://snapclass-smart-ai.streamlit.app/>
🌐 **Landing Page:** <https://snapclass-landing-page-zeta.vercel.app/>

---

## 📌 Problem Statement

Manual attendance wastes class time, and proxy attendance (one student marking for another) is easy. SnapClass uses face recognition and voice verification to mark attendance automatically and accurately.

---

## ✨ Features

### 👨‍🎓 Student
- **FaceID Login**: look at the camera and you are logged in
- **One-time Registration**: name + face capture, with optional voice enrollment
- **Enroll in Subjects**: join a class using the subject code
- **Dashboard**: see Total vs Attended classes for every subject
- **Unenroll** from a subject anytime

### 👩‍🏫 Teacher
- **Secure Login / Register**: username and password, with hashed passwords (bcrypt)
- **Manage Subjects**: create subjects (name, code, section) and share the code with students
- **AI Attendance (Photos)**: upload one or more classroom photos, and the AI detects every face and marks each enrolled student Present or Absent
- **Voice Attendance**: mark attendance using voice verification
- **Attendance Records**: summary by date and subject (e.g. `✅ 28/32 students`)

---

## 🧠 AI Pipeline

```text
Capture (camera / photos / audio)
        ↓
Face detection + embedding (dlib, face_recognition_models)
Voice embedding (Resemblyzer, librosa)
        ↓
Classifier / matching (scikit-learn)
        ↓
Student identified → Present / Absent
        ↓
Saved to Supabase (attendance log)
```

- The system uses **pretrained models** for face and voice embeddings, so no training accuracy table is needed.
- The classifier is re-trained automatically whenever a new student registers.

---

## 🏗️ System Architecture

```text
Streamlit UI (Home / Student / Teacher screens)
        │
        ├── AI Pipelines (face_pipline, voice_pipeline)
        │
        └── Supabase (students, teachers, subjects, subject_students, attendance)
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| Face AI | dlib-bin, face_recognition_models |
| Voice AI | Resemblyzer, librosa |
| ML | scikit-learn, NumPy, Pandas |
| Database | Supabase |
| Security | bcrypt, truststore |
| Extras | Segno (QR code), Pillow |

---

## 📁 Project Structure

```text
snapclass-ai-attendance/
├── app.py                      # Entry point (routes Home / Student / Teacher)
├── requirements.txt
├── .env.example
├── src/
│   ├── screens/
│   │   ├── home_screen.py      # Role selection
│   │   ├── student_screen.py   # FaceID login, register, dashboard
│   │   └── teacher_screen.py   # Login, subjects, attendance, records
│   ├── components/             # Header, subject cards, dialogs
│   ├── pipelines/
│   │   ├── face_pipline.py     # Face embeddings + classifier
│   │   └── voice_pipeline.py   # Voice embeddings
│   ├── database/
│   │   ├── config.py           # Supabase client
│   │   └── db.py               # Database functions
│   └── ui/
│       └── base_layout.py      # Styling and layout
└── README.md
```

> Update this tree to match your real folder names.

---

## ⚙️ Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/vishu56096-ctrl/snapclass-ai-attendance.git
cd snapclass-ai-attendance
```

**2. Create a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        
source venv/bin/activate     
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add environment variables**

Create a `.env` file (or Streamlit `secrets.toml`) using `.env.example`:
```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_key
```

**5. Run the app**
```bash
streamlit run app.py
```

---

## 🚀 How to Use

### Teacher
1. Register and log in with username and password.
2. Create a subject and share the subject code with students.
3. Go to **Take Attendance**, select the subject, and add classroom photos (or use voice attendance).
4. Click **Run Face Analysis** to see the Present/Absent results and save them.
5. Open **Attendance Records** to view the history.

### Student
1. Open the **Student Portal** and look at the camera to log in with FaceID.
2. New student? Enter your name, optionally record your voice, and create your profile.
3. Click **Enroll in Subject** and enter the subject code.
4. Track your Total and Attended classes on the dashboard.

---

## ⚠️ Limitations

- Face recognition accuracy depends on lighting, camera quality, and face angle.
- Students in a classroom photo must be clearly visible.
- Voice verification works best in a quiet environment.


---

## 👤 Author

**Vishal Kumar**
- GitHub: [vishu56096-ctrl](https://github.com/vishu56096-ctrl)
- LinkedIn: <https://www.linkedin.com/in/vishal-kumar-7a4003393/?isSelfProfile=true>

---

⭐ If you like this project, give it a star!