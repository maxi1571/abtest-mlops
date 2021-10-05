# SmartAd A/B Testing using A/B testing and machine learning

SmartAd is a mobile-first marketing firm. It is running an internet advertisement for a customer in order to raise brand recognition. 
Brand Impact Optimizer (BIO), a lightweight questionnaire delivered with every campaign to determine the impact of the ad they develop, 
is an additional service provided by the company. 


## Objective

* SmartAd uses a unique creative ad interactive technique to increase brand recognition. 
  The purpose is to see if a recent creative commercial resulted in a significant increase in brand recognition. 
  For the BIO service, we created a dependable hypothesis testing method. 
  
* There's no difference in brand awareness between the 2 groups vs There's difference in brand awareness between the 2 groups.


## Methods

* Classical(Traditional) A/B Testing 
* A/B testing using machine learning models.
        Logistic regression 
        Decision Tree
        Xgboost


## Result

* Traditional A/B test: SmartAd's new creative approach had an influence on brand awareness 74% of the time, but this is insufficient to infer that it is  
  effective. However, because a traditional A/B test just evaluates the experiment and the goal variable, we can't be sure the result is influenced solely by the
  new creative SmartAd strategy; other variables may also be at play i.e browser, platform os, device type, etc.
* Logistic regression: The day of the week has a greater impact on enhancing brand recognition than the SmartAd new creative approach.
* Decision Tree:  SmartAd's innovative creative approach has an impact on brand awareness.
* Xgboost: The SmartAd's innovative creative approach has a greater influence on growing brand recognition than the day of the week. 


## Conclusion

The machine learning models show that other features like the day of the week, platform operating system users, and the number of hours users spend on the site have eﬀect in addition to the creative approach. As a recommendation in addition to smartAd's creative approach, Weekdays need to be considered as a factor that has a higher effect than that of A/B testing.
