def contar_letras_a(texto):
    # contando para verificar as letras 'a' e 'A'
    count_a = sum(1 for letra in texto if letra == 'a')
    count_A = sum(1 for letra in texto if letra == 'A')

    # mostrando a quantidade de cada letra
    if count_a > 0 or count_A > 0:
        print(f"A letra 'a' minúscula aparece {count_a} vezes.")
        print(f"A letra 'A' maiúscula aparece {count_A} vezes.")
    else:
        print("A letra 'a' não aparece na string.")

# solicitando ao usuário que insira uma string
string_usuario = input("Digite uma string para verificar a presença das letras 'a' e 'A': ")

# chamando a função para realizar a verificação
contar_letras_a(string_usuario)
