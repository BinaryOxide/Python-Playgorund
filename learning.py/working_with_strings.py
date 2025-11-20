# string concatenation...here's an example,
subject = "coffee"
print("I really like to drink "+ subject)

# we can also store them...here's an example,
concatenation_ = "I really like to drink " + subject
print(concatenation_)

#---------------------------------------------------</>

 #string that we'll use for some common operation
text = "God bless you all"
print("common text = ",text)


# convert a string to lowercase 
print(text.lower())

# convert a string to upper case 
print(text.upper())

# check the case isupper or islower
print(text," = ",text.upper().isupper()) #output: true
print(text," = ",text.lower().isupper()) #output: false

# find out the length of a string 
print("length = ",len(text))

# search in index
print("text.index('d')=",text.index("d"))
print("text.index('bless')=",text.index("bless"))

# replace 
print(text.replace("bless","help"))
