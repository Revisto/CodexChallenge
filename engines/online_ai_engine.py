import openai
from dotenv import load_dotenv
import os

load_dotenv()

class OnlineAIEngine:
    def user_profile_to_text(self, user_profile):
        text_message = f"""
        User Profile Information:
        - Age: {user_profile['Age']}
        - Gender: {user_profile['Gender']}
        - Interests: {', '.join(user_profile['Interests'])}
        - Place of life (country): {user_profile['Place of life (country)']}
        - Education level: {user_profile['Education level']}
        - Job: {user_profile['Job']}
        - Previous experience working with the site: {user_profile['Previous experience working with the site']}
        - Level of familiarity with the Internet: {user_profile['Level of familiarity with the Internet']}
        - Mobile or desktop user: {user_profile['Mobile or desktop user']}
        - Other behavioral characteristics: {', '.join(user_profile['Other behavioral characteristics'])}
        """
        return text_message.strip()
    
    def process(self, user_profile, html_content, help_text):
        user_profile_text = self.user_profile_to_text(user_profile)
        openai.api_key = os.getenv("OPENAI_API")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": """You are a user that navigates with websites and tells a sequence of actions, EXAMPLE ANSWER: { "type": "input", "parameters": { "target": "input[type='text'][id='myTextInput']", "value": "We Are Developers" } } I wrote the We Are Developers for this reason. { "type": "scroll", "parameters": { "direction": "down", "times": 5 } I Scrolled down for his reason. MAKE SURE TO WRITE DESCRIPTION FOR EACH ACTION. ALWAY SEND THE ACTIONS IN THE DICTIONARY/JSON FORMAT. LIKE { "type": "input", "parameters": { "target": "input[type='text'][id='myTextInput']", "value": "We Are Developers" } }"""},
                    {"role": "user", "content": f"{html_content} {help_text} {user_profile_text} tell me sequence and write logic and description and the why of each action. MAKE SURE TO WRITE DESCRIPTION FOR EACH ACTION.  MAKE SURE TO WRITE DESCRIPTION FOR EACH ACTION. ALWAY SEND THE ACTIONS IN THE DICTIONARY/JSON FORMAT"},
                ]
            )
        output_text = response.choices[0].message['content'].strip()
        lines = output_text.split('\n')
        actions = []
        descriptions = []
        current_action = ""
        collecting_action = False
        for line in lines:
            if line.startswith("{"):
                collecting_action = True
                current_action += line
            elif line.startswith("}"):
                current_action += line
                actions.append(eval(current_action))
                current_action = ""
                collecting_action = False
            elif collecting_action:
                current_action += line
            else:
                if "```" not in line:
                    descriptions.append(line.strip())
        return {
            "sequence": [action for action in actions if action],
            "descriptions": [description for description in descriptions if description]
        }