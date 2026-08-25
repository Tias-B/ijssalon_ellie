def presenteer(dictionary , totaal):
    for key, value in dictionary.items():
        print(key + " : "  + str(value) + " euro")
    print("==================================")
    print("totaal : " + str(totaal) + " euro")

mijn_dict = {
    'vis' : 10,
    'vlees': 25,
    'overig' : 15
}


