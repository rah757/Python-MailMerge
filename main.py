#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
start = open("./Input/Letters/starting_letter.txt","r")

names = open("./Input/Names/invited_names.txt","r")
    
for name in names.readlines():
    newName = name.strip("\n")

    with open(f"./Output/ReadyToSend/letter_for_{newName}.txt","w") as file:
        for line in start.readlines():
            newLine = line.replace("[name]", newName)  
            file.write(newLine)
        start.seek(0)
    