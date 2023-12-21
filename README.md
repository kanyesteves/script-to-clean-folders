# Organizando pasta downloads do seu computador

Primeiro dia de férias, primeiro projetinho !!

## Problemática
Quem ai organiza a sua pasta de downloads? EMMMMM ? Comenta ai se sim.
Eu tenho certeza que não sou o único que sempre achou um saco ter que ficar organizando isso.

## Ideia/Solução
Pensando nisso, fiz um script em python para deixar rodando na minha crontab para sempre deixar minha pasta organizada. Resumindo, o script vai rodar a cada dia em um horário específico e irá fazer duas validações, são elas:

- Verificar se existe alguma pasta com nome do formato do arquivo, caso não tenha, é criada a pasta.
- Verificar se existe arquivos da pasta downloads com o formato da pasta criada, caso tenha, o arquivo é movido para pasta do formato correto do arquivo.

