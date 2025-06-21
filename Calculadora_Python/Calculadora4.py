import tkinter as tk

historico = [] # Lista para armazenar o histórico de operações

#def pra pegar os valores dos campos de entrada e tratar erros
def pegar_valores():
    try:
        num1 = float(num1_entry.get().strip())
        num2 = float(num2_entry.get().strip())
        return num1, num2
    except ValueError:
        resultado_label.config(text="Erro: Digite números válidos!")
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

    # Adiciona a operação ao histórico
    historico.append(f"{num1} {operador} {num2} = {resultado}")

#def mostrar historico
def mostrar_historico():
    janela_historico = tk.Toplevel(janela)
    janela_historico.title("Histórico de Operações")
    janela_historico.geometry("300x200")
    janela_historico.configure(bg="#f0f8ff")

    texto = "\n".join(historico) if historico else "Nenhuma operação realizada ainda."

    historico_label = tk.Label(janela_historico, text="Histórico:", font=("Arial", 12, "bold"), bg="#f0f0f0")
    historico_label.pack(pady=10)

    texto_box = tk.Text(janela_historico, width=40, height=10)
    texto_box.pack(padx=10, pady=5)
    texto_box.insert(tk.END, texto)
    texto_box.config(state='disabled')  # Deixa a caixa só leitura

def limpar():
    num1_entry.delete(0, tk.END)
    num2_entry.delete(0, tk.END)
    operacao_label.config(text="?")
    resultado_label.config(text="Resultado:", fg="black")

# Interface grafica
janela = tk.Tk()
janela.title("Calculadora Melhorada")
janela.geometry("550x300")
janela.configure(bg="#e0f7fa")

#Frame do num entry e resultado
entrada_frame = tk.Frame(janela, bg="#e0f7fa")
entrada_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=(10, 5), sticky="ew")

# Criando os Widgets
instrucoes_label = tk.Label(entrada_frame, text="Digite 2 números para calcular:", font=("Verdana", 12, "bold"), bg="#e0f7fa")
num1_entry = tk.Entry(entrada_frame, width=7, font=("Arial", 14))
num2_entry = tk.Entry(entrada_frame, width=7, font=("Arial", 14))
operacao_label = tk.Label(entrada_frame, text="?", font=("Arial", 16, "bold"), bg="#e0f7fa")
resultado_label = tk.Label(entrada_frame, text="Resultado:", font=("Arial", 12), bg="#ffffff", relief="sunken", width=25, anchor="w")
igual_label = tk.Label(entrada_frame, text="=", font=("Arial", 16, "bold"), bg="#e0f7fa")

# Layout do frame de entrada organizado
instrucoes_label.grid(row=0, column=0, columnspan=4, pady=(0, 10))
num1_entry.grid(row=1, column=0, padx=5)
operacao_label.grid(row=1, column=1, padx=5)
num2_entry.grid(row=1, column=2, padx=5)
resultado_label.grid(row=1, column=4, padx=5)
igual_label.grid(row=1, column=3, padx=5)

#frame para os botões de operações
op_btn_frame = tk.Frame(janela, bg="#e0f7fa")
op_btn_frame.grid(row=1, column=0, columnspan=4, pady=10)

# Dicionário para mapear os botões às operações
botoes = {
    "+": lambda: calcular("+"),
    "-": lambda: calcular("-"),
    "*": lambda: calcular("*"),
    "/": lambda: calcular("/")
}


# loop para criar os botões dinamicamente
for idx, (texto, comando) in enumerate(botoes.items()):
    btn = tk.Button(op_btn_frame, text=texto, width=5, font=("Arial", 12), bg="#d1e7dd", command=comando)
    btn.grid(row=0, column=idx, padx=5, pady=5)

#frame para os botões de limpar e histórico
ch_btn_frame = tk.Frame(janela, bg="#e0f7fa")
ch_btn_frame.grid(row=2, column=0, columnspan=4, pady=10)

# Botão para limpar os campos
btn_limpar = tk.Button(ch_btn_frame, text="Limpar", width=20, font=("Arial", 12), bg="#ffcccb", command=limpar)
btn_limpar.grid(row=0, column=0, padx=10)

# Botão para mostrar o histórico
btn_historico = tk.Button(ch_btn_frame, text="Ver Histórico", width=20, font=("Arial", 12), bg="#cce5ff", command=mostrar_historico)
btn_historico.grid(row=0, column=1, padx=10)

# Iniciando o loop da interface gráfica
janela.mainloop()
