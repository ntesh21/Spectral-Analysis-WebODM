# Spectral-Analysis-WebODM


#### The above code is the implementation of *Principle Component Analysis(PCA)* and *K-means* clustering of the image for spectral Analysis.


## Methodology:

### PCA
#### The GDAL library  is used to read the orthophoto(tif). Once the orthopoto is read by GDAL. It is converted into an array with the help of gdal_array function to read the image as an array. One we have the array of orthophoto, PCA is implemented on the image array. To implement PCA spectral library is used. principle_components(image_array) is implemented to determine the PCA components and compress the image. 

#### Original Orthophoto(tif)
![alternativetext](outputs/odm-doc2.jpeg)

#### Compressed Image(After PCA)
![alternativetext](outputs/pca-compressed.jpeg)


#### The compressed image as well as details of pca can be downloaded after the processing.


### K-Means
#### For the K-means clustering of the image rasterio library is used. K means is implemented with 10 clusters(k=10). Image is opened with rasterio. Empty array is created and filled with the raster band of the image. Then the array is converted into 1d vectors. Finally the k-means algorithm is implemented on the 1-d array and colors are segmented to get the clustered image.

#### Raster Clustered Image with k=10
![alternativetext](outputs/raster_clustered.jpg)