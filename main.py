from PIL import Image, ImageEnhance
from tkinter import filedialog, Tk
import matplotlib.pyplot as plt
import os



def select_image():
    # Hide root Tkinter window and open file dialog to select image
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )
    return file_path



def enhance_image(im):
    # Apply moderate sharpness, contrast, and color adjustments
    im = ImageEnhance.Sharpness(im).enhance(1.8)     # Sharpen slightly
    im = ImageEnhance.Contrast(im).enhance(1.2)       # Improve contrast gently
    im = ImageEnhance.Color(im).enhance(1.05)         # Subtle color boost
    return im



# --- Main Execution ---

image_path = select_image()
if image_path:
    original = Image.open(image_path)
    enhanced = enhance_image(original)

    # Show original and enhanced images side-by-side
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    axs[0].imshow(original)
    axs[0].set_title("Original Image")
    axs[0].axis('off')

    axs[1].imshow(enhanced)
    axs[1].set_title("Enhanced Image")
    axs[1].axis('off')

    plt.tight_layout()
    plt.show()

    # Ask user if they want to save the enhanced image
    user_input = input("Do you want to save the enhanced image? (y/n): ").strip().lower()
    if user_input == 'y':
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)  # Create output folder if not exists
        output_path = os.path.join(output_dir, "enhanced_output_balanced.jpg")
        enhanced.save(output_path)
        print(f"Enhanced image saved to '{output_path}'.")
    else:
        print("Image not saved.")

else:
    print("No image selected.")
