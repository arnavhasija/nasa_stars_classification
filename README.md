# nasa_stars_classification

![](/images/img2.jpg)

<h2>Background</h2>

The purpose of this project is to develop a predictive model capable of accurately classifying celestial objects, specifically stars, quasars, and galaxies, based on their distinct spectral characteristics. Spectral characteristics refer to the unique patterns of light emitted or absorbed by these celestial bodies, which can reveal essential information about their nature, composition, and physical properties.

Classifying stars, quasars, and galaxies is of paramount importance in the field of astronomy and astrophysics. Each of these objects plays a distinct role in the cosmos, and understanding their distribution and properties can significantly advance our knowledge of the universe. Here's a more detailed explanation of the project's objectives:

Star Classification: Stars are fundamental building blocks of galaxies and are responsible for the synthesis of elements through nuclear fusion. Accurate classification of stars based on their spectra can help us determine their age, temperature, chemical composition, and evolutionary stage. This information aids in studying the life cycle of stars, the formation of galaxies, and the overall structure of the universe.

Quasar Identification: Quasars, short for "quasi-stellar radio sources," are incredibly bright and distant cosmic objects powered by supermassive black holes at the centers of galaxies. They emit enormous amounts of energy across the electromagnetic spectrum, making them crucial for studying the early universe, galaxy evolution, and black hole physics. Identifying quasars accurately based on their spectral signatures allows astronomers to uncover the distant and energetic phenomena that shaped the universe's early history.

Galaxy Categorization: Galaxies, vast assemblies of stars, gas, and dust, come in various types, such as spiral, elliptical, and irregular galaxies. Spectral classification of galaxies can reveal information about their ages, chemical compositions, star formation rates, and overall dynamics. Understanding the different galaxy types and their distributions helps astronomers explore the large-scale structure of the universe, dark matter distribution, and cosmic evolution.

<h2>Why I chose this project?</h2>

I have always been intrigued by outer space and all that surrounds us in this universe. It is always a humbling experience no matter how many times I watch Carl Sagan reflecting on the appearance of “Pale Blue Dot” from 6 billion kilometers away. The universe is an endlessly fascinating and vast place, full of mysteries and wonders. The "Pale Blue Dot" image, taken by the Voyager 1 spacecraft, is a truly iconic and humbling reminder of our place in the cosmos. It's a reminder that, despite our differences and the vastness of space, we are all part of a single, interconnected system. It's a powerful reminder to appreciate and care for the planet we call home. 

Last year, when I saw the highest-resolution image of the universe captured by the James Webb Space Telescope it blew me away, and appreciate everything there is yet to be learned about this universe. This level of resolution allows astronomers to study the structure and evolution of galaxies in unprecedented detail. The image could contribute significantly to our understanding of the universe and reveal many previously unknown objects and phenomena. It remains one of the most detailed and comprehensive images of the universe ever captured. Seeing the birth and death of millions of stars makes me feel more connected and makes me want to dwell and feel the presence of every star surrounding us. I often stare at the night sky as it helps make everything I worry about feel so trivial.  I feel that it is very calming to spend time looking at the sky and contemplating the vastness of the universe. It seems to put my problems and worries into perspective and helps me feel more grounded and at peace.

![](/images/img3.JPG)

<h2>Dataset</h2>

The dataset I worked with contains a vast collection of 100,000 space observations captured by the renowned SDSS (Sloan Digital Sky Survey). Each observation is characterized by 17 distinct features and 1 essential class column, which serves the purpose of classifying the celestial objects into three categories: stars, galaxies, and quasars.

The features of this dataset are explained below and they all help provide valuable insights into the nature of each observation:

1. <b>obj_ID (Object Identifier)</b>: This feature serves as a unique identifier for each celestial object in the dataset. It is like a special code assigned to each object to distinguish it from others. The obj_ID is essential for keeping track of individual celestial objects throughout the dataset. It helps link various observations and data related to a particular object, enabling researchers to study its properties, behavior, and characteristics.

2. <b>alpha (Right Ascension angle)</b>: Alpha represents the angular position of a celestial object in the sky when observed from Earth. It is measured along the east-west direction and helps locate the object on the celestial sphere. Right Ascension is crucial for pinpointing the exact position of an object in the sky. It aids astronomers in determining when and where to observe specific celestial objects, making it an essential tool for navigation and observation planning.

