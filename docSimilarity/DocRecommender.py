# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 12:03:18 2017

@author: Achyuta
"""

"""
This is for the normal execution of the model.
Follow the todos to have your:
-connection to datasource, datasetDF here.
-implementation of extractRawText() and listOfArticles()

"""

from gensim.models import doc2vec
from DocSimilarity import DocSimilarity


#datasetDF : have your data source here, it was a dataframe for my example
#fileOrDataFrame : the document to be supplied for related articles


#todo: extract and return stream of text from file or any other data source 
def extractRawText(fileOrDataFrame):
    return None

#todo: have your implemementation of fetching meaningful titles according to tag number
def listOfArticles(datasetDF,idList):
    return [datasetDF.Category[i] for i in idList]

def generateMostSimilarDocs(datasetDF,model,rawText,topN=10):    
        docSimObj = DocSimilarity()
        tag = model.corpus_count
        taggedDocsWords = docSimObj.generateTaggedObject(rawText,tag).words
        idSet=model.docvecs.most_similar(positive=[model.infer_vector(taggedDocsWords)],topn=topN)
        idList = [x for x,_ in list(idSet)]
        listOfrelatedArticles = listOfArticles(datasetDF,idList)                
        return listOfrelatedArticles


if __name__ == '__main__':
    topN=input("Enter number of related articles to fetch for the given doc: (default : 10)\n")
    doc2vecModel = doc2vec.Doc2Vec.load_word2vec_format('/model/YourDoc2VecModel.bin',binary=True)
    rawText = extractRawText(fileOrDataFrame)
    listOfRelatedArticles = generateMostSimilarDocs(datasetDF,doc2vecModel,rawText,int(topN))
    print (listOfRelatedArticles)