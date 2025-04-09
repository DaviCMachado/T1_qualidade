test = {
    'name': 'avalia02',
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # O nome da classe deve ser 'ConvNet'
                    >>> # e não 'Convnet'.
                    >>> 'Convnet' in dir() and not 'ConvNet' in dir()
                    False
                    """
                },
                {
                    'code': r"""
                    >>> # O nome da classe deve ser 'ConvNet'
                    >>> # e não 'convnet'.
                    >>> 'convnet' in dir() and not 'ConvNet' in dir()
                    False
                    """
                },
                {
                    'code': r"""
                    >>> # O nome da classe deve ser 'ConvNet'
                    >>> # Não encontrei nenhuma classe com
                    >>> # esse nome declarada no escopo do
                    >>> # programa. Verifica se não houve
                    >>> # erro de digitação
                    >>> 'ConvNet' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # ConvNet deve ser uma classe e não
                    >>> # uma função. Você declara com a
                    >>> # palavra chave 'class' e não 'def'
                    >>> from inspect import isfunction
                    >>> isfunction(ConvNet)
                    False
                    """
                },
                {
                    'code': r"""
                    >>> # A classe ConvNet deve derivar
                    >>> # da classe nn.Module
                    >>> issubclass(ConvNet, nn.Module)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Não consigo instanciar a classe ConvNet
                    >>> # Será que você lembrou de chamar o construtor
                    >>> # da classe mãe? Lembre de adicionar essa linha
                    >>> # abaixo logo após def __init__(self):
                    >>> #
                    >>> #    super(ConvNet, self).__init__()
                    >>> #
                    >>> try:
                    ...   cnn = ConvNet()
                    ...   print(True)
                    ... except:
                    ...   print(False)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Sua rede neural não possui
                    >>> # a variável membro correspondente
                    >>> # ao objeto referente à primeira
                    >>> # camada convolucional de nome
                    >>> # self.conv1
                    >>> cnn = ConvNet()
                    >>> hasattr(cnn, 'conv1')
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Sua rede neural não possui
                    >>> # a variável membro correspondente
                    >>> # ao objeto referente à primeira
                    >>> # camada de max-pooling de nome
                    >>> # self.pool1
                    >>> cnn = ConvNet() 
                    >>> hasattr(cnn, 'pool1')
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Sua rede neural não possui
                    >>> # a variável membro correspondente
                    >>> # ao objeto referente à segunda
                    >>> # camada de convolucional de nome
                    >>> # self.conv2
                    >>> cnn = ConvNet() 
                    >>> hasattr(cnn, 'conv2')
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Sua rede neural não possui
                    >>> # a variável membro correspondente
                    >>> # ao objeto referente à camada
                    >>> # de dropout de nome
                    >>> # self.drp1
                    >>> cnn = ConvNet() 
                    >>> hasattr(cnn, 'drp1')
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Sua rede neural não possui
                    >>> # a variável membro correspondente
                    >>> # ao objeto referente à segunda
                    >>> # camada de max-pooling de nome
                    >>> # self.pool2
                    >>> cnn = ConvNet() 
                    >>> hasattr(cnn, 'pool2')
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Sua rede neural não possui
                    >>> # a variável membro correspondente
                    >>> # ao objeto referente à camada
                    >>> # feedforward de nome
                    >>> # self.lin1
                    >>> cnn = ConvNet() 
                    >>> hasattr(cnn, 'lin1')
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # A camada self.conv1 deve ser
                    >>> # do tipo Conv2d
                    >>> cnn = ConvNet() 
                    >>> str(cnn.conv1)[:6] == 'Conv2d'
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # A camada self.pool1 deve ser
                    >>> # do tipo MaxPool2
                    >>> cnn = ConvNet() 
                    >>> str(cnn.pool1)[:9] == 'MaxPool2d'
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # A camada self.conv2 deve ser
                    >>> # do tipo Conv2d
                    >>> cnn = ConvNet() 
                    >>> str(cnn.conv2)[:6] == 'Conv2d'
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # A camada self.drp1 deve ser
                    >>> # do tipo Dropout2d
                    >>> cnn = ConvNet() 
                    >>> str(cnn.drp1)[:9] == 'Dropout2d'
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # A camada self.pool2 deve ser
                    >>> # do tipo MaxPool2
                    >>> cnn = ConvNet() 
                    >>> str(cnn.pool2)[:9] == 'MaxPool2d'
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # A camada self.lin1 deve ser
                    >>> # do tipo Linear
                    >>> cnn = ConvNet() 
                    >>> str(cnn.lin1)[:6] == 'Linear'
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # A primeira convolução, self.conv1,
                    >>> # deve receber apenas um canal de entrada
                    >>> # (primeiro argumento do construtor)
                    >>> cnn = ConvNet() 
                    >>> int(str(cnn.conv1)[7:-1].split(', ')[0]) == 1
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # A primeira convolução, self.conv1,
                    >>> # deve gerar cinco canais de saída
                    >>> # (segundo argumento do construtor)
                    >>> cnn = ConvNet() 
                    >>> int(str(cnn.conv1)[7:-1].split(', ')[1]) == 5
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # A primeira convolução, self.conv1,
                    >>> # deve possuir um kernel de tamanho 6x6
                    >>> import re
                    >>> r = re.compile(r'(?:[^,(]|\([^)]*\))+')
                    >>> cnn = ConvNet() 
                    >>> s = str(cnn.conv1)[13:-1]
                    >>> eval(r.findall(s)[0].split('=')[1]) == (6, 6)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # A primeira convolução, self.conv1,
                    >>> # deve seguir passo de tamanho 2
                    >>> # ou seja, stride=2
                    >>> import re
                    >>> r = re.compile(r'(?:[^,(]|\([^)]*\))+')
                    >>> cnn = ConvNet() 
                    >>> s = str(cnn.conv1)[13:-1]
                    >>> eval(r.findall(s)[1].split('=')[1]) == (2, 2)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # A primeira camada max-pooling,
                    >>> # self.pool1, deve possuir uma
                    >>> # janela de tamanho 2
                    >>> import re
                    >>> r = re.compile(r'(?:[^,(]|\([^)]*\))+')
                    >>> cnn = ConvNet() 
                    >>> s = str(cnn.pool1)[10:-1]
                    >>> eval(r.findall(s)[0].split('=')[1]) == 2
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # A primeira camada max-pooling,
                    >>> # self.pool1, deve seguir passos
                    >>> # de tamanho 2
                    >>> import re
                    >>> r = re.compile(r'(?:[^,(]|\([^)]*\))+')
                    >>> cnn = ConvNet() 
                    >>> s = str(cnn.pool1)[10:-1]
                    >>> eval(r.findall(s)[1].split('=')[1]) == 2
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # A segunda convolução, self.conv2,
                    >>> # deve receber cinco canais de entrada
                    >>> # (primeiro argumento do construtor)
                    >>> cnn = ConvNet() 
                    >>> int(str(cnn.conv2)[7:-1].split(', ')[0]) == 5
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # A segunda convolução, self.conv2,
                    >>> # deve gerar oito canais de saída
                    >>> # (segundo argumento do construtor)
                    >>> cnn = ConvNet() 
                    >>> int(str(cnn.conv2)[7:-1].split(', ')[1]) == 8
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # A segunda convolução, self.conv2,
                    >>> # deve possuir um kernel de tamanho 3x3
                    >>> import re
                    >>> r = re.compile(r'(?:[^,(]|\([^)]*\))+')
                    >>> cnn = ConvNet() 
                    >>> s = str(cnn.conv2)[13:-1]
                    >>> eval(r.findall(s)[0].split('=')[1]) == (3, 3)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # A segunda convolução, self.conv2,
                    >>> # deve seguir passo de tamanho 1
                    >>> # ou seja, stride=1
                    >>> import re
                    >>> r = re.compile(r'(?:[^,(]|\([^)]*\))+')
                    >>> cnn = ConvNet() 
                    >>> s = str(cnn.conv2)[13:-1]
                    >>> eval(r.findall(s)[1].split('=')[1]) == (1, 1)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # A camada de dropout self.drp1
                    >>> # deve matar 25% das saídas, ou
                    >>> # seja, p=0.25
                    >>> import re
                    >>> r = re.compile(r'(?:[^,(]|\([^)]*\))+')
                    >>> cnn = ConvNet() 
                    >>> s = str(cnn.drp1)[10:-1]
                    >>> eval(r.findall(s)[0].split('=')[1]) == 0.25
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # A segunda camada max-pooling,
                    >>> # self.pool2, deve possuir uma
                    >>> # janela de tamanho 2
                    >>> import re
                    >>> r = re.compile(r'(?:[^,(]|\([^)]*\))+')
                    >>> cnn = ConvNet() 
                    >>> s = str(cnn.pool2)[10:-1]
                    >>> eval(r.findall(s)[0].split('=')[1]) == 2
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # O número de entradas em sua camada
                    >>> # self.lin1 está incorreto. A última
                    >>> # camada, feed-forward, deve receber
                    >>> # os dados serializados. Para calcular
                    >>> # a quantidade de entradas, você deve
                    >>> # calcular a quantidade de ativações
                    >>> # na camada anterior, ou seja, número
                    >>> # de canais vezes largura vezes altura.
                    >>> # É igual ao N12 da parte 1 do exercício.
                    >>> import re
                    >>> r = re.compile(r'(?:[^,(]|\([^)]*\))+')
                    >>> cnn = ConvNet() 
                    >>> s = str(cnn.lin1)[7:-1]
                    >>> eval(r.findall(s)[0].split('=')[1]) == 288
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # O número de saídas em sua camada
                    >>> # self.lin1 está incorreto. A última
                    >>> # camada deve apresentar como saída
                    >>> # o número de classes do problema de
                    >>> # classificação.
                    >>> import re
                    >>> r = re.compile(r'(?:[^,(]|\([^)]*\))+')
                    >>> cnn = ConvNet() 
                    >>> s = str(cnn.lin1)[7:-1]
                    >>> eval(r.findall(s)[1].split('=')[1]) == 10
                    True
                    """
                },
            ]
        }
    ]
}

