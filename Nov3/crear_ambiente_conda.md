Suponiendo que has instalado miniconda, es recomendable crear un ambiente de trabajo. 

-Linux: 
```
  export $MINICONDA=PATH_TO_MINICONDA (Debes reemplazar $PATH_TO_MINICONDA por el directorio donde se instalo miniconda, eg. /Users/alma/miniconda3)
  source $MINICONDA/bin/activate
``` 
- Windows:
  - Desde el menu de windows selecciona `Anoconda Prompt`, con lo que se abrirá una terminal muy parecida a una terminal de linux donde ya está activo miniconda

En ambos casos una vez activado miniconda, la siguiente instrucción creará un ambiente llamado pb_2021 y tendrá las librerias `jupyterlab numpy matplotlib` ya instaladas. 

`conda create -n pb_2021 jupyterlab numpy matplotlib`

Una vez creado el ambiente este se activa con

`conda activate 'nombre_de_ambiente'`

y se desactiva con 

`conda deactivate`
