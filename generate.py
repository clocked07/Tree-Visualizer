import pandas
import re
import sys

r = r"^[Ww]ord\.(\d+)\.(\d+)$"
try:
    assert (len(sys.argv) == 2) 
except AssertionError as e:
    raise RuntimeError("Provide the filename as CLI argument") from e

filename = sys.argv[1]

data = pandas.read_csv(filename)
ids = data["Word_ID"]
words = data["word"]
pos_tags = data["pos"]
parents = data["dep"].astype(int)

sent_id_to_sentence_mapping = {}
currCount = 0

sentences = []
for i in range(len(ids)):

    match = re.match(r, ids[i])
    sent_id = match.group(1)
    word_id = match.group(2)

    if word_id == "1" and sent_id == "1":
        currCount += 1

    if f"{currCount}-{sent_id}" not in sent_id_to_sentence_mapping:
        sent_id_to_sentence_mapping[f"{currCount}-{sent_id}"] = {}

    sent_id_to_sentence_mapping[f"{currCount}-{sent_id}"][word_id] = [f"{words[i]}", f"{pos_tags[i]}", parents[i]]
    
for sent_id in sent_id_to_sentence_mapping:
    word_to_id_mapping = sent_id_to_sentence_mapping[sent_id]
    full_sentence = ""
    nRoots = 0
    try:
        with open(f"{sent_id}.dot", "w") as f:
            f.write("digraph G {\nrankdir=BT;\n")
            for id in word_to_id_mapping:
                if word_to_id_mapping[id][2] == 0:
                    nRoots += 1
                    f.write(f"\"{id}-{word_to_id_mapping[id][0]}-{word_to_id_mapping[id][1]}\" -> \"root\";\n")
                else:
                    f.write(f"\"{id}-{word_to_id_mapping[id][0]}-{word_to_id_mapping[id][1]}\" -> \"{word_to_id_mapping[id][2]}-{word_to_id_mapping[str(word_to_id_mapping[id][2])][0]}-{word_to_id_mapping[str(word_to_id_mapping[id][2])][1]}\";\n")

                full_sentence += word_to_id_mapping[id][0] + " "

            f.write(f"\"{full_sentence}\";\n}}")
        assert(nRoots == 1)
    except:
        print("Error in file " + sent_id)
