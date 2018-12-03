file = open("input","r")
input = file.readlines()
file.close
seen=set()
duplicate=set()

for i in input:
    this_left= int(i.split('@')[1].split(':')[0].split(',')[0])
    this_top = int(i.split('@')[1].split(':')[0].split(',')[1])

    this_width= int(i.split('@')[1].split(':')[1].split('x')[0])
    this_height= int(i.split('@')[1].split(':')[1].split('x')[1])


    for x in range(1,this_width+1):
        for y in range(1,this_height+1):
            if (this_left+x,this_top+y) in seen:
                duplicate.add((this_left+x,this_top+y))
            else:
                seen.add((this_left+x,this_top+y))

print(len(duplicate))
for i in input:
    dups = False
    this_left= int(i.split('@')[1].split(':')[0].split(',')[0])
    this_top = int(i.split('@')[1].split(':')[0].split(',')[1])

    this_width= int(i.split('@')[1].split(':')[1].split('x')[0])
    this_height= int(i.split('@')[1].split(':')[1].split('x')[1])


    for x in range(1,this_width+1):
        for y in range(1,this_height+1):
            if (this_left+x,this_top+y) in duplicate:
                dups = True

    if dups == False:
        print(i)
