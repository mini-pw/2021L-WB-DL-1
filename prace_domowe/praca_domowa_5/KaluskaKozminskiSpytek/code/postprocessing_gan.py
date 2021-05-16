import numpy as np
import cv2
import matplotlib.pyplot as plt
import random
import os


def randomly_modify_image(image, mask):
    mask_r = np.where(mask == 0, 255, 0)
    cv2.imwrite(mask_folder + 'mask_r.jpg', mask_r)
    mask_r = cv2.imread(mask_folder + 'mask_r.jpg', cv2.IMREAD_GRAYSCALE)

    kernel_size = random.choice([1, 3, 5, 7])
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    img_d = cv2.dilate(image, kernel)
    mask_d = cv2.dilate(mask_r, kernel)
    img_mask_d = np.where(mask_d == 0, 0, img_d)
    img_mask_final = np.where(mask_d == 0, image, img_mask_d)

    return img_mask_final, mask_d


mask_folder = 'datasets/lungs/masks/'
image_folder = 'output/lungs/generated_images/'
masks = np.load(mask_folder + 'mask_test.npy')

non_contrast_images = os.listdir(image_folder + 'B2A')
aug_train_data = []
aug_train_masks = []


for i in range(len(masks)):
    aug_train_masks.append(masks[i])
    image = cv2.imread(image_folder + '/B2A/' + f'lung_eq_{i}.jpg', cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (512, 512), interpolation=cv2.INTER_AREA)
    image, m = randomly_modify_image(image, masks[i])
    aug_train_data.append(np.asarray(image))

original_images_folder = 'datasets/lungs/testA/'
f, ax = plt.subplots(4, 2, figsize=[8, 16])
ax[0, 0].set_title('Generated images')
ax[0, 1].set_title('Ground truth images')
for i in range(4):
    ax[i, 0].imshow(aug_train_data[i * 20].squeeze(), cmap='bone')
    ax[i, 0].axis('off')
    image = cv2.imread(original_images_folder + f'lung_{i * 20}.jpg', cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (512, 512), interpolation=cv2.INTER_AREA)
    ax[i, 1].imshow(image, cmap='bone')
    ax[i, 1].axis('off')
plt.savefig('generated_examples.png')

output_folder = 'output/lungs/'
np.save(output_folder + 'aug_train_data.npy', aug_train_data)
np.save(output_folder + 'aug_train_masks.npy', aug_train_masks)


