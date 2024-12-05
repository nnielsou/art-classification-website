import streamlit as st
import pandas as pd
import requests
from PIL import Image
from io import BytesIO


#Art Classification front

st.title("Explore Art Movements & Upload Images")
# Define the columns

# Column 1: Image upload functionality
#with col1:

# st.header("Upload Your Image")
# img_data = st.file_uploader("Upload Image", type=['png', 'jpg'])
# if img_data is not None:
#     # Get the byte data of the image
#     img_byte_arr = img_data.getvalue()
#     # Open the image for display
#     img = Image.open(BytesIO(img_byte_arr))
#     # Display the uploaded image
#     st.image(img, caption="Uploaded Image", use_container_width=True)
#     # Example API request to upload the image
#     endpoint = "https://artmovement-174222773308.europe-west1.run.app/"
#     response = requests.post(f"{endpoint}/upload", files={"file": img_byte_arr})
#     response_get = requests.get()
#     if response.status_code == 200:
#         st.success("Image uploaded successfully!")
#     else:
#         st.error("Failed to upload image.")


# Header
st.header("Upload Your Image")

# File uploader
img_data = st.file_uploader("Upload Image", type=['png', 'jpg'])

if img_data is not None:
    # Get the byte data of the image
    img_byte_arr = img_data.getvalue()

    # Open the image for display
    img = Image.open(BytesIO(img_byte_arr))

    # Display the uploaded image
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Define the API endpoint
    endpoint = "https://artmovement-174222773308.europe-west1.run.app"

    # Step 1: Upload the image via the API
    upload_response = requests.post(f"{endpoint}/upload", files={"file": img_byte_arr})

    if upload_response.status_code == 200:
        st.success("Image uploaded successfully!")

    #     # Step 2: Get the prediction from the API
    #     predict_response = requests.get(f"{endpoint}/predict")

    #     if predict_response.status_code == 200:
    #         # Extract prediction from response
    #         prediction = predict_response.text
    #         st.write(f"**Predicted Art Movement:** {prediction}")
    #     else:
    #         st.error("Failed to get a prediction from the API.")
    else:
        st.error("Failed to upload the image.")

col1, col2 = st.columns(2)
# Column 2: Art movement descriptions
with col1:
    st.header("Art Movements")
