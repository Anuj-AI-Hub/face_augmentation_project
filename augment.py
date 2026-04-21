from torchvision import transforms
import os

def generate_augmentations_from_image(img, output_folder, num_images=20):
    os.makedirs(output_folder, exist_ok=True)

    transform = transforms.Compose([
        transforms.RandomRotation(25),
        transforms.RandomHorizontalFlip(),
        transforms.RandomResizedCrop(256, scale=(0.8, 1.0)),
        transforms.ColorJitter(brightness=0.3, contrast=0.3, saturation=0.3),
    ])

    paths = []

    for i in range(num_images):
        aug_img = transform(img)
        path = f"{output_folder}/aug_{i}.jpg"
        aug_img.save(path)
        paths.append(path)

    return paths