import tkinter as tk

#Função para calcular o resultado com base no operador
def calcular(operador):
   
    operacao_label.config(text=operador)

    try:
        valor_num1 = float(num1_entry.get())
        valor_num2 = float(num2_entry.get())

        resultado = None # usamos o None para indicar que ainda não temos resultado
        
        # Verificamos qual operador foi escolhido e calculamos o resultado
        if operador == "+":
            resultado = valor_num1 + valor_num2
        elif operador == "-":
            resultado = valor_num1 - valor_num2
        elif operador == "*":
            resultado = valor_num1 * valor_num2
        elif operador == "/":
            if valor_num2 != 0:
                resultado = valor_num1 / valor_num2
            else:
                # Se for divisão por zero, atualiza o label e para a função
                resultado_label.config(text="Erro: Divisão por zero!")
                return 
            
        # printando o resultado no label
        if resultado is not None:
            resultado_label.config(text=f"Resultado: {resultado}")

    except ValueError:
        resultado_label.config(text="Erro: Digite números válidos!")

# Interface Gráfica
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("450x250")

# Criando os Widgets
txt_input = tk.Label(master=janela, text="Digite 2 números para calcular:", font=("Arial", 12))

# Entradas para os números
num1_entry = tk.Entry(master=janela, width=10, font=("Arial", 14))
num2_entry = tk.Entry(master=janela, width=10, font=("Arial", 14))

# Label para mostrar a operação selecionada e o resultado
operacao_label = tk.Label(master=janela, text="?", font=("Arial", 14))
resultado_label = tk.Label(master=janela, text="Resultado:", font=("Arial", 12))

# Botões chamando a função 'calcular' corretamente
btn_soma = tk.Button(janela, text="+", width=5, font=("Arial", 12), command=lambda: calcular('+'))
btn_subtracao = tk.Button(janela, text="-", width=5, font=("Arial", 12), command=lambda: calcular('-'))
btn_multiplicacao = tk.Button(janela, text="*", width=5, font=("Arial", 12), command=lambda: calcular('*'))
btn_divisao = tk.Button(janela, text="/", width=5, font=("Arial", 12), command=lambda: calcular('/'))

# Organizando os Widgets na tela
txt_input.grid(row=0, column=0, columnspan=3, padx=10, pady=(10,0))
num1_entry.grid(row=1, column=0, padx=10, pady=10)
operacao_label.grid(row=1, column=1)
num2_entry.grid(row=1, column=2, padx=10, pady=10)

resultado_label.grid(row=2, column=0, columnspan=3, pady=10)

# Botões de operações
btn_soma.grid(row=3, column=0, padx=5, pady=5)
btn_subtracao.grid(row=3, column=1, padx=5, pady=5)
btn_multiplicacao.grid(row=3, column=2, padx=5, pady=5)
btn_divisao.grid(row=4, column=0, columnspan=3, pady=5)

# Iniciando o loop da interface gráfica
janela.mainloop()