# Pipeline típico de limpieza de datos en pandas

## 1. Estandarizar valores faltantes o incompatibles
- Reemplazar strings como `"N/A"`, `"n/a"`, `"?"` por `np.nan`.
- Esto asegura que todos los valores faltantes estén representados de la misma forma.

## 2. Rellenar o eliminar nulos según el caso
- `fillna(valor)` para imputar (ej. `0`, promedio, mediana).
- `dropna()` si prefieres eliminar filas/columnas incompletas

rellenar valores nulos de una columna
```
df_limpio["Embarked"] = df_limpio["Embarked"].fillna("S")
```

contar los valores nulos
```
print(df_titanic["Age"].isna().sum())
```
eliminar vlaores vacios de una columna
```
df_limpio = df_original.dropna(subset=["nombre_columna"])
```
rellenar con valor representativo



## 3. Convertir tipos de columnas por eficiencia(rendimiento) y facilidad
- `astype(int)` o `pd.to_numeric(..., errors="coerce")`.
- Aquí ya puedes garantizar que las columnas numéricas sean realmente números.

```python
print(df_limpio.dtypes)
# Convertir columna 'Sex' a tipo categorico
df_limpio["Sex"] = df_limpio["Sex"].astype("category")

# Asegurar que 'Fare' esté en float64
df_limpio["Fare"] = df_limpio["Fare"].astype("float64")

print(df_limpio.dtypes)
```

```python
# Convertir (0,1) a booleano
df["Survived"] = df["Survived"].astype("bool")

# Convertir Objeto a categoría
df["Sex"] = df["Sex"].astype("category")

# Convertir Objeto a string (nuevo tipo de pandas)
df["Name"] = df["Name"].astype("string")

# Convertir a fecha
df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")

# Convertir a diferencia de tiempo
df["Duracion"] = pd.to_timedelta(df["Duracion"], errors="coerce")
```

## 4. Reemplazar valores incompatibles por representativos
- Ejemplo: si en `stock` hay strings, convertirlos a `0` o a un valor válido.
- Esto puede ir junto con el paso 1, pero lo importante es hacerlo antes de convertir tipos.

```
df_limpio = df_titanic.copy()
df_limpio["Age"] = df_limpio["Age"].fillna(df_limpio["Age"].mean())
print(f"Filas con Age rellenado: {len(df_limpio)}\n")
```

## 5. Eliminar duplicados
- `drop_duplicates()` para evitar registros repetidos.

## 6. Detectar y tratar valores atípicos (outliers)
- Usar estadísticas (`describe()`, `boxplot`) para identificar.
- Decidir si se eliminan, se corrigen o se mantienen.

## 7. Renombrar columnas (opcional)
- `df.rename(columns={"col_vieja":"col_nueva"})` para mejorar legibilidad.

## 8. Validación final
- Revisar con `df.info()` y `df.describe()` que los tipos y valores estén correctos.
- Confirmar que no queden nulos con `df.isnull().sum()`.


# Métodos más usados en pandas para columnas

## 1. `apply()`
Permite aplicar una función a cada elemento de una columna o fila.

```python
import pandas as pd

df = pd.DataFrame({"nombres": ["Ana", "Luis", "Pedro"], "edad": [20, 25, 30]})

# Convertir nombres a mayúsculas
df["nombres_mayus"] = df["nombres"].apply(lambda x: x.upper())
print(df)
```


## 2. `groupby()`
```python
grupa datos por una o varias columnas y permite aplicar funciones de agregación
df = pd.DataFrame({
    "producto": ["Laptop", "Laptop", "Celular", "Celular"],
    "precio": [1200, 1000, 800, 900]
})
```

# Precio promedio por producto
print(df.groupby("producto")["precio"].mean())

## 3. `map()`
Transforma valores de una columna usando un diccionario o función.


df = pd.DataFrame({"nombres": ["Ana", "Luis", "Pedro"]})

ciudades = {"Ana": "Quito", "Luis": "Guayaquil", "Pedro": "Cuenca"}
df["ciudad"] = df["nombres"].map(ciudades)
print(df)


## 4. fillna()
```python
df = pd.DataFrame({"nombre": ["Ana", None, "Pedro"], "edad": [20, None, 30]})

# Rellenar valores nulos con un texto o número
df["nombre"] = df["nombre"].fillna("Desconocido")
df["edad"] = df["edad"].fillna(df["edad"].mean())
print(df)

```


## 5. dropna()
```python
df = pd.DataFrame({"nombre": ["Ana", None, "Pedro"], "edad": [20, None, 30]})

# Eliminar filas con valores nulos
df = df.dropna()
print(df)

```

## 6. drop_duplicates()
```python
df = pd.DataFrame({"producto": ["Laptop", "Laptop", "Celular"], "precio": [1200, 1200, 800]})

# Eliminar duplicados
df = df.drop_duplicates()
print(df)

```

