"""
Grassroots Coach GPT Wrapper
A specialized GPT wrapper for football coaching advice and planning
"""

from openai import OpenAI
import json


class GrassrootsCoachGPT:
    def __init__(self, api_key):
        """Initialize the GPT wrapper with API key"""
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4"

        # Base system prompt for the coaching assistant
        self.system_prompt = """You are Grassroots Coach, an expert football (soccer) coaching assistant specializing in grassroots and youth development. Your expertise includes:

- Training session planning and drill design
- Age-appropriate coaching methods (U6 to U18+)
- Tactical and technical development
- Player development and motivation
- Game strategy and formations
- Safety and injury prevention
- Building positive team culture

You provide practical, actionable advice that considers:
- Limited resources and equipment
- Varying skill levels
- Fun and engagement
- Long-term player development
- Inclusive coaching practices

Always be encouraging, practical, and focus on player development over winning."""

    def get_coaching_advice(self, message, context=None):
        """
        Get general coaching advice based on a question or situation

        Args:
            message (str): The coach's question or situation
            context (dict): Additional context (age group, skill level, etc.)

        Returns:
            str: GPT response with coaching advice
        """
        messages = [{"role": "system", "content": self.system_prompt}]

        if context:
            context_str = f"\nContext: {json.dumps(context, indent=2)}"
            messages.append({"role": "system", "content": context_str})

        messages.append({"role": "user", "content": message})

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error getting coaching advice: {str(e)}"

    def generate_training_plan(self, age_group, skill_level, focus_area, duration):
        """
        Generate a complete training session plan

        Args:
            age_group (str): Age group (e.g., "U8", "U12", "U16")
            skill_level (str): Skill level (beginner, intermediate, advanced)
            focus_area (str): Main focus (passing, shooting, defending, etc.)
            duration (int): Session duration in minutes

        Returns:
            str: Detailed training plan
        """
        prompt = f"""Create a detailed {duration}-minute training session plan for:
- Age Group: {age_group}
- Skill Level: {skill_level}
- Focus Area: {focus_area}

Include:
1. Warm-up (with specific exercises and duration)
2. Technical drills (2-3 drills with setup, execution, and coaching points)
3. Small-sided game (game format and rules)
4. Cool-down
5. Key coaching points for each section
6. Equipment needed
7. Safety considerations

Make it practical for grassroots coaches with limited resources."""

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt}
        ]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=1500
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating training plan: {str(e)}"

    def suggest_drills(self, skill, players, equipment):
        """
        Suggest specific drills for a skill

        Args:
            skill (str): Skill to practice (e.g., "passing", "dribbling")
            players (int): Number of players
            equipment (list): Available equipment

        Returns:
            str: Drill suggestions
        """
        equipment_str = ", ".join(equipment) if equipment else "basic equipment (balls, cones)"

        prompt = f"""Suggest 3 specific drills for practicing {skill} with:
- Number of players: {players}
- Available equipment: {equipment_str}

For each drill provide:
1. Drill name
2. Setup (field layout, equipment placement)
3. How to execute
4. Variations for different skill levels
5. Key coaching points
6. Common mistakes to watch for

Make the drills engaging and progressive."""

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt}
        ]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=1200
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error suggesting drills: {str(e)}"

    def get_tactical_advice(self, formation, situation):
        """
        Get tactical advice for game situations

        Args:
            formation (str): Team formation (e.g., "4-3-3", "3-5-2")
            situation (str): Game situation or tactical question

        Returns:
            str: Tactical advice
        """
        prompt = f"""Provide tactical advice for a grassroots team using a {formation} formation.

Situation: {situation}

Include:
1. Key tactical principles
2. Player positioning and movement
3. Attacking and defending strategies
4. Communication points
5. How to teach this to young players
6. Common mistakes and how to correct them

Keep advice practical and age-appropriate."""

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt}
        ]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error getting tactical advice: {str(e)}"

    def custom_query(self, prompt, system_override=None):
        """
        Make a custom query with optional system prompt override

        Args:
            prompt (str): Custom user prompt
            system_override (str): Optional custom system prompt

        Returns:
            str: GPT response
        """
        system = system_override if system_override else self.system_prompt

        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=1200
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error processing custom query: {str(e)}"
