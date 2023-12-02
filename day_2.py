def part1():
    with open('day_2.txt', 'r') as file:
        games = file.readlines()
        sum = 0

        for game in games:
            g = game.split(':')
            game_no = int(g[0].replace("Game ", ""))
            rounds = g[1].split(';')
            print(game_no)
            possible = True

            for round_ in rounds:
                colours = round_.split(',')

                for colour in colours:
                    if 'red' in colour:
                        dice = int(colour.replace(" red", ""))
                        if dice > 12:
                            possible = False
                        # else:
                        #     print('Possible')
                    elif 'green' in colour:
                        dice = int(colour.replace(" green", ""))
                        if dice > 13:
                            possible = False
                        # else:
                        #     print('Possible')
                    elif 'blue' in colour:
                        dice = int(colour.replace(" blue", ""))
                        if dice > 14:
                            possible = False
                        # else:
                        #     print('Possible')

            sum += game_no if possible else 0

        print(sum)


def part2():
    with open('day_2.txt', 'r') as file:
        games = file.readlines()
        sum = 0

        for game in games:
            red = 0
            blue = 0
            green = 0

            g = game.split(':')
            game_no = int(g[0].replace("Game ", ""))
            rounds = g[1].split(';')
            print(game_no)
            for round_ in rounds:
                die = round_.split(', ')
                for dice in die:
                    if 'red' in dice:
                        dice_val = int(dice.replace(" red", ""))
                        if dice_val > red:
                            red = dice_val
                    elif 'green' in dice:
                        dice_val = int(dice.replace(" green", ""))
                        if dice_val > green:
                            green = dice_val
                    elif 'blue' in dice:
                        dice_val = int(dice.replace(" blue", ""))
                        if dice_val > blue:
                            blue = dice_val
            sum += red * blue * green
        print(sum)


part1()
part2()