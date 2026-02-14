def calculate_penalty_distance(rounds):
    # Determinate the amount of missed targets
    penalty_list = [5-score for score in rounds]
    # Return the total penalty distance
    return sum(penalty_list)*150

if __name__ == '__main__':
    print(calculate_penalty_distance([4, 4]))