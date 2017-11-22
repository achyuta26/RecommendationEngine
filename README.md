# RecommendationEngine
A recommendation engine for suggestion of articles based on a current article read. The main aim of this recommendation engine is to maintain the abstraction between a Content Management System (C.M.S.) or any website and the machine learning component for recommendation.
The ease of plug and play to a C.M.S. to get a list of related articles enhances the aim. With just a nominal implementation of connection to a C.M.S., would suffice to generate a model and have recommendation results on the fly from thereon for any article.




## Usage:

As an end user, just two API calls would be necessary to aid any website/blog to have an intelligent recommendation system:

| **API Calls** | **Method** | **Description** |
| --- | --- | --- |
| /docRecommenderapi/trainMyModelOnDataSet/ | POST|trains the model based on the dataset posted (default: csv file expected) |
| /docRecommenderapi/generateRelatedArticles/topNarticles/documentNumber | GET/POST | generate list of articles based on given article number (parameter : documentNumber) or text article as file posted. Default value for list of related articles : 10|



Should the need be for enhancing accuracy of the generated model, **DocRecommender.py** can be manipulated for console testing and performance issues.





## To-Dos for the user:

  -Since this had been run on the webscraper generated dataset csv, all the **'datasetDF'** references need to be replaced by       required datasource, after which the flow would comply as specified. 

  -**listOfArticles()** in **DocRecommender.py** needs to be implemented to return article titles or likewise parameters suited to the need.


