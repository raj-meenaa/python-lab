sampleDict = {'a': 100, 'b': 200, 'c': 300}
value_exists = 200 in sampleDict.values()
print("200 exists:", value_exists)
key_for_200 = [key for key, value in sampleDict.items() if value == 200]
print("Key for 200:", key_for_200[0] if key_for_200 else "Not found")
