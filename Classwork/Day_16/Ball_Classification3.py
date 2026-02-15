
from sklearn import tree

# Rought = 1
# Smooth = 0

# Tennis = 1
# # Cricket = 2 

def main():
    print("Ball Classification Case Study")

    # Independent varables
    Features = [[35 , 1],[47 , 1] ,[90 ,0],[48 , 1],[90 ,0],[35 , 1],[92 ,0],[35 , 1],[35 , 1],[35 , 1],[96,0],[43 , 1],[110 ,0],[35,1],[95,0]]
   
    # Dependent variables
    Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    #model Selection
    modelobj = tree.DecisionTreeClassifier()
    
    #  model training
    trainedmodel = modelobj.fit(Features , Labels)

    #model Testing
    Result = trainedmodel.predict([[37,1],[94,0]])

    print("Model Predicts the object as : ", Result)            # output : [1 2]

if __name__ == "__main__":
    main()


# Dataset size 15