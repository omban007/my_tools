import torch
from transformers import BertTokenizer, BertForQuestionAnswering

# Load pre-trained model and tokenizer
model_name = 'bert-large-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForQuestionAnswering.from_pretrained(model_name)

# Example input
question = "What is the capital of France?"
context = "France, officially the French Republic is a country whose capital is Paris."

# Tokenize input
inputs = tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors="pt")

# Perform inference
start_scores, end_scores = model(**inputs, return_dict=False)

# Find the start and end indices with the highest scores
start_index = torch.argmax(start_scores)
end_index = torch.argmax(end_scores)

# Convert token indices to text
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"].squeeze())
answer = tokens[start_index:end_index+1]
answer = tokenizer.convert_tokens_to_string(answer)

print("Question: ", question)
print("Answer: ", answer)
