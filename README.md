# 🏥 Hospital Patient Record Analysis Using MongoDB

A MongoDB-powered healthcare analytics project that explores hospital outpatient department (OPD) records and presents meaningful insights through an interactive Streamlit dashboard.

## 📌 Project Overview

The **Hospital Patient Record Analysis** project analyzes hospital records to understand appointment trends, prescription activity, doctor performance, laboratory tests, imaging services, and pharmacy records.

The project uses MongoDB as its NoSQL database and Python for data processing, database operations, and visualization.

## 🎯 Objectives

- Analyze hospital appointment and patient visit patterns.
- Understand prescription activity across doctors.
- Identify the most frequently requested laboratory tests.
- Analyze imaging service distribution.
- Explore pharmacy and medicine sales records.
- Demonstrate MongoDB CRUD operations and aggregation pipelines.
- Build an interactive healthcare analytics dashboard.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| MongoDB | NoSQL database |
| PyMongo | Python-MongoDB integration |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Plotly | Interactive visualizations |
| Streamlit | Interactive dashboard |
| Jupyter Notebook | Data exploration and analysis |

## 📂 Project Structure

```text
Hospital-Patient-Record-Analysis/
│
├── Data/
│   └── HospitalOPD/
│       ├── HospitalOPD-noname.csv
│       └── cleaned_hospital_data.csv
│
├── Notebooks/
│   └── 01_Dataset_Exploration.ipynb
│
├── Dashboard/
│   └── app.py
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## 📊 Dataset Information

**Dataset:** HospitalOPD

**Source:** [Mendeley Data – HospitalOPD Dataset](https://data.mendeley.com/datasets/j2hd2239dr/1)

The dataset contains 62,422 records of hospital OPD activities and includes information about patients, appointments, prescriptions, laboratory tests, imaging services, and pharmacy records.

### Main Data Fields

- Patient ID
- Appointment ID and appointment date
- Doctor information
- Prescription details
- Laboratory test information
- Imaging request and result information
- Medicine information
- Hospital workflow details

## 🗄️ MongoDB Database Design

**Database Name:** `hospital_analysis`

The project uses five MongoDB collections:

| Collection | Description |
|---|---|
| `appointments` | Patient appointments and workflow details |
| `prescriptions` | Prescription and doctor information |
| `laboratory` | Laboratory test records |
| `imaging` | Imaging requests and results |
| `pharmacy` | Medicine and pharmacy records |

### Database Summary

| Collection | Documents |
|---|---:|
| Appointments | 49,912 |
| Prescriptions | 50,568 |
| Laboratory | 17,848 |
| Imaging | 5,421 |
| Pharmacy | 262 |
| **Total** | **124,011** |

## 📈 Dashboard Features

The Streamlit dashboard provides interactive visualizations and analytical summaries.

### 1. Hospital Overview
- Total appointments
- Total prescriptions
- Laboratory records
- Imaging records
- Pharmacy records

### 2. Monthly Appointment Analysis
- Monthly appointment trends
- Interactive line chart

### 3. Patient Analysis
- Top 10 most active patients
- Patient visit frequency

### 4. Doctor Analysis
- Top 10 doctors by prescriptions
- Doctor-wise prescription activity

### 5. Laboratory Analysis
- Top 10 most common laboratory tests

### 6. Imaging Analysis
- Imaging service distribution

### 7. Pharmacy Analysis
- Top medicines by sales records

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Hospital-Patient-Record-Analysis.git
cd Hospital-Patient-Record-Analysis
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start MongoDB

If MongoDB Community Server is installed through Homebrew:

```bash
brew services start mongodb-community@8.3
```

Verify the MongoDB connection:

```bash
mongosh
```

```javascript
db.runCommand({ ping: 1 })
```

### 5. Configure Environment Variables

Create a `.env` file in the project root if your application uses environment variables.

Example:

```env
MONGODB_URI=mongodb://localhost:27017/
DATABASE_NAME=hospital_analysis
```

### 6. Run the Dashboard

```bash
cd Dashboard
streamlit run app.py
```

The dashboard will open in your browser, usually at:

```text
http://localhost:8501
```

**Note:** The dashboard requires MongoDB to be running and the project collections to be populated. Import the dataset into MongoDB before launching the dashboard for the first time.

## 🔍 Key Learning Outcomes

- Understanding NoSQL database concepts.
- Designing MongoDB collections.
- Connecting MongoDB with Python using PyMongo.
- Performing database operations.
- Working with MongoDB aggregation pipelines.
- Analyzing healthcare datasets using Pandas.
- Creating interactive dashboards using Streamlit and Plotly.

## 🚀 Future Enhancements

- Add patient-level filtering and search.
- Add date-range filters.
- Include more advanced MongoDB aggregation queries.
- Add additional healthcare performance indicators.
- Improve dashboard design and usability.

## 👨‍💻 Author

**Jatin Vohra**

B.Tech – Data Science

Lovely Professional University

---

*Hospital Patient Record Analysis | Python • MongoDB • PyMongo • Streamlit*