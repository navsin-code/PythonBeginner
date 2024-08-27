# # with open("weather_data .csv") as weather_file:
# #     data=weather_file.readlines()
# #     print(data)
#
# # import csv
# # with open("weather_data .csv") as weather_files:
# #     data=csv.reader(weather_files)
# #     print(data)
# #     temperatures=[]
# #     for row in data:
# #         if row[1]!="temp":
# #             temp=row[1]
# #             new_temp=int(temp)
# #             temperatures.append(new_temp)
# #     print(temperatures)
#
import pandas
# data=pandas.read_csv("weather_data .csv")
# # print(type(data))
# # print(data["temp"])
#
# data_dict=data.to_dict()
# print(data_dict)
# temp_list=data["temp"].to_list()
# # average=sum(temp_list)//len(temp_list)
# # print(average)
# max_temp=data['temp'].max()
# #get data in columns
# # print(data["condition"])
# # print(data.condition) #converted heading to an attribute
#
# #get data in a row
# print(data[data.day=="Monday"])
# print(data[data.temp==max_temp])
cinnamon_squirrel=0
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240809.csv")
gray_squirrel=len(data[data["Primary Fur Color"]=="Gray"])
black_squirrel=len(data[data["Primary Fur Color"]=="Black"])
cinnamon_squirrel=len(data[data["Primary Fur Color"]=="Cinnamon"])
data_dict={"Fur Colour":["Gray","Cinnamon","Black"],
           "Count":[gray_squirrel,cinnamon_squirrel,black_squirrel]}
df=pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")