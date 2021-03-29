import sys
sys.path.insert(1, 'D:/Faculta/Inteligenta Artificiala/Proiect1/views')
sys.path.insert(1, 'D:/Faculta/Inteligenta Artificiala/Proiect1/models')
sys.path.insert(1, 'D:/Faculta/Inteligenta Artificiala/Proiect1/controllers')

from controllerMain import controllerMain

controllerMain = controllerMain()
controllerMain.main()