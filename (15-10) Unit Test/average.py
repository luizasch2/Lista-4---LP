def average_scores(scores: dict) -> float:
    try:
        aux = scores.values()
        score = list(aux)
        return sum(score)/len(score)
    except AttributeError as error:
        raise TypeError
    






    