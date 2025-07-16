def make_positive_number():
    current = [1]

    def next_number():
        val = current[0]
        current[0] += 1
        return val
    return next_number

def is_valid(n):
    digits = [int(d) for d in str(n)]
    return len(digits) % 2 == 1 and sum(digits) % 5 == 0

def valid_numbers(next_positive):
    while True:
        num = next_positive()
        if is_valid(num):
            yield num

def count_digit_7(n):
    return str(n).count('7')

def final():
    next_positive = make_positive_number()
    valid_gen = valid_numbers(next_positive)
    count = 0
    max_sevens = 0
    best_number = None
    while count < 50:
        num = next(valid_gen)
        count += 1
        sevens = count_digit_7(num)
        if sevens > max_sevens:
            max_sevens = sevens
            best_number = num

    return best_number

result = final()
print("عددی با بیشترین رقم 7 (از بین 50 عدد معتبر):", result)