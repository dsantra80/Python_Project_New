from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)

# Load configuration
app.config.from_object('config.Config')

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return "Welcome to the GradientAI Llama-3-8B-Instruct-Gradient-1048k Interface!"

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    try:
        response = requests.post(
            app.config['GRADIENTAI_API_URL'],
            json={'prompt': prompt}
        )

        if response.status_code != 200:
            logging.error(f"API request failed: {response.text}")
            return jsonify({'error': 'Failed to generate text'}), 500

        generated_text = response.json()
        return jsonify(generated_text)

    except Exception as e:
        logging.error(f"Exception occurred: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
    