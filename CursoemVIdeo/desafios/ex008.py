# COnversão de metros para centimetros e milimetros
m = float(input('Digite o valor em metros: '))
cm = m * 100
mm = cm * 100
print(f' {m}m é equivalente a:')
print(f' {m/1000}km | {m/100}hm | {m/10}dam |', end='')
print(f' {m*10:.0f}dm | {cm:.0f}cm | {mm:.0f}mm')
