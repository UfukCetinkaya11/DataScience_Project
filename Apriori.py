import pandas as pd
from apyori import apriori
import streamlit as st

st.set_page_config(layout="wide")

# Space out the maps so the first one is 2x the size of the other three
c1, c2, c3, c4 = st.columns((2, 1, 1, 1))


st.title("Apriori algortihm", anchor=None)

st.markdown("The Apriori algorithm is used for frequent itemset mining.\ "
            "It proceeds by identifying the frequent individual items in the database and extending them to larger and larger item sets \n as long as those item sets appear sufficiently often in the database ")

support = st.slider("Support Value", min_value=0.3,
                    max_value=0.5, value=0.3)

confidence = st.slider("Confidence Value", min_value=0.6,
                       max_value=0.8, value=0.6)

data = pd.read_csv('breast-cancer.csv')

records = []

for i in range(0, len(data)):
    records.append([str(data.values[i,k]) for k in range(0,10)])


association_rules = apriori(records, min_support=support, min_confidence=confidence,min_lift=1,max_length=3)
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
    st.markdown("Rule: " + items[0] + " -> " + string)
    st.markdown("Support: " + str(item[1]))
    st.markdown("Confidence : " + str(item[2][0][2]))
    st.markdown("Lift: " + str(item[2][0][3]))
    st.markdown("======================================")
    st.markdown("Conviction " + str((1 - item[1]) / (1 - item[2][0][2])))