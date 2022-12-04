
from resources_to_create_spacy_model import *
from connect_database import mycursor


data= load_data("hospitals.json")

patterns = create_training_set(data,"ORG")
rules=generate_entityrules(patterns)

mycursor.execute("select * from mt_page_file_contents")

with open('all_collection_text.txt', encoding="utf8") as f:
    text = f.read()

for x in mycursor:
    if x[1]==372:
            text = text+x[4]
nlp = spacy.load(rules)
segments= text.split(".")

train_data=[]
for segment in segments:
    print(segment)
    result = test_model(nlp,segment)
    if result !=None:
        print(result)
        train_data.append(result)
save_data("trained_set.json",train_data)

nlp = train_spacy(train_data, 30)
nlp.to_disk("org_model8")
print("saved successfully")