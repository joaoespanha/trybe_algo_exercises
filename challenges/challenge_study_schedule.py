def study_schedule(permanence_period, target_time):
    # caso o target time seja nulo retorna None
    if target_time is None:
        return None
    counter = 0
    # percorrer o array de tuplas
    for time_tuple in permanence_period:
        start_time, end_time = time_tuple[0], time_tuple[1]
        # caso haja uma entrada invalda no permanece periodo deve retornar none
        if not isinstance(time_tuple[0], int) or not isinstance(
            time_tuple[1], int
        ):
            return None
        # checkar se o target time esta no intervalo de inteiros das tuplas
        if start_time <= target_time <= end_time:
            # adicionar +1 no contador caso esteja
            counter += 1
    # retornar o contador
    return counter


if __name__ == "__main__":
    permanence_period = [(2, 4), (1, 2), (2, 3), (2, 5), (4, 5), (4, 5)]
    print(study_schedule(permanence_period, 3))
