# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:31:59 2017

@author: Achyuta
"""

"""
The main class for generating the doc2vec model based on provided data and
return related articles based on content given a particular article

"""

from gensim.models.doc2vec import TaggedDocument
from gensim.models import doc2vec
from sklearn.utils import shuffle
import multiprocessing


class DocSimilarity(object):

    def __init__(self,datasetDF=None):
        if datasetDF is not None:
            self.datasetDF = shuffle(datasetDF)
            self.tagCounter=0 
            self.listOfTaggedObjects=list()
    
    def generateTaggedObject(self,rawContent,tag):
        str_list = rawContent.split()
        T = TaggedDocument(str_list,tag)
        return T
        
    def generateListOfTaggedObjects(self):
        for id in self.datasetDF.index:
             rawText = self.datasetDF.Content[id]        #'Content' field is used as document for the doc2vec model, edit according to your dataset
             T = self.generateTaggedObject(rawText,self.tagCounter)   
             self.tagCounter = self.tagCounter+1
             self.listOfTaggedObjects.append(T)
        
    def doc2vecModelGenerator(self):
        self.generateListOfTaggedObjects()
        cpu_cores = multiprocessing.cpu_count()
        model = doc2vec.Doc2Vec(self.listOfTaggedObjects,size = 200, window = 300, min_count = 10, workers=cpu_cores, iter =10)  #number of iterations for document to vector conversion is ideal between 10 to 20  
        return model 
        
    
        
