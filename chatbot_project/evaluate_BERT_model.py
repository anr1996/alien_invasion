import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader
from train_BERT_model import PersonaChatDataset # Import the PersonaChatDataset class
import torch

# Load the T5 model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

# load the validation data 
val_df = pd.read_parquet("/Users/adrianrich/Documents/python/chatbot_project/validation-00000-of-00001.parquet")


# Create the validation dataset
val_dataset = PersonaChatDataset(val_df, tokenizer) # Directly pass the DataFrame

# Function to evaluate the model on the validation set
def evaluate_model(model, tokenizer, dataset):
    model.eval()
    predictions, actuals = [], []
    
    data_loader = DataLoader(dataset, batch_size=8)

    with torch.no_grad():
        
        for batch in data_loader:
            input_ids = batch['input_ids']
            attention_mask = batch['attention_mask']
            labels = batch['labels']

            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            preds = torch.argmax(outputs.logits, dim=-1)
            
            predictions.extend(preds.tolist())
            actuals.extend(labels.tolist())
    return predictions, actuals
    
# evaluate the model
predictions, actuals = evaluate_model(model, tokenizer, val_dataset)

# Print a few examples

for i in range(5):
    print(f"Input: {val_df.iloc[i, 0]}")
    print(f"Predicted: {predictions[i]}")
    print(f"Actual: {actuals[i]}")
    print("_" * 50)
