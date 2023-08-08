import streamlit as st
import json
from PIL import Image
import openai
import tensorflow as tf
import numpy as np
from keras.models import load_model
import requests
from bs4 import BeautifulSoup
from streamlit_lottie import st_lottie
from page.recommendations import get_personalized_recommendations
from page.recipes import get_recipe_suggestions

openai.api_key = 'INSERT OPEN_AI KEY'


model = load_model("C:/Users/saimt/OneDrive/Desktop/Food Calorie App/Food-Calorie-App/FAV.h5")
labels = {
    0: "apple",
    1: "banana",
    2: "beetroot",
    3: "bell pepper",
    4: "cabbage",
    5: "capsicum",
    6: "carrot",
    7: "cauliflower",
    8: "chilli pepper",
    9: "corn",
    10: "cucumber",
    11: "eggplant",
    12: "garlic",
    13: "ginger",
    14: "grapes",
    15: "jalepeno",
    16: "kiwi",
    17: "lemon",
    18: "lettuce",
    19: "mango",
    20: "onion",
    21: "orange",
    22: "paprika",
    23: "pear",
    24: "peas",
    25: "pineapple",
    26: "pomegranate",
    27: "potato",
    28: "raddish",
    29: "soy beans",
    30: "spinach",
    31: "sweetcorn",
    32: "sweetpotato",
    33: "tomato",
    34: "turnip",
    35: "watermelon",
}

fruits = [
    "Apple",
    "Banana",
    "Bello Pepper",
    "Chilli Pepper",
    "Grapes",
    "Jalepeno",
    "Kiwi",
    "Lemon",
    "Mango",
    "Orange",
    "Paprika",
    "Pear",
    "Pineapple",
    "Pomegranate",
    "Watermelon",
]
vegetables = [
    "Beetroot",
    "Cabbage",
    "Capsicum",
    "Carrot",
    "Cauliflower",
    "Corn",
    "Cucumber",
    "Eggplant",
    "Ginger",
    "Lettuce",
    "Onion",
    "Peas",
    "Potato",
    "Raddish",
    "Soy Beans",
    "Spinach",
    "Sweetcorn",
    "Sweetpotato",
    "Tomato",
    "Turnip",
]




def fetch_calories(prediction):
    try:
        url = "https://www.google.com/search?&q=calories in " + prediction
        req = requests.get(url).text
        scrap = BeautifulSoup(req, "html.parser")
        calories = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        return calories
    except Exception as e:
        st.error("Can't able to fetch the Calories")
        print(e)


def processed_img(img_path):
    img = tf.keras.utils.load_img(img_path, target_size=(224, 224, 3))
    img = tf.keras.utils.img_to_array(img)
    img = img / 255
    img = np.expand_dims(img, [0])
    answer = model.predict(img)
    y_class = answer.argmax(axis=-1)
    print(y_class)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = labels[y]
    print(res)
    return res.capitalize()


def run():

    st.title("Calorie App using Image Recognition")

    path = "food.json"
    with open(path,"r") as file:
        url = json.load(file)

    st_lottie(url,
        reverse=False,
        height=275,
        width=700,
        speed=1,
        loop=True,
        quality='high',
        
)



    img_file = st.file_uploader("Choose an Image", type=["jpg", "png"])

    if img_file is not None:
        img = Image.open(img_file).resize((250, 250))
        st.image(img, use_column_width=False)
        save_image_path = "./upload_images/" + img_file.name
        with open(save_image_path, "wb") as f:
            f.write(img_file.getbuffer())

        # if st.Sbutton("Predict"):
        if img_file is not None:
            result = processed_img(save_image_path)
            print(result)
            if st.button("Additional Information"):
                prompt = f"Give three benefits and two disadvantages of {result} along with recommendation. The max tokens are set to 300 so be mindful of the length and try to be concise without ending the sentence abruptly."
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt},
                    ],
                    max_tokens=300,
                    temperature=0.9,
                ) 
                answer = response.choices[0].message.content
                st.button("Addition Info")
                st.subheader("Details about the predicted Item")
                st.write(answer) 
   
            if result in vegetables:
                st.info("**Category : Vegetables**")
            else:
                st.info("**Category : Fruit**")
            st.success("**Predicted : " + result + "**")
            cal = fetch_calories(result)
            if cal:
                st.warning("**" + cal + "(100 grams)**")

pred = ''
usp = ''
cal = ''


def pers_fr():
    st.title("Personalized Food Recommendations")

    path = "lot.json"
    with open(path,"r") as file:
        url = json.load(file)

    st_lottie(url,
        reverse=True,
        height=250,
        width=600,
        speed=1,
        loop=True,
        quality='high',
        
)
    
    # User input fields
    user_preferences = st.text_input("Enter your food preferences\n Examples include \n: \
                                     Vegetarian, Dairy-free, Nut-free, \
                                     Egg-free, Soy-free, Fish-free, etc.")
    dietary_restrictions = st.text_input("Enter your dietary restrictions")
    health_goals = st.text_input("Enter your health goals")
    usp = user_preferences

    
    if st.button("Get Personalized Recommendations"):
        recommendations = get_personalized_recommendations(user_preferences, dietary_restrictions, health_goals)
        st.write("Personalized Recommendations:")
        for recommendation in recommendations:
            st.write("- " + recommendation)

    st.markdown("## -------------------------------------------------------------")  
    return usp          
    


def rec():

    path = "recipe.json"
    with open(path,"r") as file:
        url = json.load(file)

    st_lottie(url,
        reverse=False,
        height=250,
        width=600,
        speed=1,
        loop=True,
        quality='high',
        
)    
    st.title("Personalized Recipe Suggestions")
    predicted_food_item = st.text_input("Enter the predicted food item")
    calorie_requirements = st.text_input("Enter your calorie requirements")        
    if st.button("Get Recipe Suggestions"):

        suggestions = get_recipe_suggestions(predicted_food_item, usp, calorie_requirements)
        st.write("Recipe Suggestions:")
        for suggestion in suggestions:
            st.write("--> " + suggestion)


if __name__ == "__main__":
    st.sidebar.title("Navigation")
    app_page = st.sidebar.radio("Go to", ["Calorie Finder", "Personalized Recommendations", "Recipe Suggestions"])
    
    if app_page == "Calorie Finder":
        run()
    elif app_page == "Personalized Recommendations":
        pers_fr()
    elif app_page == "Recipe Suggestions":
        rec()
    


