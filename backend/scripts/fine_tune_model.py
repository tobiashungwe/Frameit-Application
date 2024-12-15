import os
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
    DataCollatorForLanguageModeling,
)
from datasets import load_dataset

# Load the Falcon tokenizer and model
model_name = "tiiuae/falcon-7b-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)

# Define paths
script_dir = os.path.dirname(__file__)
train_file_path = os.path.join(script_dir, "../data/theme_training.txt")
output_dir = os.path.join(script_dir, "../model_output_falcon")


# Load the dataset
def load_dataset_with_datasets(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Training file not found: {file_path}")
    dataset = load_dataset("text", data_files={"train": file_path})
    return dataset["train"]


train_dataset = load_dataset_with_datasets(train_file_path)

# Prepare the data collator
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Set training arguments
training_args = TrainingArguments(
    output_dir=output_dir,
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=2,
    save_steps=10_000,
    save_total_limit=2,
    logging_dir=os.path.join(output_dir, "logs"),
    logging_steps=500,
    evaluation_strategy="steps",
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
model.save_pretrained(os.path.join(output_dir, "fine_tuned_falcon"))
tokenizer.save_pretrained(os.path.join(output_dir, "fine_tuned_falcon"))
