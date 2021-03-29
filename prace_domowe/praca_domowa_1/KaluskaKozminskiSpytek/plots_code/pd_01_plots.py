import numpy as np
import matplotlib.pyplot as plt



f =np.loadtxt("data/CT0.txt", dtype='uint8').reshape(512, 512)
all_ind = [1, 100, 200, 253, 193, 24, 32, 49, 21, 29, 121, 114, 135, 123, 198, 210, 231, 228, 239, 201, 145, 148, 152, 161, 169] # random samples
all_ind = np.array(all_ind)

fig,ax = plt.subplots(10, 2, figsize=[6,20])
plt.suptitle("Comparison of Computer Tomography images and estimated masks.\nThe number in the left top corner is the number of observation.")
for idx in range(10):
    if idx == 0:
        ax[idx, 0].set_title("CTs")
        ax[idx, 1].set_title("Estimated Masks")
    ax[idx, 0].imshow(np.loadtxt("data/CT"+str(idx)+".txt", dtype='uint8').reshape(512, 512))
    ax[idx, 1].imshow(np.loadtxt("data/Estimated"+str(idx)+".txt", dtype='uint8').reshape(512, 512), cmap='gray')
    ax[idx, 0].text(20, 70, str(all_ind[idx]), bbox={'facecolor':'white', 'pad': 2})
    ax[idx, 1].text(20, 70, str(all_ind[idx]), bbox={'facecolor':'white', 'pad': 2})       
    ax[idx, 0].axis("off")
    ax[idx, 1].axis("off")
plt.savefig('CT_Estimated.png')


fig,ax = plt.subplots(5, 4, figsize=[16,20])
plt.suptitle("Computer Tomography images with superimposed masks.\nThe number in the left top corner is the number of observation.")
for idx in range(5):
    for idxx in range(4):
        ax[idx, idxx].imshow(np.loadtxt("data/CT"+str(idx*4+idxx)+".txt", dtype='uint8').reshape(512, 512), alpha=0.4)
        ax[idx, idxx].imshow(np.loadtxt("data/Estimated"+str(4*idx+idxx)+".txt", dtype='uint8').reshape(512, 512), cmap='gray', alpha = 0.4)
        ax[idx, idxx].text(15, 35, str(all_ind[4*idx+idxx]), bbox={'facecolor':'white', 'pad': 3})
        ax[idx, idxx].text(15, 35, str(all_ind[4*idx+idxx]), bbox={'facecolor':'white', 'pad': 3})
        ax[idx, idxx].axis("off")
plt.savefig('CT_Est_transparent.png')