3. <b>delta (Declination angle)</b>: Delta denotes the angular position of a celestial object in the sky when observed from Earth. It is measured along the north-south direction and complements the Right Ascension in locating the object. Declination helps astronomers precisely locate celestial objects in the sky, providing information about their placement in relation to Earth's equator. Together with Right Ascension, it forms a celestial coordinate system essential for observational purposes.

4. <b>u, g, r, i, z (Photometric Filters)</b>: These features represent different filters used to measure the brightness of celestial objects at specific wavelengths of light. Each filter corresponds to a specific color range. By measuring the intensity of light at various wavelengths, astronomers can derive valuable information about the object's temperature, composition, and distance from Earth. These photometric measurements are important for understanding the physical properties of celestial objects.

5. <b>run_ID (Run Number)</b>: Run ID refers to a specific number assigned to a particular scanning process or data collection run conducted by the SDSS. The run_ID allows researchers to identify and group observations made during a specific data collection session. It helps ensure data integrity and facilitates the organization of observations for further analysis.

6. <b>rerun_ID (Rerun Number)</b>: Rerun ID represents a specific number indicating how the images were processed or analyzed during data reduction. The rerun_ID helps ensure consistency and allows researchers to trace the data processing steps applied to each observation. This information could be useful for reproducibility and verifying the accuracy of results.

7. <b>cam_col (Camera Column)</b>: Cam_col is a value that identifies the scanline within a particular run. This feature helps locate the specific position or scanline on the sky where the observation was taken. It aids in organizing data and enables researchers to study objects within the same scanline for potential correlations or patterns.

8. <b>field_ID (Field Number)</b>: Field_ID is a unique number that identifies individual fields in the dataset, each covering a specific area of the sky. Field_ID allows astronomers to group observations based on their location in the sky. This grouping helps study objects in different regions and understand how various celestial phenomena might vary across the sky.

9. <b>spec_obj_ID (Spectroscopic Object Identifier)</b>: Spec_obj_ID is a unique identifier assigned to optical spectroscopic objects. If two observations share the same spec_obj_ID, it means they correspond to the same celestial object. Spectroscopy provides valuable information about the composition, motion, and properties of celestial objects. Spec_obj_ID allows astronomers to associate spectroscopic data with specific objects, ensuring consistency and facilitating the analysis of object-specific characteristics.

10. <b>class (Object Class)</b>: Class is the target variable and it represents the classification of each object into one of three categories: galaxy, star, or quasar. Object classification is fundamental in understanding the diversity of celestial objects present in the dataset. By categorizing objects into galaxies, stars, or quasars, researchers can study their unique properties, evolutionary processes, and interactions within the universe.

11. <b>redshift (Redshift Value)</b>: Redshift is a numerical value representing the increase in wavelength of light from a celestial object due to its motion away from Earth. Redshift provides vital information about the distance and velocity of objects in the universe. It allows astronomers to calculate the expansion of the universe and study the cosmic evolution of galaxies and other celestial structures.

12. <b>plate (Plate ID)</b>: Plate ID is a unique identifier for each photographic plate used in the SDSS. Plates play an important role in collecting light from celestial objects and capturing their spectra. Plate ID allows researchers to associate spectroscopic data with the specific plate used, ensuring data traceability and precision.

13. <b>MJD (Modified Julian Date)</b>: MJD represents the Modified Julian Date, which indicates when a particular piece of SDSS data was taken. MJD is a precise time stamp for each observation, allowing astronomers to organize data chronologically. It helps in studying time-dependent phenomena, tracking changes in objects, and conducting temporal analyses.

14. <b>fiber_ID (Fiber ID)</b>: Fiber_ID is a unique identifier for the fiber used to collect light from the focal plane during each observation. Fiber_ID plays a critical role in spectroscopy, as it identifies which part of the sky was targeted for observation. It enables researchers to associate spectra with specific regions of celestial objects and study their chemical composition, motion, and other spectroscopic features.


