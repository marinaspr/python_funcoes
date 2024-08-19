def preenche_lista(l:list):
    x= "a"
    while x !=".":  
        x= input("elementos: ")
        l.append(x)

def exibe_lista(l: list):
    for elemento in l:
        print(elemento)

#def conta_elementos(l: list) -> int:
   #for 
    #   if 
    #    return lista

def retorna_indice(l: list, elemento) -> int:
    elemento = input("digite o elemento: ")
    tamanho=len(l)
    for i in range(tamanho):
        if elemento == l[i]:
           return i.index(elemento)
    return -1
    
#def busca(l: list, elemento) -> int:
 #   a=0
  #  for i in range(len(l)):
   #     if elemento == l[i]:
  #          a+=1
   # return a

#def conta_inteiro(l: list) -> int:
 #   a = 0
  #  for i in range(len(l)):
   #     if  type(l[i]) == float:
    #        a+=1
    #return a



lista = [-5, 22, 36, 785, -54]

