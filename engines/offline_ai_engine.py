import ollama

class OfflineAIEngine:
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
        - Mobile or desktop user: {user_profile['Mobile or desktop xauser']}
        - Other behavioral characteristics: {', '.join(user_profile['Other behavioral characteristics'])}
        """
        return text_message.strip()
    
    def process(self, user_profile, html_content, help_text):
        user_profile_text = self.user_profile_to_text(user_profile)
        response = ollama.chat(model='llama3:8b', messages=[
            {
                'role': 'user',
                'content': f'THE HTML WEB PAGE: {html_content} {user_profile_text} {help_text}',
            },
        ])
        output_text = response['message']['content']
        print(output_text)
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
            "sequence": actions,
            "descriptions": descriptions
        }