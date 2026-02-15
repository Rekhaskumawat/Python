
from sklearn import tree

# Rought = 1
# Smooth = 0

# Tennis = 1
# # Cricket = 2 

def main():
    print("Ball Classification Case Study")

    # original encoded Dataset
    # Independent varables
    X = [[35 , 1],[47 , 1] ,[90 ,0],[48 , 1],[90 ,0],[35 , 1],[92 ,0],[35 , 1],[35 , 1],[35 , 1],[96,0],[43 , 1],[110 ,0],[35,1],[95,0]]
   
    # Dependent variables
    Y = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    # independent Variables for training

    Xtrain = [[35 , 1],[47 , 1] ,[90 ,0],[48 , 1],[90 ,0],[35 , 1],[92 ,0],[35 , 1],[35 , 1],[35 , 1],[96,0],[43 , 1],[110 ,0]]
    
    # independent Variables for testing
    Xtest = [[35,1],[95,0]]

    # dependent Variables for training
    Ytrain = [1,1,2,1,2,1,2,1,1,1,2,1,2]
    
    # independent Variables for testing
    Ytest = [1,2]


    #model Selection
    modelobj = tree.DecisionTreeClassifier()
    
    #  model training
    trainedmodel = modelobj.fit(Xtrain , Ytrain)

    #model Testing
    Result = trainedmodel.predict(Xtest)

    print("Model Predicts the object as : ", Result)            # output : [1 2]

if __name__ == "__main__":
    main()


# Dataset size 15