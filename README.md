# Invoice AI Agent

**AI-powered invoice assistant** that extracts invoice data from images, preprocesses them for better OCR accuracy, stores invoices in a database, and allows querying using Groq LLM via LangChain.

---

## Features

- **OCR Extraction:** Reads invoice images using Tesseract OCR.
- **Image Preprocessing:** Converts images to grayscale and applies thresholding for better OCR accuracy.
- **Database Storage:** Stores invoice raw text in a SQLite database.
- **AI Querying:** Ask natural language questions about invoices (user name, total, date, city, etc.).
- **SQL Queries:** Optional direct database queries.
