from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# ChatGPT APIキーの設定
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/api/nannohi', methods=['POST'])
def nannohi():
    data = request.json
    date = data.get('date', '')
    
    # ChatGPT APIを呼び出す
    if date:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"What is special about {date}?",
            max_tokens=100
        )
        result = response.choices[0].text.strip()
        return jsonify({'result': result})
    
    return jsonify({'error': 'No date provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)