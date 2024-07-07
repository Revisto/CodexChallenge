from helium import start_firefox, kill_browser, go_to
from action_factory import ActionFactory
from time import sleep
from log_manager import LogManager
from utils.clean_html import clean_html_content
from utils.user_profile_manager import get_user_profile
from engine_initializer import initialize_engine
from heatmap_manager import inject_heatmap_script, initialize_heatmap, capture_heatmap

LogManager.setup_logging()

# Initialize Firefox with Helium
headless = False
driver = start_firefox(headless=headless)

# Open a URL
go_to(input("Enter the URL (e.g https://seleniumbase.io/demo_page): "))

engine_type = input("Enter engine type (offline, online_ai, offline_ai): ")
engine = initialize_engine(engine_type)

html_content = clean_html_content(driver.page_source)
help_text = open("help.txt").read()

user_profile = get_user_profile()

result = engine.process(user_profile, html_content, help_text)
actions = result["sequence"]
descriptions = result["descriptions"]

print("Actions to be executed:")
for action in actions:
    print(action)

inject_heatmap_script(driver)
sleep(2)
initialize_heatmap(driver)
sleep(1)

# Execute actions using Helium
for action_data in actions:
    action = ActionFactory.get_action(driver, action_data)
    action.execute()
    
print("Actions executed successfully!")
print("-" * 50)
print("Descriptions:")
print("\n".join(descriptions))

input("Press Enter to capture the heatmap...")
capture_heatmap(driver)
print("Heatmap captured successfully!")
print("Please check the 'heatmap.jpg' file in the current directory for the heatmap image.")

driver.quit()