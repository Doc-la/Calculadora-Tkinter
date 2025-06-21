import tkinter as tk

#def pra pegar os valores dos campos de entrada e tratar erros
def pegar_valores():
    try:
        num1 = float(num1_entry.get().strip())
        num2 = float(num2_entry.get().strip())
        return num1, num2
    except ValueError:
        resultado_label.config(text="Erro: Digite números válidos!", fg="red")
        return None, None

#def para calcular a operação com base no operador
def calcular(operador):
    num1, num2 = pegar_valores()
    if num1 is None or num2 is None:
        return

    # Dicionário para mapear operadores
    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Erro: Divisão por zero!"
    }

    #chama a função correspondente ao operador
    resultado = operacoes[operador](num1, num2)

    #atualiza o label de resultado
    resultado_label.config(text=f"{num1} {operador} {num2} = {resultado}")
    operacao_label.config(text=operador)

def limpar():
    num1_entry.delete(0, tk.END)
    num2_entry.delete(0, tk.END)
    operacao_label.config(text="?")
    resultado_label.config(text="Resultado:", fg="black")

# Interface grafica
janela = tk.Tk()
janela.title("Calculadora Melhorada")
janela.geometry("450x300")
janela.configure(bg="#e0f7fa")

# Criando os Widgets
instrucoes_label = tk.Label(janela, text="Digite 2 números para calcular:", font=("Verdana", 12, "bold"), bg="#e0f7fa")
num1_entry = tk.Entry(janela, width=7, font=("Arial", 14))
num2_entry = tk.Entry(janela, width=7, font=("Arial", 14))
operacao_label = tk.Label(janela, text="?", font=("Arial", 16, "bold"), bg="#e0f7fa")
resultado_label = tk.Label(janela, text="Resultado:", font=("Arial", 12), bg="#ffffff", relief="sunken", width=30, anchor="w")

# Dicionário para mapear os botões às operações
botoes = {
    "+": lambda: calcular("+"),
    "-": lambda: calcular("-"),
    "*": lambda: calcular("*"),
    "/": lambda: calcular("/")
}

# Layout organizado
instrucoes_label.grid(row=0, column=0, columnspan=4, padx=10, pady=(10, 5))
num1_entry.grid(row=1, column=0, padx=10, pady=10)
operacao_label.grid(row=1, column=1)
num2_entry.grid(row=1, column=2, padx=10, pady=10)

# loop para criar os botões dinamicamente
for idx, (texto, comando) in enumerate(botoes.items()):
    btn = tk.Button(janela, text=texto, width=5, font=("Arial", 12), bg="#d1e7dd", command=comando)
    btn.grid(row=2, column=idx, padx=5, pady=5)

# Resultado ocupando a linha inteira
resultado_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

# Botão para limpar os campos
btn_limpar = tk.Button(janela, text="Limpar", width=20, font=("Arial", 12), bg="#ffcccb", command=limpar)
btn_limpar.grid(row=4, column=0, columnspan=4, pady=10)

# Iniciando o loop da interface gráfica
janela.mainloop()
