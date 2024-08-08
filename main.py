import time
inicio = time.perf_counter()

arquivo = open('apache_logs.txt', 'r')
conjuntoDeLinhas = arquivo.readlines()
arquivo.close()
ips = set() 
listIps = []       
horasAndMinutos = []

for linha in conjuntoDeLinhas:
    ip = linha.split(" ", 1)[0]
    dataAndHora = linha.split()[3]

    ips.add(ip)
    listIps.append(ip)
    horasAndMinutos.append(dataAndHora[12:18])

ipComMaisConexoes = None
vezesEmQueIpSeRepetiu = 0

for i in listIps:
    ipRepeticoes = listIps.count(i)
    if ipRepeticoes > vezesEmQueIpSeRepetiu:
        vezesEmQueIpSeRepetiu = ipRepeticoes
        ipComMaisConexoes = i

# print (horasAndMinutos)
vezesEmQueAHoraSeRepetiu = 0
horaMaisAcessada = 0

for i in horasAndMinutos:
    repeticoesHoras = horasAndMinutos.count(i)  
    if repeticoesHoras > vezesEmQueAHoraSeRepetiu:
        vezesEmQueAHoraSeRepetiu = repeticoesHoras  
        horaMaisAcessada = i  
fim = time.perf_counter()
tempo_de_execucao = round(fim - inicio, 1)
print(f'\n>> Quantidade de IPs Distintos: {len(ips)} \n>> IP com Maior Número de Conexões: {ipComMaisConexoes} \n>> Minuto com Maior Quantidade de Conexões: {horaMaisAcessada[1:6]} ({vezesEmQueAHoraSeRepetiu} Conexões)')
print(f"\n     🕒 | TEMPO DE EXECUÇÃO DO CÓDIGO: {tempo_de_execucao}s \n")

# print(f"IPs Distintos: {len(Ips )}")
# print(date[0:10])
# print(horasAndMinutos)









