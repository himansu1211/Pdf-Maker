import streamlit as st
import img2pdf
from io import BytesIO

# 1. Page Configuration
st.set_page_config(
    page_title="Simple PDF Maker",
    page_icon="📄",
    layout="centered"
)

def main():
    # --- UI Header ---
    st.title("📄 Simple PDF Maker")
    st.markdown("""
    Convert your photos into a single PDF document instantly. 
    **Privacy Note:** Your images are processed in memory and not stored on our servers.
    """)
    st.divider()

    # --- Step 1: File Uploader ---
    uploaded_files = st.file_uploader(
        "Choose Images", 
        type=["jpg", "jpeg", "png"], 
        accept_multiple_files=True,
        help="You can select multiple files at once."
    )

    if uploaded_files:
        st.success(f"✅ {len(uploaded_files)} images ready for conversion.")
        
        # --- Step 2: Custom Settings ---
        with st.expander("Settings & Preview"):
            pdf_name = st.text_input("Filename", "My_Combined_Document")
            
            # Show a small preview of the uploaded files
            cols = st.columns(4)
            for idx, file in enumerate(uploaded_files):
                cols[idx % 4].image(file, caption=f"Page {idx+1}", width=100)

        # --- Step 3: Generation Logic ---
        if st.button("🚀 Generate PDF", use_container_width=True):
            try:
                # Progress Bar for "Wow" factor during presentation
                progress_bar = st.progress(0)
                st.write("Processing images...")
                
                # Convert uploaded files to bytes for img2pdf
                image_bytes_list = []
                for i, file in enumerate(uploaded_files):
                    image_bytes_list.append(file.getvalue())
                    # Update progress bar
                    progress_bar.progress((i + 1) / len(uploaded_files))

                # Core Conversion
                pdf_output = img2pdf.convert(image_bytes_list)
                
                # Provide Download Button
                st.balloons()
                st.download_button(
                    label="📥 Download PDF",
                    data=pdf_output,
                    file_name=f"{pdf_name}.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        # Display this when no files are uploaded
        st.info("Upload some images (JPG/PNG) to start the conversion.")

    # --- Footer ---
    st.markdown("---")
    st.caption("1st Year Project | Built with Python & Streamlit")

if __name__ == "__main__":
    main()