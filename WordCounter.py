#-------------------------------------------------------------------------
# first implementation - problem with last character

text = "Ala ma kota1"
word = ""
count = 0

for x in text:
    word = word + x
    if x == " " or x == text[-1]:
        word = ""
        count += 1

print("Word number: "+str(count))

#-------------------------------------------------------------------------
# first implementation - problem fixed

text = "Ala ma kota1 Ala ma Ala"
word = ""
count = 0

for x in range(0,text.__len__()):
    word = word + text[x]
    if text[x] == " " or x == text.__len__()-1:
        word = ""
        count += 1

print("Word number: "+str(count))

#-------------------------------------------------------------------------
# Shortest approach

print("Word number: "+str(text.split(" ").__len__()))

#-------------------------------------------------------------------------