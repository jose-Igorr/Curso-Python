# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# l1 = [1, 2, 3, 3,3 ]
# s1 = set(l1)

# s1 = {1, 2, 3}

s1 = {1, 2, 3}
# print(3 not in s1)
# for numero in s1:
#     print(numero)


# Métodos úteis:
s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Ola mundo', 1, 2, 3, 4))
# s1.clear()
s1.discard('Ola mundo')
s1.discard('Luiz')
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^ s2
print(s3)

# diferença simétrica ^ - Itens que não estão em ambos

