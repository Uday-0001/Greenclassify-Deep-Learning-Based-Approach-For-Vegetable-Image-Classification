import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

# Define paths (Adjust these to match your local folder structure)
# Based on your screenshot, it looks like you might have 'Vegetable Images'
# I will assume a standard structure for now, but you can change these variables.
base_dir = r'c:\Users\amdga\Desktop\deeplearning\Vegetable Images' 
train_path = os.path.join(base_dir, 'train')
validation_path = os.path.join(base_dir, 'validation')
test_path = os.path.join(base_dir, 'test')

def count_images(directory_path, set_name):
    if not os.path.exists(directory_path):
        print(f"Directory not found: {directory_path}")
        return
    
    classes = os.listdir(directory_path)
    total_images = 0
    print(f"--- {set_name} Set Analysis ---")
    for category in classes:
        category_path = os.path.join(directory_path, category)
        if os.path.isdir(category_path):
            count = len(os.listdir(category_path))
            total_images += count
            # print(f"Class '{category}': {count} images") # Uncomment for detailed counts
    
    print(f"Found {total_images} images belonging to {len(classes)} classes in {set_name}.\n")
    return classes

def plot_samples(train_path):
    if not os.path.exists(train_path):
        return

    classes = [d for d in os.listdir(train_path) if os.path.isdir(os.path.join(train_path, d))]
    
    plt.figure(figsize=(15, 15))
    
    for i, category in enumerate(classes):
        # Just plot the first 15 classes if there are more
        if i >= 15: 
            break
            
        folder_path = os.path.join(train_path, category)
        image_files = os.listdir(folder_path)
        
        if image_files:
            # Load the first image
            img_path = os.path.join(folder_path, image_files[0])
            img = mpimg.imread(img_path)
            
            plt.subplot(5, 3, i + 1) # 5 rows, 3 columns grid
            plt.imshow(img)
            plt.title(category)
            plt.axis('off')
            
    plt.tight_layout()
    # Save the plot since we can't display it directly in this environment easily
    output_path = 'data_analysis_plot.png'
    plt.savefig(output_path)
    print(f"Sample images plot saved to {output_path}")

if __name__ == "__main__":
    # 1. Count images
    classes = count_images(train_path, "Train")
    count_images(validation_path, "Validation")
    count_images(test_path, "Test")
    
    # 2. Plot samples
    if classes:
        plot_samples(train_path)
    else:
        print("Please ensure your dataset is located at: " + base_dir)
