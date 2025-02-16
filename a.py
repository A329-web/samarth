with open("Codingal.txt","w") as f:
    f.write("Hi!! I am Arjeeta")
f.close()



with open("Codingal.txt","r") as f:
    data = f.readlines()
    print("words in files are: ")
    for line in data:
        word = line.split()
        print(word)

f.close()