from conta import *
from datas import Data

conta = Conta(123, "Nico", 55.5, 1000.0)
conta2 = Conta(321, "Jose", 100.0, 5000.0)

conta3 = None

conta.saca(1200.0)
conta.saca(100.0)
print(conta.get_saldo())

d = Data(21,11,2007)
d.formatada()

Conta.codigo_banco()

# None é o null