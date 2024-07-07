from bs4 import BeautifulSoup
from random import randint

class OfflineEngine:

    def analyze_html(self, soup):
        sequence = []
        # Example: If there's a "Sign Up" button, add a click action for it
        sign_up_button = soup.find('button', text='Sign Up')
        if sign_up_button:
            sequence.append({
                "type": "clickText",
                "parameters": {
                    "target": "Sign Up"
                }
            })

        # Example: If there's a large amount of text content, add more scrolling
        text_content = soup.get_text()
        if len(text_content) > 1000:  # Arbitrary threshold for "large amount of text"
            sequence.append({
                "type": "scroll",
                "parameters": {
                    "direction": "down",
                    "times": 10  # Increase scrolling for content-rich pages
                }
            })

        # Example: If there are video elements, add a delay to simulate watching time
        video_elements = soup.find_all('video')
        if video_elements:
            sequence.append({
                "type": "delay",
                "parameters": {
                    "duration": 5  # Simulate a short watching period
                }
            })

        return sequence

    def suggest_sequence(self, user_profile, soup):
        sequence = []

        # Basic interaction for all users
        # find input text for target
        target = soup.find('input', {'type': 'text'})
        target = target if target else soup.find('input', {'type': 'search'})
        target = target if target else soup.find('input', {'type': 'email'})
        target = target if target else soup.find('input', {'type': 'password'})
        target = target if target else soup.find('input', {'type': 'tel'})
        target = target if target else soup.find('input', {'type': 'url'})
        if target:
            sequence.append({
                "type": "input",
                "parameters": {
                    "target": f"input[type='{target['type']}'][id='{target.get('id', '')}']",
                    "value": "I am testing this input field."
                }
            })

        # Customizing sequence based on user profile
        if user_profile["Age"] > 50 or (not any("tech" in interest.lower() for interest in user_profile["Interests"]) and "tech" not in user_profile["Job"].lower()) or user_profile["Level of familiarity with the Internet"].lower()=="low" or user_profile["Previous experience working with the site"].lower()=="no":
            sequence.append({
                "type": "mouseMove",
                "parameters": {
                    "startPosition": {"x": randint(0, 500), "y": randint(0, 500)},
                    "endPosition": {"x": randint(500, 1000), "y": randint(500, 1000)},
                    "duration": user_profile["Age"] * 100  # Longer duration for older users
                }
            })
            sequence.append({
                "type": "scroll",
                "parameters": {
                    "direction": "down",
                    "times": 5
                }
            })
            for text in ["About Us", "Contact", "Services", "FAQ", "Support", "Blog", "Terms of Service", "Privacy Policy"]:
                sequence.append({
                    "type": "clickText",
                    "parameters": {
                        "target": text
                    }
                })
            sequence.append({
                "type": "delay",
                "parameters": {
                    "duration": user_profile["Age"] // 7 # Longer delay for older users
                }
            })

        if user_profile["Mobile or desktop user"].lower() == "mobile":
            sequence.append({
                "type": "clickCSS",
                "parameters": {
                    "target": "button[id='mobileMenuButton']"
                }
            })

        # Additional logic based on other profile attributes
        # Example: More tech-savvy users might have a more complex interaction sequence
        for tech_keyword in ["developer", "it professional", "software engineer", "computer science", "technology"]:
            if "technology" in user_profile["Interests"]:
                for button_keyword in ["settings", "advanced", "configuration", "admin", "preferences"]:
                    button = soup.find('button', text=lambda t: button_keyword in t.lower())
                    if button:
                        sequence.append({
                            "type": "clickText",
                            "parameters": {
                                "target": button.text
                            }
                        })
                        break
                    
                sequence.append({
                    "type": "clickCSS",
                    "parameters": {
                        "target": "button[id='advancedSettings']"
                    }
                })
                
                sequence.append({
                    "type": "delay",
                    "parameters": {
                        "duration": 2
                    }
                })

        # Analyze HTML for specific elements that might interest different user groups
        help_button = soup.find('button', text=lambda t: t and "help" in t.lower())
        if help_button and user_profile["Age"] > 50:
            sequence.append({
                "type": "clickText",
                "parameters": {
                    "target": help_button.text  # Click on the first found "help" button
                }
            })

        # For users with high education level, look for and interact with academic content
        if user_profile["Education level"].lower() in ["master's", "doctorate"]:
            academic_links = soup.find_all('a', text=lambda t: "research" in t.lower() or "academic" in t.lower())
            for link in academic_links[:1]:  # Limit to the first link to avoid overloading the sequence
                sequence.append({
                    "type": "clickText",
                    "parameters": {
                        "target": link.text
                    }
                })

        # For users interested in movies, look for multimedia content
        if "movies" in user_profile["Interests"]:
            multimedia_elements = soup.find_all(['video', 'audio'])
            if multimedia_elements:
                sequence.append({
                    "type": "delay",
                    "parameters": {
                        "duration": 10  # Simulate spending time on multimedia content
                    }
                })

        # Adjust scrolling behavior based on the user's familiarity with the Internet
        if user_profile["Level of familiarity with the Internet"].lower() in ["medium", "high"]:
            sequence.append({
                "type": "scroll",
                "parameters": {
                    "direction": "down",
                    "times": 15  # More scrolling for users more familiar with the Internet
                }
            })
        else:
            sequence.append({
                "type": "scroll",
                "parameters": {
                    "direction": "down",
                    "times": 5  # Less scrolling for users less familiar with the Internet
                }
            })

        # For desktop users, add more complex mouse movements
        if user_profile["Mobile or desktop user"].lower() == "desktop":
            sequence.append({
                "type": "mouseMove",
                "parameters": {
                    "startPosition": {"x": 0, "y": 0},
                    "endPosition": {"x": randint(500, 1000), "y": randint(500, 1000)},
                    "duration": 1500
                }
            })

        return sequence

    def describe_sequence(self, sequence):
        descriptions = []
        for action in sequence:
            if action["type"] == "clickText":
                descriptions.append(f"Clicking on text '{action['parameters']['target']}' to interact with specific text elements that might be of interest.")
            elif action["type"] == "scroll":
                descriptions.append("Scrolling through the page to simulate user's exploration of the page content.")
            elif action["type"] == "delay":
                descriptions.append(f"Delaying for {action['parameters']['duration']} seconds to simulate watching or reading time for content.")
            elif action["type"] == "input":
                descriptions.append(f"Inputting text into {action['parameters']['target']} to simulate user interaction with input fields.")
            elif action["type"] == "mouseMove":
                descriptions.append("Moving the mouse cursor to simulate user's mouse movements across the screen.")
            elif action["type"] == "clickCSS":
                descriptions.append(f"Clicking on CSS element '{action['parameters']['target']}' to interact with elements identified by CSS selectors.")
            else:
                descriptions.append("Unknown action with no specific reason provided due to unknown action type.")
        return descriptions

    def process(self, user_profile, html_content, help_text):
        soup = BeautifulSoup(html_content, 'html.parser')
        sequence = self.analyze_html(soup)
        sequence += self.suggest_sequence(user_profile, soup)
        descriptions = self.describe_sequence(sequence)
        
        return {
            "sequence": sequence,
            "descriptions": descriptions
        }