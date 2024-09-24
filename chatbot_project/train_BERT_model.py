import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
import torch
from torch.utils.data import Dataset

# Load the BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

# Define the Dataset class for your data
class PersonaChatDataset(Dataset):
    def __init__(self, dataframe, tokenizer, max_len=512):
        self.tokenizer = tokenizer
        self.dataframe = dataframe
        self.max_len = max_len

    def __len__(self):
        return len(self.dataframe)
    
    def __getitem__(self, index):
        row = self.dataframe.iloc[index]
        
        # Combine 'personality' and utterances to create the input text
        history = f"Personality: {row['personality']}\nutterances: {row['utterances']}"
        label = 1 if 'positive' in row['utterances'].lower() else 0 # adjust according to your dataset
        
        inputs = self.tokenizer.encode_plus(
            history,
            max_length=self.max_len,
            padding='max_length',
            truncation = True,
            return_tensors="pt"
        )
        labels = torch.tensor(label, dtype=torch.long)
        
        return {
            'input_ids' : inputs['input_ids'].squeeze(),
            'attention_mask' : inputs['attention_mask'].squeeze(),
            'labels' : labels
        }

# Load the dataset.
train_df = pd.read_parquet("/Users/adrianrich/Documents/python/chatbot_project/train-00000-of-00001.parquet")
val_df = pd.read_parquet("/Users/adrianrich/Documents/python/chatbot_project/validation-00000-of-00001.parquet")

train_dataset = PersonaChatDataset(train_df, tokenizer)
val_dataset = PersonaChatDataset(val_df, tokenizer)

# Set up training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=5,
    per_device_train_batch_size=16,
    learning_rate=2e-5,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
    eval_strategy="steps", 
    save_steps=1000,
    save_total_limit=2,
    eval_steps=1000,
)

# Create a Trainer instance
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset
)

# Start training
trainer.train()

model.save_pretrained("/Users/adrianrich/Documents/python/chatbot_project/results")
tokenizer.save_pretrained("/Users/adrianrich/Documents/python/chatbot_project/results")

