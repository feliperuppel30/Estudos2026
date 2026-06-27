velocidade = 61
local = 102

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

PASSOUVELOCIDADE = velocidade > RADAR_1
MULTADORADAR_1 = local >= (LOCAL_1 - RADAR_RANGE)\
    and local <= (LOCAL_1 + RADAR_RANGE)
PASSOURADAR_1 = local >= (LOCAL_1 - RADAR_RANGE)

if PASSOURADAR_1:
    print('voce passou no radar 1')

if PASSOUVELOCIDADE and MULTADORADAR_1:
    print('voce foi multado no radar 1 km 100')
else: print('Não há multas registradas')
