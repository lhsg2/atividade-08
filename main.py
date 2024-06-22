money = float(input("quanto é ganhado por hora:"))
time = float(input("quantas horas trabalha por semana:"))
bruto = money*(time*4)
print(f"salario bruto:{bruto:.2f}")
ir = bruto*0.11
print(f"desconto de imposto de renda:{ir:.2f}")
inss = bruto*0.08
print(f"desconto de INSS:{inss:.2f}")
sind = bruto*0.05
print(f"desconto de sindicato:{sind:.2f}")
liquido = bruto-(ir+inss+sind)
print(f"salario liquido:{liquido:.2f}")