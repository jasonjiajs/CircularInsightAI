Step1: Data Split
- Since we have 1300 rows of data, we randomly selected 100 rows as test/validation and the rest as training data

Step2: Came up with 4 metrics: relevence of the problem, clarity of the problem, suitability of the solution, clarity of the solution
- Manually Label ~125 rows of Train Data and all Test Data
- Then we will compare 2 approach: fined tune and not tuned LLM on Test Data
- We will then run LLM to get the rest of the Train Data to fill in the labels
- Then use 
