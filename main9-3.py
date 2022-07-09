from os import linesep
import readline
import googletrans
from jupyterlab_server import translator

translator = googletrans.Translator()
read_file_path = "영어파일.txt"

with open(read_file_path, 'r') as f:
    readlines = f.readlines()
    
for lines in readlines:
    result1 = translator.translate(lines,dest='ko')
    print(result1)
    print(result1.text)