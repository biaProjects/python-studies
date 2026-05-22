> Conteúdo aprendido durante aulas da Univesp

# GUI
Graphical User Interface (GUI) proporcionam elementos visuais como ícones, janelas, menus e ponteiros.  

Uma das interfaces disponíveis para isso em Pyhton é `Tkinter`.  

Vamos colocar a mão na massa e entender na prática!

Podemos criar nosso [primeiro código](1 - code.py), abrindo uma janela vazia, ainda sem nenhumma funcionalidade.

Depois, vamos criar o [segundo código](), uma janela com um texto.  

Agora, em nosso [terceiro exemplo](), teremos uma janela que possui uma imagem.  

A posição de componentes é gerenciada pelo geometry manager da tkinter com base em diretivas definidas pelo programador, para isso, o método `pack()` é uma forma de fornecer essas orientações para o sistema.  
Podemos ver um exemplo disso em nosso [quarto exemplo]()

No [quinto exemplo]() vemos uma janela que possue vários "widgets", formando como um teclado.


# 


Agora vamos incluir funcionalidades.  

utilizaremos a abordagem de programação orientada a eventos

quando a interface é iniciada com a função mainloop(), inicia-se um loop de evento
a tela aguarda até que um evento ocorra

eventos possiveis: clicar, movimentar o mouse, pressionar uma tecla, etc


vamos para o exemplo de criar uma janela com um botão que, quando clicado, exibe a data e a hora na tela

o segundo será uma caixa de inserção de texto. o o usuário colocará uma data e o sistema retornará o dia da semana que aquela data ocorreu

nosso terceiro código será uma caixa de texto com diferentes eventos
o usuario digita caracteres, eles serão exibidos e se clicar no botão direto, esquerdo, aparecerá uma mensagem relacionada
para isso, vamos usar o componente widget Text, que funciona como um editor de texto
vamos usar também o método bind() para assoociar diferentes eventos as respectivas funções de tratamento
s padrões de evento tem o formato:
<modificador-modificador-tipo-detalhe>

anotar minuto 20 exemplos de eventos