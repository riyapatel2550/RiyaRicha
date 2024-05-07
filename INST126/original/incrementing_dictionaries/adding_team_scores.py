# adding team scores

team_scores = {"team 1" : 10,
              "team 1" : 17}

print(team_scores["team 1"])
team_scores["team 1"] += 5
print(team_scores)

team_scores["team 3"] += 12
print(team_scores)
team_name = "team 84"
team_score = 16
if team_name in team_scores.keys():
    # if the team is in teh dift already, increment
    team_scores[team_name] += team_score
else:
    # if not, assign the value to a new entry
    team_scores[team_name] = team_score

print(team_scores)

# Turn this into a function

# Steps to make a good function
# 0. Come up with a name and start the def line
# 1. Figure out what you want out of this function
# 2. Figure out what you want the input to be (argument)
# 3. Figure out how to get from input (arguments) to output (arguments)
# 4. Test it
# 5. Write a helpful docstring

def add_scores_to_team_dictionary(team_dict, score, name):
    """
    Takes a dictionary of team scores, and then a name 
    and score of a team, and either adds to the team's 
    score, or creates an entry if that team is not already 
    in the dictionary.
    """
    if team_name in team_dict.keys():
    # if the team is in the difc already, increment
        team_dict[name] += score
    else:
    # if not, assign the value to a new entry
        team_dict[name] = score
    return None

#team_scores = {"team 1" : 10,
#              "team 1" : 17}

#add_scores_to_team_dictionary(team_scores, "team 82", 34)
#print(team_scores)
#add_scores_to_team_dictionary(team_scores, "team 2", 13)
