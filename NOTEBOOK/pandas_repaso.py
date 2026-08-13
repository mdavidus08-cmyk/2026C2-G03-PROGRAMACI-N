#REPASO TUTORIA 25/27/2026
import pandas as pd
pts_examen = 42

datos = {
    "estudiante" : ['Mauricio', 'Andrés', 'Pamela', 'Luis', 'María'],
    "puntos": [40, 32, 20, 20, 38],
    "edad": [22, 19, 20, 23, 30]
}
estudiantes = pd.DataFrame(datos)
print(estudiantes)

#Crear nueva serie (nota) = puntos * 100 / pts_examen
print("\nSerie Nota del estudiante")
estudiantes['nota'] = (estudiantes['puntos'] * 100) / pts_examen
print(estudiantes)


#Listar los estudiante aprobados
print("\nFiltro estudiantes APROBADOS")
filtro = estudiantes['nota'] > 70
print(estudiantes[filtro])

estudiantes['estado'] = estudiantes['nota'].apply(
        lambda nota:"APROBADO" if nota >= 70 else "REPROBADO"
    )
print(estudiantes)

print("Promedio Notas:", estudiantes['nota'].mean())
print("Maximo Notas:", estudiantes['nota'].max())
print("Minima Notas:", estudiantes['nota'].min())
print("Desviación estndar Notas:", estudiantes['nota'].std())
print("Suma:", estudiantes['nota'].sum())
print("Cantida Notas:", estudiantes['nota'].count())
print("Mediana Notas:", estudiantes['nota'].median())
print("Moda Notas:", estudiantes['nota'].mode())