from flask import Flask, render_template, request
import os
import google.generativeai as genai
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from PIL import Image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Gemini setup
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    image_url = None
    suggestions = ""
    
    voice_input = request.form.get("voice_input", "")
    uploaded_file = request.files["image"]

    if uploaded_file.filename != "":
        filename = secure_filename(uploaded_file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        uploaded_file.save(filepath)
        image_url = f"/{filepath}"

        try:
            img = Image.open(filepath)
            prompt = f"""
You are a helpful fashion assistant AI.

The user uploaded an outfit image and said: "{voice_input}".

Analyze the image and provide:
- Description of the outfit.
- Matching suggestions (tops, bottoms, shoes, accessories).
- Recommended occasions to wear it.
- Styling tips.
- A short motivational quote.

Respond in beautiful HTML using:
- <h3> for section headings
- <ul><li> for bullet points
- <p> for quotes
            """

            response = model.generate_content([prompt, img])
            suggestions = response.text

        except Exception as e:
            suggestions = f"<p style='color:red;'>❌ Error: {str(e)}</p>"

    return render_template("result.html", suggestions=suggestions, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)
