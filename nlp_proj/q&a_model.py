import torch
from transformers import BertTokenizer, BertForQuestionAnswering

# Load pre-trained model and tokenizer
model_name = 'distilbert-base-cased-distilled-squad'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForQuestionAnswering.from_pretrained(model_name)

# Example input
question = "What is area of France?"
context = "France (French: [fʁɑ̃s] Listen), officially the French Republic (French: République française [ʁepyblik " \
          "fʁɑ̃sɛz]),[14] is a country located primarily in Western Europe. It also includes overseas regions and " \
          "territories in the Americas and the Atlantic, Pacific and Indian Oceans,[XII] giving it one of the largest " \
          "discontiguous exclusive economic zones in the world. Its metropolitan area extends from the Rhine to the " \
          "Atlantic Ocean and from the Mediterranean Sea to the English Channel and the North Sea; overseas " \
          "territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, " \
          "the French West Indies, and many islands in Oceania and the Indian Ocean. Its eighteen integral regions (" \
          "five of which are overseas) span a combined area of 643,801 km2 (248,573 sq mi) and had a total population " \
          "of over 68 million as of January 2023.[5][8] France is a unitary semi-presidential republic with its " \
          "capital in Paris, the country's largest city and main cultural and commercial centre; other major urban " \
          "areas include Marseille, Lyon, Toulouse, Lille, Bordeaux, Strasbourg and Nice. capital of france is paris"

# Tokenize input
encoding = tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors="pt")

inputs = encoding['input_ids']  #Token embeddings
sentence_embedding = encoding['token_type_ids']  #Segment embeddings
tokens = tokenizer.convert_ids_to_tokens(inputs[0]) #input tokens

start_scores, end_scores = model(input_ids=torch.tensor(inputs), token_type_ids=torch.tensor(sentence_embedding), return_dict=False)

start_index = torch.argmax(start_scores)

end_index = torch.argmax(end_scores)

answer = ' '.join(tokens[start_index:end_index+1])

corrected_answer = ''

for word in answer.split():

    # If it's a subword token
    if word[0:2] == '##':
        corrected_answer += word[2:]
    else:
        corrected_answer += ' ' + word

print(corrected_answer)
# # Perform inference
# start_scores, end_scores = model(**inputs)
#
# # Find the start and end indices with the highest scores
# start_index = torch.argmax(start_scores)
# end_index = torch.argmax(end_scores)
#
# # Convert token indices to text
# tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"])
# answer = tokens[start_index:end_index+1]
# answer = tokenizer.convert_tokens_to_string(answer)
#
# print("Question: ", question)
# print("Answer: ", answer)
