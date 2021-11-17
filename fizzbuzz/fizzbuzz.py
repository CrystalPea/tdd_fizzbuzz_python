def fizzbuzz(number):
    if number % 3 == 0:  # modulo, or remainder after division
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number
