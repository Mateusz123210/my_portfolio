package pl.edu.pwr.discreteconvolutionfunction;

import javafx.fxml.FXML;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.FileChooser;
import javafx.stage.Stage;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class HelloController{

    @FXML
    private TextField dataTextField;
    @FXML
    private TextField kernelTextField;
    @FXML
    private TextField cRepetitions;
    @FXML
    private TextField javaRepetitions;
    @FXML
    private TextArea result;
    @FXML
    private AnchorPane ap;
    private int[][] data = null;
    private int[][] kernel = null;
    private List<List<String>> dataCollection = new ArrayList<>();
    private List<List<String>> kernelCollection = new ArrayList<>();
    private final DiscreteConvolutionFunction dcf;

    public HelloController(){
        dcf = new DiscreteConvolutionFunction();
    }

    @FXML
    protected void chooseData(){
        chooseFile(dataTextField);
    }

    @FXML
    protected void chooseKernel(){
        chooseFile(kernelTextField);
    }

    @FXML
    protected void readDataFromFiles(){
        clearReadedDataAndKernel();
        String dataFile = dataTextField.getText();
        String kernelFile = kernelTextField.getText();
        if(checkIfFileNotExists(dataFile)) return;
        if(checkIfFileNotExists(kernelFile)) return;
        try{
            readFromFile(dataFile, dataCollection);
        } catch (IOException e) {
            e.printStackTrace();
            result.setText("Error in reading data from file");
            return;
        }
        try{
            readFromFile(kernelFile, kernelCollection);
        } catch (IOException e) {
            e.printStackTrace();
            result.setText("Error in reading kernel from file");
            return;
        }
        int dataSize = dataCollection.size();
        int kernelSize = kernelCollection.size();
        if(kernelSize > dataSize){
            result.setText("Kernel size can not be bigger than data size");
            return;
        }
        dataCollection.forEach(a -> {
            if(a.size() != dataSize){
                result.setText("Data file is invalid");
                return;
            }
        });
        kernelCollection.forEach(a -> {
            if(a.size() != kernelSize){
                result.setText("Kernel file is invalid");
                return;
            }
        });
        try{
            data = dataCollection.stream()
                    .map(l -> l.stream().mapToInt(Integer::parseInt).toArray())
                    .toArray(int[][]::new);
            kernel = kernelCollection.stream()
                    .map(l -> l.stream().mapToInt(Integer::parseInt).toArray())
                    .toArray(int[][]::new);
        }catch(Exception e){
            clearReadedDataAndKernel();
            result.setText("Error in loading files");
            return;
        }
        result.setText("Files readed from disc");
    }

    @FXML
    protected void runCPlusPlusMethod(){
        String cRepetitionsStr = cRepetitions.getText();
        if(cRepetitionsStr.length() == 0){
            result.setText("Write repetitions number first");
            return;
        }
        int cRepetitionsInt;
        try {
            cRepetitionsInt = Integer.parseInt(cRepetitionsStr);
        }catch(NumberFormatException e){
            result.setText("Write valid repetitions number");
            return;
        }
        if(cRepetitionsInt <= 0){
            result.setText("Repetitions number must be bigger than 0");
            return;
        }
        if(data == null || kernel == null){
            result.setText("Read data from files first");
            return;
        }
        int[][] response = null;
        long startTime = System.nanoTime();
        for(int i = 0; i < cRepetitionsInt; i++) {
            response = dcf.calculateDiscreteConvolutionFunctionNative(data, kernel);
        }
        long endTime   = System.nanoTime();
        long totalTime = endTime - startTime;
        double time = (double) totalTime / 1_000_000_000;

        result.setText("Native calculation ended\nTime: " + time +" s");
        saveResultToFile(response, "c++_result.csv");
    }

    @FXML
    protected void runJavaMethod(){
        String javaRepetitionsStr = javaRepetitions.getText();
        if(javaRepetitionsStr.length() == 0){
            result.setText("Write repetitions number first");
            return;
        }
        int javaRepetitionsInt;
        try {
            javaRepetitionsInt = Integer.parseInt(javaRepetitionsStr);
        }catch(NumberFormatException e){
            result.setText("Write valid repetitions number");
            return;
        }
        if(javaRepetitionsInt <= 0){
            result.setText("Repetitions number must be bigger than 0");
            return;
        }
        if(data == null || kernel == null){
            result.setText("Read data from files first");
            return;
        }
        int[][] response = null;
        long startTime = System.nanoTime();
        for(int i = 0; i < javaRepetitionsInt; i++) {
            response = dcf.calculateDiscreteConvolutionFunction(data, kernel);
        }
        long endTime   = System.nanoTime();
        long totalTime = endTime - startTime;
        double time = (double) totalTime / 1_000_000_000;
        result.setText("Java calculation ended\nTime: " + time +" s");
        saveResultToFile(response, "java_result.csv");
    }

    protected void saveResultToFile(int[][] res, String fileName){
        try(BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))){
            for (int[] re : res) {
                for (int i : re) {
                    writer.write(i + ";");
                }
                writer.write("\n");
            }
        } catch (IOException e) {
            result.setText(result.getText() + "\nResult has not been saved to file");
            return;
        }
        result.setText(result.getText() + "\nResult has been saved to file " + fileName + "\n" +
                "Data size: " + data.length + ", Kernel size: " + kernel.length);
    }

    protected void readFromFile(String file, List<List<String>> col) throws IOException {
        try(BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            List<String> tempRow;
            while((line = reader.readLine()) != null){
                tempRow = Arrays.asList(line.split(";"));
                col.add(tempRow);
            }
        } catch (IOException e) {
            throw new IOException();
        }
    }

    protected boolean checkIfFileNotExists(String chosenFile){
        int chosenFileLength = chosenFile.length();
        if(chosenFileLength <= 4 || (!
                chosenFile.substring(chosenFileLength - 4,chosenFileLength).equals(".csv"))){
            result.setText("Select valid csv files first!");
            return true;
        }
        Path path = Paths.get(chosenFile);
        if(!Files.exists(path)){
            result.setText("Select valid csv files first!");
            return true;
        }
        return false;
    }

    protected void chooseFile(TextField a){
        clearReadedDataAndKernel();
        a.setText("");
        Stage stage = (Stage) ap.getScene().getWindow();
        FileChooser fileChooser = new FileChooser();
        fileChooser.setTitle("Choose csv file with data");
        fileChooser.setInitialDirectory(new File(System.getProperty("user.dir")));
        fileChooser.getExtensionFilters().add(new FileChooser.ExtensionFilter("csv files", "*.csv"));
        File file = fileChooser.showOpenDialog(stage);
        if(file != null){
            a.setText(String.valueOf(file));
            result.setText("File chosen");
        }else{
            result.setText("");
        }
    }

    protected void clearReadedDataAndKernel(){
        data = null;
        kernel = null;
        dataCollection = new ArrayList<>();
        kernelCollection = new ArrayList<>();
    }
}