# Instructions for Google Colab Training

1.  **Open Google Colab:** Go to [https://colab.research.google.com/](https://colab.research.google.com/).
2.  **Upload Notebook:** Click "Upload" and select the `train_model_colab.ipynb` file I just created in your `deeplearning` folder.
3.  **Prepare Data:**
    *   Compress your `Vegetable Images` folder into a zip file named `Vegetable Images.zip`.
    *   In the Colab sidebar (folder icon), upload `Vegetable Images.zip`.
4.  **Run Cells:**
    *   Uncomment the zip extraction lines in the first cell if you uploaded a zip.
    *   Run all cells to train the model.
5.  **Download Model:**
    *   Once training is complete, a file named `vegetable_classification.h5` will appear in the files sidebar.
    *   Right-click it and select "Download".
6.  **Place in Project:**
    *   Move the downloaded `vegetable_classification.h5` file into your local `c:\Users\amdga\Desktop\deeplearning\FLASK\` folder.
