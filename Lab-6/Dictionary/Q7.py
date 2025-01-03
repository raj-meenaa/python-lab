sampleDict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
keysToRemove = ["name", "salary"]
for key in keysToRemove:
    sampleDict.pop(key, None)  

print("Updated dictionary:", sampleDict)
