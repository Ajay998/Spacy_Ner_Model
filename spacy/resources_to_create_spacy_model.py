import json
import random
import spacy
from spacy.lang.en import English
from spacy.training import Example
import os
# from spacy.training import Example

def load_data(file):
    with open(file,"r",encoding="utf-8") as f:
        data = json.load(f)
    return data


def save_data(file,data):
  with open(file,"w",encoding="utf-8") as f:
    json.dump(data,f,indent=4)


def create_training_set(data,type):
    # data= load_data(file)
    patterns= []
    for item in data:
        pattern = {
            "label":type,
            "pattern":item
        }
        patterns.append(pattern)
    return patterns



def generate_entityrules(patterns):
    nlp = English()
    ruler = nlp.add_pipe("entity_ruler")
    ruler.add_patterns(patterns)
    nlp.to_disk("rules")
    return "rules"

def test_model(model,text):
  doc = model(text)
  results = []
  entities=[]
  for ent in doc.ents:
         entities.append((ent.start_char,ent.end_char,ent.label_))
  if len(entities)>0:
      return [text,{"entities":entities}]



def train_spacy(data,iterations):
  train_data=data
  nlp=spacy.blank("en")
  if "ner" not in nlp.pipe_names:
    ner = nlp.create_pipe("ner")
    nlp.add_pipe("ner")
    print("pipe names *****",nlp.pipe_names)
  for _, annotations in train_data:
    for ent in annotations.get("entities"):
      ner.add_label(ent[2])
  other_pipes=[pipe for pipe in nlp.pipe_names if pipe != "ner"]
  with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.begin_training()
    for itn in range(iterations):
      print("starting iterations"+str(itn))
      random.shuffle(train_data)
      losses={}
      for batch in spacy.util.minibatch(data, size=2):
           for text, annotations in batch:
                  doc = nlp.make_doc(text)
                  example = Example.from_dict(doc, annotations)
                  nlp.update([example],drop=0.3,sgd=optimizer,losses=losses)
      print(losses)
  return nlp