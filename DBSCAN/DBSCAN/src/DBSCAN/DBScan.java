package DBSCAN;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.Math;
import java.util.ArrayList;
import java.util.LinkedHashSet;

public class DBScan {

	public static void main(String[] args) throws IOException {
		String filePath = "B:/UB_CS/DataMining/Project2/Data/new_dataset_1.txt";
		double [][] dataMatrix = readFileCreateMatrix(filePath).clone();
		//Finding Clusters
		DBScanAlgorithm dbs = new DBScanAlgorithm();
		ArrayList<ArrayList<Integer>> clusters = dbs.DBScan(dataMatrix, 4, 3);
		for(ArrayList<Integer> x: clusters){
			System.out.println(x);
		}
		//Calculating Jaccard Coefficient & RandIndex
		dbs.getJaccardCoefficientAndRAND(filePath, clusters);
		//Doing PCA
		double reducedDataMatrix[][] = dbs.getReducedDataMatrix(dataMatrix.clone(), clusters,2);
		String outputFilePath1 = "C:/Users/Anuj/Desktop/Clustered_Reduced.txt";
		String outputFilePath2 = "C:/Users/Anuj/Desktop/Given_Reduced.txt";
		dbs.getReducedMatrixInFileForFormedClusters(reducedDataMatrix, clusters, outputFilePath1); 
		dbs.getReducedMatrixInFileForGivenClusters(reducedDataMatrix, filePath, outputFilePath2);
	}
	
	
	//File read and construct matrix
	public static double [][] readFileCreateMatrix(String location) throws IOException{
		File fName = new File(location);
		FileReader newFile = new FileReader(fName);
		BufferedReader readFile = new BufferedReader(newFile);
		String line = null;
		int numberOfRows =1;
		int numberOfColumns = 0;
		while( (line=readFile.readLine()) !=null){
			String [] terms = line.split("\t");
			++numberOfRows;
			numberOfColumns = terms.length;
		}
		numberOfRows = (numberOfRows-1);
		numberOfColumns = (numberOfColumns-2);
		
		double dataMatrix[][] = new double[numberOfRows][numberOfColumns];
		System.out.println("Data Matrix Created with : ROWS= " + numberOfRows + " : COLUMNS= " +numberOfColumns);
		
		fName = new File(location);
		newFile = new FileReader(fName);
		readFile = new BufferedReader(newFile);
		int matrixRowsToFill = 0;
		while((line = readFile.readLine()) != null){
			String [] terms= line.split("\t");
			for(int i=2;i<terms.length;i++){
				dataMatrix[matrixRowsToFill][i-2] = Double.parseDouble(terms[i]);
			}
			++matrixRowsToFill;
		}
		System.out.println("Data Matrix filled dimensions : ROWS= " + dataMatrix.length + " : COLUMNS= " + dataMatrix[0].length);
		readFile.close();
		return dataMatrix;
	}
	

	
	

}
