#!/usr/bin/env python
# coding=latin-1
print
print "Questo programma genera i numeri primi inferiori ad un numero dato"
print
risposta="s"
while risposta=="s" or risposta=="S":
n=int(raw_input("Numeri primi inferiori ad n (n maggiore di 2): "))
listaprimi=[]
for i in range(2,n): # analizzo tutti i numeri i tra 2 ed n
primo=True # controllo se i è primo
for j in range(2,i):
if i%j==0:
primo=False # i non è primo
if primo: # i è primo, quindi lo aggiungo alla lista dei primi
listaprimi.append(i)
print "I numeri primi inferiori a ",n," sono:"
print listaprimi
risposta=raw_input("Ancora ? ")
print
print "Fine programma"