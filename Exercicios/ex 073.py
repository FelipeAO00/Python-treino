"""
Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da 
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.
"""
times = ("Palmeiras", "São Paulo", "Bahia", "Flamengo", "Coritiba", "Fluminense", 
         "Athletico-PR", "Corinthians", "Bragantino","Grêmio", "Mirassol", 
         "Chapecoense", "Atlético-MG", "Santos", "Vitória", "Botafogo", "Remo", 
         "Internacional", "Cruzeiro", "Vasco")

times_ordem = sorted(times, reverse=False) #sorted(times) resolveria 
print("-=" *40) 
print(f"Lista de times do Brasileirão\n{times}")
print("-=" *40)
print(f"Os ultimos times na tabela são respectivamente {times[-4:]}")
print("-=" *40)
print(f"A lista dos times em Ordem alfabetica é, {times_ordem}") #sorted(times) resolveria 
print("-=" *40)
print(f"A Chapecoense esta na {times.index("Chapecoense")} posição")
print("-=" *40)