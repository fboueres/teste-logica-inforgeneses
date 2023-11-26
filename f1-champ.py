# condição para parar o algoritmo caso a linha seja '0 0'
running = True

while running: 
  # recebe a primeira linha
  user_input = input().split(' ')

  if user_input == ['0', '0']:
    running = False
    break
# fim da condição para parar o algoritmo caso a linha seja '0 0'
  
  # posições dos pilotos em cada grande prêmio
  grand_prixs_positions = []
  
  for i in range(int(user_input[0])):
    grand_prixs_positions.append(input().split(' '))
  # recebe as posições de cada piloto em cada grande prêmio

  # número de pilotos
  pilots = int(user_input[1])
  
  # hash map {piloto: pontos}
  pilots_points = {}
  
  # inicializa o hash map com todos os pilotos com a pontuação igual a 0
  for pilot in range(pilots):
    pilots_points[str(pilot+1)] = 0
  
  # sistemas de pontuação  
  points_systems = []
  
  for i in range(int(input())):
    user_input = input().split(' ')
    
    # realiza uma compreensão de lista para separar até que posição pontua das pontuações por posição
    points_systems.append([user_input[0], user_input[1:]])
  
  # bloco de código para descobrir os campeões mundiais
  for points_system in points_systems:
    for positions in grand_prixs_positions:
      # recebe os pilotos que marcaram pontos no grande prêmio
      pilots_awarded = positions[:int(points_system[0])]
  
      # adiciona as pontuações ao piloto de acordo com a sua posição
      for index, pilot_awarded in enumerate(pilots_awarded):
        pilots_points[pilot_awarded] += int(points_system[1][index])
  
    # maior número de pontos acumulados
    max_points = max(pilots_points.values())
  
    # compreensão de lista para receber os pilotos que tiveram as pontuações mais altas
    champions_pilots = [
      pilot for pilot, points in pilots_points.items() 
        if points == max_points
    ]
  
    # transforma o número de identificação do piloto de string para int
    champions_pilots = [int(num) for num in champions_pilots]
  
    # para poder ordenar numericamente
    champions_pilots.sort()
  
    # cria o texto de saída com os pilotos campeões
    print(' '.join(map(str, champions_pilots)))
  
    # zera a pontuação de todos os pilotos para poder realizar o algoritmo para o próximo sistema de pontuações
    for pilot in pilots_points:
      pilots_points[pilot] = 0