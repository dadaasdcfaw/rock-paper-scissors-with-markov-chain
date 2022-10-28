# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
def score_increment(player,opp):
  #print(player,'-', opp)
  if player=='R':
    if opp=='R':return -1
    elif opp=='P':return -2
    elif opp=='S':return 1
    
  if player=='P':
    if opp=='R': return 1
    elif opp=='P':return -1
    elif opp=='S': return -2
      
  if player=='S':
    if opp=='R':return -2
    elif opp=='P': return 1
    elif opp=='S': return -1
  
  


def player(prev_opponent_play, opponent_history=[],
           play_order=[{
             "RRR": 0,
             "RRP": 0,
             "RRS": 0,             
             "RPR": 0,
             "RPP": 0,
             "RPS": 0,
             "RSR": 0,
             "RSP": 0,
             "RSS": 0,
             
             "PRR": 0,
             "PRP": 0,
             "PRS": 0,
             "PPR": 0,
             "PPP": 0,
             "PPS": 0,
             "PSR": 0,
             "PSP": 0,
             "PSS": 0,
             
             "SRR": 0,
             "SRP": 0,
             "SRS": 0,
             "SPR": 0,
             "SPP": 0,
             "SPS": 0,
             "SSR": 0,
             "SSP": 0,
             "SSS": 0,
           }]):
    if not prev_opponent_play:
        prev_opponent_play = 'R'
        opponent_history.append(prev_opponent_play)
    opponent_history.append(prev_opponent_play)

    last_three = "".join(opponent_history[-3:])
    last_two = "".join(opponent_history[-2:])
    if len(last_three) == 3:
        play_order[0][last_three] += 1

    potential_plays = [
        last_two + "R",
        last_two + "P",
        last_two + "S",
    ]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }
    prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]
