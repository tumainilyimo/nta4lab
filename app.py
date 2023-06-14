number = random.randint(1, 100)

guess = st.number_input("Enter a number (between 1 and 100):", min_value=1,max_value=100)

if st.button('Make a guess!'):
    if guess > number:
        st.write('Too high! Try a smaller number.')
    elif guess < number:
        st.write('Too low! Try a larger number.')
    else:
        st.write('Congratulations! You have guessed the number correctly.')
