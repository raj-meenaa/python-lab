sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# Length of the outermost dictionary
print("Length of dictionary:", len(sampleDict))

# Accessing the "history" value
history_value = sampleDict["class"]["student"]["marks"]["history"]
print("History marks:", history_value)
