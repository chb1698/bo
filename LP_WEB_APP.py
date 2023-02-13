# 使用OpenAI 和Streamlit库创建一个简单的Web应用程序，允许用户输入产品名称和产品描述，然后要求ChatGPT为用户生成Landing Page的Html脚本，用户可以选择输出摘要的字数、输出的语气并将生成的摘要保存到他们的设备中。把完整的代码写给我。

import streamlit as st
import openai

# Initialize the OpenAI API client
openai.api_key = "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"


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
num_words = st.slider("摘要中的字数:",
                      min_value=50, max_value=3000, value=100, step=50)
tone = st.slider("语气:", min_value=0.0, max_value=1.0, value=0.5, step=0.1)

if st.button("Generate"):
    prompt = (f"Generate a landing page HTML script for a product called '{product_name}', "
              f"which is described as follows: '{product_desc}', Need to have compelling visuals, Need to have a clear call to action.")
    html_script = generate_html(prompt, num_words, tone)
    st.write(f"```html\n{html_script}\n```")
