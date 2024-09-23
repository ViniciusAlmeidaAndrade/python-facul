aluno = input("Nome do aluno: ")
nota1 = float(input(f"nota 1 de {aluno}: "))
nota2 = float(input(f"Nota 2 de {aluno}: "))
resultado = (nota1 + nota2) / 2
if resultado >= 7:
    print(resultado, "APROVADO")
elif resultado >= 3 and resultado < 7:
    print(resultado, "RECUPERAÇÃO")
else:
    print(resultado, "REPROVADO")
