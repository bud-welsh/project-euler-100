# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

run = True
answer = 40

while run == True:
    if answer % 19 == 0:
        if answer % 18 == 0:
            if answer % 17 == 0:
                if answer % 16 == 0:
                    if answer % 15 == 0:
                        if answer % 14 == 0:
                            if answer % 13 == 0:
                                if answer % 12 == 0:
                                    if answer % 11 == 0:
                                        run = False
                                        print(answer)
                                    else:
                                        answer = answer + 20
                                else:
                                    answer = answer + 20
                            else:
                                answer = answer + 20
                        else:
                            answer = answer + 20
                    else:
                        answer = answer + 20
                else:
                    answer = answer + 20
            else:
                answer = answer + 20
        else:
            answer = answer + 20
    else:
        answer = answer + 20