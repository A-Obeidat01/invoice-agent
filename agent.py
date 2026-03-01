import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.tools import tool
from tools.db_tool import init_db, query_invoices
from tools.ocr_tool import extract_invoice_data

load_dotenv()
init_db()

# Groq LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# Tool
@tool
def database_query(sql_query: str) -> str:
    """Run a SQL query on the invoices database and return the results."""
    return query_invoices(sql_query)

@tool
def process_invoice_image(image_path: str) -> dict:
    """Process an invoice image, extract all text, and store it in the database."""
    data = extract_invoice_data(image_path)
    return data

tools = [database_query, process_invoice_image]

while True:
    question = input("Ask: ").strip()

    # image to ocr
    if question.lower().startswith("process_invoice_image"):
        file_name = question.split("(",1)[1].rstrip(")").strip('"').strip("'")
        invoice_data = process_invoice_image.run(file_name)
        print(f"Invoice processed. You can now ask questions about it!")

    # SQL
    elif "SELECT" in question.upper():
        print(database_query(question))

    # Any questions
    else:
        if 'invoice_data' in locals():
            
            prompt = f"""
You are an invoice assistant. Here is the latest invoice text:

{invoice_data['raw_text']}

Answer the question: {question}
"""
        else:
            prompt = question

        response = llm.invoke(prompt)
        print(response.content)