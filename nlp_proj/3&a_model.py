from transformers import pipeline

# Load the question-answering model trained on SQuAD (Wikipedia-based)
qa_model = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

# Provide the question
question = "What is artificial intelligence?"

# Ask the question to the Wikipedia-based model
answer = qa_model(question=question, context='wikipedia')

# Print the answer
print("Q:", question)
print("A:", answer["answer"])
