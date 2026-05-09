import torch
import matplotlib.pyplot as plt
from test import ai, test_dataset
ai.eval()
num_images_to_show = 100000
print("to see the next image close the window")
for i in range(num_images_to_show):
    image, label = test_dataset[i]
    input_image = image.view(-1, 784)
    with torch.no_grad():
        output = ai(input_image)
        _, predicted = torch.max(output.data, 1)
    plt.figure(figsize=(4, 4))
    plt.imshow(image.squeeze(), cmap='gray')
    result_text = f"Real: {label} | AI: {predicted.item()}"
    color = 'green' if label == predicted.item() else 'red' 
    plt.title(result_text, color=color, fontsize=14, fontweight='bold')
    plt.axis('off')
    print(f"image number {i+1}:  real [{label}] : pred [{predicted.item()}]")
    plt.show() 
print("--- the end---")