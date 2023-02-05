# FEST
Física Estadística - Semestre 2023/1, Universidad de los Andes, Bogotá, Colombia

SIMULACIÓN NUMÉRICA DE MARCHA ALEATORIA EN 3D

El código usado para la simulación de caminante solo requiere un único parámetro por parte del usuario: La cantidad de pasos que se desea que el caminante aleatorio ejecute. 

Advertencia: Para 10000 o más datos, la simulación tardará un tiempo en completar (no más de 30 segundos). Para mejorar la velocidad de procesamiento, otorgar un número N bajo (del orden de 1000). 

NOTA SOBRE ALEATOREIDAD: Se hace uso de la función random.choice de la librería random. Las funciones nativas de scipy pueden ser más sofisticadas a la hora de asignar probabilidades no homogéneas sobre la selección de la dirección de movimiento. 

RESULTADO: El código debe entregar un histograma que describe la frecuencia (normalizada) de las distancias finales al origen. 
