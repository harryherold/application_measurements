# Observations
* most of the time spend in `load_matrix`
* the list comprehension is the bottleneck
* `dot` operation is fine
* number of used threads is 4

# Conclusion
* eliminate list comprehension
* time consumption of computation
* What are the threads doing?
* What does `dot` utilize under the hood?
* Does the code utilizes the resources efficently?

