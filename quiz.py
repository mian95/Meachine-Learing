
import pandas as p

myData = p.DataFrame({
    "Name":["Muhammad Wahab Sadiq","Muhammad Umair Imran",
            "Muhammad Anique Ali",
            "Muhammad Abudllah Ali","Muhammad Zain azhar", "Muhammad Haseeb Ali", 
            "muhammad Hamza Ali","Alia Ali Afzal","Muhammad Umair tahir", 
            "muhammad Farhan jutt"],
    "Age":[20,20,19,30,20,25,23,22,21,34],
    "Sex":["f","M","M","f","M","M","f","f","M","M"],
    "Marks":[90,94,78,76,45,67,45,89,77,88],
    "City":["faisalabad","jaranwala","faisalabad","faisalabad","faisalabad","faisalabad","faisalabad",  "faisalabad","faisalabad","faisalabad"],
    "Date_of_birth":["2022-4-5","2022-4-5","2022-4-5","2022-4-5","2022-4-5"
                 ,"2022-4-5","2022-4-5","2022-4-5","2022-4-5","2022-4-5"],
    "Start_date":["2024-7-4","2024-7-4","2024-7-4","2024-7-4","2024-9-4",
                  "2024-7-4","2024-7-4","2024-7-4","2024-7-4","2024-7-4"],
    "End_date":["2028-8-4","2038-7-4","2098-7-7","2028-7-4","2028-2-4",
                "2028-6-4","2028-12-24","2028-7-4","2028-1-4","2028-9-9"]
 })
#  Complete DataFrame
print(myData)


#Quation No.1
# Middle Name
Q1 = myData["Name"].str.split(" ").str.get(1)
print("Middle Name \n",Q1)


#Quation No.2
# IS contain Ali
Q2 = myData["Name"].str.contains("Ali")
print("Contain Ali",Q2)
# to show the name of the student whose name contains Ali
print(myData[myData["Name"].str.contains("Ali", case=False)]["Name"].values)

#Quation No.3
# Replace the name of the city to three latters
Q3 = myData["City"].replace({"faisalabad":"Fsd",
                              "jaranwala":"Jrw"})
print("City Name in 3 Latters \n",Q3)


#Quation No.4
# Name length is more than 10
print("Names those name length more than 10 \n", myData["Name"].str.len() > 10)

#Quation No.5
# student of max age
max_age = myData["Age"].max()
print("Student of max age \n",myData.loc[myData["Age"] == max_age, "Name"].values)
# student of min age
min_age = myData["Age"].min()
print("Student 0f min age \n",myData.loc[myData["Age"] == min_age, "Name"].values)

#Quation No.6
# mean max median skew
Q6 = myData.agg({
   "Marks":["min","max","median","skew","mean"],
   "Age":["min"]
})
print(Q6)

# duration of degree
print((p.to_datetime(myData["Start_date"])) - (p.to_datetime(myData["End_date"])))

# Calculate average and median marks for male and female students
Q8 = myData.groupby("Sex")["Marks"].agg(["mean", "median"])
print(Q8)   