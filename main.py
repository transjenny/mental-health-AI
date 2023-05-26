print("welcome to the mental help app\nthis app is there to help you no matter how your feeling\nI hope this makes you feel better!")

print("starting")
def talk_loop():
    while True:
        a = input("you:")
        if "goodbye" in a:
            print("i hope i made you feel better")
            exit()
        elif "sos" in a:
            print("i cannot help you right now!!!\n call emergency services!!!")
        elif "idk" in a:
            if "gender" in a:
                print(
                    "questioning your gender can be hard but remember that people are with you can help you!\n places "
                    "like r/lgbt and other LGBTQIA community's can help you ask about yourself.\n Good like on your "
                    "journey on gender identity!")
            if "why" in a:
                if "exist" in a:
                    print("you exist to make a difference! so go make one!")
        elif "questioning" in a:
            if "gender" in a:
                print("questioning your gender can be hard but remember that people are with you can help you!\n places "
                      "like r/lgbt and other LGBTQIA community's can help you ask about yourself.\n Good like on your "
                      "journey on gender identity!")
        elif "think im" in a:
            if "trans" in a:
                print("its ok to think that your trans. try joining some LGBTQIA community`s and seeing what you can "
                      "do!\ngood luck being trans");
            if "bi" in a:
                print("its ok to think that your bi. try joining some LGBTQIA community`s and seeing what you can "
                      "do!\ngood luck being bi");
            if "gay" in a:
                print("its ok to think that your gay. try joining some LGBTQIA community`s and seeing what you can "
                      "do!\ngood luck being gay")
            if "stupid" in a:
                print("there is not a thing called being 'stupid'. people are just bad at somethings")
        elif "im" in a:
            if "feeling" in a:
                if "down" in a:
                    print("I know how that feels and its bad but if you have friends they will be a good source of "
                          "happiness! just best of luck! \n if you ever are feeling suicidal call the suicide hotline")
                if "happy" in a:
                    print("thats great and remember have fun!!")
                if "sad" in a:
                    print("I know how that feels and its bad but if you have friends they will be a good source of "
                          "happiness! just best of luck! \n if you ever are feeling suicidal call the suicide hotline")
                if "suicidal" in a:
                    print("OMG, look no matter how you feel suicide is not the right way!\ncall the suicide hotline "
                          "they will help you more!!!")
                if "depressed" in a:
                    print("ok im just a AI but i will try my best here.\n"
                          "if you feel depressed i know that can be hard ive been there!\n"
                          "when i was there i was almost always sad and was trying to be happy.\n"
                          "but all i can say is try to get HELP. if your under 18 goto kidshelpline.\n"
                          "if your over 18 use Blue Knot Foundation Helpline!\n remember if your ever feeling feeling "
                          "suicidal call the suicide hotline they will help you!")
            elif "bad" in a:
                if "everything" in a:
                    print("your NOT bad at everything just 'bad' at somethings and you can get better as stuff!")
            else:
                print("no answer for that submitting now")
                print("try updating")
print("done")
talk_loop()

