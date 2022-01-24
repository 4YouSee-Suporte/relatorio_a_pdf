<h2 align="center">
Script em Python para Geração de Relatório em PDF 💬🟩 <br>
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/4YouSee-Suporte/4yousee-sensors?style=social">
    <img alt="GitHub followers" src="https://img.shields.io/github/followers/4YouSee-Suporte?label=Follow%20me%20%3A%29&style=social">
</h2>


## ⚈ Acerca do Programa
Esse programa tem como intuito gerar um relatório em pdf a partir da leitura de arquivos .csv como os exemplos indicados nos arquivos [cliente_1.csv](https://github.com/4YouSee-Suporte/relatorio_a_pdf/blob/main/data_report_001/cliente_1.csv), [cliente_2.csv](https://github.com/4YouSee-Suporte/relatorio_a_pdf/blob/main/data_report_001/cliente_2.csv), e [cliente_3.csv](https://github.com/4YouSee-Suporte/relatorio_a_pdf/blob/main/data_report_001/cliente_3.csv). Esses arquivos foram gerados no 4yousee manager como relatórios detalhados, considerando que cada um é um relatório de uma conta, ou de um cliente.

Para mais informações, ler a documentação [Como extrair um relatório de Auditoria de Veiculação dos meus players? (Relatório detalhado)
](https://suporte.4yousee.com.br/kb/article/116548/)

A seguinte imagem apresenta um exemplo de como é o relatório, seu cover e uma das páginas com os dados dos playlogs por data.

![exemplo relatório](https://user-images.githubusercontent.com/63620799/150869768-5295cd36-495f-4a3e-a431-231b72c6a1f6.jpg)


## ⚈ Requisitos
- Baixar os arquivos em .csv referente aos clientes/contas que deseja. Deve ter ao menos um. O recomendável é selecionar nesse relatório detalhado os conteúdos e players que você espera considerar no relatório final, além de selecionar o intervalo de datas.

- Substituir os arquivos :
    - [logo.png](https://github.com/4YouSee-Suporte/relatorio_a_pdf/blob/main/img/logo.png): Essa é a logo que aparece no header de cada página e no footer.
    - [logo_2](https://github.com/4YouSee-Suporte/relatorio_a_pdf/blob/main/img/logo_2.png): Essa é a logo que aparece no cover. 
    - [background_cover.png](https://github.com/4YouSee-Suporte/relatorio_a_pdf/blob/main/img/background_cover.png): Imagem do cover.
    
- Cria arquivo [data_report_001.py](https://github.com/4YouSee-Suporte/relatorio_a_pdf/blob/main/data_report_001/data_report_001.py) baseado nas seguintes orientações:
    ```data_report_001.py
    PASTA = 'data_report_001'  # Nome da Pasta onde se encontram os arquivos .csv e o próprio arquivo data_report_001.py
    NOME_EMPRESA = "Minha Empresa de Midia"  # Nome da empresa que emite o relatório
    NOME_FANTASIA = "FORÇA MIDIA"   # Nome de fantasia da empresa que emite o relatório
    CNPJ_EMPRESA = "XX.XXX.XXX/XXXX-XX "  # CNPJ da empresa que emite o relatório
    ENDERECO_EMPRESA = "Av. Alfonso Pena, 1500, Xº andar - \nCentro - Cidade/MG"  # Endereço da empresa que emite o relatório
    TELEFONE_EMPRESA = "+55 11 9 5987-2598"  # Telefone da empresa que emite o relatório
    CLIENTE = "NOME DO CLIENTE"  # O cliente usualmente é a agencia que solicitou o relatório
    DATA_INICIAL = "20-12-2021"  # Data inicial para considerar os playlogs dos conteúdos
    DATA_FINAL = "31-12-2021" # Data inicial para considerar os playlogs dos conteúdos
    # Se o relatório (.csv) vem com playlogs de datas fora da DATA_INICIAL e DATA_FINAL, não vai ser considerado pelo programa.
    CLIENTES = {'cliente_1': {  # nome do cliente, esse nome deve ser igual ao arquivo .csv
                              'conteudos': [571, 570],  # (Lista de inteiros) Conteúdos a serem considerados para o relatório. O programa soma o total de playlogs dos conteudos
                              'players': [   # (Lista de Dict) Cada dicionário corresponde a um player
                                          {'id': 3, 'endereco': 'Endereço do Player', 'insercoes': 700},   # id do conteúdo no 4yousee manager,
                                          {'id': 7, 'endereco': 'Endereço do Player', 'insercoes': 700},   # endereço do player (localização)
                                          {'id': 8, 'endereco': 'Endereço do Player', 'insercoes': 700},   # e inserções, ou seja, quanto é o esperado 
                                          {'id': 16, 'endereco': 'Endereço do Player', 'insercoes': 700},  # no período de tempo para esse player.
                                          {'id': 17, 'endereco': 'Endereço do Player', 'insercoes': 700}   
                                        ],
                            }
                }
    ```

## ⚈ Como é o fluxo de funcionamento do 4YouSee Sensors

Assim que existir os arquivos indicados nos requisitos, e instalar as librarias através do comando `python -m pip install -r requirements.txt`, você pode executar o programa `main.py` e o resultado, o pdf irá ser gerado na pasta `data_report_001`.

Em caso você queira gerar outro pdf com outros dados, com outros clientes e informações distintas ao relatório 001, você pode criar uma pasta `data_report_002` com o arquivo `data_report_002.py` dentro de aquela pasta. Logo, será necessário mudar a linha [235](https://github.com/4YouSee-Suporte/relatorio_a_pdf/blob/main/main.py#L235) do main.py, para que aponte para a nova pasta.
