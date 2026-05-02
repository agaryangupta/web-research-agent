# 🌐 Web Research Agent (Gemini)

A minimal AI-powered research assistant that fetches information from Wikipedia and summarizes it using Google's Gemini model.

---

## 🚀 Features

* 🔍 Fetch real-time content from Wikipedia
* 🧠 AI-powered summarization using Gemini
* ⚡ Fast and lightweight Streamlit interface
* 🎯 Clean and minimal UI (black + blue theme)
* 🔗 Direct source linking

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Wikipedia API
* Google Gemini API

---

## 📂 Project Structure

```
├── app.py              # Main Streamlit app
├── requirements.txt   # Dependencies
└── README.md          # Project documentation
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/agaryangupta/web-research-agent.git
cd web-research-agent
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Set up environment variable

Create a `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

Or set it manually (Windows PowerShell):

```
setx GOOGLE_API_KEY "your_api_key_here"
```

---

### 4️⃣ Run the app

```
streamlit run app.py
```

---


## ⚠️ Important Notes

* Do NOT expose your API key publicly
* The current Gemini SDK used is deprecated — migration to `google.genai` is recommended

---

## 📈 Future Improvements

* Multi-source research (News, Arxiv, Blogs)
* Chat-style conversational UI
* Export summary as PDF
* History & saved queries
* Streaming responses

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## ⭐ Show your support

If you found this useful, give it a ⭐ on GitHub!
