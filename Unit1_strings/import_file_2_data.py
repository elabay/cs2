### basic code to import a text file into a program

file = open("guido_vonRossum_speech.txt", "r")

data = file.read()
print(type(data))

