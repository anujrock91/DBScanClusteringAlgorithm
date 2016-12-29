*********************
****  Jars   ****
*********************
Jama-1.0.3
jmat_5.0
pca_transform-1.0.1
pca_transform-1.0.1-sources
commons-cli-1.2
hadoop-core-1.2.1

The following jars are used within the code. They need to be included for the project to build.
There is one Java project that can be directly opened in eclipse


*********************
**  Density Based Clustering **
*********************

1. Open Eclispe and load the jars and open the project.
2. In the DBScan.java class, provide the path to your input file.
3. In line 29, outputFilePath1 variable, provide a path where your reduced matrix after PCA will be dumped on the system. This reduced matrix will be for algorithm output.
4. In line 30, outputFilePath2 variable, provide a path where your reduced matrix after PCA will be dumped on the system. This reduced matrix will be for Given data set.
5. Open an editor where you can run python code.
6. Open plot.py file provided. 
7. At line 7, in givenFilePath, give the path of the file created at step-4.
8. At line 8, in resultFilePath give the path of the file created at Step-3.
9 Run the code. Graphs will be plotted, and which color corresponds to which cluster can be seen on the console of the editor or the running tool.



*************************************************************************************************************************************************************

*********************
**  PCA for hadoop output **
*********************

1. Open Test.java file from the project.
2. At line 11, in groundTruthFilepath specify the path of the ground truth file.
3. At line 12, in outputFilepath specify the path of the MR output file.
4. At line 14, in outputReducedMatrixPath specify the path where reduced matrix for algorithm output will be created.
5. At line 15, in inputReducedMatrixPath specify the path where reduced matrix for given data set will be created.
6. Post this follow all the steps as per the above Density Based Clustering (5-9).

**************************************************************************************************************************************************************