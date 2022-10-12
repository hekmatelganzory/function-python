#Task 1

def get_score(**scores):

  for item, value in scores.items():

    print(f"{item} => {value}")

get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)


# Task 2

def get_people_scores(name="Unknown", **scores):

  if name != "Unknown":

    if len(scores) == 0:

      print(f"Hello {name} You Have No Scores To Show")

    else:

      print(f"Hello {name} This Is Your Score Table:")

  for item, value in scores.items():

    print(f"{item} => {value}")

get_people_scores("Samy", Math=90, Science=80, Language=70)
get_people_scores("Ahmed", Logic=70, Problems=60)
get_people_scores(Logic=70, Problems=60)
get_people_scores("Dina")


#Task 3

scores_list = {
  "Math": 90,
  "Science": 80,
  "Language": 70
}

def get_the_scores(name="Unknown", **scores):

  if name != "Unknown":

    if len(scores) == 0:

      print(f"Hello {name} You Have No Scores To Show")

    else:

      print(f"Hello {name} This Is Your Score Table:")

  for item, value in scores.items():

      print(f"{item} => {value}")

get_the_scores("Ahmed", **scores_list)
get_the_scores("Osama", **scores_list)