Overall, this dataset provides a comprehensive collection of information that allows us to understand various aspects of celestial objects, their properties, and their interactions in the vast expanse of the universe. The combination of spatial, spectral, and photometric data empowers astronomers to unveil the mysteries of the cosmos and advance our knowledge of the universe we inhabit.


<h2>Methodology</h2>

To achieve these objectives, the project will involve the following steps:

<b>Exploratory Data Analysis (EDA)</b>: EDA will involve visually and statistically examining the dataset's features, distributions, relationships, and potential patterns. EDA serves as a foundation for informed decision-making during subsequent stages of the project. I will create various visualizations to gain insights into the distribution and relationships of the features. The visualizations will include:
- Box plots to identify potential outliers and variations across different classes
- Density plots to visualize feature distributions
- Correlation heatmap to understand feature interactions and potential multicollinearity

<b>Feature Engineering</b>: Extracting relevant features from the spectral data that capture the distinguishing characteristics of each celestial object. This could involve techniques such as dimensionality reduction and feature selection to focus on the most informative aspects.

<b>Model Development</b>: Designing and training a robust machine learning model that can learn from the spectral features and classify objects accurately. Various algorithms and architectures, such as support vector machines, random forests, or convolutional neural networks, may be explored and fine-tuned to achieve optimal performance.

<b>Model Evaluation</b>: Assessing the performance of the predictive model using appropriate metrics like accuracy, precision, recall, and F1-score. The model's generalization and ability to correctly classify unseen data will be thoroughly tested to ensure its reliability.

<b>Interpretation and Insights</b>: Analyzing the model's predictions and interpreting its decision-making process to gain insights into the spectral characteristics that drive accurate classifications. Understanding these patterns can provide valuable scientific insights and aid in refining the model further.

<b>Application to New Data</b>: Deploying the trained model to classify new, previously unseen celestial objects based on their spectral data. This application will enable astronomers to efficiently analyze and categorize a vast amount of data obtained from ongoing and future sky surveys.

This project's ultimate goal is to empower astronomers with a powerful tool for classifying stars, quasars, and galaxies based on their spectral characteristics. By leveraging machine learning techniques, the project seeks to deepen our understanding of the cosmos, unravel the mysteries of the universe's evolution, and contribute to the advancement of astronomical research.


<h2>Exploratory Data Analysis (EDA)</h2>

The EDA focused on boxplots, density plots, and a correlation heatmap to gain insights into the data. The key findings are as follows:

<b>Boxplots</b>: Through boxplots, I visualized the distribution of feature values for each class ("STAR," "GALAXY," and potentially "QUASAR") separately. Notably, features "u," "g," "z," "i," and "r" displayed a few outliers in their distributions. These outliers may impact the performance of the predictive model and should be addressed using appropriate data cleansing and outlier handling techniques.

![](/images/img4.jpg)

<b>Density Plot</b>: The density plot allowed me to visualize the Probability Density Function (PDF) for each feature based on the target class. I observed considerable overlap in the distributions of feature values for different classes. This implies that simple logical statements based on individual feature values may not suffice for accurate classification. As such, I recognize the need to employ advanced statistical modeling methods to effectively categorize the classes.

<b>Correlation Heatmap</b>: By analyzing the correlation heatmap, I identified the strength and direction of linear relationships between features. Notably, "u" and "g," "u" and "z," as well as "g" and "z" exhibited perfect positive correlations (correlation coefficient of 1). Additionally, "i" and "r" displayed a very strong positive correlation (correlation coefficient of 0.96). However, most other features had relatively low correlation coefficients (close to 0), indicating weak or no linear relationships.

![](/images/img6.jpg)

<h2>Feature Engineering</h2>

The feature engineering was performed in two steps - first I calculated the magnitude differences and next feature interactions were created for bands and redshift. 

<b>1. Magnitude Differences:</b>
The feature engineering step of "Magnitude Differences" involves computing the differences between magnitudes in different bands (u, g, r, i, z). I create new features that represent the differences in brightness between adjacent bands. The differences in magnitudes can provide valuable information about the spectral characteristics of the objects. The variations in brightness across different bands can be indicative of the object's nature, such as its temperature, composition, or distance. By creating "Magnitude Differences," I aim to capture spectral variations in the objects, helping my model to distinguish different classes based on their unique brightness patterns across different bands.

