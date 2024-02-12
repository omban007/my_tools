from transformers import DistilBertTokenizer, DistilBertModel
import torch
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-cased-distilled-squad')
model = DistilBertModel.from_pretrained('distilbert-base-cased-distilled-squad')

question, text = "Who was Jim Henson?", "Jim Henson was a nice puppet"

inputs = tokenizer(question, text, return_tensors="pt")
with torch.no_grad():
    start_scores, end_scores = model(**inputs, return_dict=False)

    # Find the start and end indices with the highest scores
    start_index = torch.argmax(start_scores)
    end_index = torch.argmax(end_scores)

    # Convert token indices to text
    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"].squeeze())
    answer = tokens[start_index:end_index + 1]
    answer = tokenizer.convert_tokens_to_string(answer)

    print("Question: ", question)
    print("Answer: ", answer)

