# Grassroots Coach ⚽

An AI-powered football (soccer) coaching assistant built with Flask and OpenAI's GPT-4. Designed specifically for grassroots and youth football coaches to help with training plans, drill suggestions, tactical advice, and general coaching guidance.

## Features

### 1. General Coaching Advice
- Interactive chat interface with coaching context (age group, skill level)
- Expert guidance on player development, motivation, and team management
- Practical advice tailored to grassroots football

### 2. Training Session Planner
Generate comprehensive training plans including:
- Age-appropriate warm-up exercises
- Technical drills with coaching points
- Small-sided games
- Cool-down activities
- Equipment requirements
- Safety considerations

### 3. Drill Suggestions
Get specific drill recommendations based on:
- Skill focus (passing, dribbling, shooting, etc.)
- Number of players available
- Equipment on hand
- Progressions for different skill levels

### 4. Tactical Advice
Receive tactical guidance for:
- Different formations (4-4-2, 4-3-3, 3-5-2, etc.)
- Game situations
- Player positioning and movement
- Age-appropriate tactical concepts

## Tech Stack

- **Backend**: Flask (Python)
- **AI**: OpenAI GPT-4
- **Frontend**: HTML, CSS, JavaScript
- **API**: RESTful endpoints

## Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Setup Steps

1. **Clone the repository**
```bash
git clone <repository-url>
cd GRC1
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=your_actual_api_key_here
FLASK_ENV=development
FLASK_PORT=5000
```

5. **Run the application**
```bash
python app.py
```

6. **Access the app**
Open your browser and navigate to:
```
http://localhost:5000
```

## Usage Guide

### General Advice Chat
1. Navigate to the "General Advice" tab
2. Optionally set the age group and skill level for context
3. Type your coaching question
4. Get personalized advice from the AI coach

**Example questions:**
- "How do I motivate a team that just lost 5-0?"
- "What are some good team-building activities for U10s?"
- "How can I manage parents who coach from the sidelines?"

### Training Session Planner
1. Go to the "Training Plan" tab
2. Fill in:
   - Age group (e.g., U10, U14)
   - Skill level
   - Focus area (e.g., passing, defending)
   - Session duration
3. Click "Generate Plan"
4. Receive a detailed session plan ready to use

### Drill Suggestions
1. Navigate to "Drill Suggestions"
2. Enter:
   - Skill to practice
   - Number of players
   - Available equipment
3. Get 3 detailed drill suggestions with variations

### Tactical Advice
1. Go to "Tactical Advice" tab
2. Select formation
3. Describe the tactical situation
4. Receive strategic guidance

## API Endpoints

### POST `/api/chat`
General coaching advice
```json
{
  "message": "Your question",
  "context": {
    "age_group": "U10",
    "skill_level": "beginner"
  }
}
```

### POST `/api/training-plan`
Generate training session plan
```json
{
  "age_group": "U12",
  "skill_level": "intermediate",
  "focus_area": "passing",
  "duration": 60
}
```

### POST `/api/drill-suggestion`
Get drill suggestions
```json
{
  "skill": "dribbling",
  "players": 10,
  "equipment": ["cones", "balls", "bibs"]
}
```

### POST `/api/tactical-advice`
Get tactical advice
```json
{
  "formation": "4-3-3",
  "situation": "Playing against a team that sits deep"
}
```

### GET `/api/health`
Health check endpoint

## Project Structure

```
GRC1/
├── app.py                 # Main Flask application
├── gpt_wrapper.py         # GPT-4 wrapper with coaching prompts
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
├── templates/
│   └── index.html        # Main web interface
├── static/
│   ├── css/
│   │   └── style.css     # Styling
│   └── js/
│       └── app.js        # Frontend JavaScript
└── README.md             # This file
```

## Customization

### Modify GPT Behavior
Edit `gpt_wrapper.py` to customize:
- System prompts
- Response temperature
- Max tokens
- Model version (gpt-4, gpt-3.5-turbo, etc.)

### Add New Features
1. Add new endpoint in `app.py`
2. Add corresponding method in `gpt_wrapper.py`
3. Update frontend in `templates/index.html` and `static/js/app.js`

## Cost Considerations

This app uses OpenAI's GPT-4 API, which has associated costs:
- GPT-4: ~$0.03 per 1K prompt tokens, ~$0.06 per 1K completion tokens
- Consider using GPT-3.5-turbo for lower costs (~10x cheaper)
- Monitor usage at [OpenAI Dashboard](https://platform.openai.com/usage)

To use GPT-3.5-turbo, change `self.model = "gpt-4"` to `self.model = "gpt-3.5-turbo"` in `gpt_wrapper.py`

## Deployment

### Using Gunicorn (Production)
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Environment Variables for Production
```
FLASK_ENV=production
OPENAI_API_KEY=your_production_api_key
FLASK_PORT=5000
```

### Deployment Platforms
- **Heroku**: Add `Procfile` with `web: gunicorn app:app`
- **Railway**: Automatically detects Flask apps
- **Render**: Use `gunicorn app:app` as start command
- **DigitalOcean**: Deploy as App Platform or on Droplet

## Security Notes

- Never commit `.env` file with real API keys
- Use environment variables for sensitive data
- Implement rate limiting for production
- Add authentication if deploying publicly
- Monitor API usage to prevent abuse

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is provided as-is for educational purposes.

## Support

For issues, questions, or suggestions:
- Open an issue in the repository
- Contact the development team

## Acknowledgments

- Built with OpenAI's GPT-4
- Designed for grassroots football coaches worldwide
- Focused on player development and positive coaching

---

**Grassroots Coach** - Empowering coaches, developing players ⚽
