class Canal:
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos

    def inscrever(self, quantidade=1):
        self.inscritos += quantidade
class CanalEmpresarial(Canal):
    def __init__(self, nome, descricao, inscritos,):
        super().__init__(nome, descricao, inscritos)
        self._equipe = []
    @property
    def equipe(self):
        return self._equipe

canal_israel = Canal("Israel", "Canal de tecnologia e programação", 100)
canal_lancode = Canal("LanCode", "Canal de desenvolvimento e tutoriais", 200)
canal_duolingo = CanalEmpresarial("Duolingo", "Canal de ensino de idiomas", 20000)
print(canal_duolingo.equipe)
