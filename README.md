# doeSe
Este é um projeto de uma aplicação web que visa unir Instituições de Ensino da cidade de São José dos Campos com possíveis doadores e/ou contribuintes voluntários.

O desenvolvimento dessa plataforma é utilizado matéria Engenharia de Software da Universidade Federal de São Paulo.

## Primeiros Passos
### Pyenv
Para rodar este projeto, utilizaremos o python 3.10.2
Você pode instalar versões específicas de Python para cada projeto seu utilizando o Pyenv. [Aqui existe uma documentação em português do pyenv](https://dev.to/womakerscode/instalando-o-python-com-o-pyenv-2dc7)

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