<b>2. Magnitude-Spectral Index Interactions:</b>
The feature engineering step of "Magnitude-Spectral Index Interactions" involves interacting the magnitudes in different bands (u, g, r, i, z) with the spectral index (redshift). The redshift is a measure of how much an object's light has been shifted towards longer wavelengths due to the expansion of the universe. By interacting the magnitudes with the redshift, I aim to capture how the object's brightness in different bands changes as a function of its redshift. The interactions between magnitudes and the spectral index can reveal how an object's brightness varies with its distance from us. This is essential because the redshift is an important parameter for classifying objects like galaxies and quasars, as it provides information about their cosmological distance.

The feature engineering steps I performed aim to create new features that enhance the representation of the data and capture important spectral characteristics of the objects in the dataset. These engineered features can potentially improve my model's ability to discern subtle patterns and enhance its predictive performance. Additionally, they provide the model with richer information, enabling it to make more informed decisions when classifying stars, quasars, and galaxies based on their spectral characteristics.

<h2>Model Development</h2>

In the quest to accurately classify stars, quasars, and galaxies based on their spectral characteristics, the Random Forest Classifier was employed as a robust and powerful tool.

Central to the success of this endeavor was the utilization of the Label Binarizer technique. Given the multi-class nature of the classification task—stars, quasars, and galaxies—the Label Binarizer played a crucial role in transforming categorical labels into a binary matrix format. This transformation facilitated the model's ability to comprehend and distinguish between different classes effectively.

Initially, the Label Binarizer was employed to fit and transform the training labels (y_train). This process encoded the multi-class labels into a binary matrix suitable for model training. It enabled the Random Forest Classifier to grasp the distinct categories present in the target variable. Following the training label encoding, the Label Binarizer was also applied to transform the cross-validation (y_cv) and test labels (y_test).

Using the Label Binarizer alongside the Random Forest Classifier really boosted the performance of the classification process. The Random Forest model I ended up with showed an impressive F1-score of 0.97, highlighting its ability to effectively decipher complex spectral patterns and differentiate between stars, quasars, and galaxies.

<h2>Feature Importance</h2>

Feature importance analysis provides insights into the relevance of individual features and helps us understand their impact on the model's performance. I conducted feature importance analysis using a Random Forest classifier. This approach allowed me to rank features based on their contribution to the model's decision-making process. By leveraging the inherent feature importance attribute of the Random Forest classifier, the Gini importance scores are computed for each feature. These scores reflect the reduction in impurity achieved by each feature during the construction of decision trees within the forest. To enhance the interpretability of my findings, I visualized the feature importance scores using graphical representations such as bar plots. From insights gained from feature importance analysis, I can make informed decisions about which features to retain, modify, or exclude. By identifying and retaining only the most relevant features, I can effectively reduce the dimensionality of the dataset. This not only accelerates the model training process but also mitigates the risk of overfitting.

![](/images/img7.jpg)

The feature importance scores attributed to redshift, u_redshift, z_redshift, i_redshift, r_i, g_redshift, and r_redshift in the analysis underscore their pivotal role in the classification task. Redshift, a fundamental cosmological parameter, provides crucial information about an object's distance and cosmic evolution. The inclusion of redshift-derived attributes, such as u_redshift, z_redshift, i_redshift, g_redshift, and r_redshift, extends this insight across different spectral bands, enabling the model to glean diverse spectral signatures. Furthermore, the r-i color index encapsulates the nuanced color variations between the r and i wavelength bands, yielding essential details about an object's physical properties. The high feature importance attributed to r-i, alongside the aforementioned redshift-related features, underscores their collective significance in discerning unique characteristics across astronomical objects. By harnessing these features, the model gains a multi-faceted understanding of celestial objects, leveraging their redshift variations, color contrasts, and spectral nuances. This comprehensive approach empowers the model to make refined distinctions among stars, galaxies, and quasars, thereby enhancing its classification accuracy and overall performance.

<h2>Hyperparameter Tuning</h2>

Hyperparameter tuning is a critical step in optimizing the performance of machine learning models. It involves systematically searching through different combinations of hyperparameters to identify the configuration that yields the best results. I conducted hyperparameter tuning using a Randomized Search approach, which strikes a balance between exploring the hyperparameter space and computational efficiency.

