from typing import Literal

type Mode = Literal['r', 'w', 'a']


def openfile(File:str, mode:Mode) -> str:
    return f'reading {file} in "{mode}"'


print(openfile('gagan.txt', 'r'))  #with this it will make sure we are writing the valid mode from literal
print(openfile('gagan2.txt', 'f')) #like here you can see the red line without literal we cant see if we writing valid or not