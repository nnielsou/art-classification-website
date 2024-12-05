import streamlit as st
import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import random

# --- Page Configuration ---
st.set_page_config(page_title="Art Classifier | Discover Your Art Style", layout="wide")

# --- Define API Endpoint ---
endpoint = "https://artmovement-174222773308.europe-west1.run.app"

# --- Custom CSS for Artsper-like Aesthetics ---
st.markdown(
    """
    <style>
    /* Background and General Styling */
    body {
        background-color: #ffffff; /* White background */
        color: #000000; /* Black text for contrast */
        font-family: 'Roboto', sans-serif;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #000000; /* Black heading text */
    }
    .stButton > button {
        background-color: #ffffff; /* White button background */
        color: #000000; /* Black text */
        border: 1px solid #000000; /* Add a black border for definition */
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        transition: 0.3s ease-in-out;
    }
    .stButton > button:hover {
        background-color: #f0f0f0; /* Light gray hover effect */
        color: #000000; /* Retain black text */
    }
    /* Image hover effects */
    .stImage img {
        border-radius: 10px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .stImage img:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2); /* Retain shadow for a subtle 3D effect */
    }
    /* Center container */
    .stApp {
        max-width: 1200px;
        margin: auto;
        padding: 20px;
    }
    /* Art movements dropdown */
    .stSelectbox {
        background-color: #ffffff; /* White dropdown background */
        color: #000000; /* Black text */
        border-radius: 5px;
        border: 1px solid #000000; /* Black border */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Header / Hero Section ---
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 40px;">
        <h1 style="font-size: 3em; font-weight: bold; margin: 0; color: #111111;">Discover the Art Movement</h1>
        <p style="font-size: 1.2em; color: #555555;">Explore the world of art through AI-powered classification. Upload your image and find its style.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Define Columns for Layout ---
st.markdown("### Upload Your Artwork")

img_data = st.file_uploader("Select an image (JPG or PNG)", type=['png', 'jpg'])

if img_data is not None:
    # Display uploaded image
    img_byte_arr = img_data.getvalue()
    img = Image.open(BytesIO(img_byte_arr))
    st.image(img, caption="Uploaded Image", width=400)

    endpoint = "https://artmovement-174222773308.europe-west1.run.app"
    upload_response = requests.post(f"{endpoint}/upload", files={"file": img_byte_arr})

    #if upload_response.status_code == 200:
    #st.success("Image uploaded successfully!")
    #else:
        #st.error("Image upload failed. Please try again.")

    if st.button("Discover Art Movement"):
        predict_response = requests.get(f"{endpoint}/predict")
        if predict_response.status_code == 200:
            prediction = predict_response.text
            st.markdown(f"### 🎨 **Predicted Art Movement:** {prediction}")
        else:
            st.error("Failed to get a prediction from the API.")

# --- Right Column: Featured Art Movements ---
st.markdown("### Discover Art Movement")

# --- Featured Art Movements Section ---

cols = st.columns(4)

# Create a responsive grid for art movements
movements = [
    {"name": "Abstract Expressionism", "desc": "A post-World War II art movement that emerged in America during the 1940s and 1950s. Characterized by spontaneous, automatic, or subconscious creation, often using large canvases to evoke emotion with techniques like dripping, splashing, or smearing paint.", "img": "https://media.tate.org.uk/aztate-prd-ew-dg-wgtail-st1-ctr-data/images/.width-1200_bXrNKs2.jpg"},
    {"name": "Impressionism", "desc": "A 19th-century art style originating in France, focusing on capturing fleeting effects of light, color, and atmosphere. Painted en plein air, it emphasizes visible, loose brushstrokes over detailed realism.", "img": "https://upload.wikimedia.org/wikipedia/commons/5/54/Claude_Monet%2C_Impression%2C_soleil_levant.jpg"},
    {"name": "Pointillism", "desc": "Developed by Georges Seurat and Paul Signac in the late 19th century, this technique uses tiny dots of pure color applied in patterns that blend optically from a distance, creating vibrant effects.", "img": "https://res.cloudinary.com/dtflabxt0/image/fetch/w_1600/https://artshortlist.com/img/posts/kqXeg1M_05OCe24VpW2rppiF.jpeg"},
    {"name": "Fauvism", "desc": "An early 20th-century style emphasizing bold, unnatural colors and simplified forms, led by Henri Matisse. It prioritized emotional expression over realism with vivid, almost wild, color use.", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/f/fb/Matisse-Woman-with-a-Hat.jpg/1024px-Matisse-Woman-with-a-Hat.jpg"},
    {"name": "Renaissance", "desc": "A cultural and artistic revival from the 14th to 17th centuries centered in Europe, marking the transition from medieval to modern times. Focused on realism, perspective, anatomy, and classical themes inspired by Greco-Roman heritage.", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Sandro_Botticelli_046.jpg/520px-Sandro_Botticelli_046.jpg"},
    {"name": "Ukiyo-e", "desc": "A Japanese art form from the 17th to 19th centuries, featuring woodblock prints and paintings of 'the floating world,' depicting landscapes, kabuki actors, and daily life. Iconic artists include Hokusai and Hiroshige.", "img": "https://i.etsystatic.com/39519528/r/il/c3a97f/4486845485/il_1588xN.4486845485_f2zb.jpg"},
    {"name": "Art Nouveau/Modern", "desc": "An ornamental movement from the late 19th to early 20th century, characterized by organic, flowing lines and intricate patterns inspired by natural motifs like flowers and vines. Common in architecture and interior design.", "img": "https://www.invaluable.com/blog/wp-content/uploads/sites/77/2018/04/invaluable-art-nouveau-2b-Gustav-Klimt-668x670.jpg"},
    {"name": "Minimalism", "desc": "A 20th-century movement emphasizing simplicity and the reduction of art to its essential elements. It often uses geometric shapes, monochromatic palettes, and industrial materials for profound meaning through simplicity.", "img": "https://www.brianparkerartist.co.uk/wp-content/uploads/2023/07/Time-to-Rise-Brian-Parker-Artist-2048x2048.jpg"},
    {"name": "Pop Art", "desc": "A mid-20th-century style inspired by popular culture, including advertising and mass media. Artists like Andy Warhol and Roy Lichtenstein used bold colors and iconic imagery to blur the line between high art and everyday life.", "img": "https://via.placeholder.com/300"},
    {"name": "Rococo", "desc": "An 18th-century European style characterized by elaborate decoration, pastel colors, and lighthearted themes of love, leisure, and mythology. Prominent figures include François Boucher and Jean-Honoré Fragonard.", "img": "https://i0.wp.com/blog.artsper.com/wp-content/uploads/2021/11/3.-Honoré-Fragonard-Les-heureux-hasards-de-lEscarpolette-copie.jpg?fit=1200%2C675&ssl=1"},
    {"name": "Baroque", "desc": "A dramatic and ornate style from the late 16th to early 18th centuries, emphasizing movement, grandeur, and emotional intensity. Baroque art often featured religious and historical themes.", "img": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Orazio_Gentileschi_-_Davide_e_Golia_%28National_Gallery_of_Ireland%29.jpg"},
    {"name": "Naive Art", "desc": "Art created by self-taught artists with simple, unpolished styles, vibrant colors, and a childlike perspective.", "img": "https://the-editorialmagazine.com/wp-content/uploads/2016/12/USA-Museum_of_Modern_Art-Henri_Rousseau.jpg"},
    {"name": "Renaissance", "desc": "A cultural and artistic revival from the 14th to 17th centuries centered in Europe, marking the transition from medieval to modern times. Focused on realism, perspective, anatomy, and classical themes inspired by Greco-Roman heritage.", "img": "https://via.placeholder.com/300"},
    {"name": "Ukiyo-e", "desc": "A Japanese art form from the 17th to 19th centuries, featuring woodblock prints and paintings of 'the floating world,' depicting landscapes, kabuki actors, and daily life. Iconic artists include Hokusai and Hiroshige.", "img": "https://via.placeholder.com/300"},
    {"name": "Art Nouveau/Modern", "desc": "An ornamental movement from the late 19th to early 20th century, characterized by organic, flowing lines and intricate patterns inspired by natural motifs like flowers and vines. Common in architecture and interior design.", "img": "https://theplatosociety.org/study-discussion-groups-1/abstract-expressionism-the-art-revolution-that-was-born-in-america"},
    {"name": "Primitivism", "desc": "Inspired by the art of non-Western cultures and prehistoric traditions, this movement sought to capture a raw, unfiltered aesthetic.", "img": "https://via.placeholder.com/300"},
    {"name": "Post-Impressionism", "desc": "A late 19th-century evolution of Impressionism, focusing on deeper emotional and symbolic content. Artists like Vincent van Gogh and Paul Gauguin used bold colors and expressive techniques.", "img": "https://via.placeholder.com/300"},
    {"name": "Romanticism", "desc": "A 19th-century movement emphasizing emotion, imagination, and nature’s sublime beauty. Romantic art often depicted dramatic landscapes and heroic themes, rejecting industrialization and rationalism.", "img": "https://via.placeholder.com/300"},
    {"name": "Cubism", "desc": "Pioneered by Pablo Picasso and Georges Braque, Cubism deconstructed subjects into geometric forms, presenting multiple perspectives simultaneously. A foundational movement for abstract art.", "img": "https://via.placeholder.com/300"},
    {"name": "Neo-Impressionism", "desc": "A post-Impressionist movement led by Georges Seurat, using scientific approaches to color and light like pointillism to achieve harmony and luminosity in compositions.", "img": "https://via.placeholder.com/300"},
    {"name": "Pre-Raphaelite Brotherhood", "desc": "A group of 19th-century British artists rejecting academic standards of their time. They drew inspiration from medieval art, focusing on vibrant colors, intricate detail, and literary themes.", "img": "https://via.placeholder.com/300"},
    {"name": "Surrealism", "desc": "A 20th-century avant-garde movement exploring the unconscious mind through dreamlike imagery, unexpected juxtapositions, and absurdity. Led by artists like Salvador Dalí.", "img": "https://via.placeholder.com/300"},
    {"name": "Expressionism", "desc": "An early 20th-century movement emphasizing emotional experience over realism. Artists used exaggerated forms, vivid colors, and distorted perspectives to convey intense feelings.", "img": "https://via.placeholder.com/300"},
    {"name": "Neoclassicism", "desc": "An 18th-century revival of classical antiquity emphasizing clarity, symmetry, and moralistic themes. Prominent figures include Jacques-Louis David.", "img": "https://via.placeholder.com/300"},
    {"name": "Realism", "desc": "A mid-19th-century movement depicting life as it truly is, without romanticizing or idealizing. Focused on everyday scenes and ordinary people.", "img": "https://via.placeholder.com/300"},
    {"name": "Symbolism", "desc": "A late 19th-century movement using symbolic imagery and metaphors to express spiritual, emotional, and mystical ideas. Dreamlike and poetic in nature.", "img": "https://via.placeholder.com/300"},
]

# Display grid of art movements
for i, movement in enumerate(movements):
    col = cols[i % 4]  # Distribute art movements across the 4 columns

    # Display the image and text in each column
    with col:
        st.image(movement['img'])
        st.markdown(f"### {movement['name']}")
        st.markdown(movement["desc"])


# --- Footer Section ---
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <p style="color: #555555;">Powered by AI and Deep Learning | Made with ❤️ by Art Enthusiasts</p>
    </div>
    """,
    unsafe_allow_html=True,
)
