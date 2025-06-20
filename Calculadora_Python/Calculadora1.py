import tkinter as tk

#função Soma

def calcular_soma():
    try:
        valor_num1 = float(num1.get())
        valor_num2 = float(num2.get())
        resultado = valor_num1 + valor_num2
        operacao.config(text="+")
        txt_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        txt_resultado.config(text="Por favor, insira números válidos.")

#função subtracao

def calcular_subtracao():
    try:
        valor_num1 = float(num1.get())
        valor_num2 = float(num2.get())
        resultado = valor_num1 - valor_num2
        operacao.config(text="-")
        txt_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        txt_resultado.config(text="Por favor, insira números válidos.")

#criando a janela principal

janela = tk.Tk()
janela.title("Calculadora Mais e Menos")
janela.geometry("450x200")

#Criando os Widgets

txt_input = tk.Label(master=janela, text="Digite 2 Numeros abaixo para calcular:")

num1 = tk.Entry(master=janela, width=10)
num2 = tk.Entry(master=janela, width=10)

operacao = tk.Label(master=janela, text="")
txt_resultado = tk.Label(master=janela, text="")

btn_soma = tk.Button(master=janela, text="+", command=calcular_soma)
btn_subtracao = tk.Button(master=janela, text="-", command=calcular_subtracao)

#Organizando os Widgets -- usando o sistema de grid(linhas e colunas)
txt_input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
num1.grid(row=1, column=0, padx=10, pady=10)
num2.grid(row=1, column=2, padx=10, pady=10)

operacao.grid(row=1, column=1, padx=10, pady=10)
txt_resultado.grid(row=2, column=1, padx=10, pady=10)

#botões de soma e subtração
btn_soma.grid(row=3, column=0, padx=10, pady=10)
btn_subtracao.grid(row=3, column=1, padx=10, pady=10)

#criando o loop
janela.mainloop()
