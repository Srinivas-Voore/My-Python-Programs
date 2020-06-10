from pathlib import Path

#Absolute path
#for windows like in my pc it's =>C:\Users\srinivas\AppData\Local\Programs\Python\Python37-32
#Relative path
#a directory that we created

path=Path("Android222")
print(path.mkdir())

path=Path("Android222")
print(path.exists())

path=Path("Android222")
print(path.rmdir())

path=Path("Android222")
print(path.exists())

path=Path()
for file in path.glob('*.py'):
    print(file)
    
