# projeto-mundo-senai

### Resumo do projeto

Este projeto consiste em um jogo da velha com algumas regras diferentes, ele é desenvolvido em python utilizando a biblioteca pygame.
O jogo será implementado no Raspberry PI 3B+ com um display touch screen no nosso projeto original.

### Como utilizá-lo

Baixe o arquivo main.py e a versão mais recente do [python 3.0](https://www.python.org/downloads/).<br>
Após isso, execute o seguinte comando no terminal:

Windows: <br>
<code>pip install pygame</code>

Linux: <br>
<code> sudo apt update <br>
sudo apt install python3 python3-pip <br>
pip3 install pygame </code>

Por fim, execute o código em alguma IDE, de preferência no [Visual Studio Code](https://code.visualstudio.com/).

### Regras
O jogo funciona da mesma forma que o jogo da velha clássico, suas diferenças são:
- Não tem empate
- Só podem ter 3 símbolos no tabuleiro (X e O) para cada jogador <br>
Quando são completas as 3 jogadas, a última jogada que o jogador realizou muda de posição para onde uma nova for feita.

