# Tendo por base o arquivo de logs de um servidor, o programa que responde às seguintes questões:
# Quantos IPs distintos se conectaram ao servidor?
# Qual o IP que mais vezes conectou ao servidor?
# Em que minuto houve mais conexões ao servidor?

# arquivo = open('apache_logs.txt', 'r')
arquivo = open('apache_logs.txt', 'r')

linhas = arquivo.readlines()
listaDeIps= set()

for line in linhas:
    linhaDividida = line.split(" ", 1)[0]
    listaDeIps.add(linhaDividida)

print(f"IPs Distintos: {len(listaDeIps)}")