I followed these steps for hyperparameter tuning:

<b>Parameter Grid Definition</b>: I specified a range of hyperparameters, such as the number of estimators, maximum depth, and minimum samples per leaf, that significantly impact the Random Forest model's behavior and performance.

<b>Randomized Search</b>: Utilizing the RandomizedSearchCV function, I performed a randomized search over the defined parameter grid. This involved training and evaluating the Random Forest classifier with various hyperparameter combinations using cross-validation.

<b>Best Model Selection</b>: Upon completion of the search, I selected the hyperparameters that resulted in the highest F1 score on the cross-validation dataset.

<b>Performance Evaluation</b>: I assessed the tuned model's performance on the test dataset to ensure that the hyperparameter tuning process did not lead to overfitting.

Hyperparameter tuning is an indispensable step in the model development pipeline as it fine-tunes the model for optimal performance. The strategic utilization of this technique enhances the model's predictive capabilities and prepares it for real-world challenges.

<h2>Alternative Models</h2>

Upon achieving a good F1 score with the Random Forest (RF) model, I wanted to explore alternative modeling approaches. The motivation behind this was to determine whether other techniques could further improve the classification performance. The first contender on my list was XGBoost, a formidable model known for its adeptness in handling complex datasets. It presented itself as a sophisticated evolution of RF, introducing a range of hyperparameters to fine-tune. I planned to experiment with parameters such as the learning rate and tree depth, to unlock the model's latent potential and enhance the F1 score.

The table below shows a comparison of the types of models I wanted to explore.

| Model | Interpretability  | Computation Speed | Cons| Best Use Cases|
| ------------- | ------------- | ------------- | ------------- |------------- |
| Random Forest  | Moderate  | Moderate  | Prone to overfitting on noisy data | General classification  |
| XGBoost  | 	Low | Moderate  | Slightly more complex to tune | Medium to large datasets |
| Support Vector Machines (SVM) | Low | Low  | Can be sensitive to hyperparameters and kernel choice | High-dimensional data |
| Neural Networks | Low to Moderate | Variable  | Requires more data and extensive tuning and resource-intensive | Complex data patterns |

For this project, I decided to focus on using Random Forest and XGBoost as they are both powerful ensemble learning algorithms. The choice between them often depends on the specific characteristics of the dataset. Below is a comparison of these two models in terms of several key aspects.

<b>Accuracy</b>: XGBoost generally performs better in terms of predictive accuracy and can handle complex relationships between features and target variables. It often achieves higher accuracy due to its advanced regularization techniques and optimization algorithms. Random Forest is also accurate and performs well for a wide range of datasets. However, it may not handle extremely complex relationships as effectively as XGBoost.

<b>Interpretability</b>: XGBoost's predictive power often comes at the cost of interpretability. It can be more challenging to interpret the feature importance and interactions due to its complexity.
Random Forest: Random Forest is generally more interpretable than XGBoost. It provides straightforward feature importance rankings and insights into feature interactions.

<b>Speed and Scalability</b>: XGBoost is often faster and more scalable than Random Forest. It is designed for efficiency and can handle large datasets more effectively, making it suitable for real-time and big data applications. While Random Forest is efficient, XGBoost's optimization techniques make it better suited for large datasets with many features.

<b>Handling Imbalanced Data</b>: XGBoost has techniques to handle imbalanced data, such as using class weights and focusing on misclassification errors. Random Forest may struggle with imbalanced data and may require additional techniques, such as resampling or adjusting class weights.

<b>Hyperparameter Tuning</b>: XGBoost has a wide range of hyperparameters to fine-tune, which can lead to superior performance with proper tuning. This, however, requires careful experimentation and can be time-consuming. Random Forest has fewer hyperparameters to tune, which can make it quicker to find an initial well-performing model.

Therefore, XGBoost tends to excel in predictive accuracy and scalability, making it a go-to choice for many applications. However, if interpretability and simplicity are key, Random Forest might be a better option. I decided to try out both of these models in this project as there often tends to be a trade-off between accuracy and interpretability.

<h2>XGBoost Model</h2>

