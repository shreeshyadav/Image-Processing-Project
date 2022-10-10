import matplotlib.pyplot as plt
import tensorflow as tf
from keras.models import load_model
from skimage.transform import resize
import numpy as np

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

#print(stringlist[x[0]])

def execute(loc):
    arr=unpickle("meta")
    l=list(arr[b'fine_label_names'])
    stringlist=[x.decode('utf-8') for x in l]
    model=tf.keras.models.load_model('model_proposed.h5')
    my_image=plt.imread(loc) 
    
    
    #img=plt.imshow(my_image)
    #plt.show()
    my_image_resized=resize(my_image,(32,32,3))
    prob=model.predict(np.array([my_image_resized]))
    index=np.argsort(prob[0,:])
    s=stringlist[index[99]]+' '+"with probability "+str(prob[0,index[99]])
    return(s)
    '''print(stringlist[index[99]],'--prob',prob[0,index[99]])
    print(stringlist[index[98]],'--prob',prob[0,index[98]])
    print(stringlist[index[97]],'--prob',prob[0,index[97]])  ''' 




