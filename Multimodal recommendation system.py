import warnings
warnings.filterwarnings("ignore")
from matplotlib import pyplot as plt
import os
from PIL import Image
from dotenv import load_dotenv
from datasets import load_dataset
load_dotenv()

ds = load_dataset("huggan/flowers-102-categories")
#show number of rows
print(ds.num_rows)

#get an image from the dataset
flower = ds["train"][70]["image"]

#Display the image
plt.imshow(flower)
plt.axis("off")
plt.show()