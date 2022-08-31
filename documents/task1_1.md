# Introduction #
This technical project titled “A/B Hypothesis Testing: Ad campaign performance” aims to help an advertising company (SmartAd) to assess its additional service called Brand Impact Optimizer (BIO). Actually, the BIO service is provided to quantify the increase in brand awareness as a result of the ads it shows to online users. Two groups of users have been made: users who have been shown a dummy ad (controlled group) and users who have been shown a creative (ad) that was designed for the client (exposed group). The overall objective of this project is then to compare the two groups using the brand awareness metric (knowing or not the brand Lux) in order to figure out which one of them performs better. This goal will be reached by testing if the ads that the advertising company runs resulted in a significant lift in brand awareness using A/B testing on the two groups of users. This interim report aims to go through the understanding of the A/B testing framework. In order to do this, different points in the form of questions will be addressed and answered.

# Which online users belong to the control and exposed groups? #
Users in the controlled groups are those who have been shown a dummy ad and users in the exposed group are those who have been shown an ad designed for the client.

# How are the users targeted? #
The users are randomly targeted to be shown a dummy ad or proper ad and then to be presented the BIO (a lightweight questionnaire).

# What is the best way to make a judgment on which experiment is performing better? #
Some might think about using the counts of yes and no answers to make a judgment on which experiment is performing better? But, doing that will lead to a wrong conclusion (we could not declare that the ad had a significant impact) because the data are from a sample, not collected on the entire population of the users (this being even impossible). Then, the counts findings for a given sample will be different for another sample: we can get two opposite answers. Then, the objective is to draw a conclusion which is likely to be true for the whole population. Hence, a significance test is definitely needed to test the difference in the entire population from which the sample is made based on the results of the sample.

# What’s the statistical process that generates the data? - Which statistical model could be used to generate those data using simulation? #
The data is actually a “Yes” and “No” response of online users to the question (Do you know the brand Lux?). The outcome (response) of each user could not be known in advance and has two possible values: 1 (yes) or 0 (no). This is then a Bernoulli trial for each user. Hence, for all the users (being independent), we have a Binomial trial which is a Bernoulli process. Then, one can say that a Bernoulli process has been used for generating the data. Consequently, a Binomial distribution can be used to simulate the data.

# Which statistical tests are appropriate to use for this project? #
Using the central limit theorem, a binomial distribution can be approximated by a normal distribution. Then, a z-test can be used for the test.

# P-values, type I and type II errors #
A p-value quantifies how likely it is to erroneously reject a specific statistical hypothesis, were it true, based on a given set of data. p-values can then be calculated based on the cumulative distribution function (CDFs) of the statistics used for the test. 
Basically, in statistics, a Type I error is a false positive conclusion (rejecting the null hypothesis when it is true, while a Type II error is a false negative conclusion (failing to reject the null hypothesis when it is false). Note that by definition, p-values are related to type I errors.

# How does the classical A/B testing using the z-score framework work? #
The classical A/B using the z-score framework uses the approximation of the distribution of X (here binomial) to a normal distribution to test whether the difference in the conversion rate between the two groups is 0 or not. The approximation statistic test is used to compute the z-score (observed value of the statistic) which in turn is used to calculate the p-value to draw a conclusion.

# How does sequential A/B testing work? #
Unlike the classical A/B testing which requires data collection to be completed and requires a large sample size for reliable conclusions, the sequential sampling works in a very non-traditional way. Instead of a fixed sample size, one chooses one item (or a few) at a time, and then tests his hypothesis. The conclusion can result in either:
- Rejecting the null hypothesis (H0) in favor of the alternate hypothesis (H1) and stop,
- Keep the null hypothesis and stop,
- unable to reach either conclusion with current observation and continue sampling.

# What are some of the advantages of sequential A/B testing? # 
Some advantages of sequential A/B testing over the classical A/B testing:
- optimize necessary observation (sample size)
- reduce the likelihood of error
- gives a chance to finish experiments earlier without increasing the possibility of false results
 
# How is A/B testing done using machine learning? #
The problem in statistical A/B testing which leads to the use of machine learning is that user behavior is vastly more complex than just the two variables used to compare the controlled and exposed group. Differences between users can come from many other factors. Then, the machine learning approach enables modeling complex systems that include all of the ongoing events, user features, and more. There are a number of algorithms that can be used, each with strengths and weaknesses. Those models/algorithms are used to determine the relevant features which can explain the difference between the controlled and the exposed group.
 
# What are the pros and cons of using Machine learning to perform A/B testing? #
The most important advantage of using machine learning to perform A/B testing is especially that with machine learning one can incorporate the complexity and dynamic nature of data and draw insights, which is not possible when using classical A/B testing. Cons of using Machine learning might be the challenge in finding the best model to use to fit the data.

# Problem formulation for machine learning and target variable #
The target variable, here, is the response to the question: Do you know the brand Lux? Only users who have responded will be considered. The possible values are 0 or 1 associated with yes or no. Problem formulation: What are the relevant features that determine the conversion in brand awareness?

