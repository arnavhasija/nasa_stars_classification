# nasa_stars_classification
The purpose of this project is to build a predictive model that can classify stars, quasars, and galaxies based on their spectral characteristics

<h2>Why I chose this project?</h2>

I have always been intrigued by outer space and all that surrounds us in this universe. It is always a humbling experience no matter how many times I watch Carl Sagan reflecting on the appearance of “Pale Blue Dot” from 6 billion kilometers away. The universe is an endlessly fascinating and vast place, full of mysteries and wonders. The "Pale Blue Dot" image, taken by the Voyager 1 spacecraft, is a truly iconic and humbling reminder of our place in the cosmos. It's a reminder that, despite our differences and the vastness of space, we are all part of a single, interconnected system. It's a powerful reminder to appreciate and care for the planet we call home. 

Last year, when I saw the highest-resolution image of the universe captured by the James Webb Space Telescope it blew me away, and appreciate everything there is yet to be learned about this universe. This level of resolution allows astronomers to study the structure and evolution of galaxies in unprecedented detail. The image could contribute significantly to our understanding of the universe and reveal many previously unknown objects and phenomena. It remains one of the most detailed and comprehensive images of the universe ever captured. Seeing the birth and death of millions of stars makes me feel more connected and makes me want to dwell and feel the presence of every star surrounding us. I often stare at the night sky for as long as I can as it always helps make all that I overthink and worry about feel so trivial.  I feel that it is very calming and therapeutic to spend time looking at the sky and contemplating the vastness of the universe. It seems to put my problems and worries into perspective and helps me feel more grounded and at peace.

![](/images/img1.JPG)

<h2>Dataset</h2>

The dataset I worked with contains a vast collection of 100,000 space observations captured by the renowned SDSS (Sloan Digital Sky Survey). Each observation is characterized by 17 distinct features and 1 essential class column, which serves the purpose of classifying the celestial objects into three categories: stars, galaxies, and quasars.

The features of this dataset are explained below and they all help provide valuable insights into the nature of each observation:

1. obj_ID (Object Identifier): This feature serves as a unique identifier for each celestial object in the dataset. It is like a special code assigned to each object to distinguish it from others. The obj_ID is essential for keeping track of individual celestial objects throughout the dataset. It helps link various observations and data related to a particular object, enabling researchers to study its properties, behavior, and characteristics.

2. alpha (Right Ascension angle): Alpha represents the angular position of a celestial object in the sky when observed from Earth. It is measured along the east-west direction and helps locate the object on the celestial sphere. Right Ascension is crucial for pinpointing the exact position of an object in the sky. It aids astronomers in determining when and where to observe specific celestial objects, making it an essential tool for navigation and observation planning.

3. delta (Declination angle): Delta denotes the angular position of a celestial object in the sky when observed from Earth. It is measured along the north-south direction and complements the Right Ascension in locating the object. Declination helps astronomers precisely locate celestial objects in the sky, providing information about their placement in relation to Earth's equator. Together with Right Ascension, it forms a celestial coordinate system essential for observational purposes.

4. u, g, r, i, z (Photometric Filters): These features represent different filters used to measure the brightness of celestial objects at specific wavelengths of light. Each filter corresponds to a specific color range. By measuring the intensity of light at various wavelengths, astronomers can derive valuable information about the object's temperature, composition, and distance from Earth. These photometric measurements are important for understanding the physical properties of celestial objects.

5. run_ID (Run Number): Run ID refers to a specific number assigned to a particular scanning process or data collection run conducted by the SDSS. The run_ID allows researchers to identify and group observations made during a specific data collection session. It helps ensure data integrity and facilitates the organization of observations for further analysis.

6. rerun_ID (Rerun Number): Rerun ID represents a specific number indicating how the images were processed or analyzed during data reduction. The rerun_ID helps ensure consistency and allows researchers to trace the data processing steps applied to each observation. This information could be useful for reproducibility and verifying the accuracy of results.

7. cam_col (Camera Column): Cam_col is a value that identifies the scanline within a particular run. This feature helps locate the specific position or scanline on the sky where the observation was taken. It aids in organizing data and enables researchers to study objects within the same scanline for potential correlations or patterns.

8. field_ID (Field Number): Field_ID is a unique number that identifies individual fields in the dataset, each covering a specific area of the sky. Field_ID allows astronomers to group observations based on their location in the sky. This grouping helps study objects in different regions and understand how various celestial phenomena might vary across the sky.

9. spec_obj_ID (Spectroscopic Object Identifier): Spec_obj_ID is a unique identifier assigned to optical spectroscopic objects. If two observations share the same spec_obj_ID, it means they correspond to the same celestial object. Spectroscopy provides valuable information about the composition, motion, and properties of celestial objects. Spec_obj_ID allows astronomers to associate spectroscopic data with specific objects, ensuring consistency and facilitating the analysis of object-specific characteristics.

10. class (Object Class): Class is the target variable and it represents the classification of each object into one of three categories: galaxy, star, or quasar. Object classification is fundamental in understanding the diversity of celestial objects present in the dataset. By categorizing objects into galaxies, stars, or quasars, researchers can study their unique properties, evolutionary processes, and interactions within the universe.

11. redshift (Redshift Value): Redshift is a numerical value representing the increase in wavelength of light from a celestial object due to its motion away from Earth. Redshift provides vital information about the distance and velocity of objects in the universe. It allows astronomers to calculate the expansion of the universe and study the cosmic evolution of galaxies and other celestial structures.

12. plate (Plate ID): Plate ID is a unique identifier for each photographic plate used in the SDSS. Plates play an important role in collecting light from celestial objects and capturing their spectra. Plate ID allows researchers to associate spectroscopic data with the specific plate used, ensuring data traceability and precision.

13. MJD (Modified Julian Date): MJD represents the Modified Julian Date, which indicates when a particular piece of SDSS data was taken. MJD is a precise time stamp for each observation, allowing astronomers to organize data chronologically. It helps in studying time-dependent phenomena, tracking changes in objects, and conducting temporal analyses.

14. fiber_ID (Fiber ID): Fiber_ID is a unique identifier for the fiber used to collect light from the focal plane during each observation. Fiber_ID plays a critical role in spectroscopy, as it identifies which part of the sky was targeted for observation. It enables researchers to associate spectra with specific regions of celestial objects and study their chemical composition, motion, and other spectroscopic features.


Overall, this dataset provides a comprehensive collection of information that allows us to understand various aspects of celestial objects, their properties, and their interactions in the vast expanse of the universe. The combination of spatial, spectral, and photometric data empowers astronomers to unveil the mysteries of the cosmos and advance our knowledge of the universe we inhabit.