# Dictionary of art movements
    art_movements = {
        "Abstract Expressionism": "A post-World War II art movement that emerged in America during the 1940s and 1950s. Characterized by spontaneous, automatic, or subconscious creation, often using large canvases to evoke emotion with techniques like dripping, splashing, or smearing paint.",
        "Impressionism": "A 19th-century art style originating in France, focusing on capturing fleeting effects of light, color, and atmosphere. Painted en plein air, it emphasizes visible, loose brushstrokes over detailed realism.",
        "Pointillism": "Developed by Georges Seurat and Paul Signac in the late 19th century, this technique uses tiny dots of pure color applied in patterns that blend optically from a distance, creating vibrant effects.",
        "Fauvism": "An early 20th-century style emphasizing bold, unnatural colors and simplified forms, led by Henri Matisse. It prioritized emotional expression over realism with vivid, almost wild, color use.",
        "Renaissance": "A cultural and artistic revival from the 14th to 17th centuries centered in Europe, marking the transition from medieval to modern times. Focused on realism, perspective, anatomy, and classical themes inspired by Greco-Roman heritage.",
        "Ukiyo-e": "A Japanese art form from the 17th to 19th centuries, featuring woodblock prints and paintings of 'the floating world,' depicting landscapes, kabuki actors, and daily life. Iconic artists include Hokusai and Hiroshige.",
        "Art Nouveau/Modern": "An ornamental movement from the late 19th to early 20th century, characterized by organic, flowing lines and intricate patterns inspired by natural motifs like flowers and vines. Common in architecture and interior design.",
        "Minimalism": "A 20th-century movement emphasizing simplicity and the reduction of art to its essential elements. It often uses geometric shapes, monochromatic palettes, and industrial materials for profound meaning through simplicity.",
        "Pop Art": "A mid-20th-century style inspired by popular culture, including advertising and mass media. Artists like Andy Warhol and Roy Lichtenstein used bold colors and iconic imagery to blur the line between high art and everyday life.",
        "Rococo": "An 18th-century European style characterized by elaborate decoration, pastel colors, and lighthearted themes of love, leisure, and mythology. Prominent figures include François Boucher and Jean-Honoré Fragonard.",
        "Baroque": "A dramatic and ornate style from the late 16th to early 18th centuries, emphasizing movement, grandeur, and emotional intensity. Baroque art often featured religious and historical themes.",
        "Naive Art": "Art created by self-taught artists with simple, unpolished styles, vibrant colors, and a childlike perspective.",
        "Primitivism": "Inspired by the art of non-Western cultures and prehistoric traditions, this movement sought to capture a raw, unfiltered aesthetic.",
        "Post-Impressionism": "A late 19th-century evolution of Impressionism, focusing on deeper emotional and symbolic content. Artists like Vincent van Gogh and Paul Gauguin used bold colors and expressive techniques.",
        "Romanticism": "A 19th-century movement emphasizing emotion, imagination, and nature’s sublime beauty. Romantic art often depicted dramatic landscapes and heroic themes, rejecting industrialization and rationalism.",
        "Cubism": "Pioneered by Pablo Picasso and Georges Braque, Cubism deconstructed subjects into geometric forms, presenting multiple perspectives simultaneously. A foundational movement for abstract art.",
        "Neo-Impressionism": "A post-Impressionist movement led by Georges Seurat, using scientific approaches to color and light like pointillism to achieve harmony and luminosity in compositions.",
        "Pre-Raphaelite Brotherhood": "A group of 19th-century British artists rejecting academic standards of their time. They drew inspiration from medieval art, focusing on vibrant colors, intricate detail, and literary themes.",
        "Surrealism": "A 20th-century avant-garde movement exploring the unconscious mind through dreamlike imagery, unexpected juxtapositions, and absurdity. Led by artists like Salvador Dalí.",
        "Expressionism": "An early 20th-century movement emphasizing emotional experience over realism. Artists used exaggerated forms, vivid colors, and distorted perspectives to convey intense feelings.",
        "Neoclassicism": "An 18th-century revival of classical antiquity emphasizing clarity, symmetry, and moralistic themes. Prominent figures include Jacques-Louis David.",
        "Realism": "A mid-19th-century movement depicting life as it truly is, without romanticizing or idealizing. Focused on everyday scenes and ordinary people.",
        "Symbolism": "A late 19th-century movement using symbolic imagery and metaphors to express spiritual, emotional, and mystical ideas. Dreamlike and poetic in nature."
    }


predict_response = requests.get(f"{endpoint}/predict")

if st.button('Predict !'):
    if predict_response.status_code == 200:
        # Extract prediction from response
        prediction = predict_response.text
        st.write(f"**Predicted Art Movement:** {prediction}")
    else:
        st.error("Failed to get a prediction from the API.")


    # Create an expander for each art movement
resultat = st.selectbox('You selected',art_movements.keys())
st.write(art_movements[resultat])




# # Add some custom CSS for enhanced design
# st.markdown(
#     """
#     <style>
#     .stImage img {
#         border: none;  /* Remove border */
#         border-radius: 15px;  /* Optional: add rounded corners if desired */
#         box-shadow: none;  /* Remove shadow */
#         padding: 0;  /* No padding around the image */
#         transition: transform 0.3s ease-in-out;  /* Smooth zoom effect */
#     }
#     .stImage img:hover {
#         transform: scale(1.05);  /* Slight zoom effect on hover */
#     }
#     /* Custom padding for the columns */
#     .stColumns .css-1l02z5t {
#         padding-left: 20px;
#         padding-right: 20px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
