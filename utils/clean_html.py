from bs4 import BeautifulSoup, Comment

# Function to load HTML content from a file
def load_html_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to clean HTML content by removing unnecessary tags
def clean_html_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove script and style elements
    for script_or_style in soup(['script', 'style']):
        script_or_style.decompose()
    
    # Remove comments
    for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
        comment.extract()
    
    # Remove meta and noscript tags
    for meta_or_noscript in soup(['meta', 'noscript']):
        meta_or_noscript.decompose()
    
    # Remove unnecessary attributes from all tags
    for tag in soup.find_all(True):
        # Keep some attributes if necessary, e.g., 'href' for 'a' tags
        if tag.name == 'a':
            attrs_to_keep = ['href']
        else:
            attrs_to_keep = []
        
        for attr in list(tag.attrs):
            if attr not in attrs_to_keep:
                del tag[attr]
    
    # Optionally, further clean up by removing or simplifying other tags or attributes
    
    # Return the cleaned HTML as a string
    return str(soup)

# Function to save the cleaned HTML content to a new file
def save_cleaned_html(cleaned_html, output_file_path):
    with open(output_file_path, 'w') as file:
        file.write(cleaned_html)

