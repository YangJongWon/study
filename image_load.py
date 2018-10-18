#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import os
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt
import skimage.io
import skimage.transform

get_ipython().run_line_magic('matplotlib', 'inline')
print ("Packs loaded")


# In[5]:


cwd = os.getcwd()
print ("Current folder is %s" % (cwd) ) 

def print_typeshape(img):
    print("Type is %s" % (type(img)))
    print("Shape is %s" % (img.shape,))


# In[6]:


# Load 
cat = imread(cwd + "/images/cat.jpg")
print_typeshape(cat)
# Plot
plt.figure(0)
plt.imshow(cat)
plt.title("Original Image with imread")
plt.draw()


# In[7]:


# Load
cat2 = imread(cwd + "/images/cat.jpg").astype(np.float)
print_typeshape(cat2)
# Plot
plt.figure(0)
plt.imshow(cat2)
plt.title("Original Image with imread.astype(np.float)")
plt.draw()


# In[8]:


# Load
cat3 = imread(cwd + "/images/cat.jpg").astype(np.float)
print_typeshape(cat3)
# Plot
plt.figure(0)
plt.imshow(cat3/255.)
plt.title("Original Image with imread.astype(np.float)/255.")
plt.draw()


# In[9]:


# Resize
catsmall = imresize(cat, [100, 100, 3])
print_typeshape(catsmall)
# Plot
plt.figure(1)
plt.imshow(catsmall)
plt.title("Resized Image")
plt.draw()


# In[10]:


# Grayscale
def rgb2gray(rgb):
    if len(rgb.shape) is 3:
        return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
    else:
        print ("Current Image if GRAY!")
        return rgb
catsmallgray = rgb2gray(catsmall)

print ("size of catsmallgray is %s" % (catsmallgray.shape,))
print ("type of catsmallgray is", type(catsmallgray))

plt.figure(2)
plt.imshow(catsmallgray, cmap=plt.get_cmap("gray"))
plt.title("[imshow] Gray Image")
plt.colorbar()
plt.draw()


# In[11]:


# Convert to Vector
catrowvec = np.reshape(catsmallgray, (1, -1));
print ("size of catrowvec is %s" % (catrowvec.shape,))
print ("type of catrowvec is", type(catrowvec))

# Convert to Matrix
catmatrix = np.reshape(catrowvec, (100, 100));
print ("size of catmatrix is %s" % (catmatrix.shape,))
print ("type of catmatrix is", type(catmatrix))


# In[29]:


# Load from Folder
cwd  = os.getcwd()
path = cwd + "/images/cats"
print(path)
valid_exts = [".jpg",".gif",".png",".tga", ".jpeg"]
# print ("Images in %s are: \n %s" % (path, os.listdir(path)))
print ("%d files in %s" % (len(os.listdir(path)), path))


# In[30]:






# Append Images and their Names to Lists
imgs = []
names = []
for f in os.listdir(path):
    # For all files 
    ext = os.path.splitext(f)[1]
    # Check types 
    if ext.lower() not in valid_exts:
        continue
    fullpath = os.path.join(path,f)
    imgs.append(imread(fullpath))
    names.append(os.path.splitext(f)[0]+os.path.splitext(f)[1])
print ("%d images loaded" % (len(imgs)))


# In[31]:


# Check
nimgs = len(imgs)


# In[32]:


len(imgs)


# In[33]:


randidx = np.sort(np.random.randint(nimgs, size=3))


# In[34]:



randidx = np.sort(np.random.randint(nimgs, size=3))
print ("Type of 'imgs': ", type(imgs))
print ("Length of 'imgs': ", len(imgs))
for curr_img, curr_name, i     in zip([imgs[j] for j in randidx]
           , [names[j] for j in randidx]
           , range(len(randidx))):
    print ("[%d] Type of 'curr_img': %s" % (i, type(curr_img)))
    print ("    Name is: %s" % (curr_name))
    print ("    Size of 'curr_img': %s" % (curr_img.shape,))


# In[35]:


# Plot Images in 'imgs' list
nimgs = len(imgs)
randidx = np.sort(np.random.randint(nimgs, size=3))
for curr_img, curr_name, i     in zip([imgs[j] for j in randidx]
           , [names[j] for j in randidx], range(len(randidx))):
    plt.figure(i)
    plt.imshow(curr_img)
    plt.title("[" + str(i) + "] ")
    plt.draw()


# In[41]:


print ("That was all!")


# In[ ]:




