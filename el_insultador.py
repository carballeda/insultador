# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 13:54:40 2023

@author: carballeda
"""
import random

# el insultador
player1=input('¡Hola, bienvenido/a al insultador! Dime tu nombre: ')
res=input(f'{player1}, ¿quieres que te insulte? Responde \"s\" o \"n\".\n')
insultos=['Te falta una patatina para el kilo.',
          'No eres el lápiz más afilado de la caja.',
          'Te faltan dos sandwiches para ser un picnic.',
          'Nadie al volante.',
          'La inteligencia te persigue pero tú eres más veloz.',
          'Por personas como tú el champú lleva instrucciones.',
          'Te acunaron muy cerca de la pared.',
          'Tienes el cociente intelectual a temperatura ambiente.',
          'Tripitiste parbulitos.',
          'Vienes de Cortilandia.',
          'Más tonto/a y naces ladrillo.',
          'Eres más corto/a que el rabito de una boina.',
          'Eres tonto/a desde que tu padre y tu madre eran novios.',
          'Te falla la placa base.',
          '¿Te sacaste el DNI a la segunda?',
          'Te faltan tres minutos de microondas.',
          'Eres más tonto/a que cagar de pie.',
          'Eres inteligente pero asintomático/a.',
          'Tú eres tonto/a global.',
          'Eres tonto/a 360: te mire por donde te mire, eres tonto.',
          'No tienes todos los patitos en línea.'
          ]
while res == 's':
    print(random.choice(insultos))
    print('\n')
    res=input('¿Quieres más? Responde \"s\" o \"n\".\n')
print('\n')
print('Ha sido un placer. Vuelve cuando quieras que te insulte.')