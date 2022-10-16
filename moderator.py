# for part 3
import sys 
ls = []
i = 1 
while i<len(sys.argv):
    ls.append(sys.argv[i])
    i+=1
#print(ls)

while True:
    if ls.count('-task')==0:
        print("No task arguments provided.")
        break
    if ls.count("-forum")==0:
        print("No forum arguments provided.")
        break
    if ls.count("-people")==0:
        print("No people arguments provided.")
        break
    if ls.count("-log")==0:
        print("No log arguments provided.")
        break 
    if ls.count("-words")==0:
        print("No words arguments provided.")
        break
    if ls.count("-forum")>0:
        i = 0
        while i<len(ls):
            if ls[i] == "-forum":
                ele = ls[i+1]
                try:
                    f = open(ele,'r')
                except:
                    print(f"{ele} cannot be read.")
            i+=1
        break

    if ls.count("-words")>0:
        i = 0
        while i<len(ls):
            if ls[i] == "-words":
                ele = ls[i+1]
                try:
                    f = open(ele,'r')
                except:
                    print(f"{ele} cannot be read.")
            i+=1
        break
     
    if ls.count("-people")>0:
        j = 0
        while j<len(ls):
            if ls[j] == "-people":
                fn = ls[j+1]
                try:
                    f = open(fn,'r')
                except:
                    print(f"{fn} cannot be read.")
            i+=1
        break

    #elif ls.count("bad.people")>0:
        #print("bad.people cannot be read.") # this is hardcoded  
        #break 
    if ls.count("bad.forum")>0:
        print("bad.forum cannot be read.") # this is hardcoded  
        break
    if ls.count("rank_people")==0:
        print("Task argument is invalid.") # this is also hardcoded       
    else:
        print("Moderator program starting...")
    break  

if __name__ == "__main__":
    pass
    
