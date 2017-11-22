# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 12:21:26 2017

@author: Achyuta
"""

"""
Run this file for API calls as:
 /docRecommenderapi/trainMyModelOnDataSet/ : to train your model
 /docRecommenderapi/generateRelatedArticles/topNarticles/documentNumber : generate articles suggestions based on content, given
  a document or document number
"""

from __future__ import print_function
from flask import Flask, request
import pandas as pd
import io
from DocSimilarity import DocSimilarity
from gensim.models import doc2vec
from DocRecommender import generateMostSimilarDocs

app = Flask(__name__)

mainDataSet = dict()


def convertFileToDataFrame(file):
    stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
    datasetDF = pd.DataFrame.from_csv(stream)
    return datasetDF

    
@app.route('/docRecommenderapi/trainMyModelOnDataSet/', methods=['POST'])
def trainMyModel():
    file = request.files['file']                                                #todo: have function for CMS connection setup  here
    datasetDF = convertFileToDataFrame(file)
    mainDataSet['_datasetDF'] = datasetDF    
    docSimilarityObject = DocSimilarity(datasetDF=datasetDF)
    doc2vecModel = docSimilarityObject.doc2vecModelGenerator()
    doc2vecModel.save_word2vec_format('/model/YourDoc2VecModel.bin',binary=True)
    return "Model successfully saved at current execution path +/model/YourDoc2VecModel.bin"
    
    
    
@app.route('/docRecommenderapi/generateRelatedArticles/',defaults={'topNarticles': 10,'documentNumber': 0},methods=['GET','POST'])    
@app.route('/docRecommenderapi/generateRelatedArticles/<int:topNarticles>/<int:documentNumber>',methods=['GET','POST'])    
def generateRelatedArticles(topNarticles,documentNumber):
    datasetDF = mainDataSet['_datasetDF'] 
    file = request.files['file']
    if file is None:
        stream = datasetDF.Content[documentNumber-1]
    else:
        stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
        
    doc2vecModel = doc2vec.Doc2Vec.load_word2vec_format('/model/YourDoc2VecModel.bin',binary=True)
    listOfrelatedArticles = generateMostSimilarDocs(datasetDF,doc2vecModel,str(stream),topN=topNarticles)
    return str(listOfrelatedArticles)


if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)


