# Life Satisfaction Prediction

A small machine learning project that predicts a country's average life satisfaction score from its GDP per capita, using simple linear regression.

## Overview

The script loads a public dataset of countries with their GDP per capita (USD) and life satisfaction score, plots the relationship, fits a linear regression model, and then asks you for a GDP per capita value and predicts the corresponding life satisfaction.

## How it works

1. **Load the data.** `lifesat.csv` is read directly from the [`ageron/data`](https://github.com/ageron/data) repository, so there is nothing to download manually.
2. **Prepare features.** `GDP per capita (USD)` is the input (`X`) and `Life satisfaction` is the target (`y`).
3. **Visualize.** A scatter plot shows life satisfaction against GDP per capita.
4. **Train.** A scikit-learn `LinearRegression` model is fitted to the data.
5. **Predict.** You enter a GDP per capita value in the terminal and the model prints the predicted life satisfaction.

## Requirements

- Python 3.8+
- pandas
- numpy
- scikit-learn
- matplotlib

Install the dependencies with:

```bash
pip install pandas numpy scikit-learn matplotlib
```

## Usage

Clone the repository and run the script:

```bash
git clone https://github.com/savesummers/LIFE-SATISFACTION-PREDICTION.git
cd LIFE-SATISFACTION-PREDICTION
python model.py
```

A scatter plot window will open first. Close it to continue, then enter a GDP per capita value when prompted:

```
Enter GDP per capita (USD): 37655
Life Satisfaction Prediction:  [[6.30165767]]
```

The prediction is printed on a 0 to 10 life satisfaction scale. The exact number depends on the current version of the dataset.

> An internet connection is required, because the dataset is fetched from GitHub each time the script runs.

## Project structure

```
LIFE-SATISFACTION-PREDICTION/
├── LICENSE      # MIT license
├── README.md    # Project documentation
└── model.py     # Data loading, plotting, training and prediction
```

## Limitations

- The model uses a **single feature** (GDP per capita), so it ignores other factors that influence life satisfaction, such as health, social support and freedom.
- The dataset is **small**, so the model is best treated as a learning example rather than a reliable forecasting tool.
- Linear regression assumes a straight-line relationship. In practice, the effect of income on life satisfaction tends to flatten at higher income levels.
- Input values far outside the range of the training data (the plot covers roughly 23,500 to 62,500 USD) are extrapolations and may give unrealistic predictions.
- The script expects a whole number as input, so decimals will raise an error.

## Possible improvements

- Use the logarithm of GDP per capita to better capture diminishing returns.
- Try other models, such as k-nearest neighbors, and compare them.
- Add more features, such as life expectancy or social support.
- Evaluate the model with a train/test split or cross-validation.
- Handle invalid input and offline use gracefully.

## Data source

The data comes from [`ageron/data`](https://github.com/ageron/data) (`lifesat/lifesat.csv`), a dataset used in Aurélien Géron's book *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
