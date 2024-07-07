
# CodeX - Web Behavior Simulation Tool 🌐

## Overview
This tool is designed to simulate user behavior on web pages, such as movements, clicks, scrolls, and stops, and generate heatmaps based on these interactions. It supports simulating specific user journeys with goals or interactions on the website and creates detailed reports. The tool is built with scalability in mind and utilizes a structured approach to manage different types of actions. 🚀👨‍💻

![Web Automation Picture](https://cdn.dribbble.com/userupload/15151398/file/original-9708a2bcd647a6bf8e8f5cfb8149e568.png?resize=1024x768)

## 🧠 Engines Deep Dive
The tool incorporates three distinct engines to simulate user behavior:

### Online AI Engine 🌐💡
- **Technology Used:** OpenAI models, including ChatGPT.
- **Description:** This engine leverages OpenAI's powerful models to simulate complex user behaviors on web pages. It requires an OpenAI API key and uses the models to generate sequences of user actions based on the content of the web page and a given user profile. 🗝️🔮

### Offline Engine 🛠️🐍
- **Technology Used:** Python.
- **Description:** A highly accurate and efficient engine built with conditional logic. It generates sequences of user actions without the need for external AI models. This engine is particularly useful for simulating straightforward user behaviors based on predefined logic. 🏎️💨

### Offline AI Engine 🤖🔌
- **Technology Used:** Ollama, Python.
- **Description:** Utilizes the Ollama library to run models like Llama 3, Phi 3, and others on local machines. This engine is free and open-source, making it an excellent choice for projects with limited budgets. However, it requires significant GPU resources. The Llama3:8b model is used for simulating user actions. 🌟🆓
  - **How to Use:** [Ollama Installation Guide](https://ollama.com/download)
  - **Models:** [Ollama Model Library](https://ollama.com/library)

## 📚 Action Structure
The tool's architecture includes a dedicated action file for each type of user interaction, located in the `actions/` directory. This modular approach enhances the tool's scalability and maintainability. 🛠️📈 The engines output sequences of actions in a structured format, such as:

```json
{
  "type": "scroll",
  "parameters": {
    "direction": "down",
    "times": 5
  }
},
{
  "type": "clickCSS",
  "parameters": {
    "target": "button[id='myButton']"
  }
},
...
```

## 📊 Heatmap Generation 🌡️🔥
The tool generates heatmaps based on the simulated user interactions, providing visual insights into user engagement and behavior on the website. These heatmaps can be customized based on the type of interactions simulated and the goals of the analysis. 🎨📈
Library used: [Heatmap.js](https://www.patrick-wied.at/static/heatmapjs/) 📚🔗

## How to Use 🚀
1. **Install Dependencies:** Run `pip install -r requirements.txt` to install the required Python libraries. 🛠️
2. Provide openai API key in a `.env` file following the format in `.env.sample`.
3. Ollama installation is required for the Offline AI Engine. Follow the [Ollama Installation Guide](https://ollama.com/download) to set up the required environment and make sure ```llama3:8b``` model is available for use.
4. **Run the Tool:** Execute the execute_actions.py script using `python execute_actions.py` and follow the prompts to select the engine and provide the necessary inputs. 🚀

### 🛠️ Technology Stack Power-Up

- **Python 🐍**: The backbone of your engines and action logic, providing the flexibility and power needed for web behavior simulation.

- **Helium 🎈**: Simplifies web automation, making it a breeze to execute simulated actions across browsers.

- **Ollama 🦙**: Powers the Offline AI Engine with its open-source AI models, perfect for running complex simulations locally.

- **GPT (OpenAI) 🧠**: The brain behind the Online AI Engine, generating realistic user action sequences.

- **WebDriver Manager 🚗**: Ensures your browser drivers are always up to date, critical for seamless web automation tasks.

## Configuration
To use the Online AI Engine, you must provide your OpenAI API key. Place the key in a `.env` file, following the format provided in `.env.sample`.

## Conclusion
This web behavior simulation tool offers a versatile and scalable solution for simulating user interactions on websites. With its three engines, it caters to a wide range of requirements, from simple, logic-based simulations to complex, AI-driven user behavior modeling.