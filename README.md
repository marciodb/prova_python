# provaautomacao
Estruturação de um projeto em Python utilizando o selenium.

Guia de instalação:

Baixe o projeto e descompacte
Abra o Pycharm
Arraste a pasta do projeto para dento da IDE
Identifique o caminho do projeto baixado

Agora com a IDE aberta, siga pelos diretórios: TestCase>ProvaTestCase e execute o teste através dessa classe.


*OBSERVE QUE OS OBJETOS SÃO MAPEADOS NAS CLASSES DO DIRETÓRIO "PAGEOBJECTS", SUAS AÇÕES E COMPORTAMENTOS SÃO EXECUTADOS NO "TASKS" 
E SUAS VALIDAÇÕES NO "VERIFICATIONPOINTS".


*OBSERVE QUE A CLASSE TESTCASE APENAS INSTANCIA E CHAMA AS AÇÕES DAS CLASSES TASKS PARA EXECUTAR O TESTE.

Qualquer problema, lembre-se de verificar se você instalou o unnitest, o selenium e o driver do navegador que está utilizando.

Esse projeto foi feito utilizando:

IDE: Pycharm Version 3.6
Python 3
Selenium
Unnitest

O desafio contempla:

Caso de teste: realizar uma compra com sucesso.
1.              Acessar o site: www.automationpractice.com.
2.              Escolha um produto qualquer na loja.
3.              Adicione o produto escolhido ao carrinho.
4.              Prossiga para o checkout.
5.              Valide se o produto foi corretamente adicionado ao carrinho e prossiga caso esteja tudo certo.
6.              Realize o cadastro do cliente preenchendo todos os campos obrigatórios dos formulários.
7.              Valide se o endereço está correto e prossiga.
8.              Aceite os termos de serviço e prossiga.
9.              Valide o valor total da compra.
10.             Selecione um método de pagamento e prossiga.
11.             Confirme a compra e valide se foi finalizada com sucesso.
