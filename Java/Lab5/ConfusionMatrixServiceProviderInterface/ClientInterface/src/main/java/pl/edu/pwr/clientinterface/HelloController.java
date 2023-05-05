package pl.edu.pwr.clientinterface;

import ex.api.AnalysisException;
import ex.api.AnalysisService;
import ex.api.DataSet;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import javafx.scene.layout.AnchorPane;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import java.io.*;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;

public class HelloController implements Initializable {

    @FXML
    private TextField chooseFileTextField;
    @FXML
    private AnchorPane ap;
    @FXML
    private Label messageLabel;
    @FXML
    private TextArea matrixTextArea;
    @FXML
    private ListView availableServicesListView;
    @FXML
    private TextField resultTextField;
    private List<String> header = new ArrayList<>();
    private List<List<String>> data = new ArrayList<>();
    private int datalength = 0;
    private ServiceLoader<AnalysisService> loader;

    @FXML
    private void chooseFile(){
        resultTextField.setText("");
        Stage stage = (Stage) ap.getScene().getWindow();
        FileChooser fileChooser = new FileChooser();
        fileChooser.setTitle("Choose csv file with data");
        fileChooser.setInitialDirectory(new File(System.getProperty("user.dir")));
        fileChooser.getExtensionFilters().add(new FileChooser.ExtensionFilter("csv files", "*.csv"));
        File file = fileChooser.showOpenDialog(stage);
        if(file != null){
            chooseFileTextField.setText(String.valueOf(file));
        }
    }

    @FXML
    private void calculate() throws AnalysisException {
        resultTextField.setText("");
        DataSet ds = checkValidEdited2();
        if(ds == null) return;
        messageLabel.setText("");
        Object selectedService = availableServicesListView.getSelectionModel().getSelectedItem();
        if(selectedService == null){
            messageLabel.setText("Choose service first!");
            return;
        }
        messageLabel.setText("");
        String selectedServiceName = selectedService.toString();
        for(AnalysisService service: loader){
            if(service.getName().equals(selectedServiceName)){
                service.submit(ds);
                break;
            }
        }
    }

    @FXML
    private void getResult() throws AnalysisException {
        Object selectedService = availableServicesListView.getSelectionModel().getSelectedItem();
        if(selectedService == null){
            messageLabel.setText("Choose service first!");
            return;
        }
        messageLabel.setText("");
        String selectedServiceName = selectedService.toString();
        for(AnalysisService service: loader){
            if(service.getName().equals(selectedServiceName)){
                DataSet res = service.retrieve(true);
                if(res == null){
                    messageLabel.setText("Service processes data or does not have required data!");
                }else{
                    resultTextField.setText(res.getData()[0][0]);
                }
            }
        }
    }

    private boolean checkIfFileExists(){
        String chosenFile = chooseFileTextField.getText();
        int chosenFileLength = chosenFile.length();
        if(chosenFileLength <= 4 || (!
                chosenFile.substring(chosenFileLength - 4,chosenFileLength).equals(".csv"))){
            messageLabel.setText("Select valid csv file first!");
            return false;
        }
        Path path = Paths.get(chosenFile);
        if(!Files.exists(path)){
            messageLabel.setText("File does not exist!");
            return false;
        }
        return true;
    }

