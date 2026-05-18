#import numpy for numerical operation

import numpy as np

#------------------------------------------------------------------
# STEP 1 : Define Inputs Features
#
#   these are the inputs coming to the neuron
#    Example : could be marks , pixel values , or any features
#------------------------------------------------------------------

inputs = np.array([2.0 , 3.0 ,4.0])

#------------------------------------------------------------------
# STEp 2 : Define Weights
#
#   Each input has a corresponding weight (w1 ,w2,w3)
#   Weight reperesent importance of each input
#------------------------------------------------------------------

weights = np.array([0.5 , 0.3 , 0.2])

#------------------------------------------------------------------
# STEP 3 : DEfine Bias
#
#   Bias is an additional parameter that helps shift the output
#   It allows the model to fit data better
#------------------------------------------------------------------

bias = 1.0

#------------------------------------------------------------------
# STEP 4: Calculate Weighted Sum (Z)
#
#   Formula : Z = (x1*w1 + x2*w2 +x3*w3 +.......+ xn*wn) + bias
#   Using numpy dot product for efficient calculation
#------------------------------------------------------------------

weighted_sum = np.dot(inputs , weights)+ bias

# Manual Calculation 
# (2.0*0.5 + 3.0*0.3 + 4.0*0.2)+1.0 = 3.7

#------------------------------------------------------------------
# STEP 5: Activation Function (ReLU)
#
#   ReLU(Rectifier Linear Unit):
#       if value > 0 -> return value
#       if value < 0 -> returen 0
#------------------------------------------------------------------

def relu(x):
    return max(0,x)

#------------------------------------------------------------------
# STEP 6 : Final Output
#
#   pass the weighted sum through activation function
#------------------------------------------------------------------

output = relu(weighted_sum)

#------------------------------------------------------------------
# STEP 7 : Display the output
#------------------------------------------------------------------

print("Inputs : ", inputs)
print("Weight : ", weights)
print("Bias : ", bias)
print("Weight Sum (z) : ", weighted_sum)
print("Final Output : ", output)