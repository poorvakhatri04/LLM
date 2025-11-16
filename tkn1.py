import tiktoken
print("tiktoken version:", tiktoken.__version__)
tokenizer=tiktoken.get_encoding("gpt2")
text=("Hello, do you like tea? <|endoftext|> In the sunlit terraces"
      "of someunknownPalace.")
integers=tokenizer.encode(text,allowed_special={"<|endoftext|>"})
print(integers)
strings=tokenizer.decode(integers)
print(strings)
integers=tokenizer.encode("Darshit")
print(integers)
strings=tokenizer.decode(integers)
print(strings)