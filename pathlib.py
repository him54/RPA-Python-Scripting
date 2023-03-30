from pathlib import Path
p1 = Path('files/hello1.txt')

# print(type(p1)) #<class 'pathlib.WindowsPath'>
#
#Important 
# print(p1.name) #hello1.txt   Give full file name
# print(p1.stem) #hello1  Give first portion
# print(p1.suffix)  #.txt   Give .portion 
#
# p2 = Path("files")
# print(list(p2.iterdir())) #[WindowsPath('files/hello1.txt'), WindowsPath('files/hello2.txt')]

#With Rename
p2 = Path("files")
for path in p2.iterdir():
    new_filename = "new-" + path.stem + path.suffix
    if path.is_file():
        newName = p2 / new_filename
        print(newName)
        path.rename(newName)   #files\new-hello1.txt
                               #files\new-hello2.txt



#Without renam
dir = Path("files")
for file in dir.iterdir():
    if file.is_file():
        new_name = dir / ("new " + file.stem + file.suffix)
        with file.open('rb') as f1, new_name.open('wb') as f2:
            f2.write(f1.read())
    file.unlink()
