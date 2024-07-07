import logging
import base64

def inject_heatmap_script(driver):
    driver.execute_script("""
        var script = document.createElement('script');
        script.type = 'text/javascript';
        script.src = 'https://cdn.jsdelivr.net/npm/heatmap.js@2.0.5/build/heatmap.min.js';
        document.head.appendChild(script);
    """)

def initialize_heatmap(driver):
    try:
        driver.execute_script("""
            var heatmapInstance = h337.create({
                container: document.body, // Use the body as the container
                radius: 90
            });
            document.onmousemove = function(ev) { // Attach event to the document
                heatmapInstance.addData({
                x: ev.pageX, // Use pageX for whole document
                y: ev.pageY, // Use pageY for whole document
                value: 1
                });
            };
        """)
    except Exception as e:
        logging.error(f"Error initializing heatmap: {e}")

def capture_heatmap(driver):
    canvas_data_url = driver.execute_script("""
        var canvas = document.querySelector('canvas');
        return canvas.toDataURL('image/jpeg');
    """)
    # Decode the base64 URL to binary data
    image_data = base64.b64decode(canvas_data_url.split(",")[1])

    # Save the image data to a JPG file
    with open("heatmap.jpg", "wb") as file:
        file.write(image_data)