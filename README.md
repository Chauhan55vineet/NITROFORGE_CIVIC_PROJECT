<div align="center">

<!-- Logo / Banner -->
<img src="https://img.shields.io/badge/CivicPulse-AI-16a34a?style=for-the-badge&logo=leaf&logoColor=white" alt="CivicPulse AI" height="50"/>

# 🏛️ CivicPulse AI
### Digital Governance, Civic Triage & Public Information Platform

**Hackathon Track · Civic Pulse, Digital Governance & Public Information**

---

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/YOUR_USERNAME/civicpulse-ai)

---

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=flat-square&logo=fastapi&logoColor=white)
![HuggingFace](https://img.shields.io/badge/🤗_Hugging_Face-BLIP_+_Mistral--7B-FFD21E?style=flat-square)
![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=flat-square&logo=render&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Rule 4](https://img.shields.io/badge/Rule_4-Zero_Mock_Data-red?style=flat-square)

</div>

---

## 📋 Table of Contents

- [🎯 What is CivicPulse AI?](#-what-is-civicpulse-ai)
- [✨ Features](#-features)
- [🤖 AI Models Used](#-ai-models-used)
- [🏗️ System Architecture](#️-system-architecture)
- [🌐 Live APIs (Zero Fake Data)](#-live-apis-zero-fake-data)
- [📁 Project Structure](#-project-structure)
- [🚀 Quick Start — Run Locally](#-quick-start--run-locally)
- [☁️ Deploy on Render](#️-deploy-on-render)
- [🔑 Environment Variables](#-environment-variables)
- [📡 API Reference](#-api-reference)
- [👥 Team Roles & Code Ownership](#-team-roles--code-ownership)
- [🏆 Hackathon Compliance Checklist](#-hackathon-compliance-checklist)

---

## 🎯 What is CivicPulse AI?

> **Democratizing civic governance through AI-powered multimodal intelligence.**

In an era of rapid legislative changes, viral misinformation, and expanding civic infrastructure, citizens face two critical failures:
1. **Unreported hazards** — potholes, leaking pipes, dangling wires, and illegal dumping go unfixed because reporting is bureaucratically complex.
2. **Inaccessible policies** — government welfare schemes are written in legalese, published only in English, and unreachable for the majority of citizens.

**CivicPulse AI** solves both — a single platform where citizens can:
- 📸 **Snap a photo** of any civic defect → AI analyses severity, drafts a formal petition, and maps it publicly.
- 📜 **Ask about any welfare scheme** → AI explains eligibility, required documents, and legal rights in their regional language.
- 🗺️ **Track progress live** on a public geospatial accountability dashboard.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📸 **Multimodal Civic Triage** | Upload a photo of a civic hazard → BLIP Vision describes it → Mistral-7B produces structured severity report (P1–P4), dept. routing, SLA, and formal petition |
| 🗺️ **Live Geospatial Map** | Leaflet.js map with real-time ticket markers; severity colour-coded (Red = Critical, Amber = High) |
| 🌦️ **Environmental Corroboration** | Live rainfall & PM2.5 AQI from Open-Meteo boosts urgency score automatically for waterlogging/pothole complaints |
| 📜 **Scheme Rights Explainer** | Ingests live PIB government RSS feeds; Mistral-7B translates welfare schemes into plain Hindi, Tamil, Telugu, Bengali, Marathi |
| 🔊 **Voice Accessibility** | Browser Web Speech API reads explanations aloud in chosen regional language |
| 🏛️ **Audit Trail** | Every ticket status change (Submitted → Investigation → Work Order → Resolved) is logged with timestamp and authority note |
| ⚡ **Zero Mock Data** | All data is live: geocoding, weather, AQI, government RSS, and persistent SQLite database |

---

## 🤖 AI Models Used

```
┌────────────────────────────────────────────────────────────────┐
│                     CIVICPULSE AI PIPELINE                     │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  CITIZEN UPLOADS PHOTO                                          │
│         │                                                       │
│         ▼                                                       │
│  ┌─────────────────────────────────────────┐                   │
│  │  Stage 1 — VISION                       │                   │
│  │  Salesforce/blip-image-captioning-large │                   │
│  │  "A cracked road with a deep pothole"   │                   │
│  └─────────────────────────────────────────┘                   │
│         │  (natural language scene caption)                     │
│         ▼                                                       │
│  ┌─────────────────────────────────────────┐                   │
│  │  Stage 2 — LANGUAGE (Instruction LLM)  │                   │
│  │  mistralai/Mistral-7B-Instruct-v0.3    │                   │
│  │  JSON → severity / SLA / petition      │                   │
│  └─────────────────────────────────────────┘                   │
│         │                                                       │
│         ▼                                                       │
│  ┌──────────────────────────┐                                   │
│  │  Ticket saved to SQLite  │ + Geo + Weather context           │
│  └──────────────────────────┘                                   │
└────────────────────────────────────────────────────────────────┘
```

| Stage | Model | Provider | Purpose |
|-------|-------|----------|---------|
| **Vision** | `Salesforce/blip-image-captioning-large` | Hugging Face Inference API | Converts citizen photo → natural language defect description |
| **Language** | `mistralai/Mistral-7B-Instruct-v0.3` | Hugging Face Inference API | Converts description → structured triage JSON + multilingual scheme explanations |

> **Free tier:** HF Serverless Inference API gives ≈1,000 requests/day — more than enough for hackathon demos. No GPU required.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        CITIZEN / SMALL BUSINESS                      │
│            Photo Upload · GPS Location · Scheme Query                │
└──────────────────────────────┬──────────────────────────────────────┘
                               │  HTTPS
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    FRONTEND (Single Page App)                         │
│   Tailwind CSS · Leaflet.js · Web Speech API · Lucide Icons          │
│                  Served by FastAPI StaticFiles                        │
└──────────────────────────────┬──────────────────────────────────────┘
                               │  REST API calls
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     BACKEND (FastAPI / Python)                        │
│                                                                       │
│  ┌──────────────────┐  ┌─────────────────────┐  ┌────────────────┐  │
│  │   ai_service.py  │  │    live_apis.py      │  │  database.py   │  │
│  │  BLIP + Mistral  │  │  OSM · Open-Meteo    │  │ SQLite +       │  │
│  │  HF Inference    │  │  PIB RSS Feed        │  │ Audit Logs     │  │
│  └──────────────────┘  └─────────────────────┘  └────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
  HF Inference API    OpenStreetMap Nominatim      SQLite DB (Render
  (BLIP + Mistral)    Open-Meteo Weather/AQI       Persistent Disk)
                      PIB India RSS Feed
```

---

## 🌐 Live APIs (Zero Fake Data)

> This project strictly complies with **Rule 4 — No Dummy Data / Hardcoded JSON**.

| API | What It Provides | Endpoint |
|-----|-----------------|----------|
| 🗺️ **OpenStreetMap Nominatim** | Live GPS → real street/ward/city reverse geocoding | `nominatim.openstreetmap.org/reverse` |
| 🌦️ **Open-Meteo Weather** | Real-time precipitation, temperature, weather code | `api.open-meteo.com/v1/forecast` |
| 💨 **Open-Meteo Air Quality** | Live PM2.5, European AQI sensor data | `air-quality-api.open-meteo.com/v1/air-quality` |
| 📰 **PIB India RSS Feed** | Live government notices & welfare scheme updates | `pib.gov.in/RssMain.aspx` |
| 🗄️ **SQLite (Active DB)** | Persistent grievance tickets + municipal audit trail | Local / Render Disk |

---

## 📁 Project Structure

```
civicpulse-ai/
│
├── backend/
│   ├── __init__.py
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # 🚀 FastAPI app: all REST endpoints + static serve
│   │   ├── ai_service.py    # 🤖 HF BLIP vision + Mistral-7B LLM triage engine
│   │   ├── live_apis.py     # 🌐 Live: OpenStreetMap, Open-Meteo, PIB RSS
│   │   └── database.py      # 🗄️ SQLite: tickets table, audit logs, ORM
│   ├── static/
│   │   └── index.html       # 🎨 Full SPA UI (Tailwind + Leaflet + Speech API)
│   ├── data/
│   │   └── .gitkeep         # DB created at runtime (excluded from git)
│   └── uploads/
│       └── .gitkeep         # Evidence photos stored at runtime
│
├── requirements.txt         # 📦 All Python dependencies
├── render.yaml              # ☁️ Render deploy blueprint (one-click)
├── run.py                   # ▶️ Local dev launcher
├── .env.example             # 🔑 Environment variable template
├── .gitignore               # 🙈 Excludes .env, __pycache__, DB files
└── README.md                # 📖 This file
```

---

## 🚀 Quick Start — Run Locally

### Prerequisites
- Python 3.10 or newer
- Git

### Step 1: Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/civicpulse-ai.git
cd civicpulse-ai
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set your Hugging Face token *(optional but recommended)*
Get a free token at **[huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)** (READ access is enough).

```bash
# Windows PowerShell
$env:HF_TOKEN = "hf_XXXXXXXXXXXXXXXX"

# Windows CMD
set HF_TOKEN=hf_XXXXXXXXXXXXXXXX

# Linux / macOS
export HF_TOKEN="hf_XXXXXXXXXXXXXXXX"
```

> **No token?** The app runs fully in **intelligent heuristic fallback mode** — all maps, geocoding, weather, and government feeds still work for demos!

### Step 4: Launch
```bash
python run.py
```

| URL | Purpose |
|-----|---------|
| `http://127.0.0.1:8000` | Main Citizen Portal |
| `http://127.0.0.1:8000/docs` | Interactive Swagger API Docs (great for judges!) |

---

## ☁️ Deploy on Render

### Method 1: One-Click Deploy (Fastest)

1. Click the deploy button below:

   [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/YOUR_USERNAME/civicpulse-ai)

2. Render will auto-detect `render.yaml` and provision everything.

3. Add your `HF_TOKEN` in the **Environment Variables** section during setup.

---

### Method 2: Manual Render Dashboard Deploy (Step-by-Step)

#### Step 1 — Push to GitHub
```bash
# Inside your project folder
git init
git add .
git commit -m "feat: CivicPulse AI - Initial hackathon submission"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/civicpulse-ai.git
git push -u origin main
```

#### Step 2 — Create a New Render Web Service
1. Go to **[dashboard.render.com](https://dashboard.render.com)** → **New** → **Web Service**
2. Connect your GitHub account and select the **`civicpulse-ai`** repository
3. Click **Connect**

#### Step 3 — Configure the Service

| Setting | Value |
|---------|-------|
| **Name** | `civicpulse-ai` |
| **Region** | Singapore *(closest to India)* |
| **Branch** | `main` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT` |
| **Plan** | Free *(or Starter for no-sleep)* |

#### Step 4 — Add Environment Variable
Click **Advanced** → **Add Environment Variable**:

| Key | Value |
|-----|-------|
| `HF_TOKEN` | `hf_XXXXXXXXXXXXXXXX` ← your actual token |

#### Step 5 — Add Persistent Disk *(keeps DB & uploads alive across restarts)*
Click **Advanced** → **Add Disk**:

| Setting | Value |
|---------|-------|
| **Name** | `civicpulse-data` |
| **Mount Path** | `/opt/render/project/src/backend/data` |
| **Size** | `1 GB` |

#### Step 6 — Deploy!
Click **Create Web Service**. Render will:
1. Pull your GitHub repo
2. Run `pip install -r requirements.txt`
3. Start the FastAPI server
4. Assign a public HTTPS URL like `https://civicpulse-ai.onrender.com`

Your app will be live in **3–5 minutes** ✅

---

### ⚠️ Important Render Notes

> **Free Plan Sleep:** Render's free tier spins down services after 15 minutes of inactivity. First request after sleep takes ~30 seconds to boot. Upgrade to **Starter plan** (\$7/month) to prevent this for live demos.

> **Ephemeral Disk:** Without a Persistent Disk, uploaded images and the SQLite database are wiped on each deploy. The `render.yaml` includes a disk configuration to prevent this.

---

## 🔑 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `HF_TOKEN` | Optional | Hugging Face API token. Enables BLIP Vision + Mistral-7B. Get free token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) |
| `PORT` | Auto-set by Render | Port the server binds to. Defaults to `8000` locally. |
| `RENDER` | Auto-set by Render | When present, disables hot-reload and binds to `0.0.0.0` |

Copy `.env.example` to `.env` for local development:
```bash
cp .env.example .env
# Then edit .env and add your HF_TOKEN
```

---

## 📡 API Reference

Full interactive documentation available at `/docs` (Swagger UI) when the server is running.

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/health` | System health check — shows HF connection status and live API availability |
| `POST` | `/api/triage` | Submit a civic grievance with image upload + optional GPS coordinates |
| `GET` | `/api/tickets` | List all civic grievance tickets from the live database |
| `GET` | `/api/tickets/{id}` | Get a single ticket with full municipal audit trail |
| `POST` | `/api/tickets/{id}/status` | Update ticket status (authority action + audit log entry) |
| `GET` | `/api/schemes/live` | Fetch live government policy notifications from PIB RSS feed |
| `POST` | `/api/schemes/explain` | Multilingual AI explanation of a government scheme |
| `POST` | `/api/config/key` | Set Hugging Face token at runtime (no restart needed) |

### Example: Submit a Triage Request
```bash
curl -X POST https://civicpulse-ai.onrender.com/api/triage \
  -F "image=@/path/to/pothole_photo.jpg" \
  -F "latitude=28.5450" \
  -F "longitude=77.1926" \
  -F "notes=Deep pothole near school gate causing accidents"
```

### Example: Explain a Scheme in Hindi
```bash
curl -X POST https://civicpulse-ai.onrender.com/api/schemes/explain \
  -H "Content-Type: application/json" \
  -d '{
    "title": "PM Kisan Samman Nidhi",
    "summary": "Rs 6000 annual income support directly to farmer bank accounts",
    "language": "Hindi"
  }'
```

---

## 👥 Team Roles & Code Ownership

Every team member owns and can independently explain their module to judges *(Hackathon Rule 6)*.

### 🤖 Member 1 — AI & Multimodal Intelligence
**File:** [`backend/app/ai_service.py`](backend/app/ai_service.py)

Responsible for:
- The **two-stage HF pipeline**: BLIP caption → Mistral-7B JSON triage
- Structured prompt engineering with strict `[INST]...[/INST]` format for Mistral
- `_clean_json_fence()` — robust JSON extraction from LLM output
- Multilingual scheme explainer generating regional-language eligibility checklists
- Intelligent heuristic fallback (no API key needed for demo)

### 🌐 Member 2 — Backend, Live APIs & Database
**Files:** [`backend/app/live_apis.py`](backend/app/live_apis.py), [`backend/app/database.py`](backend/app/database.py), [`backend/app/main.py`](backend/app/main.py)

Responsible for:
- **Rule 4 compliance** — live `httpx` calls to Nominatim, Open-Meteo, PIB RSS
- **Dynamic urgency boosting** — rainfall × category multiplier logic
- SQLite schema: `tickets` + `audit_logs` relational tables
- FastAPI REST endpoints with Pydantic request/response schemas
- CORS middleware, static file serving, multipart file upload handling

### 🎨 Member 3 — Frontend, Map & Voice UX
**File:** [`backend/static/index.html`](backend/static/index.html)

Responsible for:
- Responsive single-page application (Tailwind CSS dark theme)
- **Leaflet.js** interactive geospatial map with live ticket markers and pop-ups
- Browser `navigator.geolocation` GPS capture for citizen reports
- **Web Speech API** (`SpeechSynthesisUtterance`) voice read-aloud in 7 Indian languages
- Tab navigation, upload dropzone, real-time loading states, scheme selector

---

## 🏆 Hackathon Compliance Checklist

| Rule | Requirement | Status |
|------|-------------|--------|
| ✅ Rule 1 | IIT/NIT/IIIT/BITS students graduating 2027+ | — |
| ✅ Rule 2 | 2–3 team members | — |
| ✅ Rule 4 | **Zero hardcoded/mock data** — all live APIs | **Verified** |
| ✅ Rule 5 | Open-source libraries used; core AI logic built during hackathon | **Verified** |
| ✅ Rule 6 | All members can explain architecture independently | See section above |
| ✅ 7a | No fake/static/hardcoded data | All data is live runtime |
| ✅ 7c | No pre-recorded demos — app is fully functional live | **Verified** |

---

## 📄 License

This project is licensed under the **MIT License** — free to use, share, and modify.

---

<div align="center">

**Built with ❤️ for the Civic Pulse, Digital Governance & Public Information Hackathon Track**

*Powered by Hugging Face · FastAPI · OpenStreetMap · Open-Meteo · PIB India*

</div>
