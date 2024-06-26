from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import GridSearchCV

import pandas as pd
import os


class MLAlgorithm():
    def __init__(self) -> None:
        pass

    def algorithm(self, csv_path: str) -> pd.DataFrame:
        """
        Runs the machine learning algorithm

        Parameters:
            csv_path (str): a string of the CSV file path
        """
        # Load the CSV file
        if os.path.exists(csv_path):
            self.data = pd.read_csv(csv_path)
        else:
            raise Exception("File not found.")

        # Define features and target variable
        self.features = ['end_tidal_co2', 'feed_vol', 'oxygen_flow_rate', 'resp_rate', 'bmi']
        target = 'referral'

        # Split data into features and target variable
        X = self.data[self.features]
        y = self.data[target]

        # Split data into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Define preprocessing steps
        numeric_features = X.columns
        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean')),
            ('scaler', StandardScaler())])

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features)])

        # Define classifiers with probability=True for SVC
        classifiers = {
            'SVM': SVC(probability=True),
            'RandomForest': RandomForestClassifier()
        }

        # Pipeline with preprocessing and classifier
        pipelines = {}
        for clf_name, clf in classifiers.items():
            pipelines[clf_name] = Pipeline(steps=[('preprocessor', preprocessor),
                                                  ('classifier', clf)])

        # Hyperparameters grid for grid search
        param_grids = {
            'SVM': {'classifier__C': [0.1, 1, 10], 'classifier__gamma': [0.1, 1, 10]},
            'RandomForest': {'classifier__n_estimators': [100, 200, 300], 'classifier__max_depth': [None, 10, 20]}
        }

        # Train and evaluate models
        self.results = {}
        for clf_name, pipeline in pipelines.items():
            print(f"Training {clf_name}...")
            clf_grid = GridSearchCV(pipeline, param_grid=param_grids[clf_name], cv=5, scoring='roc_auc')
            clf_grid.fit(X_train, y_train)
            self.results[clf_name] = clf_grid

            print(f"Best parameters for {clf_name}: {clf_grid.best_params_}")
            print(f"Train AUC for {clf_name}: {clf_grid.best_score_}")
            print(f"Test AUC for {clf_name}: {roc_auc_score(y_test, clf_grid.predict_proba(X_test)[:, 1])}")
            print()

            # Save the best model

        return self.extract_result()

    def extract_result(self) -> pd.DataFrame:
        """
        Extract referral predictions using SVM and RF

        Returns:
            self.data (pd.DataFrame): A dataframe of the updated patient referrals predicitons
        """

        # Extract features from the entire dataset
        X_all = self.data[self.features]

        # Predict probabilities for each patient using the trained models
        svm_probs_all = self.results['SVM'].predict_proba(X_all)[:, 1]
        # rf_probs_all = self.results['RandomForest'].predict_proba(X_all)[:, 1]

        # Define a threshold to classify patients as referred or not referred
        threshold = 0.5  # You can adjust this threshold based on your preference and model performance

        # Classify patients as referred or not referred based on the threshold
        svm_predictions_all = (svm_probs_all >= threshold).astype(int)
        # rf_predictions_all = (rf_probs_all >= threshold).astype(int)

        self.data['referral'] = svm_predictions_all

        return self.data

    def fetch_analysis_results(self) -> list:

        data = self.data

        analysis_data = []

        for index, row in data.iterrows():
            patient_data = {}
            for column in data.columns:
                patient_data[column] = row[column]
            analysis_data.append(patient_data)

        return analysis_data