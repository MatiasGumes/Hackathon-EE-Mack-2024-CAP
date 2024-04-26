# fazemos a criptografia da pasta como uma forma de segurança é realizado o acesso à pasta do computador por meio do caminho a essa pasta em seguida é feita a verificação se se trata de uma foto ou uma pessoa real na webcam ao pressionar a tecla "esc", a webcam é deligada e é realizada a captura do último frame (salva no computador) em seguida é realizado o reconhecimento se no passo anterior, foi identificado que é uma foto, o sistema é barrado, aparecendo a mensagem "NÃO É POSSIVELNÃO É POSSÍVEL REALIZAR O RECONHECIMENTO" se for identificado um rosto real, segue para a autenticação, como mostrado nas imagens.

Instruções:
  Deve-se ter instaladas todas as bibliotecas necessárias. Note que a pasta do diretório das imagens que compõem o banco de dados é uma pasta independente local, de modo que deve-se alterar o caminho para essa pasta no código, visto que cada máquina pode ter um caminho diferente para essa pasta.
  O código deve ser divido em células, de modo a ficar dividido nas seguintes células:
- criptografia da pasta (início em "#criptografia da pasta" e fim em " descriptografar_pasta(caminho_pasta, chave)")
- acesso à pasta (início em "#acessar a pasta" e fim em "print(file)")
- realizar a verificação rosto real x foto e captura de frame (início "#diferenciação rosto foto x rosto real + captura de rosto real" e fim em "cv2.destroyAllWindows()")
- reconhecimento facial (início em "#reconhecimento facial (comparação da captura de rosto real com banco de dados)" e fim em "print("ROSTO NÃO IDENTIFICADO")")

  Cada célula deve ser rodada manualmente (executando o "run" da célula). Atenção para: ao pressionar o esc (no momento de fechar a webcam), em seguida é necessário interromper o kernel (interromper a célula manualmente) para poder rodar a próxima célula.
