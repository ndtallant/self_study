# Machine Learning Method Summaries

## Decision Trees

#### What assumptions does it make about the data?

#### What is it optimizing for?
A decision tree minimizes entropy in the data that it is splitting, which in turn maximizes information gain. The implementation of this model in sci-kit learn can also optimize for "gini" which is functionaly equivalent. 

#### What parameters does it have?
- splitter: "best" or "random"
- max\_depth: integer or None (splits until all leaves are pure or at the min\_samples\_split)
- min\_samples\_split: minimum number of samples required to split an internal node
- max\_features: number of features considered for each split (defaults to the square root of the number of features)

#### How are those parameters selected?

#### How you score new data with it?

#### How do you interpret the model and its predictions?

#### Implementation Reference
- Low Complexity 
- Likely to Overfit
- High Interpretability 
- Training Time depends on the depth of the tree and number of features. 
- **Testing/Scoring Time?** Slow, Medium, Fast

## Logistic Regression

#### What assumptions does it make about the data?

#### What is it optimizing for?

#### What parameters does it have?

#### How are those parameters selected?

#### How you score new data with it?

#### How do you interpret the model and its predictions?

- Complexity? Low, Medium, High
- Likely to Overfit? Yes, No
- Interpretability? Low, Medium, High
- Training Time? Slow, Medium, Fast
- Testing/Scoring Time? Slow, Medium, Fast

## Support Vector Machines

#### What assumptions does it make about the data?

#### What is it optimizing for?

#### What parameters does it have?

#### How are those parameters selected?

#### How you score new data with it?

#### How do you interpret the model and its predictions?

- Complexity? Low, Medium, High
- Likely to Overfit? Yes, No
- Interpretability? Low, Medium, High
- Training Time? Slow, Medium, Fast
- Testing/Scoring Time? Slow, Medium, Fast
