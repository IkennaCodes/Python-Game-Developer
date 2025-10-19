subjects = {"Mathematics":"4","English":"3.5","Science":"4","Computing":"3","History":"3"}
print(subjects)

#How many subjects do you take?
print(len(subjects))

#Delete the subject you don't like
del subjects ["History"]
print(subjects)

#Add a new subject
subjects ["Art"] = "2"
print(subjects)

#Help! Science is so hard!
subjects ["Science"] = "5"
print (subjects)

#What subjects do you do?
print(subjects.keys())

#How hard are your suubjects?
print(subjects.values())