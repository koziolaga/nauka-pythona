def print_dict(d):
    for key in samolot:
        print("{0}:{1}".format(key, samolot[key]))

if __name__ == "__main__":
    samolot = {'name': 'boeing',
                'przebieg': 10000,
                'type': 'pasazerski'}

    print_dict(samolot)
