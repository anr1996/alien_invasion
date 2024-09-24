import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from transformers import BertTokenizer, BertForSequenceClassification
import torch

class ChatbotGUI(QWidget):
    def __init__(self):
        super().__init__()
        
        # load the trained T5 model and tokenizer
        self.tokenizer = BertTokenizer.from_pretrained('/Users/adrianrich/Documents/python/chatbot_project/results')# replace with the correct path
        self.model = BertForSequenceClassification.from_pretrained('/Users/adrianrich/Documents/python/chatbot_project/results') # replace with the correct path

        # Set up the window
        self.setWindowTitle("Chatbot")
        self.setGeometry(100,100,400, 300)

        # Set up the layout
        self.layout = QVBoxLayout()
        
        # add a Qlabel for the title or instructions
        self.title_label = QLabel("Ask the Chatbot", self)
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.title_label)
        
        # Set up the input box
        self.input_box = QTextEdit(self)
        self.input_box.setPlaceholderText("Type your question here...")
        self.layout.addWidget(self.input_box)

        # Set up the submit button
        self.submit_button = QPushButton("Ask", self)
        self.submit_button.clicked.connect(self.get_response)
        self.layout.addWidget(self.submit_button)

        # Set up the output area
        self.output_area = QTextEdit(self)
        self.output_area.setReadOnly(True)
        self.layout.addWidget(self.output_area)


        # Set layout
        self.setLayout(self.layout)

    def get_response(self):
        user_input = self.input_box.toPlainText()
        
        # tokenize the input
        inputs = self.tokenizer.encode_plus(
            user_input, 
            return_tensors='pt', 
            max_length=512, 
            truncation=True, 
            padding='max_length'
        )
        
        input_ids = inputs["input_ids"]
        attention_mask = inputs["attention_mask"]
        
        # Generate the response using the Bert model
        with torch.no_grad():
            outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            print(f"Logits: {logits}") # Debugging print
            prediction = torch.argmax(logits, dim=-1).item()
            print(f"Prediction: {prediction}") # Debugging print
        
        response_text = "Positive Response" if prediction == 1 else "Negative Response"
        self.output_area.setText(response_text)


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    chatbot = ChatbotGUI()
    chatbot.show()
    sys.exit(app.exec_())
    

