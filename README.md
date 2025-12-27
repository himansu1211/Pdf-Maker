# 📄 Simple PDF Maker

A simple web application that converts multiple images (JPG/PNG) into a single PDF document. Built with Python and Streamlit, and deployed on Vercel for easy access.

## 🚀 Features

- **Easy Image Upload**: Upload multiple images at once via drag-and-drop or file selection.
- **Instant Conversion**: Convert images to PDF in seconds with a progress indicator.
- **Custom Filename**: Set a custom name for your PDF output.
- **Preview Images**: View thumbnails of uploaded images before conversion.
- **Privacy-Focused**: Images are processed in memory and not stored on servers.
- **Responsive Design**: Works on desktop and mobile devices.

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web app framework
- **img2pdf**: Library for converting images to PDF
- **Vercel**: Deployment platform

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Local Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd pdf-maker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Open your browser to `http://localhost:8501`

## 🌐 Deployment

This project is configured for deployment on Vercel:

1. Connect your GitHub repository to Vercel
2. Vercel will automatically detect the `vercel.json` configuration
3. Deploy the application

The `api/index.py` serves as a bridge between Streamlit and Vercel's serverless environment.

## 📖 Usage

1. **Upload Images**: Click on the file uploader and select multiple JPG or PNG images
2. **Configure Settings**: Expand the settings panel to customize the PDF filename and preview images
3. **Generate PDF**: Click the "🚀 Generate PDF" button to start conversion
4. **Download**: Once processing is complete, download your PDF using the download button

## 📁 Project Structure

```
pdf-maker/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── vercel.json         # Vercel deployment configuration
├── api/
│   └── index.py        # Vercel serverless function wrapper
└── README.md           # This file
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Built by Himansu Kumar Sahu**
