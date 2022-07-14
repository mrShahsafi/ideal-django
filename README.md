# ideal-django
an ideal template for django project


## How It Works?

### Create a whole dj project:

```shell
➜  ideal-django git:(main) ✗ python3 main.py

enter your new Dj project directory:)
leave it blank if you wanna current directory
->
enter which dj version do you need
leave it blank if you wanna the last version
->
enter your new Dj project name
Oh!you can not ignore this one..
->samsamsami
crate at /Users/amirosein/Desktop/project/DjangoProjects/samsamsami
modular settings crated.
.gitignore crated.
other files crated.
finished.

```

- and there you go!

### Create a new webapp to existing project:

```python

Python 3.9.13 (main, May 24 2022, 21:28:31) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.30.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from src.create import create_webapp

In [2]: create_webapp(mainapp_name="product",project_dir="/Users/amirosein/Desktop/project/DjangoProjects/samsamsami")
product created.


```

- Easy peasy right?


## You Can Edit With Modules You Wanna Add To WebApp

```shell
 src/configs/mainapp.py 
```
