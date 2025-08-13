from predict import predict_message

while True:
    user_input = input("Enter your message (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    result = predict_message(user_input)
    print("Prediction:", result)