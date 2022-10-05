# doeSe
Este é um projeto de uma aplicação web que visa unir Instituições de Ensino da cidade de São José dos Campos com possíveis doadores e/ou contribuintes voluntários.

O desenvolvimento dessa plataforma é utilizado matéria Engenharia de Software da Universidade Federal de São Paulo.

# Primeiros Passos

### Django + Vue
Como molde deste projeto, utilizaremos o boilerplate conhecido como "Djavue2". No entanto, seu projeto já está datado e com versões antigas de algumas libraries. Por conta disso, utilizaremos um [fork que pode ser encontrado aqui](https://github.com/huogerac/djavue). Para subir este template, execute os seguintes comandos:

```bash
# Digite o comando abaixo caso ainda não tenha o comando vue
$ npm install -g @vue/cli

$ vue init huogerac/djavue doese  # vue init evolutio/djavue doese
$ cd doese
# Para criar os containers docker
$ docker-compose build
# Para iniciar os containers docker
$ docker-compose up -d
```

## Virtual environment
Uma alternativa ao Docker é utilizar o ambiente virtual. Use o pyenv para gerenciar as versões de Python e seus virtualenvs. Para instalar ele, use o pyenv-installer.
Você pode instalar versões específicas de Python para cada projeto seu utilizando o Pyenv. [Aqui existe uma documentação em português do pyenv](https://dev.to/womakerscode/instalando-o-python-com-o-pyenv-2dc7)

```bash
$ curl https://pyenv.run | bash
```

Reinicie o terminal e você já deve conseguir usar o pyenv.

### Instale uma versão do 3.10.x.
```bash
pyenv install 3.10.2
```

### Crie um virtualenv doese com a versão que você acabou de instalar.
```bash
pyenv virtualenv 3.10.2 doese
```

