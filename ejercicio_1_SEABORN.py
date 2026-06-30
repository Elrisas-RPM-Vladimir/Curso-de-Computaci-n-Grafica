# LIBRERÍA: Seaborn
# Para qué sirve: hacer gráficos estadísticos bonitos con pocas líneas
# Se aplica en: análisis de notas, ventas, encuestas, salud

import seaborn as sns
import matplotlib.pyplot as plt

# Datos simples: notas de 10 estudiantes
notas = [12, 14, 15, 11, 18, 13, 16, 10, 17, 14]
cursos = ["Lunes","Martes","Miércoles","Jueves","Viernes",
          "Lunes","Martes","Miércoles","Jueves","Viernes"]

# FUNCIÓN 1: set_theme() — cambia el estilo visual del gráfico
sns.set_theme(style="whitegrid")
print("Tema aplicado")

# FUNCIÓN 2: histplot() — muestra cuántas veces se repite cada nota
sns.histplot(notas, bins=5, color="steelblue")
plt.title("Distribución de notas")
plt.xlabel("Nota")
plt.ylabel("Cantidad de estudiantes")
plt.show()

# FUNCIÓN 3: barplot() — promedio de notas por día
import pandas as pd
df = pd.DataFrame({"nota": notas, "dia": cursos})
sns.barplot(data=df, x="dia", y="nota", palette="Blues_d")
plt.title("Promedio de notas por día")
plt.show()

# FUNCIÓN 4: boxplot() — muestra el rango y la mediana
sns.boxplot(x=notas, color="lightgreen")
plt.title("Boxplot de notas")
plt.show()

# FUNCIÓN 5: scatterplot() — relaciona dos listas de números
horas = [2, 3, 5, 1, 6, 4, 7, 1, 5, 3]
sns.scatterplot(x=horas, y=notas, color="red")
plt.title("Horas de estudio vs Nota")
plt.xlabel("Horas")
plt.ylabel("Nota")
plt.show()

print("✅ Ejercicio Seaborn completado")