## 7. rename()
```python
df = pd.DataFrame({"nombre": ["Ana", "Luis"], "edad": [20, 25]})

# Renombrar columnas
df = df.rename(columns={"nombre": "Nombre", "edad": "Edad"})
print(df)

```

## 8. astype()
```python
df = pd.DataFrame({"edad": ["20", "25", "30"]})

# Convertir a entero
df["edad"] = df["edad"].astype(int)
print(df)

```

## 9. pd.to_numeric()
```python
df = pd.DataFrame({"valores": ["10", "20", "error", "30"]})

# Convertir a numérico, ignorando errores
df["valores_num"] = pd.to_numeric(df["valores"], errors="coerce")
print(df)

```

#  Métodos para selección de datos

## 10. loc[]
Selecciona filas y columnas por etiquetas (nombres).
```python
df = pd.DataFrame({"nombre": ["Ana", "Luis", "Pedro"], "edad": [20, 25, 30]})

# Seleccionar fila con índice 1 (Luis)
print(df.loc[1])

# Seleccionar filas con condición
print(df.loc[df["edad"] > 20])

# Seleccionar filas y columnas específicas
print(df.loc[0:1, ["nombre"]])

```

## `11. iloc[]`
Selecciona filas y columnas por posición numérica.
```python
df = pd.DataFrame({"nombre": ["Ana", "Luis", "Pedro"], "edad": [20, 25, 30]})

# Seleccionar primera fila
print(df.iloc[0])

# Seleccionar primera fila y primera columna
print(df.iloc[0, 0])

# Seleccionar varias filas y columnas por rango
print(df.iloc[0:2, 0:2])

```

## `12. query()`
Permite filtrar filas usando expresiones tipo SQL.
```python
df = pd.DataFrame({"nombre": ["Ana", "Luis", "Pedro"], "edad": [20, 25, 30]})
print(df.query("edad > 20"))

```

## 13. `sort_values()`
Ordena filas por valores de una columna.
```python
df = pd.DataFrame({"nombre": ["Ana", "Luis", "Pedro"], "edad": [30, 20, 25]})
print(df.sort_values(by="edad"))

```

## 14. `value_counts()`
Cuenta la frecuencia de valores en una columna.
```python
df = pd.DataFrame({"ciudad": ["Quito", "Quito", "Cuenca", "Guayaquil"]})
print(df["ciudad"].value_counts())

```

## 15. `unique()` y `nunique()`
Devuelve valores únicos y el número de valores únicos.
```python
df = pd.DataFrame({"ciudad": ["Quito", "Quito", "Cuenca", "Guayaquil"]})
print(df["ciudad"].unique())   # Valores únicos
print(df["ciudad"].nunique())  # Número de valores únicos

```

# Metodos de Columna `str`


```python
import pandas as pd

df = pd.DataFrame({"nombres": ["Ana", "Luis", "Pedro", "Ana"], "edad": [20, 25, 30, 20]})

# Contar elementos no nulos en la columna
print(df["nombres"].count())

# Número de valores únicos
print(df["nombres"].nunique())

# Valores únicos
print(df["nombres"].unique())

# Frecuencia de cada valor
print(df["nombres"].value_counts())

# Describir estadísticas básicas
print(df["edad"].describe())

```

# Metodos de Columna de datos numericos

```python
df = pd.DataFrame({"valores": [10, 20, 30, 40, 50]})

# Suma total
print(df["valores"].sum())

# Promedio
print(df["valores"].mean())

# Mediana
print(df["valores"].median())

# Máximo y mínimo
print(df["valores"].max())
print(df["valores"].min())

# Desviación estándar
print(df["valores"].std())

# Varianza
print(df["valores"].var())

# Valor acumulado
print(df["valores"].cumsum())

# Producto acumulado
print(df["valores"].cumprod())

# Diferencia entre valores consecutivos
print(df["valores"].diff())

# Redondear
print(df["valores"].round(1))

```


# Método para varias funciones de agregación personalizadas

El método `agg()` permite aplicar **varias funciones de agregación** a la vez sobre un grupo.  
Es similar a `apply`, pero pensado específicamente para agregaciones.

```python
# Ejemplo: calcular varias estadísticas de la edad por clase

#funcion personalizada
def rango(x):
    """Devuelve el rango de valores: máximo - mínimo"""
    return x.max() - x.min()


df_limpio.groupby("Pclass")["Age"].agg(["mean", "min", "max", "count",rango])
```

## matriz xorrelacion Series.`corr()`
da la correlacion de 2 caractersticas o mas  columnas de un dataframe
```python
correlacion_Ventas_Precio=df[["Ventas","Precio"]].corr()
```

