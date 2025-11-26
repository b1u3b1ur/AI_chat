from the_cleaner import clean
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

training = "train_clean.txt"
chatbot = ChatBot("Paul")

trainer = ListTrainer(chatbot)
cleaned_c = clean(training)
trainer.train(cleaned_c)

exit_conditions = ("q","quit","exit")

while True:
    query = input("Paul> ")
    if query in exit_conditions:
        break
    else:
        print(f"Paul {chatbot.get_response(query)}")
