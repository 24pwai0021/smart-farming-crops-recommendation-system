{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "27159ac7-e54a-4056-9920-6b08fc62be9c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in c:\\users\\shanz\\anaconda3\\lib\\site-packages (2.3.3)\n",
      "Requirement already satisfied: numpy in c:\\users\\shanz\\anaconda3\\lib\\site-packages (2.3.5)\n",
      "Requirement already satisfied: scikit-learn in c:\\users\\shanz\\anaconda3\\lib\\site-packages (1.7.2)\n",
      "Requirement already satisfied: joblib in c:\\users\\shanz\\anaconda3\\lib\\site-packages (1.5.2)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\shanz\\anaconda3\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\shanz\\anaconda3\\lib\\site-packages (from pandas) (2025.2)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\shanz\\anaconda3\\lib\\site-packages (from pandas) (2025.2)\n",
      "Requirement already satisfied: scipy>=1.8.0 in c:\\users\\shanz\\anaconda3\\lib\\site-packages (from scikit-learn) (1.16.3)\n",
      "Requirement already satisfied: threadpoolctl>=3.1.0 in c:\\users\\shanz\\anaconda3\\lib\\site-packages (from scikit-learn) (3.5.0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\shanz\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install pandas numpy scikit-learn joblib\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a83e071d-c170-4c0d-8c7f-4f0a42d7cc3d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 0.9931818181818182\n",
      "Model Saved\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import accuracy_score\n",
    "import joblib\n",
    "\n",
    "df = pd.read_csv(\"Crop_recommendation.csv\")\n",
    "\n",
    "X = df.drop(\"label\", axis=1)\n",
    "y = df[\"label\"]\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(\n",
    "    X, y, test_size=0.2, random_state=42\n",
    ")\n",
    "\n",
    "model = RandomForestClassifier(\n",
    "    n_estimators=100,\n",
    "    random_state=42\n",
    ")\n",
    "\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "pred = model.predict(X_test)\n",
    "\n",
    "print(\"Accuracy:\", accuracy_score(y_test, pred))\n",
    "\n",
    "joblib.dump(model, \"crop_model.pkl\")\n",
    "\n",
    "print(\"Model Saved\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f48ac7f3-8e39-4ae2-a5e6-05e6a8cbb36e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Recommended Crop: rice\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import joblib\n",
    "\n",
    "model = joblib.load(\"crop_model.pkl\")\n",
    "\n",
    "sample = pd.DataFrame({\n",
    "    \"N\": [90],\n",
    "    \"P\": [42],\n",
    "    \"K\": [43],\n",
    "    \"temperature\": [20.8],\n",
    "    \"humidity\": [82.0],\n",
    "    \"ph\": [6.5],\n",
    "    \"rainfall\": [202.9]\n",
    "})\n",
    "\n",
    "crop = model.predict(sample)\n",
    "\n",
    "print(\"Recommended Crop:\", crop[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "8b1cbe58-8a9f-4c9c-90bd-f90f64a4baeb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Recommended Crop: maize\n"
     ]
    }
   ],
   "source": [
    "sample = pd.DataFrame({\n",
    "    \"N\":[60],\n",
    "    \"P\":[40],\n",
    "    \"K\":[40],\n",
    "    \"temperature\":[25],\n",
    "    \"humidity\":[70],\n",
    "    \"ph\":[6.5],\n",
    "    \"rainfall\":[100]\n",
    "})\n",
    "\n",
    "crop = model.predict(sample)\n",
    "\n",
    "print(\"Recommended Crop:\", crop[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "80ca6b99-b72e-412a-ba2a-83f81fed395f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "a935adde-d513-47f3-b0ea-ff873c6e629f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Temperature: 30.2\n",
      "Humidity: 75\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "url = \"https://api.open-meteo.com/v1/forecast?latitude=24.86&longitude=67.01&current=temperature_2m,relative_humidity_2m\"\n",
    "\n",
    "data = requests.get(url).json()\n",
    "\n",
    "print(\"Temperature:\", data[\"current\"][\"temperature_2m\"])\n",
    "print(\"Humidity:\", data[\"current\"][\"relative_humidity_2m\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "59de1893-71e3-4835-9b30-a69abb673b13",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
