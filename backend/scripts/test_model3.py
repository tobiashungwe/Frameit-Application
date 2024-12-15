from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "mosaicml/mpt-7b-storywriter"


# Load the model with quantization
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name, trust_remote_code=True, torch_dtype="auto", device_map="cpu"
)

# Test the model
prompt = "Once upon a time in the Mushroom Kingdom..."
input_ids = tokenizer(prompt, return_tensors="pt").input_ids
output = model.generate(input_ids, max_length=100)
print(tokenizer.decode(output[0], skip_special_tokens=True))
