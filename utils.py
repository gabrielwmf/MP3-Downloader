import re

# Essa função abaixo remove caracteres inválidos para sistemas de arquivos.
def sanitize_filename(filename):
   return re.sub(r'[\/:*?"<>|]\'', '', filename)


# Essa função abaixo verifica se o link pertence aos padrões do youtube.
# Retorna True se for válido, caso o contrário retorna False
def is_valid_youtube_link(link):
   valid_prefixes = [
      "https://www.youtube.com/",
      "https://youtube.com/",
      "https://youtu.be/",
   ]

   return any(link.startswith(prefix) for prefix in valid_prefixes)