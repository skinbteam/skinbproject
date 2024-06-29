import spacy

# Load a pre-trained spaCy NER model
nlp = spacy.load("en_core_web_sm")
# Annotate text with recognized entities
text = "Apple is a company based in California."
doc = nlp(text)


if not doc.ents:
    print("No entities found.")
else:
    # Extract recognized entities
    for ent in doc.ents:
        print(ent.text, ent.label_)