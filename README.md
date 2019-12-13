# Car Evaluation developed by Yash Choudhary
# Use Machine Learning Algorithm to predict vehicle evaluations
# Use it to decide which car to buy or build

Note: User must have Python preinstalled.
 
# How To Use the project to predict car results:
	Open your command prompt
	Go to the project directory using the cd command
	Now we have to download the python libraries used in the project (only one time requirement)
		use the command - "pip install -r requirements.txt"
	Now we can start the GUI by typing the command "python KNN_GUI.py"
	

# How to make your own model (Only for users with programming knowledge):
	Open your IDE or text editer (can use IDLE)
	Open the KNN_MODEL.py file
	Save the training data file you have in the same directory as KNN_MODEL.py file
	Change "car.txt" in line 7 to your training data-set file name
	Fit the label encoder, variable (x, y) according to your data
	You can customize how much % of data you want to use as training data and testing data in line 23
	Try for different values of k or neighbors (Only odd numbers) in line 25
	Try till you reach atleast 95% accuracy or more.

	
# Data File Format:
	The data file should be in a csv format for the program to run.
	Read the Example Data file, named "Ex-Data" to check out the format.
