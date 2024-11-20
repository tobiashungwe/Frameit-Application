from transformers import GPT2LMHeadModel, GPT2Tokenizer

def load_model(model_path):
    """
    Load the fine-tuned model and tokenizer from the specified path.
    """
    tokenizer = GPT2Tokenizer.from_pretrained(model_path)
    model = GPT2LMHeadModel.from_pretrained(model_path)
    return model, tokenizer

def generate_text(model, tokenizer, prompt, max_length=100, num_return_sequences=1):
    """
    Generate text using the fine-tuned model given an input prompt.
    """
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        no_repeat_ngram_size=2,  # Avoid repeating phrases
        top_k=50,                # Consider top 50 options for diversity
        top_p=0.95,              # Nucleus sampling for creativity
        temperature=0.7          # Lower value -> less randomness
    )
    return [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

def main():
    # Path to the fine-tuned model
    model_path = "../model_output/fine_tuned_gpt2"
    
    
    
    # Load the fine-tuned model and tokenizer
    model, tokenizer = load_model(model_path)
    print("Model and tokenizer loaded successfully!")

    # Example input prompts
    prompts = [
        "Halloween:",
        "Fortnite:",
        "Superheroes:",
        "Christmas:",
    ]

    # Generate and print text for each prompt
    for prompt in prompts:
        print(f"Prompt: {prompt}")
        generated_texts = generate_text(model, tokenizer, prompt)
        for i, text in enumerate(generated_texts):
            print(f"Generated Text {i + 1}: {text}")
        print("-" * 80)

if __name__ == "__main__":
    main()
