from fizzbuzz.src import fizz_buzz_game

valid_input = [1, 2, 3, 5, 9, 15, 30, 29, 91, 90,100, 101]
invalid_input = [0, -3, -15, 3.0, 'three']
def test_fizz_buzz():

    assert fizz_buzz_game.fizz_buzz(valid_input[0]) == 1
    assert fizz_buzz_game.fizz_buzz(valid_input[1]) == 2
    assert fizz_buzz_game.fizz_buzz(valid_input[2]) == "Fizz"
    assert fizz_buzz_game.fizz_buzz(valid_input[3]) == "Buzz"
    assert fizz_buzz_game.fizz_buzz(valid_input[4]) == "Fizz"
    assert fizz_buzz_game.fizz_buzz(valid_input[5]) == "Fizz Buzz"
    assert fizz_buzz_game.fizz_buzz(valid_input[6]) == "Fizz Buzz"
    assert fizz_buzz_game.fizz_buzz(valid_input[7]) == 29
    assert fizz_buzz_game.fizz_buzz(valid_input[8]) == 91
    assert fizz_buzz_game.fizz_buzz(valid_input[9]) == "Fizz Buzz"
    assert fizz_buzz_game.fizz_buzz(valid_input[10]) == "Buzz"
    assert fizz_buzz_game.fizz_buzz(valid_input[11]) == 101


def test_fizz_buzz_negative():

    assert fizz_buzz_game.fizz_buzz(invalid_input[0]) == "only positive integers are allowed"
    assert fizz_buzz_game.fizz_buzz(invalid_input[1]) == "only positive integers are allowed"
    assert fizz_buzz_game.fizz_buzz(invalid_input[2]) == "only positive integers are allowed"
    assert fizz_buzz_game.fizz_buzz(invalid_input[3]) == "only positive integers are allowed"
    assert fizz_buzz_game.fizz_buzz(invalid_input[4]) == "only positive integers are allowed"