To further enhance the classification accuracy, F1-score, and overall predictive capabilities I built an XGBoost model. XGBoost model's robustness lies in its adaptability to complex data and its capacity to handle intricate relationships within features. Furthermore, XGBoost's ensemble nature, combining the predictions of multiple models, mitigates overfitting risks and enhances generalization. While my initial Random Forest model showcased commendable F1-scores, I aspired for even higher levels of precision, recall, and overall predictive accuracy. XGBoost is known for its ability to effectively balance precision and recall, a key factor in achieving elevated F1-scores. The model achieves this through a sophisticated interplay of boosting and regularization techniques, optimizing the trade-off between false positives and false negatives. After building the model, I fine-tuned the model using hyperparameter tuning techniques to identify the optimal parameter combination. This ensured that the model adapts well to my specific dataset and maximizes its predictive power.

<h3>Precision, Recall, and F1-Score Analysis</h3>

Below is the confusion matrix obtained when the prediction was made using the test data.

![](/images/img8.JPG)

For the GALAXY class, the model demonstrates exceptional precision of 0.98, signifying that when it predicts an object as a galaxy, it is correct 98% of the time. Additionally, the recall of 0.99 implies that the model captures 99% of all actual galaxies. This combination of high precision and recall leads to an impressive F1-score of 0.98, indicating a robust ability to accurately classify galaxies.

The QSO class also showcases remarkable performance. The model achieves a precision of 0.96, meaning that 96% of objects predicted as QSOs are indeed QSOs. The recall of 0.93 indicates that the model identifies 93% of all actual QSOs. This balance between precision and recall contributes to an F1-score of 0.95, highlighting the model's effectiveness in recognizing QSOs.

For the STAR class, the model attains the highest level of precision and recall, both equating to 1.00. This signifies that the model's predictions for stars are consistently correct, and it captures all instances of actual stars. Consequently, the F1-score of 1.00 reflects the model's impeccable ability to classify stars with complete accuracy.

The overall accuracy of the tuned XGBoost model is an impressive 0.98, denoting that it correctly classifies celestial objects nearly 98% of the time. The macro average F1-score of 0.98 demonstrates the model's balanced performance across all classes, further affirming its generalization ability.

Therefore, the tuned XGBoost model delivers exceptional results with high precision, recall, and F1-scores for each class. Its ability to accurately classify celestial objects as galaxies, quasars, or stars showcases its potential for a variety of astronomical applications, such as object categorization and identification in large-scale sky surveys. The successful outcome of the tuned XGBoost model emphasizes its significance as a valuable tool in advancing our understanding of celestial bodies and their intricate characteristics.

<h3>Summary of Findings</h3>

Throughout this project, my primary goal was to construct a robust classification model capable of effectively distinguishing between stars, galaxies, and quasars. I delved into two powerful algorithms - the Random Forest Classifier and the XGBoost Classifier - in my quest to unveil the intricate details hidden within the spectral signatures of these cosmic entities.

My exploration unveiled the strengths of the Random Forest model, which, after careful tuning, emerged as a strong contender. Achieving an impressive F1-score of 0.97, this model demonstrated its ability to uncover the subtle patterns inherent in the spectral data. By thoughtfully engineering attributes, especially those derived from redshift values and color indices, I enhanced the model's capacity to differentiate between these celestial objects. The classification report that followed highlighted its precision, recall, and overall accuracy, confirming the Random Forest model's competence in this astronomical classification task.

Building on this success, I proceeded to craft an XGBoost model with the aim of surpassing the F1-score I achieved earlier. Remarkably, this endeavor led me to a model that achieved an F1-score of 0.98, surpassing my expectations. Precision and recall metrics for each class reaffirmed the model's adeptness in handling intricate distinctions. This exploration further emphasized the significance of redshift-related parameters and magnitude variations in refining the model's classification accuracy. The classification report attested to the model's remarkable capability to discern the subtle differences embedded within the astronomical classes.

In conclusion, this project showcases my journey in developing effective models that unravel the complexities of celestial spectra. By meticulously engineering features, fine-tuning algorithms, and making innovative choices, I created models that not only met but exceeded my goals. As I look ahead, the potential applications of these models extend beyond my explorations here, casting a promising light on their role in enhancing our understanding of the cosmos.
