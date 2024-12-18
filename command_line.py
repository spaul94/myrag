import openai
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
    print("Введите ваш запрос (или 'exit' для выхода):")
    while True:
        user_input = input(">> ")
        if user_input.lower() == "exit":
            print("Выход из программы.")
            break
        result = get_response_from_openai(user_input)
        print("Ответ от OpenAI:")
        print(result)

if __name__ == "__main__":
    main()