#    [a,b,c,d]
#   X[1,2,3,5]
#   Y[2,3,1,6]
#    [R,R,B,B]

# predict(3,3) -> ?
import numpy as np
import math

def EucDistance(p1, p2):

    Ans = math.sqrt(((p1['X']-p2['X'])**2) + ((p1['Y']-p2['Y'])**2))

    return Ans

def MarvellousKNeighboursClassifier():
    
    Border = "-"*50

    data = [{'point': 'A', 'X':1 , 'Y': 2 , 'label':'Red'},
            {'point': 'B', 'X':2 , 'Y': 3 , 'label':'Red'},
            {'point': 'C', 'X':3 , 'Y': 1 , 'label':'Blue'},
            {'point': 'D', 'X':5 , 'Y': 6 , 'label':'Blue'}
            
            ]
    print(Border)
    print("Marvellous UserDefine KNN")
    print(Border)

    print(Border)
    print("Training Data Set")
    print(Border)

    for i in data:
        print(i)

    print(Border)

    new_point = {'X':3 ,'Y':3}

    print(data[0])
    print(new_point)

    result = EucDistance(data[0] , new_point)

    print(result)

def main():

    MarvellousKNeighboursClassifier()

if __name__ == "__main__":
    main()