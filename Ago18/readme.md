Actividades:

1.- En esta clase revisaremos la forma de accesar a la terminal de trabajo en linux/MAC(OS) y Windows,
y verificaremos que ya esté instalado el editor (Visual Studio Code), así como el compilador de C, y git. 

2.- Haremos la creación del repositorio local de Github y veremos como lo estaremos usando durante el curso. 

  - Crea una copia de tu repositorio en tu maquina local:
  
  - Desde la terminal de linux, o bien la terminal en visual studio code, clona tu repositorio:
  
      ``` 
      cd Documentos/cursos/
      git clone https://github.com/DCIPB/pb2021_main-usuario.git
      ```
  - Para actualizar tu repositorio e incluir los cambios que has realizado en el repositorio en linea usa la instrucción 

      `git pull`
  
  - Para actualizar tu repositorio e incluir los cambios que YO he realizado en mi repositorio báse usa la instrucción 

      `git pull https://github.com/alxogm/PB2021 --allow-unrelated-histories`
  
  - Realiza un cambio en tu repositorio local. Para inicar crea una rama de trabajo: 
  
     `git checkout -b nombre_rama`
   Veras un mensaje que te indica que ya estás trabajando en una rama diferente a la rama principal. 
   Ahora puedes realizar cambios, por ejemplo  crea de nuevo tu primer programa "hello.c" en la carpeta Ago18, 
   añadiendole comentarios. 
  
  - Crea un registro de los cambios en el repositorio local con las instrucciones
    
    `git add Ago18/hello.c`
    
    `git commit `  (En este paso requeriras añadir un comentario que indique el cambio que estás realizando)
  
  - Puedes hacer mas cambios, y repetir los pasos anteriores, por ejemplo crear otros archivos o modificar el ya creado, etc, etc.
  
  - Finalmente, actualiza tu repositorio en linea con los cambios que hiciste localmente con la instrucción
    
    `git push`
    
  - Puedes repetir el proceso anterior todas las veces que necesites, una vez que estés listo para incorporar los cambios a la rama principal
  deberás crear el "pull request" desde el repositorio en linea. Una vez yo, o un ayudante, lo haya aceptado, podrás cerrarlo, y borrar la rama.
  
En tu repositorio local podrás moverte entre la rama principal o cualquier otra rama con la instrucción 

  ` git checkout master (o el nombre de la rama)` # recuerda hacer `git pull` siempre antes de modificar la rama principal, para que tengas la versión actualizada. 
 
La instrucción `git status`te permite revisar el estado de tu repositorio en cualquier momento, por ejemplo puedes ver si tu 
repositorio local tiene actualizaciones que no se encuentran en el repositorio en linea.
  
3.- Asegurate de practicar los comandos básicos de git, ya que los estarás usando todo el curso: 
   
   ``` 
   git status
   git pull
   git pull https://github.com/alxogm/PB2021 
   git add lista_nombre_de_archivos
   git commit
   git push
   
   ```
   
   Otras [instrucciones de git](https://training.github.com/downloads/es_ES/github-git-cheat-sheet.pdf) mas avanzadas las iremos viendo durante el curso, según vayan apareciendo. 
