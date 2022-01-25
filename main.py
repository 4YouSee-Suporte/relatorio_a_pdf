import csv
from datetime import timedelta, datetime
from os import path
from fpdf import FPDF
import pandas as pd

class Personal(FPDF):
    def cover_page(self):
        """
        Primeira imagem do arquivo final. Ela possui a logo centralizada com uma cor de fondo definida.
        """
        self.image("img/background_cover.png", 0, 0, 220, 300)
        self.image("img/logo_2.png", 60, 100, 105)
        self.set_font("Helvetica", size=15)
        self.set_text_color(255, 255, 255)
        self.set_xy(70, 185)
        self.multi_cell(w=90, h=5, txt="RELATÓRIO DE AUDITAGEM", border=0, align="L")
        self.set_font("Helvetica", size=12)
        self.set_text_color(82, 86, 89)
        self.set_xy(80, 265)
        self.multi_cell(w=75, h=5, txt=NOME_EMPRESA, border=0, align="L")
        self.set_xy(82, 270)
        self.multi_cell(w=75, h=5, txt=CNPJ_EMPRESA, border=0, align="L")
        self.set_text_color(0)

    def header(self):
        """
        O header apresenta as informações da empresa que emite o relatório e vai em toads as páginas exceto no cover.
        :return: nada.
        """
        if self.page_no() != 1:
            # Rendering logo:
            self.image("img/logo.png", 14, 12, 50)
            # Setting font: helvetica bold 10
            self.set_font("helvetica", "B", 10)
            # Drawing a rectangle
            self.set_line_width(0.5)
            self.rect(x=9,  y=7, w=193, h=25, style="D")
            self.line(x1=70, y1=10, x2=70, y2=29)
            self.line(x1=150, y1=10, x2=150, y2=29)
            # Establishing new margins
            self.set_margins(left=2, top=0.5)
            # Moving cursor to the right:
            self.cell(71)
            # Printing text
            self.set_font(family='helvetica', style="B")
            self.cell(20, 25, "ENDEREÇO", border=0, align="C")
            self.cell(59)
            self.cell(20, 25, "TELEFONE", border=0, align="L")
            self.ln(6)
            self.set_font(family='helvetica', style="")
            self.set_xy(72, 16)
            self.multi_cell(0, 5, ENDERECO_EMPRESA)
            self.set_xy(152, 16)
            self.multi_cell(0, 5, TELEFONE_EMPRESA)
            # Performing a line break
            self.ln(20)

    def sub_header(self):
        """
        Informações carregadas dinámicamente por player/unidade a partir do modulo data_report_001.py
        Ex.: nome_player = "Cliente_1 Endereço do Player - Player 7" 
        :return: nada.
        """
        # INFORMAÇÕES DO PAINEL
        TOP_RECTANGLE_X = 12;TOP_RECTANGLE_Y = 43;TOP_RECTANGLE_W = 187;TOP_RECTANGLE_H = 26

        # QUADRO PRINCIPAL
        self.rect(x=TOP_RECTANGLE_X, y=TOP_RECTANGLE_Y, w=TOP_RECTANGLE_W, h=TOP_RECTANGLE_H, style="D")

        # PRIMEIRA LINHA VERTICAL
        self.line(x1=TOP_RECTANGLE_X + 80, y1=TOP_RECTANGLE_Y, x2=TOP_RECTANGLE_X + 80, y2=TOP_RECTANGLE_Y + TOP_RECTANGLE_H)

        self.set_font(family='helvetica', style="B")
        self.cell(12)
        self.cell(20, 10, f"PLAYER", 0)
        self.cell(59)
        self.cell(20, 10, f"CLIENTE", 0)
        # offset = self.x
        self.set_font(family='helvetica', style="")
        self.set_xy(TOP_RECTANGLE_X + 2, TOP_RECTANGLE_Y + 11)
        self.multi_cell(75, 5, txt=nome_player, border=0, align="L")

        self.set_xy(TOP_RECTANGLE_X + 81, TOP_RECTANGLE_Y + 11)
        self.multi_cell(67, 5, txt=CLIENTE, border=0, align="L")

        self.ln(14)

    def footer(self):
        if self.page_no() != 1:
            # Position cursor at 1.5 cm from bottom:
            self.set_y(-15)
            # Setting font: helvetica italic 8
            self.set_font("helvetica", "", 10)
            # Drawing line
            self.set_line_width(0.5)
            self.line(x1=9, y1=283, x2=202, y2=283)
            # Rendering logo:
            self.image("img/logo.png", 10, 285, 20)
            # Printing page number:
            self.cell(0, 10, f"Página {self.page_no()} de {{nb}}", 0, 0, "R")

    def colored_table(self, rows, col_widths=(30, 60, 35, 45)):
        """
        Criação das tabelas com os dados de reproduções e datas.
        :param rows: informação pronta para ser colocada na tabela
        :param col_widths:
        :return: nada
        """
        headings = ['Data', 'Reproduções']
        # Colors, line width and bold font:
        self.set_fill_color(38, 190, 67)
        self.set_text_color(0)
        # self.set_draw_color(255, 0, 0)
        # self.set_line_width(0.3)
        self.set_font(family='helvetica', style="B")
        # Center the table
        offset_table = 37
        self.cell(offset_table)
        for col_width, heading in zip(col_widths, headings):
            self.cell(col_width, 7, heading, 0, 0, "C", True)
        self.ln()
        # Color and font restoration:
        self.set_fill_color(240, 240, 240)
        self.set_text_color(0)
        self.set_font(family='helvetica')
        fill = False
        for row in rows:
            self.cell(offset_table)
            print(f"\t\t\t\t\t{row[0]} - {row[1]}")
            self.cell(col_widths[0], 8, row[0], 0, 0, "C", fill)
            self.cell(col_widths[1], 8, row[1], 0, 0, "C", fill)
            # self.cell(col_widths[2], 8, row[2], 0, 0, "C", fill)
            # self.cell(col_widths[3], 8, row[3], 0, 0, "C", fill)
            self.ln()
            fill = not fill
        self.cell(sum(col_widths), 0, "", 0)
        self.assinatura(TOP_RECTANGLE_Y=43)

    def assinatura(self, TOP_RECTANGLE_Y=0, TOP_RECTANGLE_X = 12):
        """
        Informação de assinatura que vai localizada após cada tabela.
        :param TOP_RECTANGLE_Y:
        :param TOP_RECTANGLE_X:
        :return: nada
        """
        TOP_ASSINATURA = TOP_RECTANGLE_Y + 185

        # Aqui é possível colocar uma assinatura mais um carimbo

        self.set_xy(TOP_RECTANGLE_X + 1, TOP_ASSINATURA)
        self.multi_cell(73, 5, txt="___________________________", border=0, align="L")

        self.set_xy(TOP_RECTANGLE_X + 1, TOP_ASSINATURA + 6)
        self.multi_cell(73, 5, txt=NOME_EMPRESA, border=0, align="L")

        self.set_xy(TOP_RECTANGLE_X + 1, TOP_ASSINATURA + 12)
        self.multi_cell(73, 5, txt=NOME_FANTASIA, border=0, align="L")

        self.set_xy(TOP_RECTANGLE_X + 1, TOP_ASSINATURA + 18)
        self.multi_cell(73, 5, txt=f"CNPJ: {CNPJ_EMPRESA}", border=0, align="L")


