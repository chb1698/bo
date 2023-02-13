import os
import streamlit as st
import openai

# Get the API key from the environment variable
openai_api_key = os.environ.get("OPENAI_API_KEY")
if openai_api_key:
    openai.api_key = openai_api_key
else:
    st.write("OpenAI API key not found in the environment variables.")


def generate_html(prompt, num_words, tone):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=num_words,
        n=1,
        stop=None,
        temperature=tone,
    )

    message = completions.choices[0].text
    return message


st.title("让AI帮你设计广告着陆页 - By 流星")

product_name = st.text_input("输入产品名称:")
product_desc = st.text_area("输入产品描述:")
num_words = st.slider("脚本中的字数:",
                      min_value=50, max_value=3000, value=100, step=50)
tone = st.slider("创造力:", min_value=0.0, max_value=1.0, value=0.5, step=0.1)

if st.button("Generate"):
    prompt = (f"Generate a landing page HTML script for a product called '{product_name}', "
              f"which is described as follows: '{product_desc}', Need to have compelling visuals, Need to have a clear call to action.")
    html_script = generate_html(prompt, num_words, tone)
    st.write(f"```html\n{html_script}\n```")
