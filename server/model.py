#%%
from torchvision import transforms, models
import torch
from PIL import Image
import torch.nn.functional as F
from visualize_maskrcnn_predictions import vis_keypoints
import numpy as np
import cv2



#%%

class KeypointRCNN():
    def __init__(self):
        self.model = models.detection.keypointrcnn_resnet50_fpn(pretrained=True)
        self.model.eval()
        self.transform = transforms.Compose([
            # transforms.Resize(64),
            transforms.ToTensor(),
            transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
        ])

    def __call__(self, x):
        x = self.transform(x)
        # x = x.view(1, x.shape[0], x.shape[1],  x.shape[2]) 
        # *unpacks the argument of the x.shape
        # or x = x.unsqueeze(0)
        x = x.view(1, *x.shape)
        x = self.model(x)
        return x

# %%
def visualise_keypoints(img, predictions):
    keypoint = predictions[0]["keypoints"]
    keypoint= keypoint.detach()
    keypoint_score = predictions[0]["keypoints_scores"]
    keypoint_score = keypoint_score.detach()


    keypoint = keypoint[0]   # get the keypoint with the highest confidence
    keypoint_score = keypoint_score[0]

    # FORMAT AS EXPECTED
    k = torch.zeros(4, keypoint.shape[0])
    k[0:2, :] = keypoint.T[0:2, :]
    k[2, :] = keypoint_score
    k[3, :] = keypoint.T[2, :]
    k = k.numpy()
    img = np.array(img) 

    # Convert RGB to BGR 
    img = img[:, :, ::-1].copy() 
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    img = vis_keypoints(img, k)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = img.convert('RGB')
    return img

# %%

if __name__ == '__main__':
    img = Image.open('../Images/walking.jpg')
    img = Image.open('../Images/camel.jpg')
    img = Image.open('../Images/baseball.jpg')
    img = Image.open('../Images/baseball2.jpeg')
    img = Image.open('../Images/harry.jpeg')
    img = Image.open('../Images/peoples.png').convert('RGB')
    # img = Image.open('../Images/white_bkgd.png').convert('RGB')
    #img.show() 

    model = KeypointRCNN()

    predictions = model(img)
    print(len(predictions[0]))

    img = visualise_keypoints(img, predictions)
    img.show()

# %%
