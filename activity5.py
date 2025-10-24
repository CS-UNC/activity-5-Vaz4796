def more_than_20(file):
    wordls_20 = []

    with open(file, 'r') as worlds_file:

        for worlds in worlds_file:

            world = worlds.strip()
            len(world)
            if len(world) > 20:
                wordls_20.append(world)


    return wordls_20