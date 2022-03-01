import funz
import parse as parse_data

input_txt = funz.readfile("testo.txt")
input_txt = funz.cleanString(input_txt)
input_dict= funz.lettersAbsFreq(input_txt)
lettercnt = funz.lettersCount(input_txt)
for i in input_dict:
    input_dict[i] /= lettercnt / 100 

lang_data = parse_data.parse(parse_data.readfile("dataset"))

#with open("out2.txt","w") as out:
#    out.write(str(input_dict))

dists = {x : 0 for x in lang_data}

for langname,lang in lang_data.items():
    for inputf , letterf in zip(input_dict.values(),lang.values()):
        dists[langname] += abs(inputf - letterf)

result = list(dists.keys())[0]

for lang,freq in dists.items():
    #print( lang + " : " + str(freq))
    if freq < dists[result]:
        result = lang

print(result)
