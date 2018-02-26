
# coding: utf-8

# In[38]:

import os
import face_recognition
from PIL import Image, ImageDraw
from shutil import copyfile


# In[39]:

#keep all the pictures in one folder names all_images
#resultant folders will be stored in results folder. Ex - /results/1, /results/2
#set threshold on experimentation
threshold = 0.5


# In[40]:

file_encodings = []
file_names = []
for file in os.listdir('./all_images'):
    if(file.endswith('.jpg')):
        file_names.append(file)
        temp_image = face_recognition.load_image_file('./all_images/'+file)
        image_encoding = face_recognition.face_encodings(temp_image)[0]
        file_encodings.append(image_encoding)


# In[41]:

compare_mat = []
for encoding1 in file_encodings:
    comparisions = face_recognition.face_distance(file_encodings, encoding1)
    compare_mat.append(comparisions)


# In[42]:

clustered_list = []
for file_name in file_names: 
    clustered_list.append(file_name)


# In[43]:

clusters = []
i = 0
while i!=len(clustered_list):
    temp=[]
    j=0
    while j!=len(compare_mat[i]):
        com = compare_mat[i][j]
        if com!=0 :
            if com<threshold:
                temp.append(clustered_list[j])        
        j+=1
    clusters.append(temp)
    i+=1
    


# In[44]:

l = clusters
len_l = len(l)
i = 0
while i < (len_l - 1):
    for j in range(i + 1, len_l):

        i_set = set(l[i])
        j_set = set(l[j])

        if len(i_set.intersection(j_set)) > 0:
            l.pop(j)
            l.pop(i)
            ij_union = list(i_set.union(j_set))
            l.append(ij_union)
            len_l -= 1
            i -= 1
            break
    i += 1
clusters = l


# In[45]:

print clusters


# In[46]:

def createResultantFolders(clusters):
    index=1
    for cluster in clusters:
        directory=os.getcwd()+"/resultant/"+str(index)
        if not os.path.exists(directory):
            os.makedirs(directory)
        for file in cluster:
            copyfile(os.getcwd()+"/all_images/"+file, directory+'/'+file)
        index+=1


# In[47]:

createResultantFolders(clusters)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



