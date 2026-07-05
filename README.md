**Portuguese Version:**

# Humberto Ex Slayer

Projeto final da disciplina de Introdução à Programação, desenvolvido por:
- **Pedro Alves de França**
- **Tom Maciel Nogueira**  
- **Pedro Sabino Pinho Azevedo** 
- **Gabriel Pereira do Nascimento** 
- **Gabriel Lira Pinto Jansen** 
- **José Vinícius Flor Vila Nova**
  
utilizando Python e Pygame.

## Sobre o projeto

Humberto Ex Slayer é um jogo 2D inspirado em títulos do gênero Run and Gun, como Metal Slug e Cuphead. O jogador controla Humberto, um estudante que precisa explorar os corredores e salas do Centro de Informática (CIn), coletando power-ups para adquirir novas habilidades e enfrentar os inimigos que surgem durante a jornada.

O projeto teve como objetivo consolidar os conceitos de lógica de programação e da linguagem Python aprendidos ao longo da disciplina, além de proporcionar experiência prática com Git, GitHub e desenvolvimento colaborativo.

## Controles

| Tecla | Ação |
|-------|------|
| A | Mover para a esquerda |
| D | Mover para a direita |
| W | Pular |
| O | Ataque básico |
| P | Dash |
| I | Ataque especial |

## Arquitetura do projeto
├── Assets/
│ ├── Audio/
│ ├── Sprites/
│ └── ...
├── constantes.py
├── entities.py
├── game.py
└── README.md

### constantes.py
Centraliza todas as configurações globais do jogo, como dimensões da janela, parâmetros físicos (gravidade e força do pulo), tempos de recarga (cooldowns) e definição das cores utilizadas.

### entities.py
Implementa a camada de domínio do jogo, contendo a estrutura das entidades. Utiliza uma classe base para concentrar comportamentos comuns e classes derivadas para representar o jogador e os diferentes tipos de inimigos.

### game.py
Representa o núcleo da aplicação. É responsável por inicializar o Pygame, carregar os assets, controlar o loop principal do jogo, gerenciar colisões, renderizar os elementos gráficos e controlar a navegação entre as telas.

## Tecnologias utilizadas

- Python
- Pygame
- Git
- GitHub
- Visual Studio Code
- sys (Python Standard Library)

## Recursos gráficos

Durante o desenvolvimento foram utilizados sprites produzidos e adaptados pela equipe, além de recursos obtidos através do The Spriters Resource e apoio do Gemini para concepção de alguns elementos visuais.

## Objetivos de aprendizagem

- Lógica de programação
- Programação Orientada a Objetos
- Desenvolvimento de jogos em Python
- Controle de versão com Git
- Trabalho colaborativo utilizando GitHub

## Tutorial de inicialização do Jogo

-Antes de iniciar, certifique-se de que o Python 3 esteja instalado em seu computador.
-Clone este repositório:
-git clone <https://github.com/pedroalvesdefranca-dev/intro-programming-final-project.git> 
-Acesse a pasta do projeto:
-cd <intro-programming-final-project>
-Instale a biblioteca Pygame:
-pip install pygame
-Execute o jogo:
-python game.py

**English Version:**

# Humberto Ex Slayer

Final project for the Introduction to Programming course, developed using Python and Pygame.

## About the Project

Humberto Ex Slayer is a 2D game inspired by classic Run and Gun titles such as Metal Slug and Cuphead. The player controls Humberto, a student who must explore the corridors and rooms of the Center for Informatics (CIn), collecting power-ups to gain new abilities and become strong enough to defeat the enemies encountered throughout the adventure.

The main goal of this project was to reinforce the programming logic and Python concepts learned during the course, while also providing practical experience with Git, GitHub, and collaborative software development.

## Controls
|Key | Action|
|....|.......|
| A |	Move left |
| D | Move right |
| W |	Jump |
| O |	Basic attack |
| P |	Dash |
| I |	Special attack |

## Project Architecture
├── Assets/
│   ├── Audio/
│   ├── Sprites/
│   └── ...
├── constantes.py
├── entities.py
├── game.py
└── README.md

## constantes.py

Centralizes the game's global settings, including screen dimensions, physics parameters (gravity and jump force), cooldown timers, and color definitions.

## entities.py

Implements the game's domain layer by defining all game entities. It uses a base class to encapsulate shared behaviors and specialized subclasses for the player character and different enemy AI types.

## game.py

Represents the core of the application. It initializes Pygame, loads the game assets, runs the main game loop, handles collision detection, renders graphics, and manages screen transitions.

## Technologies Used

- Python
- Pygame
- Git
- GitHub
- Visual Studio Code
- sys (Python Standard Library)
- Graphic Resources

During development, the team created and adapted several sprites. Additional visual assets were obtained from The Spriters Resource, while Google Gemini was used as a creative assistant during the conceptual design of some environments and graphical elements.

## Learning Objectives

- Programming Logic
- Object-Oriented Programming (OOP)
- Game Development with Python
- Version Control using Git
- Collaborative Development with GitHub

## Getting Started

- Before running the game, make sure Python 3 is installed on your computer.
- Clone this repository:
- git clone https://github.com/pedroalvesdefranca-dev/intro-programming-final-project.git
- Navigate to the project directory:
- cd intro-programming-final-project
- Install the Pygame library:
- pip install pygame
- Run the game:
- python game.py
