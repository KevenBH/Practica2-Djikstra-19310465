#Importamos librerias para crear los nodos, aristas y mostrar el grafo
import networkx as nx
import matplotlib.pyplot as plt
g=nx.Graph()

#Creamos los nodos y posiciones en el grafo 
g.add_node("Puerto Vallarta",pos=(-10,10))
g.add_node("Autlán de Navarro",pos=(5,6))
g.add_node("Ameca",pos=(8,11))
g.add_node("Tala",pos=(12,9))
g.add_node("Ciudad Guzman",pos=(11,1))
g.add_node("Tesistan",pos=(15,20))
g.add_node("GDL",pos=(18,11))
g.add_node("Tlaquepaque",pos=(20,8))
g.add_node("Zapopan",pos=(17,15))
g.add_node("San Juan de los Lagos",pos=(25,27))
g.add_node("Lagos de Moreno",pos=(30,30))
g.add_node("Tonala",pos=(23,6))
g.add_node("Ocotlan",pos=(27,3))
g.add_node("Tepatitlan",pos=(26,12))
g.add_node("Arandas",pos=(31,9))

#Creamos las aristas del grafo y su peso/distancia
g.add_edge("Puerto Vallarta", "Tesistan", weight=315)
g.add_edge("Puerto Vallarta", "Ameca", weight=226)
g.add_edge("Puerto Vallarta", "Autlán de Navarro", weight=257)
g.add_edge("Tesistan", "Ameca", weight=74)
g.add_edge("Tesistan", "Zapopan", weight=14)
g.add_edge("Tesistan", "San Juan de los Lagos", weight=162)
g.add_edge("Ameca", "Tala", weight=42)
g.add_edge("Ameca", "Ciudad Guzman", weight=161)
g.add_edge("Ameca", "Autlán de Navarro", weight=143)
g.add_edge("Tala", "Zapopan", weight=43)
g.add_edge("Tala", "GDL", weight=47)
g.add_edge("Tala", "Ciudad Guzman", weight=138)
g.add_edge("Ciudad Guzman",	"Tlaquepaque", weight=134)
g.add_edge("Ciudad Guzman",	"Tonala", weight=143)
g.add_edge("Ciudad Guzman",	"Ocotlan", weight=179)
g.add_edge("Zapopan", "GDL", weight=10)
g.add_edge("Zapopan", "San Juan de los Lagos", weight=150,)
g.add_edge("Zapopan", "Lagos de Moreno", weight=192)
g.add_edge("GDL", "Tepatitlan", weight=74)
g.add_edge("GDL", "Tlaquepaque", weight=7)
g.add_edge("Tlaquepaque", "Tonala", weight=9)
g.add_edge("Tonala", "Ocotlan", weight=71)
g.add_edge("Tonala", "Arandas", weight=116)
g.add_edge("Tonala", "Tepatitlan", weight=62)
g.add_edge("Ocotlan", "Arandas", weight=79)
g.add_edge("Tepatitlan", "Arandas",	weight=56)
g.add_edge("Tepatitlan", "Lagos de Moreno",	weight=112)
g.add_edge("San Juan de los Lagos",	"Lagos de Moreno", weight=47)

pos = nx.get_node_attributes(g,'pos')# Atributes que tiene el nodo
labels = nx.get_edge_attributes(g,'weight')# Atributos que tiene las aristas

nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)
nx.draw(g,pos,with_labels=True)

print(nx.dijkstra_path(g,source= "Tonala",target="Arandas")) #Imprime el camino a seguir en la consola
print(nx.dijkstra_path_length(g,source= "Tonala",target="Arandas")) #Imprime la distancia del camino en la consola
plt.show() #Muestra el grafo



#origen= (str(input('Introduce Entidad de Partida: ')))
#origen= origen.title()
#destino= (str(input('Introduce Entidad de Destino: ')))
#destino= destino.title()
#print(nx.shortest_path(g,source="Puerto Vallarta",target="Arandas"))



