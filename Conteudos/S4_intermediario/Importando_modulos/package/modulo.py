# __all__ = [
#     'variavel',
#     'soma_do_modulo',
#     'nova_variavel',
# ]

# Com package na frente do noome não funciona aqui, mas funciona fora
from package.modulo_b import fala_oi

# from modulo_b import fala_oi
# fala_oi()

variavel = 'Alguma coisa'


def soma_do_modulo(x, y):
    return x + y


nova_variavel = 'OK'
print(__name__)
