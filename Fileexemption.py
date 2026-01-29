fileName = "myfile.txt"
 
f = None
try:
  f=open(fileName,"r")
  # manually open the fileName
  contents = f.read()
  print("The contents of the file ")
  print(contents)
except FileNotFoundError:
  print("The file ", fileName, " does not exist.")
finally:
  if f:
    f.close()
    print("file is closed")
   