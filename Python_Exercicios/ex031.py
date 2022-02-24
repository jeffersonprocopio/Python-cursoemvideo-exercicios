#Programa para verificar o preço do km e distancia
km = float(input("Qual é a distância da sua viagem? "))
print("Você está presetes a começar uma viagem de {:.1f}Km".format(km))
preco = km * 0.50 if km <= 200 else km * 0.45
print("E o preço da sua passagem será de R${:.2f}".format(preco))

#ou

#p1 = (km * 0.50)
#p2 = (km * 0.45)

#if km <= 200:
    #print("Você está presetes a começar uma viagem de {:.1f}Km".format(km))
    #print("E o preço da sua passagem será de R${:.2f}".format(p1))

#else:
    #print("Você está prestes a começar uma viagem de {:.1f}Km".format(km))
    #print("E o preço da sua passem será de R${:.2f}".format(p2))