import openai
import streamlit as st
import os

# Укажите ваш OpenAI API ключ
openai.api_key = os.environ['OPENAI_KEY']

def get_response_from_openai(prompt):
    try:
        # Запрос к OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Используем новую модель
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,  # Максимальное количество токенов в ответе
            temperature=0.7  # Температура: степень "креативности"
        )
        # Возврат текста ответа
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Произошла ошибка: {e}"

def main():
    st.title("Chat с OpenAI GPT-3.5")
    st.write("Введите сообщение для OpenAI и получите ответ!")

    # Состояние чата
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Отображение чата
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Поле ввода текста
    user_input = st.chat_input("Введите ваш запрос")

    if user_input:
        # Добавление сообщения пользователя
        st.session_state["messages"].append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        # Получение ответа от OpenAI
        response = get_response_from_openai(user_input)

        # Добавление ответа от модели
        st.session_state["messages"].append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.write(response)

if __name__ == "__main__":
    main()