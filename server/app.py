from flask import Flask, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai
import os

app = Flask(__name__)

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_GENAI_API_KEY"))

@app.route('/chat', methods=['POST'])
def chatbot():
    try:
        #Extract the prompt fronm the post request
        data = request.json
        prompt = data.get("prompt","")
        if not prompt:
            return jsonify({"error":"No prompt is provided. prompt is required"}), 400
        
        #Add context to the prompt
        user_context = "Assume you are talking to a chatbot"
        full_promt = user_context + prompt

        #Generate the response using gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(full_promt)

        return jsonify({"response":response.text})
    except Exception as e:
        return jsonify({"error":str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)
