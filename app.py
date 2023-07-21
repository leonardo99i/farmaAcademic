import tkinter as tk
import pandoc

# Defina as regras de formatação
formatacao = {
    'fonte': 'Times New Roman',
    'tamanho_fonte': 12,
    'espacamento_linhas': 1.5,
    'margens': {'superior': 3, 'esquerda': 3, 'inferior': 3, 'direita': 3},
    'cabecalho': 1,
    'rodape': 1,
    'numero_paginas': True,
}

# Crie a janela principal
janela = tk.Tk()

# Crie uma caixa de texto para entrada
entrada = tk.Text(janela)
entrada.pack()

# Crie uma caixa de seleção para a fonte
fontes = ['Times New Roman', 'Arial', 'Calibri']
fonte_selecionada = tk.StringVar(janela)
fonte_selecionada.set(fontes[0])
fonte_selecao = tk.OptionMenu(janela, fonte_selecionada, *fontes)
fonte_selecao.pack()

# Crie uma caixa de seleção para o tamanho da fonte
tamanhos_fonte = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
tamanho_fonte_selecionado = tk.IntVar(janela)
tamanho_fonte_selecionado.set(tamanhos_fonte[0])
tamanho_fonte_selecao = tk.OptionMenu(janela, tamanho_fonte_selecionado, *tamanhos_fonte)
tamanho_fonte_selecao.pack()

# Crie um botão para formatar o texto
def formatar_texto():
    # Obtenha o texto da caixa de entrada
    texto = entrada.get(1.0, 'end')

    # Defina a fonte e o tamanho da fonte
    formatacao['fonte'] = fonte_selecionada.get()
    formatacao['tamanho_fonte'] = tamanho_fonte_selecionado.get()

    # Formate o texto em ABNT
    texto_formatado = pandoc.convert(texto, format=formatacao)

    # Coloque o texto formatado na caixa de saída
    saida.delete(1.0, 'end')
    saida.insert(1.0, texto_formatado)

botao_formatar = tk.Button(janela, text='Formatar', command=formatar_texto)
botao_formatar.pack()

# Crie uma caixa de texto para saída
saida = tk.Text(janela)
saida.pack()

# Inicialize a janela
janela.mainloop()
