# hongOS

hongOS es un proyecto de fin de grado desarrollado por el alumno del grado de Ingeniería del Software de la Universidad de Sevilla Pablo Santos Ortiz. Es una aplicación desarrollada en django capaz de clasificar distintos tipos de hongos silvestres gracias a un modelo de redes neuronales.

### Instalación y ejecución

Para correr la aplicación es necesario tener instalado python 3 (preferiblemente python 3.10), y pip, el instalador de paquetes de python. Lo siguiente es clonar el repositorio y ejecutar el siguiente comando en la raíz del repositorio:

`pip install -r requirements.txt`

Seguidamente accedemos a la carpeta del proyecto (hongOS_project) donde se encuentra el fichero manage.py y ejecutamos los siguientes comandos:

`python3 manage.py makemigrations`

`python3 manage.py migrate`

`python3 manage.py runserver`

