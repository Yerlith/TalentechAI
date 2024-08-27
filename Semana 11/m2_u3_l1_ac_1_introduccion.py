# -*- coding: utf-8 -*-
"""M2-U3-L1-Ac-1-Introduccion.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RqBNYPZdIe5MB47TjGmfZwQBWZyuzYtv
"""

import random

class Agent:
  def __init__(self, acciones):
    self.acciones = acciones
    self.Q = {}
    for accion in self.acciones:
      self.Q[accion] = {}

  def seleccionarAccion(self, estado):
    return random.choice(self.acciones)

acciones_Posibles = ['izquierda', 'derecha', 'arriba', 'abajo']
agente=Agent(acciones_Posibles) # Pass the possible actions when creating the Agent instance
estado_actual= [0,0]
accion_seleccionada=agente.seleccionarAccion(estado_actual)

print("Accion seleccionada por el agente:",accion_seleccionada)

class EntornoRL:
  def __init__(self, estados):
    self.estados = estados
    def tomar_acciones(self, accion):

      nuevo_estado = random.choice(self.estados)
      recompensa = random.randint(-10, 10)
      return nuevo_estado, recompensa

      estados_posibles = ['A', 'B', 'C', 'D']
      entorno = EntornoRL(estados_posibles)
      accion = 'izquierda'
      nuevo_estado, recompensa = entorno.tomar_acciones(accion)
      print("Nuevo estado:", nuevo_estado)
      print("Recompensa:", recompensa)

class QLearning:
  def __init__(self,estados, acciones,alpha=0.1, gamma=0.9, epsilon=0.1):
    self.estados = estados
    self.acciones = acciones
    self.alpha = alpha
    self.gamma = gamma
    self.epsilon = epsilon
    self.q.table = {}

class QLearning:
  def __init__(self,estados, acciones,alpha=0.1, gamma=0.9, epsilon=0.1):
    self.estados = estados
    self.acciones = acciones
    self.alpha = alpha
    self.gamma = gamma
    self.epsilon = epsilon
    self.q_table = {} # Changed q.table to self.q_table

  def actualizar_q_table(self, estado, accion, recompensa, nuevo_estado): # Made this function a method of the QLearning class
    if estado not in self.q_table: # Changed estado_actual to estado
      self.q_table[estado] = {a:0 for a in self.acciones}
    if nuevo_estado not in self.q_table:
      self.q_table[nuevo_estado] = {a:0 for a in self.acciones}

    q_actual= self.q_table[estado][accion] # Changed q.actual to q_actual and estado_actual to estado
    max_q_nuevo_estado = max(self.q_table[nuevo_estado].values())
    nuevo_valor_q = (1 - self.alpha) * q_actual + self.alpha * (recompensa + self.gamma * max_q_nuevo_estado)
    self.q_table[estado][accion] = nuevo_valor_q # Changed estado_actual to estado

estados = ['A', 'B', 'C', 'D']
acciones = ['izquierda', 'derecha']
q_learning = QLearning(estados, acciones)  # Change variable name to 'q_learning'

estado_actual = 'A'
accion='izquierda'
nuevo_estado = 'B'
recompensa = 10
nuevo_estado = 'B'  # This line seems redundant, as 'nuevo_estado' is already defined

q_learning.actualizar_q_table(estado_actual, accion, recompensa, nuevo_estado)  # Use the correct variable name

print("Tabla Q actualizada:")
print(q_learning.q_table)  # Use the correct variable name