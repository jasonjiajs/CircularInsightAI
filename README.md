Step1: Data Split
- Since we have 1300 rows of data, we randomly selected 100 rows as test/validation and the rest as training data

Step2: Came up with 4 metrics: relevance of the problem, clarity of the problem, suitability of the solution, clarity of the solution
- Manually Label ~125 rows of Train Data and all Test Data
- Then we will compare 2 approaches: compare the accuracy of tuned LLM and not tuned LLM on Test Data with our labels done manually(we will use as a ground truth)
- Fine Tune Approach:
  1. Run LLM to get the rest of the Train Data to fill in the labels,
  2. Use the Train Data to tune the LLM
  3. Use tuned LLM to label Test Data
- Non Fine Tune Approach:
  1. Use LLM to label Test Data
- Then we will compare the accuracy to decide which version of LLM to use.
- These metrics are used as a negative filter, ideas with low scores should be flagged or filtered out, however, ideas with high scores don't necessarily mean much(means is not wrong)
  
Step3: Label the problems to 1 of the 5 categories: Food Waste, Plastic Waste, 
