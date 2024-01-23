import openai
import streamlit as st

# استخدم الرمز المخفي الخاص بك للوصول إلى Assistants API
openai.api_key = "YOUR_API_KEY_HERE"

# انشاء مساعد
assistant = openai.Assistant(
    name="My Chat Assistant",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)

# عرض واجهة Streamlit
st.title("My Chat Assistant")

# اضافة مربع نص لإدخال الرسائل
message = st.text_input("Enter your message")

# عرض الردود على الرسائل المضافة إلى النقطة
if message:
    thread = openai.Thread.create()
    openai.Thread.Message.create(
        thread_id=thread.id,
        role="user",
        content=message
    )
    run = openai.Thread.Run.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
        instructions="Please address the user as Jane Doe. The user has a premium account."
    )
    run = openai.Thread.Run.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    response = run.steps[-1].content
    st.write("Assistant response:", response)
