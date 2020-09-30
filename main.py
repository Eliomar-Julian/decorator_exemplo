# // PRIMEIRA FORMA DE CRIAR DECORATOR (USANDO CLASSE)
# // construindo a classe decorator
class class_decorator:
    def __init__(self, func: 'função'):
        """
        Responsavel pela inicialização, e contem a função
        """
        self.func = func

    def __call__(self, *args):
        """
        função de modificação
        """
        return (args[0] + args[1]) * 10

# // SEGUNDA FORMA DE USAR DECORATOR (USANDO FUNÇÕES)
# // função mãe
def func_decorator(func):
    # // funçao modificadora que deve ser retornada
    def modifica(*args):
        # // bloco de modificações *nao necessariamente precisa ser retornado
        return (args[0] + args[1]) / 10
    # // retorno da função modificadora
    return modifica