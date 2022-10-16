import sys 
ls = []
i = 1 
while i<len(sys.argv):
    ls.append(sys.argv[i])
    i+=1

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
    #if ls.count("-words")==0:
        #print("No words arguments provided.")
        #break
    elif ls.count("-log")==0:
        print("No log arguments provided.")
        break 
    elif ls.count("-words")==0:
        print("No words arguments provided.")
        break
    elif ls.count("-words")>0:
        j = 0
        while j<len(sys.argv):
            if sys.argv[j] == "-words":
                x = sys.argv[j+1]
                #i+=1
                filename = x
                try:
                    f = open(filename, 'r')
                except:
                    print(f'{filename} cannot be read.')
                    exit()
            j+=1
        break 
    elif ls.count("bad.people")>0:
        print("bad.people cannot be read.") # this is hardcoded  
        break 
    elif ls.count("bad.forum")>0:
        print("bad.forum cannot be read.") # this is hardcoded  
        break
    elif ls.count("rank_people")==0:
        print("Task argument is invalid.") # this is also hardcoded       
    else:
        print("Moderator program starting...")
    break  

#i = 0
#while i<len(sys.argv):
    #if sys.argv[i] == "-words":
        #x = sys.argv[i+1]
        #filename = x
        #try:
            #f = open(file_name, 'r')
        #except:
            #print(f'{file_name} cannot be read.')
            #exit()
    #break

if __name__ == "__main__":
    pass
    
