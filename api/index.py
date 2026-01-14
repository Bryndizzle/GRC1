from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import os
import sys

# Add parent directory to path for imports
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from gpt_wrapper import GrassrootsCoachGPT
from seo_specialist_agent import OffsiteSEOSpecialistAgent

app = Flask(__name__,
            template_folder=os.path.join(parent_dir, 'templates'),
            static_folder=os.path.join(parent_dir, 'static'),
            static_url_path='/static')
CORS(app)

# Initialize the GPT wrappers (lazy initialization to avoid errors if key not set)
def get_coach_gpt():
    api_key = os.environ.get('OPENAI_API_KEY')
    if api_key:
        return GrassrootsCoachGPT(api_key=api_key)
    return None

def get_seo_agent():
    api_key = os.environ.get('OPENAI_API_KEY')
    if api_key:
        return OffsiteSEOSpecialistAgent(api_key=api_key)
    return None

@app.route('/')
def index():
    """Serve the main coaching app interface"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests with the coaching GPT"""
    coach_gpt = get_coach_gpt()
    if not coach_gpt:
        return jsonify({'error': 'OpenAI API key not configured'}), 500
    try:
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
    coach_gpt = get_coach_gpt()
    if not coach_gpt:
        return jsonify({'error': 'OpenAI API key not configured'}), 500
    try:
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
    coach_gpt = get_coach_gpt()
    if not coach_gpt:
        return jsonify({'error': 'OpenAI API key not configured'}), 500
    try:
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
    coach_gpt = get_coach_gpt()
    if not coach_gpt:
        return jsonify({'error': 'OpenAI API key not configured'}), 500
    try:
        data = request.json
        formation = data.get('formation', '')
        situation = data.get('situation', '')

        advice = coach_gpt.get_tactical_advice(formation, situation)
        return jsonify({'advice': advice})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== SEO SPECIALIST AGENT ROUTES ====================

