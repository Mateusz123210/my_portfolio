package com.example.filesmd5snapshotapplication;

import com.example.directorysearch.FileChooser;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import com.example.directorysearch.Checker;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;
import java.io.IOException;
import java.util.HashMap;

public class HelloController {
    private String directory = "";
    private Checker checker;
    private FileChooser chooser;
    public HelloController(){
        this.checker = new Checker();
        this.chooser = new FileChooser();
    }
    @FXML private AnchorPane ap;
    @FXML
    private Label directoryText;

    @FXML
    private Button chooseDirectory;

    @FXML
    private TextField directoryTextField;

    @FXML
    private TextField messagesTextField;

    @FXML
    private TextField errorsTextField;

    @FXML
    private TextArea changesTextArea;

    @FXML
    private Button repeatCheckButton;

    private boolean occupied = false;

    private synchronized boolean setOccupied(boolean value){
        if (value == false){
            occupied = false;
            return true;
        }else{
            if(occupied == true){
                return false;
            }else{
                occupied = true;
                return true;
            }
        }
    }

    private void checkChanges() throws IOException {
        if (this.directory == null || this.directory.length() == 0){
            directoryTextField.setText("");
            messagesTextField.setText("");
            errorsTextField.setText("Choose directory first");
            changesTextArea.setText("");
        }else{
            directoryTextField.setText(this.directory);
            HashMap<String, String> checksStatus = checker.check(this.directory);
            if (checksStatus.containsKey("error")){
                messagesTextField.setText("");
                errorsTextField.setText(checksStatus.get("error"));
                changesTextArea.setText("");
            }else{
                messagesTextField.setText(checksStatus.get("message"));
                errorsTextField.setText("");
                checksStatus.remove("message");
                String changes = "";
                for(String key: checksStatus.keySet()){
                    changes = changes + key + " - " + checksStatus.get(key) +"\n";
                }
                changesTextArea.setText(changes);
            }
        }
    }

    @FXML
    private void onRepeatCheckClick() throws IOException {
        checkChanges();
        messagesTextField.setText(messagesTextField.getText()+" - repeat check");
    }

    @FXML
    protected void onChooseDirectoryClick() throws IOException {
        if(setOccupied(true)){
            Stage stage = (Stage) ap.getScene().getWindow();
            String chosenDirectory = chooser.ChooseDirectory(stage);
            setOccupied(false);
            this.directory = chosenDirectory;
            checkChanges();
        }
    }
}