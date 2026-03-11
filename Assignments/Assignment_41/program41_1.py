'''
    Description :- 
        write a Python program that classifies a new data point using K_nearest Neighbours
        alorithm.
        the alogithm shoulb be implemented maually without using any MIL library

        the program should include :
            -> calculate Euclidean Distance
            -> Sort Distance
            -> Select K nearest Neighbours
            -> predict the class based on majority voting

        Dataset :-

            Point   X   Y   Label
            A       1   2    Red
            B       2   3    Red
            C       3   1    Blue
            D       6   5    Blue

        Task :-

            Accept the X and Y coordinate od a new point from the user
            Comput Euclidean Distance
            sort the distance
            select K =3
            predict the class label
        
        Input:-

        Enter X coordinate :- 2
        Enter Y Coordinate :- 2

        Output:-
        Predicted Class - Red
'''

import math

Border = "-"*50

#-------------------------------------------------------------------------------
#  Function to calculate the Euclidean Distance from the input coordinate
#-------------------------------------------------------------------------------

def EuclideanDisatance(P1 , P2):
    
    Distance = math.sqrt(((P1['X'] - P2['X'])**2) + (P1['Y'] - P2['Y'])**2)
    return Distance

#-------------------------------------------------------------------------------
#  Function to sort the distance in increasing order
#-------------------------------------------------------------------------------

def SortedDistance(Data):

    sorted_Data = sorted(Data , key = lambda item : item['Distance'])
    
    return sorted_Data

#-------------------------------------------------------------------------------
#  Function to to predict the output when K value is changed
#-------------------------------------------------------------------------------

def PredictClass(Data , K):
    
    nearest = SortedDistance(Data)

    print(Border)
    print("Nearest elements are :- ")
    for d in nearest[:K]:
        print(d)
    print(Border)

    #votes

    votes = {}

    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label,0)+1

    print(Border)
    print("Votes are :-")
    print(Border)

    for d in votes:
        print("Name : ",d , ", Number of votes :" , votes[d])

    print(Border)

    predicted_class = max(votes , key=votes.get)

    print("Predicted class of input when K is" , K  ," : ", predicted_class)
    print(Border)


def UserDefinedKNN(new_x , new_y, K):

    Data = [{'point': 'A', 'X':1 , 'Y': 2 , 'label':'Red'},
            {'point': 'B', 'X':2 , 'Y': 3 , 'label':'Red'},
            {'point': 'C', 'X':3 , 'Y': 1 , 'label':'Blue'},
            {'point': 'D', 'X':6 , 'Y': 5 , 'label':'Blue'}
            
            ]
            
    print(Border)
    print("DataSet ")

    for i in Data:
        print(i)
    
    print(Border)

    new_point = {'X' : new_x , 'Y' : new_y}

    for d in Data:
        d['Distance'] = EuclideanDisatance(d , new_point)

    print("Euclidean Distance are :- ")

    for d in Data:
        print(d)
    
    SortedDistance(Data)

    PredictClass(Data ,K)


def main():

    new_x = int(input("Enter the X coordinate :- "))
    new_y = int(input("Enter the Y coordinate :- "))
    K = int(input("Enter the K value :- "))

    UserDefinedKNN(new_x , new_y , K)

if __name__ == "__main__":
    main()