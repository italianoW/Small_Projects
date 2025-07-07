import numpy as np
import random

# Maze layout (0 = livre, 1 = parede, 2 = trap)
maze_5x5 = [[0, 0, 1, 2, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 2, 0, 2],
            [0, 1, 2, 1, 2],
            [0, 0, 0, 0, 0]]

maze_20x20 = [[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
              [0, 0, 2, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
              [0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
              [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
              [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0],
              [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
              [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
              [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
              [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
              [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
              [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 1, 2],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

maze = maze_20x20

rows, cols = len(maze), len(maze[0])
goal_state = (rows-1, cols-1)
start_state = (0, 0)

# Ações
actions = ['up', 'down', 'left', 'right']
action_dict = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
n_actions = len(actions)

# Tabela Q
Q = np.zeros((rows, cols, n_actions))

# Hiperparâmetros
alpha = 0.1      # taxa de aprendizado : Controls how much new information overrides old Q-values.
gamma = 0.9      # fator de desconto : Determines the importance of future rewards versus immediate rewards.
epsilon = 0.1    # taxa de exploração : Probability of choosing a random action (explore) instead of the best-known action (exploit).
episodes = 1000  # número de episódios

# Verifica se uma posição é válida
def is_valid(maze, state):
    x, y = state
    if 0 <= x < rows and 0 <= y < cols:
        return maze[x][y] != 1
    return False

# Executa uma ação
def step(state, action_index):

    dx, dy = action_dict[actions[action_index]]
    new_state = (state[0] + dx, state[1] + dy)
    if not is_valid(maze, new_state):
        return state, -69  # parede ou fora dos limites e penalidade
    if new_state == goal_state:
        return new_state, 10  # recompensa por chegar ao objetivo
    x ,y = new_state
    if maze[y][x] == 2:
        return new_state, -4 #penalidade por bomba + passo
    return new_state, -1  # penalidade por passo

# Escolhe uma ação (ε-greedy)
def choose_action(state):
    if random.random() < epsilon:
        return random.randint(0, n_actions - 1)
    return np.argmax(Q[state[0], state[1]])

# Treinamento
for _ in range(episodes):
    
    state = start_state
    
    while state != goal_state:
        
        action_index = choose_action(state)
        next_state, reward = step(state, action_index)
            


        # Atualiza Q-table
        max_future_q = np.max(Q[next_state[0], next_state[1]])
        current_q = Q[state[0], state[1], action_index]
        Q[state[0], state[1], action_index] += alpha * (reward + gamma * max_future_q - current_q)

        state = next_state

  # Teste do caminho aprendido
state = start_state
path = [state]
while state != goal_state:
    action = np.argmax(Q[state[0], state[1]])
    state, _ = step(state, action)
    path.append(state)

print("Caminho aprendido:")
print(path,"\n",len(path))
