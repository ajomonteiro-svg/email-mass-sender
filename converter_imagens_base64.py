import base64
import os

# Function to convert images to Base64
def convert_image_to_base64(image_path):
    # Check if the file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"{image_path} not found")
    
    # Open the image file in binary mode
    with open(image_path, 'rb') as image_file:
        # Encode the image to Base64
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')
    return base64_image

# Example usage
if __name__ == '__main__':
    image_path = 'path_to_your_image.png'  # Specify your image path
    try:
        base64_str = convert_image_to_base64(image_path)
        print(f'Base64 String: {base64_str}')
    except Exception as e:
        print(f'Error: {e}')