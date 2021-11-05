Asumiendo creaste un ambiente de conda siguiendo las instrucciones en . Cada vez que quieras utilizar python deberás activar dicho ambiente

Linux: 
```
  export $MINICONDA=PATH_TO_MINICONDA (Debes reemplazar $PATH_TO_MINICONDA por el directorio donde se instaló miniconda, eg. /Users/alma/miniconda3)
  source $MINICONDA/bin/activate
  conda activate "nombre_de_ambiente" 
```

  
Windows:
 ```
  abre Anaconda Prompt desde el menú de inicio (o acceso rápido)
  conda activate "nombre_de_ambiente"
 ```
  
En ambos casos, una vez activo el ambiente el nombre del mismo aparece al inicio de la linea de comandos. Al teclear `which python` verán
que indica la versión instalada en el directorio donde instalaron miniconda y el ambiente. 

Hay 3 formas básicas de usar python:
  1) Desde la línea de comandos, tecleando `python` + ENTER se abre una nueva línea de comandos que acepta instrucciones de python de forma interactiva. 
  2) Desde un cuaderno de Jupyter (lo que estaremos usando más en clase). Tecleando `jupyter lab`+ ENTER se abre una ventana nueva, como un explorador, con un cuaderno de trabajo que aceptará instrucciones de python de forma interactiva. 
  3) Usando un script de python. En este caso se debe crear primero un script con las instrucciones de python que posteriormente se ejecuta de la forma
 `python nombre_script.py` Ver por ejemplo el script proporcionado para la realización de los proyectos 1 y 2.
 
 

