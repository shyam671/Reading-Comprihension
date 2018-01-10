## Readme ##
* The relationship between a pair of sentance is understood by discovering whether the pair of sentences entail or contradict each other. Thus, forming a fundamental understanding of language and developing a notion towards sementic representaion and hence, developing an intution behind the relationships across sentences in Reading-Comprihension task .
*  [SNLI](https://nlp.stanford.edu/projects/snli/) dataset which is precursor to the Reading-Comprihension task has been used in the project. 
* The problem of Reading-Comprihension task has been proposed as sentence classification as we have considered only two labels from  the datset i.e entailment and contradiction. 
* In oder to have less training time for the network we have considered only 100,000 pairs of sentences with entailment and contradiction labels.
## Code ##

* For extracting the pairs of sentences from SNLI dataset use preprocess_1.py & preprocess_2.py .
* Non-lexical , Co-occurrence matrix  features along with linear regression/SVM as classifier have been used to create baselines
methods.
* We have also used CNN for this task which gave far better accuracy than baseline methods.
* Siamese Network using CNN features proved to be the best network in performing the task with the accuracy of ~80 % achieving
the highest accuracy among all the methods.
* Although, the networks have not been trained for higher epochs due resource issues . So, still there is chance of improving the accuracy utilizing the entire dataset for training.For more detils of the project, please refer to the report.

