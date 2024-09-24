from transformers import BertTokenizer, BertForSequenceClassification

# Load the model and tokenizer from the last checkpoint
model = BertForSequenceClassification.from_pretrained('/Users/adrianrich/Documents/python/chatbot_project/results/checkpoint-6705')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Save the model and tokenizer to the results directory
model.save_pretrained('/Users/adrianrich/Documents/python/chatbot_project/results')
tokenizer.save_pretrained('/Users/adrianrich/Documents/python/chatbot_project/results')