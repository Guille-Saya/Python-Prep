#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

a = 15
print(a)


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
type(8.5)




# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
type(a)




# 4) Crear una variable que contenga tu nombre

# In[2]:
nom = "Guillermo Sayavedra"
print(nom)



# 5) Crear una variable que contenga un número complejo

# In[3]:
b = 10 + 5j




# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:

type(b)



# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
e = "True" #esto es un str
f = True #esto es un boleano




# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9

# In[5]:
print(type(e))
print(type(f))




# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

suma = 10 + 6.5



# 11) Realizar una operación de suma de números complejos

# In[2]:
g = 6 + 7j
h = 8 + 9j
print(g+h)




# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
i = g + 23
print(i)




# 13) Realizar una operación de multiplicación

# In[5]:
9 * 3




# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
print(2**8)



# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
27 / 4




# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
27 // 4




# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
27 % 4




# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
4 * 6 + 3




# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

print("Hola "+"Guillermo")



# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
"2"== 2 # "2" es un str y 2 es un int




# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
"2" == str(2)




# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:
a = float(3.8) #Al tener comillas y el float esta cambiado por una coma es un str y se produce el error




# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

# In[15]:

t=3
t-=1
print(t)



# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
1<<2 #esto representa al numero 4 en la tabla binaria, indica que el primer numero se corre dos lugares a la izquierda




# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
2 + int("2") #no se puede hacer porque uno es un int y el otro un str, cambiaría el resultado si cmbiamos un str a int o viceversa





# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
m = 10
print(m+5)



# %%
