texto_simulado = "Exemplo de teclas digitadas ." with open("keylog_simulado.txt", "w") as f: for letra in texto_simulado: f.write(letra + "\n") print("Keylog simulado salvo em keylog_simulado.txt")
