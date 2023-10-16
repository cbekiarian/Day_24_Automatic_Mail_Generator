#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names_.txt","r") as file:
    for name in file.readlines():
        name = name.strip()
        with open("./Input/Letters/starting_letter",mode = "r") as letter:
            text = letter.read()
            new_text = text.replace( "[name]", name)

            with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as new_letter:
                new_letter.write(new_text)
