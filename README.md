sentiment_analysis_fun
======================

A naive approach to classify movie reviews. This project starts as exercise of 
the coursera course ["Introduction to data science"](https://www.coursera.org/course/datasci)

The train and test datasets are available on this [Kaggle competition](http://www.kaggle.com/c/sentiment-analysis-on-movie-reviews).
This project contains scripts to transform these datasets in feature vectors based on [AFINN](http://www2.imm.dtu.dk/pubdb/views/publication_details.php?id=6010) sentiment dictionary.

Below, we can find the main used scripts:

- afinn_refiner: reduces origin AFINN dictionary to keep only those words that are more frequent on train dataset
- vector_data_builder: transforms the train data in vectors with 58 features (positions). 
The features corresponds to the 57 words of the reduced AFINN dictionary.
