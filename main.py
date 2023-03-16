import generator as gen # bring over the functions for generating names.

repeat = "y"

while repeat.lower() == 'y':
    Race = input("What is your character's race?: ")
    Sex = input("What is your character's sex?: ")

    # male name generators
    if Race.lower() == 'altmer' and Sex.lower() == 'male':
        gen.altgenm()

    if Race.lower() == 'argonian' and Sex.lower() == 'male':
        gen.arggenm()

    if Race.lower() == 'bosmer' and Sex.lower() == 'male':
        gen.bosgenm()

    if Race.lower() == 'breton' and Sex.lower() == 'male':
        gen.bregenm()

    if Race.lower() == 'dunmer' and Sex.lower() == 'male':
        gen.dungenm()

    if Race.lower() == 'khajiit' and Sex.lower() == 'male':
        gen.khagenm()

    if Race.lower() == 'nord' and Sex.lower() == 'male':
        gen.nordgenm()

    if Race.lower() == 'redguard' and Sex.lower() == 'male':
        gen.redgenm()

    # female name generators
    if Race.lower() == 'altmer' and Sex.lower() == 'female':
        gen.altgenf()

    if Race.lower() == 'argonian' and Sex.lower() == 'female':
        gen.arggenf()

    if Race.lower() == 'bosmer' and Sex.lower() == 'female':
        gen.bosgenf()

    if Race.lower() == 'breton' and Sex.lower() == 'female':
        gen.bregenf()

    if Race.lower() == 'dunmer' and Sex.lower() == 'female':
        gen.dungenf()

    if Race.lower() == 'khajiit' and Sex.lower() == 'female':
        gen.khagenf()

    if Race.lower() == 'nord' and Sex.lower() == 'female':
        gen.nordgenf()

    if Race.lower() == 'redguard' and Sex.lower() == 'female':
        gen.redgenf()

    repeat = input("Rerun the program? (Y/N): ")
