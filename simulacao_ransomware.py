import base64
from pathlib import Path

pasta = Path("test_files")

for arquivo in pasta.glob("*"):
    conteudo = arquivo.read_bytes()
    codificado = base64.b64encode(conteudo)
    novo = arquivo.with_suffix(".simulado")
    novo.write_bytes(codificado)

print("Simulação concluída! Arquivos '.simulado' criados.")
print("Mensagem fictícia: Seus arquivos foram 'codificados' para fins educativos.")
