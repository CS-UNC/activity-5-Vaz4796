def more_than_20(file):
    wordls_20 = []

    with open(file, 'r') as worlds_file:

        for worlds in worlds_file:

            world = worlds.strip()
            len(world)
            if len(world) > 20:
                wordls_20.append(world)


    return wordls_20



def has_no_e(word):
    return "e" not in word


def uses_only(worlds, letters):
    return set(worlds).issubset(set(letters))


def all_uses_only(file, letter):
    only_worlds = []

    with open(file, 'r') as worlds_file:
        for world in worlds_file:
            worlds = world.strip()
            if worlds and uses_only(worlds, letter):
                 only_worlds.append(worlds)
    return only_worlds