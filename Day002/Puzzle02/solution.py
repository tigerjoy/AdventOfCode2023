import re

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
        "cube_counts": [],
        "max_count_for_color": {}
    }
    for game in games:
        cube_counts = {}
        for color in patterns:
            pattern = patterns[color]
            match = re.search(pattern, game)
            count = match.group(1) if match else 0
            if count:
                cube_counts[color] = int(count)
                if color not in parsed_games["max_count_for_color"]:
                    parsed_games["max_count_for_color"][color] = int(count)
                elif int(count) > parsed_games["max_count_for_color"][color]:
                    parsed_games["max_count_for_color"][color] = int(count)

        parsed_games["cube_counts"].append(cube_counts)
    
    return parsed_games

if __name__ == "__main__":
    with open("input.txt", "r") as file:
      total = 0
      for line in file:
        game_idx, cube_counts, max_count_for_color = dict.values(parse_game(line))
        power = 1
        for color in max_count_for_color:
            power *= max_count_for_color[color]
        total += power
    
    with open("output.txt", "w") as file:
       file.write(str(total))
