import re

def is_valid_game(cube_counts):
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    for cube_count in cube_counts:
      for color in limits:
          if color not in cube_count:
              continue
          if cube_count[color] > limits[color]:
              return False
    
    return True

def parse_game(line):
  line = line.strip().lower()
  game_idx, games = line.split(":")
  games = games.split(";")
  match = re.search("\d+", game_idx)
  idx = int(match.group()) if match else 0
  patterns = {
      "red": "(\d+) red",
      "green": "(\d+) green",
      "blue": "(\d+) blue"
  }
  parsed_games = {
      "game_idx": idx,
      "cube_counts": []
  }
  for game in games:
      cube_counts = {}
      for color in patterns:
          pattern = patterns[color]
          match = re.search(pattern, game)
          count = match.group(1) if match else 0
          if count:
              cube_counts[color] = int(count)
      
      parsed_games["cube_counts"].append(cube_counts)
  
  return parsed_games

if __name__ == "__main__":
    with open("input.txt", "r") as file:
      total = 0
      for line in file:
        game_idx, cube_counts = dict.values(parse_game(line))
        total += game_idx if is_valid_game(cube_counts) else 0
    
    with open("output.txt", "w") as file:
       file.write(str(total))
