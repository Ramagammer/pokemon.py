import tkinter as tk
from tkinter import *
import numpy as np
import sys
import time
import pygame

pygame.init()
pygame.mixer.music.load("/Users/rherz/desktop/pyprojects/x2mate.com - Pokemon Soundtrack battle (sonido batalla) (128 kbps).mp3")
pygame.mixer.music.play(-1)
ruta_archivo_sonido = "/Users/rherz/desktop/pyprojects/aipom.mp3"
sonido_ataque = pygame.mixer.Sound(ruta_archivo_sonido)

def imprimir_con_retraso(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class Pokemon:
    def __init__(self, nombre, tipos, movimientos, EVs, puntos_de_salud='===================='):
        self.nombre = nombre
        self.tipos = tipos
        self.movimientos = movimientos
        self.ataque = EVs['ataque']
        self.defensa = EVs['defensa']
        self.puntos_de_salud = puntos_de_salud
        self.barras = 20


    def info(self,Pokemon2):
        print("----- BATALLA DE POKÉMON -----")
        print(f'\n{self.nombre}')
        print("tipo/", self.tipos)
        print("ataque/", self.ataque)
        print("defensa/", self.defensa)
        print("Nv./", 3*(1 + np.mean([self.ataque,self.defensa])))
        print("\nVS")
        print("tipo/", self.tipos)
        print("tipo/", self.tipos)
        print("tipo/", self.tipos)
        print(f'\n{Pokemon2.nombre}')
        print("tipo/", Pokemon2.tipos)
        print("ataque/", Pokemon2.ataque)
        print("defensa/", Pokemon2.defensa)
        print("Nv./", 3*(1 + np.mean([Pokemon2.ataque,Pokemon2.defensa])))
        time.sleep(2)


    def ventaja(self, Pokemon2):
        version = ['fuego', 'agua', 'planta']
        for i,k in enumerate(version):
    
            if self.tipos == k:
                
                if Pokemon2.tipos == k:
                    cadena_1_ataque = '\nNo es muy efectivo...'
                    cadena_2_ataque = '\nNo es muy efectivo...'
    
                
                if Pokemon2.tipos == version [(i+1)%3]:
                    Pokemon2.ataque *= 2
                    Pokemon2.defensa *= 2
                    self.ataque /= 2
                    self.defensa /= 2
                    cadena_1_ataque = '\nNo es muy efectivo...'
                    cadena_2_ataque = '\n¡Es muy eficaz!'
    
                if Pokemon2.tipos == version [(i+2)%3]:
                   self.ataque *= 2
                   self.defensa *= 2
                   Pokemon2.ataque /= 2
                   Pokemon2.defensa /= 2
                   cadena_1_ataque = '\n¡Es muy eficaz!'
                   cadena_2_ataque = '\nNo es muy efectivo...'
    
                return cadena_1_ataque, cadena_2_ataque
    
    
    def turno(self, Pokemon2, cadena_1_ataque, cadena_2_ataque):
    
        while (self.barras > 0) and (Pokemon2.barras > 0):
    
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}\n")
            print(f"\n{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}\n")
    
            # POKEMON 1
        
            print(f"¡Adelante {self.nombre}!")
            for i, x in enumerate(self.movimientos):
                print(f"{i+1}.", x)
            index = None
            while index is None:
             try:
                index = int(input('Elige un movimiento: '))
                if index < 1 or index > 4:
                    print(f"Elegí un ataque aprendido por {self.nombre}. (del 1 al 4)")
                    index = None
             except ValueError:
                print(f"¡Es tu turno de atacar!, Elegí un ataque aprendido por {self.nombre}.")
            imprimir_con_retraso(f"\ni{self.nombre} usó {self.movimientos[index-1]}!")
            sonido_ataque.play()
            time.sleep(2)  
            sonido_ataque.stop()
            time.sleep(1)
            imprimir_con_retraso(cadena_1_ataque)
        
            Pokemon2.barras -= self.ataque
            Pokemon2.puntos_de_salud = ""
            
            for j in range (int(Pokemon2.barras+.1*Pokemon2.defensa)):
                Pokemon2.puntos_de_salud += "="
        
            time.sleep(1)
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}\n")
            print(f"\n{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}\n")
            time.sleep(.5)
        
            if Pokemon2.barras <= 0:
                imprimir_con_retraso("\n..." + Pokemon2.nombre + ' se debilito')
                break
        
            # POKEMON 2
        
            print(f"¡Adelante {Pokemon2.nombre}!")
            for i, x in enumerate(Pokemon2.movimientos):
                print(f"{i+1}.", x)
            index = None
            while index is None:
             try:
                index = int(input('Elige un movimiento: '))
                if index < 1 or index > 4:
                    print(f"Elegí un ataque aprendido por {Pokemon2.nombre}. (del 1 al 4)")
                    index = None
             except ValueError:
                print(f"¡Es tu turno de atacar!, Elegí un ataque aprendido por {Pokemon2.nombre}")
            imprimir_con_retraso(f"\ni{Pokemon2.nombre} usó {Pokemon2.movimientos[index-1]}!")
            sonido_ataque.play()
            time.sleep(2)  
            sonido_ataque.stop()
            time.sleep(1)
            imprimir_con_retraso(cadena_2_ataque)
        
            self.barras -= Pokemon2.ataque
            self.puntos_de_salud = ""
            
            for j in range (int(self.barras+1*self.defensa)):
                self.puntos_de_salud += "="
        
            time.sleep(1)
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}\n")
            print(f"\n{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}\n")
            time.sleep(.5)
        
            # Comprobar si pokemon2 se debilito
        
            if self.barras <= 0:
                imprimir_con_retraso("\n..." + self.nombre + ' se debilito.')
                break
        
    
    def batalla(self, Pokemon2):
            
        # Imprime info de lucha
        self.info(Pokemon2)
        
        # Considera ventaja de tipo
        cadena_1_ataque, cadena_2_ataque = self.ventaja(Pokemon2)
    
        # Lucha real...
        # Sigue mientras Salud > 0
        self.turno(Pokemon2, cadena_1_ataque, cadena_2_ataque)
    
        # Recibir dinero (premio por ganar)
    
        money = np.random.choice(5000)
        imprimir_con_retraso(f"\nEl oponente de pagó ${money}.\n")


if __name__ == '__main__':
     Charizard = Pokemon('Charizard', 'fuego', ['Lanzallamas', 'Pirotecnia', 'Giro fuego', 'Ascuas'], {'ataque':12, 'defensa':8})
     Blastoise = Pokemon('Blastoise', 'agua', ['Pistola Agua', 'Burbuja', 'Hidropulso', 'Hidrobomba'], {'ataque':10, 'defensa':10})
     Venusaur = Pokemon('Venusaur', 'planta', ['Latigo Cepa', 'Hoja afilada', 'Rayo solar', 'Abatidoras'], {'ataque':8, 'defensa':12})
     
Blastoise.batalla(Venusaur)
pygame.mixer.music.stop()




