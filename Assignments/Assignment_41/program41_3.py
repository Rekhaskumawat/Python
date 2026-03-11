'''
    Description :- 
        Use KNN to predict Whwtjer a student passes or fail baesd on the study hours and attendent

        Dataset :-

            Study Hours   Attendence   Result
                2              60       Fail
                5              80       Pass
                6              85       Pass
                1              50       Fail

        Task :-

            Accept input from user (study hours , Addentence)
            Apply KNN alorithm
            predict whether the stuent Passes or fail
        
        Input:-

        Enter Study Hours :- 4
        Enter Attendence :- 70

        Output:-
        Predicted result : Pass
'''

import math

Border = "-"*50

#-------------------------------------------------------------------------------
#  Function to calculate the Euclidean Distance from the input coordinate
#-------------------------------------------------------------------------------

def EuclideanDisatance(P1 , P2):
    
    Distance = math.sqrt(((P1['StudyHours'] - P2['StudyHours'])**2) + (P1['Attendence'] - P2['Attendence'])**2)
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
        label = neighbour['Result']
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

    Data = [{'StudyHours':2 , 'Attendence': 60 , 'Result':'Fail'},
            {'StudyHours':5 , 'Attendence': 80 , 'Result':'Pass'},
            {'StudyHours':6 , 'Attendence': 85 , 'Result':'Pass'},
            {'StudyHours':1 , 'Attendence': 50 , 'Result':'Fail'},
            ]
            
    print(Border)
    print("DataSet ")

    for i in Data:
        print(i)
    
    print(Border)

    new_point = {'StudyHours' : new_x , 'Attendence' : new_y}

    for d in Data:
        d['Distance'] = EuclideanDisatance(d , new_point)

    print("Euclidean Distance are :- ")

    for d in Data:
        print(d)
    
    SortedDistance(Data)

    PredictClass(Data ,K)


def main():

    new_x = int(input("Enter Study Hours :- "))
    new_y = int(input("Enter the Attendence :- "))
    K = int(input("Enter the K value :- "))

    UserDefinedKNN(new_x , new_y , K)

if __name__ == "__main__":
    main()