# Food-Calorie-Estimation

## Setup Instructions
1. Unzip the provided folder and go inside the root directory
2. Make sure you have Anaconda installed in the python environment. If not, download from the
given link:
https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html
`conda 23.7.2.dev12 documentation`
3. Create a new virtual environment or choose the base environment from your VsCode settings once conda is available.
`conda create -n food_classification_app python`
`conda activate food_classification_app`
4. Install the required dependencies:
pip install -r requirements.txt
5. Check for the `Fav.h5` model and make sure it’s in the root directory of the project. Note: The
FaV.h5 model is the saved version of the food classification model. You do not need to run the model file.
6. Run the Streamlit app:
streamlit run app.py
Note: If you encounter any issues during installation or running the app, please make sure that
you have Conda installed and properly set up. Additionally, it's recommended to use a virtual
environment to avoid conflicts with other packages on your system.

—----------------------------------------------------------------------------------------------------------------------------
## Instructions (In case you need to train the model)

(Only follow the below steps in situations the saved model is not recognized by
the system)

If for some reason your system is not able to recognize the Fav.h5 saved model, you’ll need to
train the model with the following steps.

1. The first lines of the code will download the dataset from the Kaggle repository (present
as an alternate to the original dataset). This is done so as to reduce the load of file size
on the project. Once downloaded give your full path of the directory you’re in to the
`‘dataset_dir’` variable.(See fig.) The time for downloading is usually around 10-12 minutes.


![image](https://github.com/thisissaim/Food-Calorie-Estimation/assets/78817243/ff9c3048-64fe-4c2d-8715-bc323809cb47)


2. Similarly, enter your directory name for the filename followed by the name of the dataset
i.e (fruit-and-vegetable-image-recognition)

![image](https://github.com/thisissaim/Food-Calorie-Estimation/assets/78817243/9a8a47e4-d1a5-4460-827b-f74bf2f26cdb)



4. Run all cells as it is. The last cell of the code is executed as:


![image](https://github.com/thisissaim/Food-Calorie-Estimation/assets/78817243/24b73859-0a9a-403f-810c-d953afd40739)


You now can check whether a FAV.h5 file was created in the directory.
Once trained, you can follow the above steps to run the streamlit application.
Note: The model training can take upto 40 minutes on a lightweight laptop. Therefore
make sure to only re-
