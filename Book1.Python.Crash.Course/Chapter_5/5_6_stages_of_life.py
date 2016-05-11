age = 14
life_stage = "The person is a {}"

if age < 2:
    print(life_stage.format('baby'))
elif age < 4:
    print(life_stage.format('toddler'))
elif age < 13:
    print(life_stage.format('kid'))
elif age < 20:
    print(life_stage.format('teenager'))
elif age < 65:
    print(life_stage.format('adult'))
else:
    print(life_stage.format('elder'))