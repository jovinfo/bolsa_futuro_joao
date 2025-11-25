from abc import ABC, abstractmethod

class ProcessadorDeArquivo(ABC):
    @abstractmethod
    def lerArquivo(self, caminho: str) -> str:
        pass

    @abstractmethod
    def analisarConteudo(self, conteudo: str) -> list:
        pass

    def salvarNoBanco(self, registros: list):
        for registro in registros:
            print(f"Salvando registro [{registro}] no DB...")

    def processar(self, caminho: str) -> str:
        conteudo = self.lerArquivo(caminho)
        registros = self.analisarConteudo(conteudo)
        self.salvarNoBanco(registros)
        return f"Foram processados {len(registros)} registros."

class ProcessadorCSV(ProcessadorDeArquivo):
    def lerArquivo(self, caminho: str) -> str:
        print(f"Lendo arquivo CSV em '{caminho}'...")
        return "valor1,valor2,valor3"

    def analisarConteudo(self, conteudo: str) -> list:
        print("Analisando conteúdo CSV...")
        return conteudo.split(',')

class ProcessadorTXT(ProcessadorDeArquivo):
    def lerArquivo(self, caminho: str) -> str:
        print(f"Lendo arquivo TXT em '{caminho}'...")
        return "linha1\nlinha2\nlinha3\nlinha4"

    def analisarConteudo(self, conteudo: str) -> list:
        print("Analisando conteúdo TXT...")
        return conteudo.split('\n')
    