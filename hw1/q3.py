# Formula
# C(map) = arg max P(c) P(d|c)
#           c in C

# Question 1: Explain in your own words what each term means: P(c), P(d∣c) and P(c∣d)?
# Answer:
# P(c) - general probability of a single class 'c' occurring before looking at any specific document
# P(d|c) - probability of seeing the document 'd', given it belongs to class 'c'
# P(c|d) -  probability of a document belonging to class 'c' given the specific document 'd'


# Question 2: Why can the denominator P(d) be ignored when comparing classes?
# Answer:
# The denominator P(d) is constant for all classes because it represents the 
# probability of seeing that specific document across the entire dataset. 
# Since the argmax function only cares about which class produces the highest 
# relative value to determine the "most likely class" dividing by a constant 
# does not change the final ranking or result.
