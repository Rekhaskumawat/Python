# Mapping

    # dictionary :- {key : value} pair , no Dupication , last key value will be overwritten, updateable

Information ={ "Name":"Rahul" ,
               "Age": 25 , 
               "City": "PUNE" , 
               "Marks":89.90 , 
               "City" :"MUMBAI"}

print(type(Information))
print(Information)
print(Information["City"])

Information["Age"] = 26
print(Information)