from thefuzz import fuzz, process
import re

originalAdd = "#1991, Datta Nagar, Koregaon Bhima, Pune, 412216" # doc address
manualAdd = "1991, Data Nagar, Koregaonn Bhimaa, Pune, 412216" # manual address

print(originalAdd)
print(manualAdd)

#function for extract house no , pincode
def numnerList(address):
    str4 = re.findall(r'\d+', address) # extract numbers from addresses
    res = list(map(int, str4)) #convert string into integer and then map to make a list
    return res #it will return [house no , pincode , any other number...]

listOfNumbers1 = numnerList(originalAdd)  # it will atore the results for str1
#print(listOfNumbers1) 
listOfNumbers2 = numnerList(manualAdd) # it will atore the results for str1
#print(listOfNumbers2)

# Extract words from string
def wordExtract(word):
    word1 = re.findall(r'[a-zA-Z]+', word) # extract word from string 
    return word1


listOfWords1 = wordExtract(originalAdd) # list of words for original address
#print(listOfWords1)
listOfWords2 = wordExtract(manualAdd) # list of words for manual address
#print(listOfWords2)

#converting list of word into string  
originalAddText = " ".join(map(str, listOfWords1))
#print(originalAddText)
manualAddText = " ".join(map(str, listOfWords2))
#print(manualAddText)


# compare digit lists house no, pincode
# if listOfNumbers1 != listOfNumbers2:
#     print("house no and pincode matched")
# else:
#     print("house no and pincode not matched")

# it will return ratio by comparing only addresses string
match = fuzz.ratio(originalAddText, manualAddText)

#check the approvable
# if match>=90 and listOfNumbers1[0] == listOfNumbers2[0]:
#     print("Loan approved")
# else:
#     print("Please write correct address")




# compare digit lists house no, pincode
if listOfNumbers1 == listOfNumbers2:
    print("house number amd pin code matched")
    if listOfNumbers1[0] == listOfNumbers2[0] and listOfNumbers2[-1] == listOfNumbers2[-1]:
         if match>=90:
            print("document matched with property address")
         else:
            print("")      
   
else:    
    if listOfNumbers1[0] != listOfNumbers2[0]:
        print("house number not matched")
        print("------------------")
    if listOfNumbers1[-1] != listOfNumbers2[-1]:
        print("pin code not matched")
        print("------------------")
    



    