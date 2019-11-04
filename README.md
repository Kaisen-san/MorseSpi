# MorseSpi

> Desenvolvido para PAE **CM2004 - Internet das Coisas usando o Hardware Embarcado Raspberry PI**

O projeto MorseSpi visa criar uma interface de comunicação entre agentes de missões especiais. Na aplicação, um dos agentes (o supervisor), além de ter acesso a câmera presa ao equipamento do agente portador, pode enviar uma mensagem ao mesmo por meio de uma interface web. Tal mensagem será traduzida para código morse e executada no equipamento do agente portador por meio do LED e do buzzer embutidos no hardware.

Para que possam se comunicar, é necessário que ambos os agentes estejam conectados à internet. Com isso, o agente supervisor poderá ajudar a manter o agente portador informado sobre o andamento/perigos da missão.

*Em palavras menos fictícias...*

Na página web, uma caixa de texto possibilita ao usuário inserir uma mensagem e enviá-la ao Raspberry Pi. A mensagem pode conter qualquer letra e número contemplados pelo Código Morse Internacional. Além disso, a página web também apresenta um stream ao vivo da câmera do Raspberry Pi para monitoração. Ao enviar a mensagem, o Raspberry Pi irá reproduzi-la por meio de som (buzzer tocando/pausando) e luz (LED ligando/desligando), de acordo com a tradução para Código Morse, respeitando os intervalos padrões entre letras e palavras.

Lembrando que, é preciso conectar-se a internet para habilitar a comunicação entre a página web e o Raspberry Pi, uma vez que ambos conectam-se ao servidor MQTT test.mosquitto.org.

## Materiais Utilizados
- Raspberry Pi 3B
- PiCamera
- LED Vermelho
- Buzzer
- Resistor 1kΩ
- Resistor 330Ω

## Instruções
> TODO

## Integrantes

Nome | RA | GitHub
------------ | ------------- | -------------
Felipe Andrade | 15.00175-0 | Kaisen-san
Vinícius Pereira | 16.03343-4 | VinPer