def load_data_from_csv(csv_filepath):
    """
    Carrega as informações do csv e devolve ela pronta para ser processada dentro do programa
    :param csv_filepath: rota do arquivo .csv
    :return: headings, rows
    """
    headings, rows = [], []
    with open(csv_filepath, encoding="utf8") as csv_file:
        for row in csv.reader(csv_file, delimiter=","):
            if not headings:  # extracting column names from first row:
                headings = row
            else:
                rows.append(row)
    return headings, rows


def load_data(csv_filepath):
    """
    Gera dataframe do csv, para melhor manipulação das informações.
    :param csv_filepath:
    :return:
    """
    df = pd.read_csv(csv_filepath, sep=';', encoding="ISO-8859-1")
    return df


def filter_data(df, cliente, id_player):
    """
    A partir das informações do dataframe, é realizada a filtragem para calcular as insercções por conteúdo.]
    A filtragem está dada pela contagem total de conteúdos em uma data, e um player.
    :param df: informação criada na função load_data
    :param cliente: informação vinda do modulo data_report_001.py
    :param id_player: informação vinda do modulo data_report_001.py
    :return: informação pronta para serem carregadas dentro do pdf.
    """
    rows = []
    start_date = datetime.strptime(DATA_INICIAL, '%d-%m-%Y')
    end_date = datetime.strptime(DATA_FINAL, '%d-%m-%Y')
    delta = timedelta(days=1)
    total = 0
    while start_date <= end_date:
        count_logs = 0
        for conteudo in CLIENTES[cliente]['conteudos']:
            new_df = df[(df['Data e Hora'].str[:10] == start_date.strftime("%d/%m/%Y")) & (df['ID do Conteúdo'] == conteudo) & (df['ID do Player'] == id_player)]
            count_logs += len(new_df)
        row = [start_date.strftime("%d/%m/%Y"), str(count_logs)]
        total += count_logs
        rows.append(row)
        start_date += delta
    print("\n{}, player {}: {:,} playlogs".format(cliente, id_player, total))
    return rows



def verify_files(folder):
    """
    Verifica a existência dos arquivos .csv antes de criar o pdf.
    :param folder:
    :return: True caso estejam os arquivos ou False caso não estejam
    """
    text = ''
    for cliente, recurso in CLIENTES.items():
        if not path.exists(f"{folder}/{cliente}.csv"):
            text += f"■ Não foi encontrado o arquivo {cliente}.csv na pasta /{folder}/\n"

    if text:
        print(f"\n{text}")
        return True
    else:
        return False


if __name__ == '__main__':
    from data_report_001.data_report_001 import *
    # TODO: Como verificar que player tenha enviado todos os playlogs?
    # TODO: Generar .csv vía API do 4yousee manager.
    # Antes de Executar, verifique:
    #       - Criar arquivo data_report_00n.py
    #       - Id de conteúdos rodando em cada player.
    #       - Baixar .csv por conta/cliente.

    if not verify_files(PASTA):
        # Instantiation of inherited class
        pdf = Personal()
        pdf.alias_nb_pages()

        # Cria página para cover
        pdf.add_page()

        # Cria conteúdo de portada
        pdf.cover_page()

        for cliente, recurso in CLIENTES.items():
            for i in recurso['players']:
                id_player = i['id']
                nome_player = f"{cliente.capitalize()} {i['endereco']} - Player {i['id']}"

                # Cria página
                pdf.add_page()

                # Coloca subheader na página
                pdf.sub_header()

                # Adiciona tabela com total playlogs
                df = load_data(f"{PASTA}/{cliente}.csv")
                data = filter_data(df, cliente, id_player)
                pdf.colored_table(data)


        pdf.output(f"{PASTA}/{PASTA}.pdf")
        if path.exists(f"{PASTA}/{PASTA}.pdf"):
            print(f"\nRelatório gerado com sucesso : {PASTA}/{PASTA}.pdf\n")
