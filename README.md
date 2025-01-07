# cfv-transfer-learning

Geração de Dataset de cartas do jogo Cardfight! Vanguard através de API e aplicação de método de Transfer Learning em uma rede de Deep Learning na linguagem Python para bootcamp em dio.me

# Files 

__Dataset Generator.py__ - Gera um dataset a partir da API de CFV utilizando os clans mencionados no código

__Transfer Learning.py__ - Treina um modelo a partir do dataset criado, carrega modelo vgg16 e treina novamente em cima do modelo já existente

__Confusion Matrix.py__ - Gera Matriz de confusão e imprime métricas

__Face Recognition.ipynb__ - Seguindo tutorial, reconhecimento facial em tempo real

# Libraries Required
- json
- requests
- numpy
- keras
- matplotlib
- tensorflow

# Credits
- Cardfight! Vanguard API made by [Brent Pappas](https://pappasbrent.com/)
- [Original Notebook](https://colab.research.google.com/github/kylemath/ml4a-guides/blob/master/notebooks/transfer-learning.ipynb)
