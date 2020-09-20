
import rasterio as rio
from rasterio.plot import show
from sklearn import cluster
import matplotlib.pyplot as plt
import matplotlib.colors as mc
import numpy as np


def k_means_raster():
        elhas_raster = rio.open("./static/assets/pca-compressed.jpeg")
        print(elhas_raster.meta)
        # Read, enhance and show the image
        elhas_arr = elhas_raster.read() # read the opened image
        vmin, vmax = np.nanpercentile(elhas_arr, (5,95))  # 5-95% contrast stretch
        # create an empty array with same dimension and data type
        imgxyb = np.empty((elhas_raster.height, elhas_raster.width, elhas_raster.count), elhas_raster.meta['dtype'])
        # loop through the raster's bands to fill the empty array
        for band in range(imgxyb.shape[2]):
                imgxyb[:,:,band] = elhas_raster.read(band+1)
        print(imgxyb.shape)
        # convert to 1d array
        img1d=imgxyb[:,:,:3].reshape((imgxyb.shape[0]*imgxyb.shape[1],imgxyb.shape[2]))
        cl = cluster.KMeans(n_clusters=10) # create an object of the classifier
        param = cl.fit(img1d) # train it
        img_cl = cl.labels_ # get the labels of the classes
        img_cl = img_cl.reshape(imgxyb[:,:,0].shape) # reshape labels to a 3d array (one band only)
        # Create a custom color map to represent our different 4 classes
        cmap = mc.LinearSegmentedColormap.from_list("", ["black","red","green","yellow"])
        # Show the resulting array and save it as jpg image
        plt.figure(figsize=[20,20])
        plt.imshow(img_cl, cmap=cmap)
        plt.axis('off')
        plt.savefig("./static/assets/raster_clustered.jpg", bbox_inches='tight')
        return "Clustered"
