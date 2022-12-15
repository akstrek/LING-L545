# Project

`Machine Learning based text classification approach for language identification`

# About the Project
In this project, I implement a machine-learning model to identify the language of the given input name. The dataset contains names from various languages around the globe. I use CountVectorizer from sklearn.feature extraction.text to vectorize input names as a preprocessing step and then use the vectorized representation of the names as input to the machine learning model. For language classification, we have implemented a multinomial naive Bayes algorithm which is a popular Bayesian learning approach in Natural Language Processing. The Machine Learning algorithm has been implemented from scratch and the machine learning model guesses the tag of a text using the Bayes theorem and calculates each tag's likelihood for a given sample and outputs the tag with the highest probability.

# Built with:
- Pandas
* numpy
+ sklearn
+ Multinomial Naive Bayes

# Data Description:
- The [Male given names by language wikipedia dataset](https://en.wiktionary.org/wiki/Category:Male_given_names_by_language) was used in this project.
* This dataset consisted of two hundred subcategories including languages from around the globe.
+ Due to such enormous dataset where the collection of male-given names was hosted on the Wikipedia URL under vast language subcategories, I have implemented pywikibot for data collection.
+ [Pywikibot](https://www.mediawiki.org/wiki/Manual:Pywikibot/Installation#Configure_Pywikibot) is a Python library and set of scripts that interface with the MediaWiki API. Using this pywikibot module, we are successfully able to access all the subcategory pages of the respective Wikipedia page.
