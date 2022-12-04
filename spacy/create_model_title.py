from resources_to_create_spacy_model import *
from connect_database import mycursor
from clean_text import clean_text

data= load_data("titles.json")
patterns = create_training_set(data,"TITLE")
rules=generate_entityrules(patterns)
mycursor.execute("select * from mt_page_file_contents")
text=''

for x in mycursor:
   if x[1]==445:
            text = text+clean_text(x[4])
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

nlp = train_spacy(train_data, 31)
nlp.to_disk("title_model2")
print("saved successfully")