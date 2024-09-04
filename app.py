import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import os

model = T5ForConditionalGeneration.from_pretrained("fine_tuned_t5_model")
tokenizer = T5Tokenizer.from_pretrained("fine_tuned_t5_tokenizer")


device = torch.device("cuda" if torch.cuda.is_available else "cpu")
model.to(device)


st.title("Abstractive Text Summarization")

input_text = st.text_area("Enter the text you want to summarize",height=300)

if st.button("Generate Summary"):
    if input_text.strip():
        input_text = "summarize: " + input_text
        inputs = tokenizer.encode(input_text,return_tensors="pt",max_length=512,truncation=True).to(device)

        summary_ids = model.generate(inputs,max_length=150,min_length=40,length_penalty=2.0,num_beams=4,early_stopping=True)
        summary = tokenizer.decode(summary_ids[0],skip_special_tokens=True)

        st.subheader("Generated Summary")
        st.write(summary)
    else:
        st.warning("Please Enter some text to summarize")

if st.button("Click here for extractive text summarization"):
    os.system("streamlit run newapp.py")

if __name__ == "__main__":
    st.write("Ready to summarize your text!")
