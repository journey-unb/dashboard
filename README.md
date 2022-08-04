# Dashboard APC

## Instalação

1. Clone o projeto e entre na pasta do repositório:
```sh
$ git clone https://github.com/journey-unb/dashboard.git
$ cd dashboard
```
2. Faça a migração dos dados (CSV para SQL) utilizando o script
`data_migrator.py`:
```sh
$ python data_migrator.py
```
Esse script criará um banco de dados `data.db` (utilizando SQLite) que
conterá todas os dados necessários para gerar o dashboard.
