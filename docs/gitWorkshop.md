# Taller de git
El siguiente documento es un transcripto del taller de git dictado para el equipo de IT SABF 2020

### Definimos aliases
https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases

### inicializamos un repositorio
git init

### Queremos tener nuestro repositorio en un servidor remoto, por esto agregamos un remoto para poder pushear al mismo, en este caso utilizamos el protocolo SSH
git remote add origin git@github.com:frandelgado/git-workshop2.git

# Vamos a crear un commit inicial para poder subir algo al remoto que acabamos de agregar
touch README.md
git commit 'Add README'

### Finalmente, subimos o "pusheamos" nuestra rama actual en local al servidor remoto que elijamos
git push --set-upstream origin master 
### De ahora en mas cuando hagamos un push desde esta branch por defecto siempre se hace el push al remoto origin

### creamos la branch development para mantener la version de codigo de desarrollo
git checkout -b 'development'

### Nos paramos sobre la banch de desarollo
git checkout development

### Ahora que trenemos nuestras ramas de desarollo y de produccion queremos desarrollar una nueva funcionalidad.
### Empezamos creando nuestra branch para la feature.
git checkout -b 'add-models-to-admin'

### Codeamos nuestra feature, commiteamos con un grado razonable de granularidad. 
git commit -m 'Add RecurringExpense and Expense models to django admin'

### Pusheamos nuestra nueva branch con la feature que queremos agregar.
git push -u origin add-models-to-admin

### Agregamos una view y la commiteamos.
git commit -m 'Add UserView'

### Nos damos cuenta de que este commit no va, entonces tenemos que sacarlo
#### vemos el hash del commit para despues hacer un cherry-pick 
git log

#### Hacemos el cherry-pick en una nueva branch
git co development
git co -b 'add-user-view'
git cherry-pick {}
git push -u origin add-user-view

### Una vez que ya esta aprobada la feature branch add-models-to-admin
desde github resolvemos el PR

### Ahora tenemos el PR con add-user-view
#### debemos rebasear ya que el primer commit de add-user view no apunta al ultimo commit de development
git rebase -i origin master

