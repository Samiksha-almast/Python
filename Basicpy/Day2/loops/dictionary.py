#Dictionary
students={
    101:{"Name":"Khushi","Scores":[70,67,95]},
    101:{"Name":"Sam","Scores":[79,97,89]},
    101:{"Name":"Koko","Scores":[20,73,84]},
    101:{"Name":"Adarsh","Scores":[0,76,59]},
    101:{"Name":"Khushu","Scores":[63,37,89]},
}

#calculate average score and flad pass/fail
for sid, details in students.items():
    avg=sum(details["Scores"])/ len(details["Scores"])
    details["Average"]=avg
    details["Passed"]=avg>=30 #boolean flag

#print names of students who passed
print("Students who passed:")
for sid, details in students.items():
    if details["Passed"]:
        print(details["Name"])