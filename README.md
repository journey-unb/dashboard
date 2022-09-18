# Dashboard - APC

Este repositório contém o código do Projeto Final da matéria Algoritmo e Programação de Computadores.

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

3. Execute o arquivo principal para iniciar o servidor do dashboard:
```sh
$ python main.py
```
4. Abra o navegador e entre neste website: [`http://127.0.0.1:8050`](http://127.0.0.1:8050).

## Autores

Este projeto foi idealizado pelos professores:
- Nilton Correia da Silva
- Fabricio Ataídes Braz

E desenvolvido pelos alunos:
- Bruno Ricardo de Menezes
- Caio Alexandre Ornelas SIlva 
- Caio Felipe Rocha Rodrigues
- Gabriel Henrique Castelo Costa
- Gabriel Moura dos Santos
- Gabriel Sant Ana Murari
- Gabriella Reinert Tosta
- Jefferson Marques dos Santos
- Vinícius Borba Camacho Nonato
- Vítor Gonçalves de Andrade Silva

## Licença

Este projeto está protegido sob a licença MIT:

```
MIT License

Copyright (c) 2022 UnB

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
