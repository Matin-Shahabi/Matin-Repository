def positive_numbers():
    n = 1
    while True:
        yield n
        n += 1

def is_valid(n):
    digits = [int(d) for d in str(n)]
    return all(d % 2 == 1 for d in digits) and sum(digits) == 5

def valid_numbers():
    for num in positive_numbers():
        if is_valid(num):
            yield num

def count_digit_7(n):
    return str(n).count('7')

def process_stream():
    count = 0
    max_sevens = -1
    best_number = None


    for num in valid_numbers():
        if count >= 50:
            break
        count += 1

        num_sevens = count_digit_7(num)
        if num_sevens > max_sevens:
            max_sevens = num_sevens
            best_number = num

result = process_stream()
print("عددی که بیشترین تعداد رقم ۷ را دارد:", result)