@app.route('/api/seo/chat', methods=['POST'])
def seo_chat():
    """Handle chat requests with the SEO Specialist Agent"""
    seo_agent = get_seo_agent()
    if not seo_agent:
        return jsonify({'error': 'OpenAI API key not configured'}), 500
    try:
        data = request.json
        message = data.get('message', '')
        context = data.get('context', {})

        if not message:
            return jsonify({'error': 'No message provided'}), 400

        response = seo_agent.get_seo_advice(message, context)
        return jsonify({'response': response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/seo/link-building-strategy', methods=['POST'])
def link_building_strategy():
    """Generate a comprehensive link building strategy"""
    seo_agent = get_seo_agent()
    if not seo_agent:
        return jsonify({'error': 'OpenAI API key not configured'}), 500
    try:
        data = request.json
        business_name = data.get('business_name', '')
        industry = data.get('industry', '')
        target_pages = data.get('target_pages', [])
        competitors = data.get('competitors', [])

        if not business_name or not industry:
            return jsonify({'error': 'Business name and industry are required'}), 400

        strategy = seo_agent.generate_link_building_strategy(
            business_name, industry, target_pages, competitors
        )
        return jsonify({'strategy': strategy})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/seo/digital-pr-campaign', methods=['POST'])
def digital_pr_campaign():
    """Generate a digital PR campaign plan"""
    seo_agent = get_seo_agent()
    if not seo_agent:
        return jsonify({'error': 'OpenAI API key not configured'}), 500
    try:
        data = request.json
        business_name = data.get('business_name', '')
        industry = data.get('industry', '')
        unique_angle = data.get('unique_angle', '')
        target_audience = data.get('target_audience', '')
        budget_level = data.get('budget_level', 'low')

        if not business_name or not industry:
            return jsonify({'error': 'Business name and industry are required'}), 400

        campaign = seo_agent.generate_digital_pr_campaign(
            business_name, industry, unique_angle, target_audience, budget_level
        )
        return jsonify({'campaign': campaign})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/seo/community-strategy', methods=['POST'])
def community_strategy():
    """Generate a community visibility strategy for Reddit, Quora, YouTube, etc."""
    seo_agent = get_seo_agent()
    if not seo_agent:
        return jsonify({'error': 'OpenAI API key not configured'}), 500
    try:
        data = request.json
        business_name = data.get('business_name', '')
        industry = data.get('industry', '')
        target_platforms = data.get('target_platforms', ['Reddit', 'Quora', 'YouTube'])
        products_services = data.get('products_services', '')

        if not business_name or not industry:
            return jsonify({'error': 'Business name and industry are required'}), 400

        strategy = seo_agent.generate_community_strategy(
            business_name, industry, target_platforms, products_services
        )
        return jsonify({'strategy': strategy})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/seo/aeo-strategy', methods=['POST'])
def aeo_strategy():
    """Generate an Answer Engine Optimization (AEO) strategy for AI visibility"""
    seo_agent = get_seo_agent()
    if not seo_agent:
        return jsonify({'error': 'OpenAI API key not configured'}), 500
    try:
        data = request.json
        business_name = data.get('business_name', '')
        industry = data.get('industry', '')
        key_topics = data.get('key_topics', [])
        target_queries = data.get('target_queries', [])

        if not business_name or not industry:
            return jsonify({'error': 'Business name and industry are required'}), 400

        strategy = seo_agent.generate_aeo_strategy(
            business_name, industry, key_topics, target_queries
        )
        return jsonify({'strategy': strategy})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/seo/reputation-audit', methods=['POST'])
def reputation_audit():
    """Generate a brand reputation audit and improvement plan"""
    seo_agent = get_seo_agent()
    if not seo_agent:
        return jsonify({'error': 'OpenAI API key not configured'}), 500
    try:
        data = request.json
        business_name = data.get('business_name', '')
        industry = data.get('industry', '')
        known_issues = data.get('known_issues', '')

        if not business_name or not industry:
            return jsonify({'error': 'Business name and industry are required'}), 400

        audit = seo_agent.generate_reputation_audit(
            business_name, industry, known_issues
        )
        return jsonify({'audit': audit})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/seo/listicle-strategy', methods=['POST'])
def listicle_strategy():
    """Generate a strategy for getting featured in listicles and roundups"""
    seo_agent = get_seo_agent()
    if not seo_agent:
        return jsonify({'error': 'OpenAI API key not configured'}), 500
    try:
        data = request.json
        business_name = data.get('business_name', '')
        industry = data.get('industry', '')
        product_category = data.get('product_category', '')
        key_differentiators = data.get('key_differentiators', '')

        if not business_name or not industry:
            return jsonify({'error': 'Business name and industry are required'}), 400

        strategy = seo_agent.generate_listicle_roundup_strategy(
            business_name, industry, product_category, key_differentiators
        )
        return jsonify({'strategy': strategy})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/seo/report', methods=['POST'])
def seo_report():
    """Generate an offsite SEO report template and recommendations"""
    seo_agent = get_seo_agent()
    if not seo_agent:
        return jsonify({'error': 'OpenAI API key not configured'}), 500
    try:
        data = request.json
        business_name = data.get('business_name', '')
        current_metrics = data.get('current_metrics', None)
        goals = data.get('goals', None)

        if not business_name:
            return jsonify({'error': 'Business name is required'}), 400

        report = seo_agent.generate_offsite_seo_report(
            business_name, current_metrics, goals
        )
        return jsonify({'report': report})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/seo/outreach-templates', methods=['POST'])
def outreach_templates():
    """Generate customized outreach templates for various SEO activities"""
    seo_agent = get_seo_agent()
    if not seo_agent:
        return jsonify({'error': 'OpenAI API key not configured'}), 500
    try:
        data = request.json
        outreach_type = data.get('outreach_type', 'guest_post')
        business_name = data.get('business_name', '')
        industry = data.get('industry', '')
        context = data.get('context', '')

        if not business_name or not industry:
            return jsonify({'error': 'Business name and industry are required'}), 400

        templates = seo_agent.generate_outreach_templates(
            outreach_type, business_name, industry, context
        )
        return jsonify({'templates': templates})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ==================== HEALTH CHECK ====================

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'app': 'Grassroots Coach', 'agents': ['coaching', 'seo']})

# Vercel handler
handler = app
