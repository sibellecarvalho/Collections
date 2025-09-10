usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
assistiram

len(assistiram)

set(assistiram)

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

for usuario in set(assistiram):
    print(usuario)

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

usuarios_data_science | usuarios_machine_learning

usuarios_data_science & usuarios_machine_learning

usuarios_data_science - usuarios_machine_learning

fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning
15 in fez_ds_mas_nao_fez_ml

23 in fez_ds_mas_nao_fez_ml

usuarios_data_science ^ usuarios_machine_learning

usuario = {1, 5, 76, 34, 52, 13, 17}
len(usuario)

usuario.add(13)
len(usuario)

usuario.add(765)
len(usuario)

usuario = frozenset(usuario)
usuario

type(usuario)

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto.split()

set(meu_texto.split())

aparicoes = {
    "Guilherme" : 1,
    "cachorro"  : 2,
    "nome" : 2,
    "vindo" : 1,
}

type(aparicoes)

aparicoes["Guilherme"]

aparicoes["xpto"]

aparicoes.get("xpto", 0)

aparicoes = dict(Guilherme = 2, cachorro = 1)
aparicoes

aparicoes = {
    "Guilherme" : 1,
    "cachorro"  : 2,
    "nome" : 2,
    "vindo" : 1,
}

aparicoes["Carlos"] = 1
aparicoes

aparicoes["Carlos"] = 2
aparicoes

del aparicoes["Carlos"]
aparicoes

"cachorro" in aparicoes

"Carlos" in aparicoes

for elemento in aparicoes:
    print(elemento)
     
for elemento in aparicoes.keys():
    print(elemento)

for elemento in aparicoes.values():
    print(elemento)

1 in aparicoes.values() 

for elemento in aparicoes.keys():
    valor = aparicoes[elemento]
    print(elemento, aparicoes[elemento])

for elemento in aparicoes.items():
    print(elemento)

for chave ,valor in aparicoes.items():
    print(chave , "=", valor)   

["palavra {}".format(chave) for chave in aparicoes.keys()]
