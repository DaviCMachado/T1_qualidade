test = {
    'name': 'avalia01',
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # O valor de N1 não está correto.
                    >>> # Esse é o número de canais da saída
                    >>> # da primeira convolução (número inteiro)
                    >>> import convns as N
                    >>> N.N1 == N1
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # O valor de N2 não está correto.
                    >>> # Aparentemente você esqueceu de considerar
                    >>> # o stride=2 (a convolução se move de duas
                    >>> # em duas casas)
                    >>> import convns as N
                    >>> N.N2 == 59
                    False
                    """
                },
                {
                    'code': r"""
                    >>> # O valor de N2 não está correto.
                    >>> # Use a fórmula 1+(W-K)/S onde
                    >>> # W é a dimensão da entrada (64),
                    >>> # K é o tamanho do kernel (6)
                    >>> # S é o stride.
                    >>> # Obs.: Se a divisão não der inteiro
                    >>> #       arredonde para baixo.
                    >>> import convns as N
                    >>> N.N2 == N2
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # O valor de N3 não está correto.
                    >>> # Esse é o volume. Basta multiplicar
                    >>> # N3=N1*N2*N2
                    >>> import convns as N
                    >>> N.N3 == N3
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # O valor de N4 não está correto.
                    >>> # O padding não altera o número
                    >>> # de canais.
                    >>> import convns as N
                    >>> N.N4 == N4
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # O valor de N5 não está correto.
                    >>> # Use a fórmula 1+(W-K)/S onde
                    >>> # W é a dimensão da entrada anterior (N2)
                    >>> # K é o tamanho da janela do max-pooling (2)
                    >>> # S é o stride (2)
                    >>> import convns as N
                    >>> N.N5 == N5
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # O valor de N6 não está correto.
                    >>> # Esse é o volume. Basta multiplicar
                    >>> # N6=N4*N5*N5 (mesmo que fez para
                    >>> # calcular N3)
                    >>> import convns as N
                    >>> N.N6 == N6
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # O valor de N7 não está correto.
                    >>> # Esse é o número de canais da saída
                    >>> # da segunda convolução (número inteiro)
                    >>> import convns as N
                    >>> N.N7 == N7
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # O valor de N8 não está correto.
                    >>> # Use a fórmula 1+(W-K)/S onde
                    >>> # W é a dimensão da entrada anterior (N5)
                    >>> # K é o tamanho do kernel (3)
                    >>> # S é o stride (1)
                    >>> import convns as N
                    >>> N.N8 == N8
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # O valor de N9 não está correto.
                    >>> # Esse é o volume. Basta multiplicar
                    >>> # N9=N7*N8*N8
                    >>> import convns as N
                    >>> N.N9 == N9
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # O valor de N10 não está correto.
                    >>> # O padding não altera o número
                    >>> # de canais.
                    >>> import convns as N
                    >>> N.N10 == N10
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # O valor de N11 não está correto.
                    >>> # Use a fórmula 1+(W-K)/S onde
                    >>> # W é a dimensão da entrada anterior (N8),
                    >>> # K é o tamanho da janela do max-pooling (2)
                    >>> # S é o stride (2)
                    >>> # Obs.: Se a divisão não der inteiro
                    >>> #       arredonde para baixo.
                    >>> import convns as N
                    >>> N.N11 == N11
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # O valor de N12 não está correto.
                    >>> # Esse é o volume da convolução
                    >>> # anterior. Basta multiplicar
                    >>> # N12=N10*N11*N11
                    >>> import convns as N
                    >>> N.N12 == N12
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # O valor de N13 não está correto.
                    >>> # Lembre que precisamos um número
                    >>> # de saídas igual à quantidade de
                    >>> # classes que queremos classificar.
                    >>> import convns as N
                    >>> N.N13 == N13
                    True
                    """
                },
            ]
        }
    ]
}

