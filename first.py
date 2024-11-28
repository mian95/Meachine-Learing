# import pandas as pd 

# air = pd.read_csv("air.csv")
# titanic = pd.read_csv("titanic.csv")
# airQ = pd.read_csv("air_quality_long.csv")
# # print(air)
# # print(airQ)
# # print(air.head(10))
# # print(titanic.head(10))

# titanic2 = titanic.agg(
#     {
#         "Survived": ["mean","min","max","median","skew"],
#         "Pclass": ["mean","min","max","median","skew"],
#         "Age": ["mean","min","max"],
#         "Fare": ["mean","min","max","median","skew"],
#     }
# )
# titanic3 = titanic.rename(columns={
#     "Fare":"Ticket_price",
#     "Sex":"Gender",
# })
# # print(titanic3.describe())

# print(airQ.info())

# import pandas as p


# data = p.DataFrame({
#     "name": ["Muhammad Umair imran", "Muhammad Hamza Manzoor", "Abdul Wahab Sadiq"],
#     "age": ["20", "30", "21"],
#     "Sex": ["male", "male", "male"],
#     "marks": ["94", "92", "92"],
# })

# print(data["name"].str.split(" ").str.get(1))




import pandas as p

myData = p.DataFrame({
    "Name":["Muhammad Wahab Saqiq","Muhammad Umair Imran",
            "Muhammad anique ali",
            "Muhammad Abullah ali","Muhammad Zain azhar", "muhammad haseeb ali", 
            "muhammad hamza ali","muhammad faaiz ali","muhammad umair tahir", 
            "muhammad farhan jutt"],
    "Age":["20","20","19","30","20","25","23","22","21","24"],
    "Sex":["M","M","M","M","M","M","M","M","M","M"],
    "Marks":["90","98","78","76","45","67","45","89","77","88"],
    "City":["fsd","jrw","lhr","krc","fsd","jrw","lhr","krc","LA","London"],
    "Date_of_birth":["2022-4-5","2022-4-5","2022-4-5","2022-4-5","2022-4-5"
                 ,"2022-4-5","2022-4-5","2022-4-5","2022-4-5","2022-4-5"],
    "Start_date":["2024-7-4","2024-7-4","2024-7-4","2024-7-4","2024-7-4",
                  "2024-7-4","2024-7-4","2024-7-4","2024-7-4","2024-7-4"],
    "End_date":["2028-7-4","2028-7-4","2028-7-4","2028-7-4","2028-7-4",
                "2028-7-4","2028-7-4","2028-7-4","2028-7-4","2028-7-4"]
 })
 
print(myData["Name"])