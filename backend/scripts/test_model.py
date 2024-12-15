import os
from transformers import (
    GPT2Tokenizer,
    GPT2LMHeadModel,
    Trainer,
    TrainingArguments,
    TextDataset,
    DataCollatorForLanguageModeling,
)

# Load the GPT-2 tokenizer and model
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Dynamically construct paths
script_dir = os.path.dirname(__file__)  # Get the directory of the current script
train_file_path = os.path.join(
    script_dir, "../data/theme_training.txt"
)  # Path to the training data
output_dir = os.path.join(
    script_dir, "../model_output"
)  # Output directory for the fine-tuned model


# Tokenize the training data
def load_dataset(file_path, tokenizer):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Training file not found: {file_path}")
    dataset = TextDataset(tokenizer=tokenizer, file_path=file_path, block_size=128)
    return dataset


train_dataset = load_dataset(train_file_path, tokenizer)

data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Set training arguments
training_args = TrainingArguments(
    output_dir=output_dir,
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=2,
    save_steps=10_000,
    save_total_limit=2,
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
)

# Train the model
trainer.train()

# Save the fine-tuned model
model.save_pretrained(os.path.join(output_dir, "fine_tuned_gpt2"))
tokenizer.save_pretrained(os.path.join(output_dir, "fine_tuned_gpt2"))
