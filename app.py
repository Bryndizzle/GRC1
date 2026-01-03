from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from dotenv import load_dotenv
from gpt_wrapper import GrassrootsCoachGPT

load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize the GPT wrapper (optional - only needed for AI features)
api_key = os.getenv('OPENAI_API_KEY')
coach_gpt = GrassrootsCoachGPT(api_key=api_key) if api_key else None

@app.route('/')
def index():
    """Serve the main coaching app interface"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests with the coaching GPT"""
    try:
        if not coach_gpt:
            return jsonify({'error': 'OpenAI API key not configured. Set OPENAI_API_KEY in .env file.'}), 503

        data = request.json
        message = data.get('message', '')
        context = data.get('context', {})

        if not message:
            return jsonify({'error': 'No message provided'}), 400

        response = coach_gpt.get_coaching_advice(message, context)
        return jsonify({'response': response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/training-plan', methods=['POST'])
def training_plan():
    """Generate a training session plan"""
    try:
        if not coach_gpt:
            return jsonify({'error': 'OpenAI API key not configured. Set OPENAI_API_KEY in .env file.'}), 503

        data = request.json
        age_group = data.get('age_group', '')
        skill_level = data.get('skill_level', 'beginner')
        focus_area = data.get('focus_area', 'general')
        duration = data.get('duration', 60)

        plan = coach_gpt.generate_training_plan(age_group, skill_level, focus_area, duration)
        return jsonify({'plan': plan})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/drill-suggestion', methods=['POST'])
def drill_suggestion():
    """Get drill suggestions based on criteria"""
    try:
        if not coach_gpt:
            return jsonify({'error': 'OpenAI API key not configured. Set OPENAI_API_KEY in .env file.'}), 503

        data = request.json
        skill = data.get('skill', '')
        players = data.get('players', 10)
        equipment = data.get('equipment', [])

        drills = coach_gpt.suggest_drills(skill, players, equipment)
        return jsonify({'drills': drills})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/tactical-advice', methods=['POST'])
def tactical_advice():
    """Get tactical advice for game situations"""
    try:
        if not coach_gpt:
            return jsonify({'error': 'OpenAI API key not configured. Set OPENAI_API_KEY in .env file.'}), 503

        data = request.json
        formation = data.get('formation', '')
        situation = data.get('situation', '')

        advice = coach_gpt.get_tactical_advice(formation, situation)
        return jsonify({'advice': advice})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'app': 'Grassroots Coach'})

if __name__ == '__main__':
    port = int(os.getenv('FLASK_PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
