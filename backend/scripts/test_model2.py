from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "mosaicml/mpt-7b-storywriter"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)

prompt = """Exercise:
- Activity: Dodgeball
- Equipment: 10 balls, 2 teams
- Rules: Each team must eliminate the other by hitting players with the ball.

Generate a story overlay for the theme 'Mario':
"""

input_ids = tokenizer.encode(prompt, return_tensors="pt")
output = model.generate(input_ids, max_length=300, temperature=0.7, do_sample=True)
print(tokenizer.decode(output[0], skip_special_tokens=True))
