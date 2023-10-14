from nim import play
import pickle 

# Load the trained AI from the pickle file
with open("trained_ai_250k.pkl", "rb") as file:
    ai = pickle.load(file)

play(ai)
