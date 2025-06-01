# 🧠 Manga2AnimeAI – Turn Manga into Animated Stories with AI

**Manga2AnimeAI** is an experimental project that brings static manga panels to life by transforming them into animated storytelling experiences using cutting-edge AI technologies.

This project combines web scraping, OCR, large language models (LLMs), and (upcoming) text-to-speech and animation generation to create a seamless manga-to-video pipeline.

---

## 🚀 Features

- 🖼️ **Manga Scraper** – Extracts manga panels from supported websites
- 🔍 **OCR Engine** – Reads and extracts text from manga panels using Tesseract OCR
- 🧠 **Script Generator** – Uses LLaMA 3 to turn extracted dialogues into a coherent story narration
- 🗣️ (Coming soon) **Voiceover Generation** – Converts script into character voices using TTS
- 🎞️ (Coming soon) **Panel Animation** – Applies zoom, pan, and transition effects to simulate animation

---

## 📸 Demo (Day 1 Progress)

> Implemented panel scraping, OCR reading, and LLaMA 3 script generation!

```
[Insert gif or image demo here if available]
```

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Selenium / BeautifulSoup** – For scraping and browser automation
- **EasyOCR** – For reading manga panel text
- **LLaMA 3** – For generating narrative scripts
- **(Planned)** OpenAI / Bark / ElevenLabs – For voiceover
- **(Planned)** MoviePy / After Effects automation – For animated panel creation

---

## 🔧 Setup Instructions

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/manga2animeai.git
   cd manga2animeai
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Ollama**

4. **Run the pipeline**

   ```bash
   python main.py
   ```

---

## 📌 To-Do

- [x] Manga panel scraping
- [x] OCR text extraction
- [x] LLaMA 3 script generation
- [ ] Voiceover synthesis
- [ ] Animation rendering
- [ ] Export to video format

---

## 🤝 Contributing

Pull requests are welcome! If you have ideas, feedback, or improvements, feel free to open an issue or contribute a PR.

---

## 📄 License

MIT License

---

## 🙌 Acknowledgements

- [Meta LLaMA 3](https://ai.meta.com/llama/)
- Manga websites for publicly available content used only for testing
