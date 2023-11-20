'''步骤 1
file_name = "example.txt"
try:
    file_name = "example.txt"
    with open(file_name, "r") as file:
        for line in file:
            line = line.rstrip()
            print(line)
第一段代码：
打开名为 'example.txt' 的文件以供读取。
同样使用 with 语句来确保文件在结束时被正确关闭。
在迭代文件的每一行之前，使用 rstrip() 来去除每行末尾的换行符。
输出每一行的内容。

第二段代码：
打开名为 'fichier.txt' 的文件以供读取。
使用 with 语句来确保文件在结束时被正确关闭。
在迭代文件的每一行之前，使用 rstrip("\n\r") 来去除每行末尾的换行符和回车符。
输出每一行的内容。
'''
file_name = "example.txt"
try:
    file_name = "example.txt"
    with open(file_name, "r") as f:
        for l in f:
            l = l.rstrip("\n\r")
            print(l)
except FileNotFoundError:
    print("Erreur : Le fichier spécifié n'a pas été trouvé.")
except IOError:
    print("Erreur : Une erreur d'entrée/sortie s'est produite lors de la lecture du fichier.")
except FileExistsError:
    print("Erreur : Le fichier que vous essayez de créer existe déjà.")
except PermissionError:
    print("Erreur : Vous n'avez pas la permission d'accéder au fichier.")
finally:
    print("C'est la fin du programme.")

