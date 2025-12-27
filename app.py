import streamlit as st
import img2pdf
from io import BytesIO

st.set_page_config(
    page_title="Simple PDF Maker",
    page_icon="📄",
    layout="centered"
)

def main():
    st.title("📄 Simple PDF Maker")
    st.markdown("""
    Convert your photos into a single PDF document instantly. 
    **Privacy Note:** Your images are processed in memory and not stored on our servers.
    """)
    st.divider()

    uploaded_files = st.file_uploader(
        "Choose Images", 
        type=["jpg", "jpeg", "png"], 
        accept_multiple_files=True,
        help="You can select multiple files at once."
    )

    if uploaded_files:
        st.success(f"✅ {len(uploaded_files)} images ready for conversion.")
        
        with st.expander("Settings & Preview"):
            pdf_name = st.text_input("Filename", "My_Combined_Document")
            
            st.markdown("**Preview of Uploaded Images:**")
            cols = st.columns(4)
            for idx, file in enumerate(uploaded_files):
                cols[idx % 4].image(file, caption=f"Page {idx+1}", width=100)

        if st.button("🚀 Generate PDF", use_container_width=True):
            try:
                progress_bar = st.progress(0)                
                image_bytes_list = []
                for i, file in enumerate(uploaded_files):
                    image_bytes_list.append(file.getvalue())
                    progress_bar.progress((i + 1) / len(uploaded_files))

                # Generate PDF
                pdf_output = img2pdf.convert(image_bytes_list)
                
                st.success("🎉 PDF generated successfully!")
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
        
        st.info("Upload some images (JPG/PNG) to start the conversion.")

    
    st.markdown("---")
    st.caption("Built with Python & Streamlit")

if __name__ == "__main__":
    main()