    @FXML
    private void getDataFromFile(){
        if(! checkIfFileExists()) return;
        messageLabel.setText("");
        data.clear();
        try(BufferedReader reader = new BufferedReader(new FileReader(chooseFileTextField.getText()))) {
            header = Arrays.asList(reader.readLine().split(";"));
            String line;
            List<String> tempRow;
            while((line = reader.readLine()) != null){
                tempRow = Arrays.asList(line.split(";"));
                data.add(tempRow);
            }
            datalength = header.size();
            if(datalength < 2){
                messageLabel.setText("File contains invalid data!");
                return;
            }
            if(data.size() != datalength){
                messageLabel.setText("File contains invalid data!");
                return;
            }
            data.forEach(d -> {
                if(d.size() != datalength){
                    messageLabel.setText("File contains invalid data!");
                    return;
                }
            });
            renderUserView();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void renderUserView(){
        int max = 5;
        for(int i = 0; i < datalength; i++){
            if(header.get(i).length() > max) {
                max = header.get(i).length();
            }
        }
        for(int i = 0; i < datalength; i++) {
            for(int j = 0; j < datalength; j++) {
                if (data.get(i).get(j).length() > max) {
                    max = data.get(i).get(j).length();
                }
            }
        }
        matrixTextArea.setText("");
        matrixTextArea.appendText(getJustified("Class", max));
        for(int i = 0; i < datalength; i++){
            matrixTextArea.appendText(getJustified(header.get(i), max));
        }
        matrixTextArea.appendText("\n");
        for(int i = 0; i < datalength; i++){
            matrixTextArea.appendText(getJustified(header.get(i), max));
            for(int j = 0; j < datalength; j++) {
                matrixTextArea.appendText(getJustified( data.get(i).get(j), max));
            }
            matrixTextArea.appendText("\n");
        }
    }

    private String getJustified(String s, int len){
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < len - s.length(); i++)
            sb.append(" ");
        sb.append(s + " ");
        return sb.toString();
    }

    private String checkValidEdited(){
        String[] lines = matrixTextArea.getText().split(("[\\r\\n]+"));
        String outputString = "";
        StringBuilder sb = new StringBuilder();
        datalength = lines.length - 1;
        if(datalength < 2){
            messageLabel.setText("Edited matrix has invalid format");
            return null;
        }
        for(int i = 0; i < lines.length; i++){
            lines[i] = lines[i].trim();
            String [] tempStr= lines[i].split("\\s+");
            if(tempStr.length != datalength + 1) {
                messageLabel.setText("Edited matrix has invalid format");
                return null;
            }
            for(int j = 1; j < datalength + 1; j++){
                sb.append(tempStr[j] + ";");
            }
            sb.append("\n");
        }
        return sb.toString();
    }

    private DataSet checkValidEdited2(){
        String[] lines = matrixTextArea.getText().split(("[\\r\\n]+"));
        String[] outputHeader = new String[datalength];
        String[][] outputData = new String[datalength][datalength];
        datalength = lines.length - 1;
        if(datalength < 2){
            messageLabel.setText("Edited matrix has invalid format or was not readed in yet!");
            return null;
        }
        lines[0] = lines[0].trim();
        String [] tmpStr= lines[0].split("\\s+");
        if(tmpStr.length != datalength + 1) {
            messageLabel.setText("Edited matrix has invalid format");
            return null;
        }
        for(int j = 1; j < datalength + 1; j++){
            outputHeader[j - 1] = tmpStr[j];
        }
        for(int i = 1; i < lines.length; i++){
            lines[i] = lines[i].trim();
            String [] tempStr = lines[i].split("\\s+");
            if(tempStr.length != datalength + 1) {
                messageLabel.setText("Edited matrix has invalid format");
                return null;
            }
            for(int j = 1; j < datalength + 1; j++){
                outputData[i - 1][j - 1] = tempStr[j];
            }
        }
        DataSet ds = new DataSet();
        ds.setData(outputData);
        ds.setHeader(outputHeader);
        return ds;
    }

    @FXML
    private void saveDataToFile() {
        if (!checkIfFileExists()) return;
        String outputString = checkValidEdited();
        if (outputString == null) return;
        messageLabel.setText("");
        try (FileWriter writer = new FileWriter(chooseFileTextField.getText())) {
            writer.write(outputString);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        matrixTextArea.setFont(Font.font("Consolas"));
        messageLabel.setTextFill(Color.color(1, 0, 0));
        loader = ServiceLoader.load(AnalysisService.class);
        ObservableList<String> observableList = FXCollections.observableArrayList();
        for(AnalysisService service: loader){
            observableList.add(service.getName());
        }
        availableServicesListView.setItems(observableList);
    }
}