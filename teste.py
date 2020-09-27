class decorador:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args):
        print('ola {}'.format( args[0]))
        if args[1] == True:
            print('Seu acesso foi liberado')
            return
        print('Acesso negado')


@decorador
def func(arg1=None, arg2=True):
    pass


if __name__ == '__main__':
    func("leo", False)


