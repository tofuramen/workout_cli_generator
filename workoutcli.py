import random

big_backworkouts = ['deadlift', 'trapbar deadlift']
big_legworkouts = ['backsquat', 'frontsquat', 'deadlift']
big_chestworkouts = ['Barbell Bench Press', 'Dumbbell Bench Press']
big_shoulderworkouts = ['Standing Military Press', 'Seated Military Press']

back_workouts = ['Underhand Bent-Over Row', 'Overhand Bent-Over Row', 'Pull-ups', 'Lat Pull-down',
                 'Single-Arm Dumbbell Row', 'Seated-Row', 'T-Bar Row', 'Good-mornings']

leg_workouts = ['Romanian Deadlift', 'Leg Press', 'Calf Raises', 'Bulgarian Split Squats', 'Dumbbell Lunges',
                'Bar-Bell Calf Raises', 'Dumbbell Step-Up',
                'Swiss-Ball Leg Curl', 'Reverse-Lunge', 'Body weight Jump Squats', 'Hip-Thrusts', 'Overhead Squats',
                'Kettlebell/Dumbbell Goblet Squat']

chest_workouts = ['Incline Dumbbell-Press', 'Incline Bench Press', 'Incline Dumbbell Fly',
                  'Cable-Crossover', 'Chest-Press Machine', 'Dumbbell Fly', 'Low Cable-Crossover', 'Landmine Press',
                  'Floor Press', 'Push-ups', 'Dips']

shoulder_workouts = ['Barbell Shoulder Shrug', 'Dumbbell Shoulder Shrug', 'Wide-Grip Dips', 'Wide-grip bench press',
                     'wide push-ups', 'Farmer’s Walk', 'Bent-Over Reverse Fly', 'Front Raise', 'Lateral Raise']

bicep_workouts = ['Bicep-Curls', 'Incline Dumbbell Curl', 'Hammer curl', 'Reverse Barbell Curl',
                  'Standing Cable Curl', 'concentration curl', 'preacher curl']

tricep_workouts = ['Close-Grip Bench Press', 'Cable Rope Tricep Pushdown', 'Lying Tricep Extension',
                   'Tricep Dips', 'Diamond Push-ups', 'Standing Tricep Extension', 'one-arm kettlebell floor press']

core_workouts = ['Plank', 'Hanging Knee-raise', 'Side-Plank', 'Leg Raise', 'Flutter Kicks', 'Mountain Climbers',
                 'Ab Wheel-rollout',
                 'Russian Twists', 'Swiss-ball crunches', 'Situp and throw', 'Medicine Ball V-up', 'Weighted-Situp']

# print(random.sample(core_workouts, 2))

upperbody = big_chestworkouts + big_shoulderworkouts + big_backworkouts
upperbody_accessory = chest_workouts + tricep_workouts + shoulder_workouts + bicep_workouts
lowerbody = big_legworkouts
lowerbody_accessory = leg_workouts + core_workouts
fullbody = upperbody + lowerbody
fullbody_accessory = chest_workouts + tricep_workouts + shoulder_workouts + bicep_workouts + leg_workouts + core_workouts


def compound_workout(difficulty, which_compound):
    print(
        f"Okay your difficulty level is {workout_difficulty.lower()} and you chose a compound workout for your {compound_type.lower()}.") 

    while difficulty.lower() == "groovy":
        if which_compound.lower() == "upperbody":
            print(random.sample(upperbody, 1))
            print(random.sample(upperbody_accessory, 4))
        elif which_compound.lower() == "lowerbody":
            print(random.sample(lowerbody, 1))
            print(random.sample(lowerbody_accessory, 3))
        else:
            print(random.sample(fullbody, 2))
            print(random.sample(fullbody_accessory, 2))
        break

    while difficulty.lower() == "wildin":
        if which_compound.lower() == "upperbody":
            print(random.sample(upperbody, 2))
            print(random.sample(upperbody_accessory, 5))
        elif which_compound.lower() == "lowerbody":
            print(random.sample(lowerbody, 2))
            print(random.sample(lowerbody_accessory, 5))
        else:
            print(random.sample(fullbody, 2))
            print(random.sample(fullbody_accessory, 5))
        break


def bodysplit_workout(difficulty, primary_muscle, secondary_muscle):
    print(
        f'Okay your difficulty level is {split_difficulty.lower()}. The primary muscle you chose is: {primary.lower()} and the secondary muscle you chose is: {secondary.lower()}.') 

    while difficulty.lower() == "groovy":
        if primary.lower() == "legs":
            print(random.sample(big_legworkouts, 1))
            print(random.sample(leg_workouts, 3))
        elif primary.lower() == "chest":
            print(random.sample(big_chestworkouts, 1))
            print(random.sample(chest_workouts, 3))
        elif primary.lower() == "back":
            print(random.sample(big_backworkouts, 1))
            print(random.sample(back_workouts, 3))
        else:
            print(random.sample(big_shoulderworkouts, 1))
            print(random.sample(shoulder_workouts, 3))
        break

    while difficulty.lower() == "wildin":
        if primary.lower() == "legs":
            print(random.sample(big_legworkouts, 1))
            print(random.sample(leg_workouts, 5))
        elif primary.lower() == "chest":
            print(random.sample(big_chestworkouts, 1))
            print(random.sample(chest_workouts, 5))
        elif primary.lower() == "back":
            print(random.sample(big_backworkouts, 1))
            print(random.sample(back_workouts, 5))
        else:
            print(random.sample(big_shoulderworkouts, 1))
            print(random.sample(shoulder_workouts, 5))
        break

    while True:
        if secondary.lower() == "shoulders":
            print(random.sample(shoulder_workouts, 3))
        elif secondary.lower() == "core":
            print(random.sample(core_workouts, 3))
        elif secondary.lower() == "core":
            print(random.sample(tricep_workouts, 3))
        else:
            print(random.sample(bicep_workouts, 3))
        break


question1 = "What level of difficulty do you want for you workouts? Groovy or Wildin? "
workout_difficulty = " "
split_difficulty = " "

question2 = "What kind of workout would you like? Compound or split? "
workout_type: str = " "

question3 = "Do you want to do upperbody, lowerbody or fullbody? "
compound_type = " "

question4 = "What is the primary muscle group? Chest, Back, Legs or Shoulders? "
primary = " "

question5a = "What is the secondary muscle group? Triceps, Biceps, Shoulders or core? "
question5b = "What is the secondary muscle group? Triceps, Biceps or core? "
secondary = " "

while True:
    workout_type = input(question2)
    if workout_type.lower() == 'compound':
        workout_difficulty = input(question1)
        compound_type = input(question3)
        compound_workout(workout_difficulty, compound_type)
    else:
        split_difficulty = input(question1)
        primary = input(question4)
        if primary.lower() == 'shoulders':
            secondary = input(question5b)
            bodysplit_workout(split_difficulty, primary.lower, secondary)
        else:
            secondary = input(question5a)
            bodysplit_workout(split_difficulty, primary.lower, secondary)
    break























