Descrição do Projeto

    A Estação Inteligente de Ambiente é um sistema desenvolvido para o monitoramento e análise das condições climáticas de uma sala de aula, levando em conta temperatura, umidade, número de pessoas, luminosidade e a quantidade de máquinas.

    O objetivo do projeto é garantir o bem-estar das pessoas no local, além de manter a vida útil dos equipamentos e otimizar os gastos de energia, ajustando o ambiente de maneira inteligente e automatizada.

    A solução encontrada é utilizar sensores conectados a um Raspberry Pi, que é responsável por processar os valores recebidos pelos sensores e acionar os indicadores visuais (LEDs) para representar o estado térmico da sala.

=============================================================================================
Objetivos

    1 - Promover o conforto térmico de estudandes e professores;
    2 - Manter a saúde dos notebooks e computadores contra o superaquecimento
    3 - Monitorar a luminosidade e uso de energia;
    4 - Contribuir com a sustentabilidade e redução de gastos;
    5 - Fornecer dados confiáveis para tomadas de decisão sobre climatização;

=============================================================================================
Funcionamento Geral

    A estação coleta os dados de:

        Temperatura e umidade (sensor DHT22);
        Quantidade de pessoas (sensor PIR);
        Luminosidade (sensor LDR)
    
    Em seguida, com base nos valores, o sistema calcula:

        Temperatura ideal para as máquinas (21–24 °C);
        Temperatura ideal para as pessoas (22–25 °C);
        Temperatura ideal combinada (22–23 °C);

    Em seguida, aciona um LED indicador:

        LED	Significado
        🟥 Vermelho	Temperatura extrema — risco para pessoas ou máquinas
        🟨 Amarelo	Temperatura amena — aceitável, mas não ideal
        🟩 Verde	Temperatura ideal — ambiente equilibrado

    Essas informações permitem ajustes manuais do ar-condicionado conforme a real necessidade do ambiente.

=============================================================================================
Tecnologias Utilizadas

    Python (processamento no Raspberry Pi)
    GPIO (leitura dos sensores)
    Bibliotecas de IoT como Adafruit_DHT
    Hardware:
        Raspberry Pi 3/4    
        DHT22
        HC-SR501
        LDR + resistor
    LEDs

=============================================================================================
Por que esse projeto é útil?

    Este projeto contribui para:

        Economia de energia ao evitar refrigeração excessiva.
        Saúde e conforto dos presentes, mantendo clima ideal.
        Sustentabilidade, ao monitorar iluminação e clima.
        Maior vida útil dos equipamentos, evitando superaquecimento.
        Um ambiente inteligente garante melhor desempenho dos alunos e preserva recursos da instituição.