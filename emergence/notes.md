---
geometry: margin=1in
---

# Intro with quote

# Outline

# Motivation

- introduce Crutchfield, complexity research from physics perspective
- point to picture, explain limitations of hardware setup

# Predicted Information Gain

- Bayes rule:
$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$
- prob of being in ground state, given measurement of 1 depends on:
    - prob of measuring 1 in ground state
    - prob of ground state
    - prob of measuring 1 (regardless of state)
- write on board, make sure everyone knows entropy measure
- actions chosen to gain information - quantifying what it means to make a good
  experiment
- transition with what is a state?


# Defining State

- write a couple example states on the board
- emphasize intractability, compare with solution of super high-res sensors and
  lots of compute power (google cars)
- explain figure
- to figure out better ways to extract hidden states, let's do a simple example

# Data slide

- keep up for ~15 seconds, say that the point is to appreciate the difficulty of
  the task

# Markov approach

- don't change slide right away, use first couple numbers in sequence and
  demonstrate counting transitions

  start     followed by
  -----     -----------
  0         1
            0
  1         1
            0

- introduce idea of word lengths

- show golden mean process

# Epsilon Machines

- walk through construction of tree, possibly on board
- emphasize that each edge of tree encodes observed probabilities
- future morphs as a basis set for the parse tree
- label nodes of parse tree, find transition probabilities

# Logistic Map

- useful part of epsilon machines is ability to extract statistics from them

# SM time series
- stationary process

# dimensionality examples
- long and short time scales mean we need to hang on to lots of states
- examples: robot on a beach, then goes in water
- observing physical process with nonstationarity - phase change, brains

# general theory of filters

- Kalman filters use knowledge of motion to cut down on computation
- what if we could get that knowledge automatically, from data?
- filters create equivalence classes of data/states

# Conclusion
- discuss advantages/disadvantages of very adaptive systems with control over
  their own data collection 





