# 📺 TrendStory Generator

Transform YouTube trending videos into fun, creative AI-generated stories using gRPC and Gradio. This app fetches real-time trending video titles in Pakistan and allows users to generate imaginative stories with themes like comedy, satire, fantasy, and more.

---

## 🚀 Features

- 🔥 Fetches trending YouTube titles (Pakistan region)
- 🎭 Choose from story themes: Comedy, Sarcasm, Tragedy, Satire, Fantasy
- 🤖 Uses gRPC to request AI-generated stories from a backend service
- 🖼️ Stylish and modern Gradio-based interface
- 💡 Option to refresh trending list anytime

---

## 🧰 Tech Stack

- **Python 3.8+**
- **gRPC + Protobuf**
- **Gradio UI**
- **YouTube Data API v3**
- **Google API Client**


---

## 🔧 Prerequisites

- Python 3.8 or higher
- A valid **YouTube Data API key**
- gRPC and `protoc` compiler installed

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/trendstory-generator.git
cd trendstory-generator
```

### 2. Create a virual Environment
```
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
```

### 3. Install required packages
```
pip install -r requirements.txt
```

### 🔑 YouTube API Setup

Go to the Google Cloud Console

Create a project and enable the YouTube Data API v3

Go to "Credentials" → Create an API key

Replace the API key in frontend.py:

### Run the server
```
python trendstory_server.py
```
### Run the frontend
```
python frontend.py
```
