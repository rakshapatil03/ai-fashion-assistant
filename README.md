# 👗 AI Fashion Assistant Web App

An AI-powered web app that acts like your personal fashion stylist.  
Upload a clothing photo and describe your fashion need using **voice**, and get smart suggestions from AI ✨.

---

## 💡 Features

- 🧥 Upload an outfit image
- 🎤 Use voice input to describe your goal or question
- 🧠 AI (Gemini 1.5 Flash) gives:
  - Matching suggestions (tops, bottoms, shoes, accessories)
  - Occasions to wear it
  - Styling tips and improvements
  - Fashion confidence quotes
- 🖼️ Displays your uploaded image with suggestions
- 🎨 Clean, aesthetic design with beautiful fonts

---

## 📸 How It Works

1. Upload a clothing item or outfit image
2. Speak your fashion question or styling goal (e.g. “Suggest a matching blazer”)
3. Click “Generate”
4. See your image + beautifully formatted AI suggestions

## 📁 Project Structure Instructions

To run this project correctly, make sure you create and organize the following folders:

- `templates/` folder should contain:
  - `index.html`
  - `result.html`

- `static/` folder should contain:
  - `style.css`

- Place `app.py`, `.env`, `requirements.txt`, and `.gitignore` in the root folder.

- Uploaded images will be stored in:
  - `static/uploads/` (automatically created when you run the app)

## 🔐 Gemini API Key Setup

This project uses Google's Gemini API. To run it, you'll need your own API key.

### Steps:
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey) and generate a Gemini API key.
2. Create a `.env` file in the root folder of the project.
3. Inside `.env`, add your key like this:
