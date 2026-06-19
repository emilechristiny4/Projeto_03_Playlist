import streamlit as st

musicas = {
    "Frank ocean": {
        "Pyramids": "https://www.youtube.com/watch?v=dMV31MWIjLE&list=RDdMV31MWIjLE&start_radio=1",
        "white ferrari": "https://www.youtube.com/watch?v=xQ6TZGc-IHU&list=RDxQ6TZGc-IHU&start_radio=1"
    },
    "veigh": {
        "Artista generico": "https://www.youtube.com/watch?v=3JeHfhW9uWU&list=RD3JeHfhW9uWU&start_radio=1",
        "marra": "https://www.youtube.com/watch?v=-0fOO3TyenI&list=RD-0fOO3TyenI&start_radio=1",
    },
    "Orochi": {
        "champagne": "https://www.youtube.com/watch?v=6BgxLcofzoo&list=RD6BgxLcofzoo&start_radio=1"
    },
}


st.sidebar.image("logo.png")
artista = st.sidebar.selectbox("Selecione o artista",musicas.keys())
musicas_artista = musicas[artista]
st.title(artista)
video, sobre = st.tabs(['video','sobre'])
with video:
    for musica in musicas_artista.items():
        titulo, link = musica
        st.subheader(titulo)
        st.video(link)
with sobre:
    if artista == "Frank ocean":
       st.markdown("""
# 🎤 Tudo sobre Frank Ocean

## 📌 Informações pessoais
- **Nome de nascimento:** Christopher Edwin Breaux (posteriormente mudou legalmente para Frank Ocean)
- **Nascimento:** 28 de outubro de 1987
- **Local de nascimento:** Long Beach, Califórnia, Estados Unidos
- **Profissão:** Cantor, compositor, rapper e produtor musical
- **Gêneros musicais:** R&B alternativo, soul, hip hop e neo-soul
- **Anos de atividade:** 2006–presente
- **Ex-grupo:** Odd Future

## 🌎 Infância
Apesar de nascer na Califórnia, Frank Ocean cresceu em Nova Orleans, Louisiana. Desde jovem, gostava de música e economizava dinheiro para gravar em estúdios. Após o furacão Katrina destruir sua casa e seu estúdio em 2005, mudou-se para Los Angeles para perseguir a carreira musical.

## ✍️ Início da carreira
Antes de se tornar famoso, trabalhou em diversos empregos e escrevia músicas para outros artistas, incluindo:
- Beyoncé
- Justin Bieber
- John Legend
- Brandy
- Alicia Keys

Em 2010 entrou para o coletivo Odd Future, onde fez amizade com Tyler, The Creator.

## 🎶 Discografia

### Mixtape
- **Nostalgia, Ultra (2011)**

### Álbuns de estúdio
1. **Channel Orange (2012)**
2. **Blonde (2016)**

### Álbum visual
- **Endless (2016)**

## 🎵 Principais músicas
- Thinkin Bout You
- Novacane
- Swim Good
- Pyramids
- Lost
- Super Rich Kids
- Pink + White
- Nikes
- Nights
- Self Control
- Ivy
- White Ferrari
- Chanel
- Biking
- Provider
- Dear April
- Cayendo

## 🤝 Colaborações
Frank Ocean já trabalhou com:
- Beyoncé
- Jay-Z
- Kanye West
- Tyler, The Creator
- Travis Scott
- Calvin Harris
- André 3000
- A$AP Rocky
- Kendrick Lamar
- John Mayer

## 🏆 Prêmios
- 2 Grammy Awards
- 1 Brit Award
- Eleito uma das 100 pessoas mais influentes do mundo pela revista Time em 2013.

## 🏳️ Vida pessoal
Em julho de 2012, Frank Ocean publicou uma carta aberta revelando que sua primeira paixão havia sido um homem. A declaração foi amplamente elogiada e teve grande impacto na representação LGBTQ+ na música.

## 💎 Outros projetos
Além da música, criou:
- **Homer**, marca de luxo de joias e acessórios.
- **Blonded Radio**, programa de rádio transmitido pela Apple Music.
- Trabalhos como fotógrafo e editor da revista *Boys Don't Cry*.

## 📊 Curiosidades
- Seu nome artístico é inspirado em Frank Sinatra e no filme "Ocean's 11".
- É conhecido por fazer longos períodos sem lançar álbuns.
- Seu álbum **Blonde** é considerado um dos melhores discos da década de 2010 por diversos críticos.
- É uma das maiores influências do R&B alternativo moderno.

## 📀 Álbuns

| Ano | Projeto |
|------|----------|
| 2011 | Nostalgia, Ultra |
| 2012 | Channel Orange |
| 2016 | Endless |
| 2016 | Blonde |

Até 2026, Frank Ocean continua em atividade, mas sem lançar um novo álbum de estúdio desde **Blonde** (2016), mantendo um dos maiores hiatos de sua carreira.
""")
    elif artista =="veigh":
        st.markdown("""
# 🎤 Tudo sobre Veigh

## 📌 Informações pessoais
- **Nome de nascimento:** Thiago Veigh da Silva
- **Nascimento:** 12 de setembro de 2001
- **Local de nascimento:** Itapevi, São Paulo, Brasil
- **Profissão:** Cantor, rapper e compositor
- **Gêneros musicais:** Trap, rap e R&B
- **Anos de atividade:** 2019–presente

## 🌎 Infância
Veigh nasceu em Itapevi, na Grande São Paulo. Desde jovem, teve contato com a música e começou a escrever suas próprias letras. Cresceu ouvindo rap nacional e internacional, influências que moldaram seu estilo.

## ✍️ Início da carreira
Veigh começou lançando músicas de forma independente e ganhou destaque com faixas que viralizaram nas plataformas digitais. Seu crescimento foi impulsionado pelas redes sociais e pelo apoio de outros artistas da cena do trap brasileiro.

## 🎶 Discografia

### Álbum de estúdio
1. **Dos Prédios (2022)**
2. **Dos Prédios Deluxe (2023)**
3. **Eu Venci o Mundo (2024)**

## 🎵 Principais músicas
- Novo Balanço
- Clickbait
- Vida Chique
- Taylor
- Perdoa por Tudo Vida
- Mandraka
- Dos Prédios
- Invisível Pt. 2
- Ballena
- Mônaco Freestyle

## 🤝 Colaborações
Veigh já trabalhou com:
- Teto
- WIU
- Borges
- KayBlack
- MC Cabelinho
- Baco Exu do Blues
- Vulgo FK
- Yunk Vino
- Nagalli
- G.A

## 🏆 Conquistas
- Um dos artistas mais ouvidos do Brasil no Spotify.
- Álbum **Dos Prédios** entre os mais reproduzidos do país.
- Diversos singles presentes nas principais paradas musicais brasileiras.

## 🏠 Vida pessoal
Veigh é conhecido por manter a vida pessoal mais reservada. Em suas músicas, costuma retratar vivências, conquistas e a realidade das periferias de São Paulo.

## 💎 Outros projetos
- Fundador da gravadora **Supernova Entertainment**.
- Participação em festivais e grandes eventos do rap nacional.
- Parcerias com marcas e artistas do cenário urbano.

## 📊 Curiosidades
- O apelido "Veigh" vem do sobrenome "Thiago".
- É um dos principais nomes da nova geração do trap brasileiro.
- O álbum **Dos Prédios** foi um dos maiores sucessos do rap nacional em 2022.
- Suas músicas frequentemente alcançam milhões de reproduções em poucos dias.

## 📀 Álbuns

| Ano | Projeto |
|------|----------|
| 2022 | Dos Prédios |
| 2023 | Dos Prédios Deluxe |
| 2024 | Eu Venci o Mundo |

Atualmente, Veigh é considerado um dos maiores representantes do trap brasileiro, acumulando bilhões de reproduções nas plataformas digitais e uma base de fãs em constante crescimento.
""")
    elif artista ==  "Orochi":
        st.markdown("""
# 🎤 Tudo sobre Orochi

## 📌 Informações pessoais
- **Nome de nascimento:** Flávio César Costa de Castro
- **Nascimento:** 24 de março de 1999
- **Local de nascimento:** São Gonçalo, Rio de Janeiro, Brasil
- **Profissão:** Rapper, cantor, compositor e empresário
- **Gêneros musicais:** Trap, rap e trap-funk
- **Anos de atividade:** 2013–presente
- **Gravadora:** Mainstreet Records

## 🌎 Infância
Orochi nasceu em São Gonçalo, no Rio de Janeiro. Desde a adolescência, desenvolveu interesse pelo rap e começou a participar de batalhas de rima na região, destacando-se pelo freestyle.

## ✍️ Início da carreira
Orochi começou profissionalmente em 2013, aos 14 anos, na Batalha do Tanque. Em 2015, tornou-se o campeão mais jovem da história do Duelo Nacional de MCs, aos 16 anos. Após se afastar das batalhas, passou a investir em sua carreira musical.

## 🎶 Discografia

### EP
- **Trip (2018)**

### Álbuns de estúdio
1. **Celebridade (2020)**
2. **Lobo (2021)**
3. **Vida Cara (2023)**
4. **Vida Cara Deluxe (2023)**
5. **442 (2024)**
6. **Eu Odeio o Dia dos Namorados (2025)**

### Mixtapes
- **Para Todas do Job (2024)**
- **Mixtape Chiró (2025)**

## 🎵 Principais músicas
- Amor de Fim de Noite
- Balão
- Mitsubishi
- Mainstreet
- Mesma História
- Horas Iguais
- Sereia
- To de Gucci
- Acendam as Velas
- Vida Cara
- Poetas no Topo 2

## 🤝 Colaborações
Orochi já trabalhou com:
- Borges
- Oruam
- MC Poze do Rodo
- BIN
- Chefin
- PL Quest
- Filipe Ret
- Tz da Coronel
- Ryan SP
- Caio Luccas

## 🏆 Conquistas
- Campeão nacional do Duelo de MCs em 2015.
- Fundador da Mainstreet Records.
- Um dos principais nomes do trap nacional.
- Bilhões de reproduções nas plataformas digitais.
- Participação no Rock in Rio 2022.

## 🏠 Vida pessoal
Orochi é conhecido por ostentar carros, joias e uma vida de luxo, frequentemente retratada em suas músicas. Apesar disso, mantém parte da vida pessoal reservada.

## 💎 Outros projetos
- Fundador da gravadora **Mainstreet Records**.
- Responsável por impulsionar artistas como Borges, Chefin e Oruam.
- Participações em festivais e grandes eventos do rap nacional.

## 📊 Curiosidades
- Seu nome artístico é inspirado no personagem Orochi, de **The King of Fighters**.
- Foi o campeão mais jovem do Duelo Nacional de MCs.
- Começou nas batalhas de rima aos 14 anos.
- É considerado um dos artistas que popularizaram o trap-funk no Brasil.
- Possui uma tatuagem com o nome "Mainstreet".

## 📀 Álbuns

| Ano | Projeto |
|------|----------|
| 2018 | Trip (EP) |
| 2020 | Celebridade |
| 2021 | Lobo |
| 2023 | Vida Cara |
| 2023 | Vida Cara Deluxe |
| 2024 | 442 |
| 2024 | Para Todas do Job |
| 2025 | Eu Odeio o Dia dos Namorados |
| 2025 | Mixtape Chiró |

Atualmente, Orochi é um dos maiores nomes do trap brasileiro e também um dos empresários mais influentes do gênero através da Mainstreet Records.
""")