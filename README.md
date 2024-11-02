# Question 1
# Gradient Descent

**Status**: Solved  
**Difficulty**: Easy

### Problem Statement

Your task is to minimize the function via Gradient Descent:  
\( f(x) = x^2 \)

Gradient Descent is an optimization technique widely used in machine learning for training models. It is crucial for minimizing the cost or loss function and finding the optimal parameters of a model.

For the above function, the minimizer is clearly \( x = 0 \), but you must implement an iterative approximation algorithm through gradient descent.

### Input:

- **iterations**: The number of iterations to perform gradient descent. \( \text{iterations} \geq 0 \).
- **learning_rate**: The learning rate for gradient descent. \( 1 > \text{learning_rate} > 0 \).
- **init**: The initial guess for the minimizer. \( \text{init} \neq 0 \).

Given the number of iterations to perform gradient descent, the learning rate, and an initial guess, return the value of \( x \) that globally minimizes this function.

### Output:

- The value of \( x \) after the specified number of iterations, rounded to 5 decimal places.

### Requirements:

- Implement gradient descent for the given function.
- Round the final result to 5 decimal places using Python's `round()` function.

