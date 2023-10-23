import streamlit as st
import openai
import time
import json
import sys

st.title("Multi intent Sample Bot")


def init_config():
    if "deployment_name" not in st.session_state:
        sys.path.insert(0, "../../0_common_config")
        from config_data import get_deployment_name_turbo, set_environment_details_turbo

        st.session_state["deployment_name"] = get_deployment_name_turbo()
        set_environment_details_turbo()
        print(
            "deployment_name",
            st.session_state["deployment_name"],
            "\nopenai.api_base",
            openai.api_base,
            "\nopenai.api_type",
            openai.api_type,
        )
    return st.session_state["deployment_name"]


if "messages" not in st.session_state:
    st.session_state.messages = []
    system_prompt = ""
    with open("metaprompt-1.txt", "r") as file:
        # system_prompt = file.read().replace('\n', '')
        system_prompt = file.read()
        st.session_state.messages.append({"role": "system", "content": system_prompt})
        st.text_area(label="System Prompt", value=system_prompt, height=500)

counter = 0
for message in st.session_state.messages:
    if counter == 0:
        counter += 1
        continue
    else:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Hello!!!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            engine=init_config(),
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            try:
                full_response += response.choices[0].delta.get("content", "")
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            except:
                pass
        message_placeholder.markdown(full_response)
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )
