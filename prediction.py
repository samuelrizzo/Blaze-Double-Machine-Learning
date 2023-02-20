import tensorflow as tf
import numpy as np
import pandas as pd
from scraper import pegarUltimosResultados

# Obter os resultados anteriores da roleta
resultados = pegarUltimosResultados()

# Verificar se há pelo menos 20 resultados
if len(resultados) < 20:
    print('Não há resultados suficientes para fazer uma previsão.')
    exit()

# Definir um dicionário para codificar as cores como 0 (para preto ou branco) e 1 (para vermelho)
cores = {'V': 1, 'P': 0, 'B': 0}

# Criar DataFrame pandas com os resultados anteriores da roleta e as cores correspondentes codificadas
df = pd.DataFrame({'resultado': resultados, 'cor': [cores[r] for r in resultados]})

# Dividir o DataFrame em conjuntos de treinamento e teste
train_df = df.iloc[:15]
test_df = df.iloc[15:]

# Criar um modelo de rede neural usando TensorFlow
model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation='sigmoid', input_shape=(1,)),
    tf.keras.layers.Dense(3, activation='softmax')
])

# Compilar o modelo e definir os hiperparâmetros
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Treinar o modelo
model.fit(train_df['cor'], tf.keras.utils.to_categorical(train_df.index % 3, num_classes=3), epochs=1000, verbose=0)

# Usar o modelo treinado para prever a próxima cor da roleta
ultimo_resultado = test_df.iloc[-1]['cor']
proximo_resultado = np.argmax(model.predict(np.array([ultimo_resultado])), axis=-1)

# Imprimir a previsão da próxima cor da roleta
if proximo_resultado == 0:
    print('Próximo resultado: preto')
elif proximo_resultado == 1:
    print('Próximo resultado: vermelho')
else:
    print('Próximo resultado: branco')
