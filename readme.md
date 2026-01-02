# 🤖 Jarvis – AI Voice Assistant (Python)

Jarvis is a **local AI voice assistant** built using Python and LLaMA models.
It can understand voice commands, answer questions, fetch news/weather, control system tasks, and respond using speech — all **offline-friendly**.

---

## 🚀 Features

* 🎤 Voice input & speech output
* 🧠 Local LLM (LLaMA-based, no cloud dependency)
* 🌦️ Weather updates
* 📰 News headlines
* 🖥️ System information
* 🔍 App search on local system
* 🪄 GUI interface (Tkinter)
* ⚡ Fast and lightweight

---

## 📁 Project Structure

```
Jarvis/
│
├── app_scanner.py          # Finds installed apps
├── llama.py                # LLM interaction logic
├── main.py                 # Entry point
├── speak.py                # Text-to-speech
├── takeCommand.py          # Speech recognition
├── system_info.py          # System information
├── news.py                 # News API integration
├── jarvis_dashboard.py     # GUI interface
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/jarvis-ai.git
cd jarvis-ai
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup environment variables

Create a `.env` file (do **not** upload this to GitHub):

```env
LLAMA_MODEL_PATH=path/to/your/model.gguf
NEWS_API_KEY=your_news_api_key
WEATHER_API_KEY=your_weather_api_key
WOLFRAM_APP_ID=your_wolfram_id
```

📌 Example:

```
LLAMA_MODEL_PATH=assets/models/tinyllama.gguf
```

---

### 4️⃣ Download LLM Model

Download a GGUF model from:

* [https://huggingface.co/TheBloke](https://huggingface.co/TheBloke)

Recommended:

```
tinyllama-1.1b-chat.Q8_0.gguf
```

Place it inside:

```
assets/models/
```

---

### 5️⃣ Run the assistant

```bash
python main.py
```

---

## 🧠 How It Works

* Uses **LLaMA via llama-cpp-python**
* Speech recognition via **SpeechRecognition**
* Text-to-speech using **pyttsx3**
* GUI built with **Tkinter**
* Modular and easy to extend

---

## 🔐 Security Notes

✔ No API keys are hardcoded
✔ `.env` is ignored via `.gitignore`
✔ Model files are not uploaded
✔ Logs are local only

---

## 📦 Requirements

See `requirements.txt`

---

## 🛠️ Future Improvements

* Add multi-language support
* Improve response memory
* Add plugin system
* GPU acceleration

---

## 👤 Author

**Krish Verma**
Passionate about AI, system automation, and intelligent assistants.

---

## ⭐ Star this repo if you found it helpful!

---

### 💬 Need help?

Open an issue or message me — happy to help!

---

**Happy coding! 🚀**
