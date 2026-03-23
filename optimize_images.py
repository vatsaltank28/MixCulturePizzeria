import os
import re
from PIL import Image  # type: ignore

def clean_filename(filename):
    """
    Renames files to clean, URL-friendly names:
    - Converts to lowercase
    - Replaces spaces, brackets, and non-alphanumeric chars with hyphens
    - Removes leading/trailing hyphens
    """
    name, _ = os.path.splitext(filename)
    name = name.lower()
    name = re.sub(r'[^a-z0-9]+', '-', name)
    name = name.strip('-')
    return f"{name}.webp"

def optimize_image(input_path, output_path, max_width=1200, target_size_kb=200):
    try:
        with Image.open(input_path) as img:
            # WebP natively supports RGBA (transparency), so we don't need to force RGB
            # unless the image mode is something exotic.
            if img.mode not in ('RGB', 'RGBA'):
                img = img.convert('RGBA')
            
            # 1. Resize to max width ~1200px maintaining aspect ratio
            width, height = img.size
            if width > max_width:
                ratio = max_width / width
                new_height = int(height * ratio)
                # Use High-quality downsampling filter
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            # 2 & 3. Convert to WebP and compress under 200KB
            quality = 90 # Start with high quality
            
            while True:
                # Save the image to the output path with WebP format
                img.save(output_path, "WEBP", quality=quality)
                
                # Check the resulting file size
                size_kb = os.path.getsize(output_path) / 1024
                
                # If it's under the target size or we hit the minimum quality floor, stop
                if size_kb <= target_size_kb or quality <= 10:
                    break
                
                # Reduce quality and try again
                quality -= 5
                
            print(f"Optimized: '{os.path.basename(input_path)}'\n"
                  f"       -> '{os.path.basename(output_path)}' ({size_kb:.1f} KB, Quality: {quality})\n")
            
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            
            new_filename = clean_filename(filename)
            output_path = os.path.join(output_folder, new_filename)
            
            optimize_image(input_path, output_path)

if __name__ == "__main__":
    # Configure your folders here
    INPUT_DIR = "Mix Culture Food Photos" # Name of your folder containing the images
    OUTPUT_DIR = "optimized-images"
    
    if os.path.exists(INPUT_DIR):
        print(f"Starting optimization from '{INPUT_DIR}' to '{OUTPUT_DIR}'...\n")
        process_folder(INPUT_DIR, OUTPUT_DIR)
        print("Done! All images have been optimized.")
    else:
        print(f"Error: Input folder '{INPUT_DIR}' does not exist.")
