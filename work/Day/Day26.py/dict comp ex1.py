sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

sentence_to_list = sentence.split()

new_dict = {sentence:len(sentence) for sentence in sentence_to_list}
print(new_dict)

