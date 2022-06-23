import pandas as pd
from apyori import apriori

data = pd.read_csv('breast-cancer.csv')

records = []

for i in range(0, len(data)):
    records.append([str(data.values[i,k]) for k in range(0,10)])
print(records)

association_rules = apriori(records, min_support=0.2, min_confidence=0.6,min_lift=1,max_length=3)
print(association_rules)
association_rules = list(association_rules)

empty_list = []
for x in range(len(association_rules)-1):
    if(len(association_rules[x][0]) > 1):
        empty_list.append(association_rules[x])

association_rules = empty_list


for item in association_rules:
    pair = item[0]
    items = [x for x in pair]
    items_concat = [x for x in pair]
    items_concat.pop(0)
    string = ""
    for x in range(len(items_concat)):
        if(x != len(items_concat) and x != 0):
            string = string +" , "+  items_concat[x]
        else:
            string = string + " " + items_concat[x]
    print("Rule: " + items[0] + " -> " + string)
    print("Support: " + str(item[1]))
    print("Confidence : " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("Conviction " + str((1-item[1])/(1-item[2][0][2])))
    print("======================================")
