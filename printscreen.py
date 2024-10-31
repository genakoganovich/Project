from mss import mss
import os
from PIL import Image
import win32api

OUT_PATH = '../output/014_printscreen'

def get_ordered_monitors():
    monitors = []
    for m in win32api.EnumDisplayMonitors():
        info = win32api.GetMonitorInfo(m[0])
        monitors.append((info['Monitor'], info['Device']))
    return sorted(monitors, key=lambda m: m[0][0])  # Sort by left coordinate


# Create a directory to store the screenshots if it doesn't exist
os.makedirs(OUT_PATH, exist_ok=True)

# Get ordered monitors
ordered_monitors = get_ordered_monitors()

# Initialize mss
with mss() as sct:
    # List to store individual screenshots
    screenshots = []

    # Capture screenshot for each monitor
    for i, (monitor_rect, monitor_device) in enumerate(ordered_monitors, 1):
        screenshot = sct.grab({
            'left': monitor_rect[0],
            'top': monitor_rect[1],
            'width': monitor_rect[2] - monitor_rect[0],
            'height': monitor_rect[3] - monitor_rect[1]
        })

        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
        screenshots.append(img)
        print(f"Screenshot of screen {i} ({monitor_device}) captured")

    # Calculate the total width and maximum height
    total_width = sum(img.width for img in screenshots)
    max_height = max(img.height for img in screenshots)

    # Create a new image with the total size
    combined_image = Image.new('RGB', (total_width, max_height))

    # Paste screenshots side by side
    current_width = 0
    for img in screenshots:
        combined_image.paste(img, (current_width, 0))
        current_width += img.width

    # Save the combined image
    output_path = os.path.join(OUT_PATH, "combined_screenshot.png")
    combined_image.save(output_path)

print(f"Combined screenshot saved as {output_path}")