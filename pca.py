
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
import numpy as np
import pandas as pd
import cv2
from spectral import *

def pca_compress(image):
        # Load image and make into Numpy array
        im = Image.open('./static/uploads/'+image)
        n = np.array(im)
        #Apply principle component
        pc = principal_components(n)
        co_varience = pc.cov
        pc_0999 = pc.reduce(fraction=0.999)
        eigen_values = pc_0999.eigenvalues
        print(len(pc_0999.eigenvalues))
        img_pc = pc_0999.transform(n)
        im_details = imshow(img_pc[:,:,:3], stretch_all=True)
        print(im_details)
        print(img_pc.shape)
        image = img_pc[:,:,:3]
        #Image array after pca
        im = Image.fromarray((image).astype(np.uint8), 'RGB')
        #Save Image
        im.save("static/assets/pca-compressed.jpeg")
        results = [['Covarience', co_varience],['Eigen Values', eigen_values], ['Length of Eigen Values', len(eigen_values)], ['Shape of Compressed Image', img_pc.shape]]        # Create the pandas DataFrame
        df = pd.DataFrame(results, columns = ['Result', 'Value'])
        df.to_excel("static/assets/pca_results.xlsx")
        return "Compressed"