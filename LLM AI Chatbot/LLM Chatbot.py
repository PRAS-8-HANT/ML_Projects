{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4615e34d-16bc-4473-bfb7-dc8678b3a6f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "from hugchat import hugchat\n",
    "from hugchat.login import Login\n",
    "\n",
    "# App title\n",
    "st.set_page_config(page_title=\"🤗💬 HugChat\")\n",
    "\n",
    "# Hugging Face Credentials\n",
    "with st.sidebar:\n",
    "    st.title('🤗💬 HugChat')\n",
    "    if ('EMAIL' in st.secrets) and ('PASS' in st.secrets):\n",
    "        st.success('HuggingFace Login credentials already provided!', icon='✅')\n",
    "        hf_email = st.secrets['EMAIL']\n",
    "        hf_pass = st.secrets['PASS']\n",
    "    else:\n",
    "        hf_email = st.text_input('Enter E-mail:', type='password')\n",
    "        hf_pass = st.text_input('Enter password:', type='password')\n",
    "        if not (hf_email and hf_pass):\n",
    "            st.warning('Please enter your credentials!', icon='⚠️')\n",
    "        else:\n",
    "            st.success('Proceed to entering your prompt message!', icon='👉')\n",
    "    \n",
    "# Store LLM generated responses\n",
    "if \"messages\" not in st.session_state.keys():\n",
    "    st.session_state.messages = [{\"role\": \"assistant\", \"content\": \"How may I help you?\"}]\n",
    "\n",
    "# Display chat messages\n",
    "for message in st.session_state.messages:\n",
    "    with st.chat_message(message[\"role\"]):\n",
    "        st.write(message[\"content\"])\n",
    "\n",
    "# Function for generating LLM response\n",
    "def generate_response(prompt_input, email, passwd):\n",
    "    # Hugging Face Login\n",
    "    sign = Login(email, passwd)\n",
    "    cookies = sign.login()\n",
    "    # Create ChatBot                        \n",
    "    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())\n",
    "    return chatbot.chat(prompt_input)\n",
    "\n",
    "# User-provided prompt\n",
    "if prompt := st.chat_input(disabled=not (hf_email and hf_pass)):\n",
    "    st.session_state.messages.append({\"role\": \"user\", \"content\": prompt})\n",
    "    with st.chat_message(\"user\"):\n",
    "        st.write(prompt)\n",
    "\n",
    "# Generate a new response if last message is not from assistant\n",
    "if st.session_state.messages[-1][\"role\"] != \"assistant\":\n",
    "    with st.chat_message(\"assistant\"):\n",
    "        with st.spinner(\"Thinking...\"):\n",
    "            response = generate_response(prompt, hf_email, hf_pass) \n",
    "            st.write(response) \n",
    "    message = {\"role\": \"assistant\", \"content\": response}\n",
    "    st.session_state.messages.append(message)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "49cd4436-ba4a-40a4-b6d2-49b8f80b0999",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "88f71b58-6860-4d2c-8aac-4e9a17e15757",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ad5f5806-628e-4e82-9b75-16de7cdbabf2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d967786f-f71d-48eb-bc36-c1d1cbfc2491",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "14a34b32-58e9-4113-8e5e-c921c5274ba6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
