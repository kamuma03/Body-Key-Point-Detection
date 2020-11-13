#%%
from torchvision import transforms, models
import torch
from PIL import Image
import torch.nn.functional as F
from visualize_maskrcnn_predictions import vis_keypoints
import numpy as np
import cv2



#%%
model= models.detection.keypointrcnn_resnet50_fpn(pretrained=True)

## model.eval()
## x = [torch.rand(3, 300, 400), torch.rand(3, 500, 400)]
## predictions = model(x)

## print(predictions)
## print(len(x))
# %%
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
])
# %%

img = Image.open('Images/walking.jpg')
#img.show()
x = transform(img)

# x = x.view(1, x.shape[0], x.shape[1],  x.shape[2]) 
# *unpacks the argument of the x.shape
# or x = x.unsqueeze(0)
x = x.view(1, *x.shape)

print(x.shape)
# z =[x, x]
# %%
model.eval()
predictions = model(x)
print(len(predictions[0]))
predictions


# %%
keypoint = predictions[0]["keypoints"]
keypoint= keypoint.detach()
keypoint_score = predictions[0]["keypoints_scores"]
keypoint_score = keypoint_score.detach()


keypoint = keypoint[0]   # get the keypoint with the highest confidence
keypoint_score = keypoint_score[0]


k = torch.zeros(4, keypoint.shape[0])

k[0:2, :] = keypoint.T[0:2, :]
k[2, :] = keypoint_score
k[3, :] = keypoint.T[2, :]

# keypoint = keypoint.T
# first_half = keypoint[0:2, :]
# second_half = keypoint[2, :]
# print(keypoint.shape)
# print(keypoint_score.unsqueeze(0).shape)
# keypoint = torch.cat((first_half, keypoint_score.unsqueeze(0), second_half))
# keypoint = keypoint.numpy()


k = k.numpy()

print(k.shape)
print(k)

img = np.array(img) 
# Convert RGB to BGR 
img = img[:, :, ::-1].copy() 

img = vis_keypoints(img, k )

img = cv2.cvtColor(img, cv2)
img = Image.fromarray(img)

img.show()

# %%

# %%
