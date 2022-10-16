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
    
    elif ls.count("-forum")==0:
        print("No forum arguments provided.")
        break
    elif ls.count("-people")==0:
        print("No people arguments provided.")
        break
    elif ls.count("-log")==0:
        print("No log arguments provided.")
        break 
    elif ls.count("-words")==0:
        print("No words arguments provided.")
        break
    elif ls.count("-forum")>0:
        s = '-forum'
        index = []
        i = 0
        while i < len(ls):
            if s == ls[i]:
                index.append(i)
            i += 1
        new_index = ls[index[0]+1]
        try:
            f = open(new_index,'r')
        except FileNotFoundError:
            print(f"{new_index} cannot be read.")
            exit()

    elif ls.count("-words")>0:
        s = '-words'
        index = []
        i = 0
        while i < len(ls):
            if s == ls[i]:
                index.append(i)
            i += 1
        new_index = ls[index[0]+1]
        try:
            f = open(new_index,'r')
        except FileNotFoundError:
            print(f"{new_index} cannot be read.")
            exit()
     
    elif ls.count("-people")>0:
        s = '-people'
        index = []
        i = 0
        while i < len(ls):
            if s == ls[i]:
                index.append(i)
            i += 1
        new_index = ls[index[0]+1]
        try:
            f = open(new_index,'r')
        except FileNotFoundError:
            print(f"{new_index} cannot be read.")
            exit()

    #elif ls.count("bad.people")>0:
        #print("bad.people cannot be read.") # this is hardcoded  
        #break 
    #if ls.count("bad.forum")>0:
        #print("bad.forum cannot be read.") # this is hardcoded  
        #break
    elif ls.count("rank_people")==0:
        print("Task argument is invalid.") # this is also hardcoded       
    else:
        print("Moderator program starting...")
    break  

if __name__ == "__main__":
    pass
    
