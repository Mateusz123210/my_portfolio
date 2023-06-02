package pl.edu.pwr.cellsmachine;


import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.FileChooser;
import javafx.stage.Stage;

import java.io.File;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.ResourceBundle;

public class HelloController implements Initializable {

    @FXML
    private TextField selectedScriptTextField;
    @FXML
    private AnchorPane ap;
    @FXML
    private Button simulation;
    @FXML
    private Label message;
    private Stage stage;
    private int size = 30;
    private ScriptManager manager;
    private Boolean simulationStarted = false;
    List<List<Button>> buttons = new ArrayList<>();

    public HelloController(){
        manager = new ScriptManager();
    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        Button button = null;
        for(int i = 0; i < size; i++){
            List<Button> newButtons = new ArrayList<>();
            for(int j = 0; j < size; j++){
                button = new Button();
                button.setLayoutX(10 + j * 22);
                button.setLayoutY(65 + i * 22);
                button.setMinHeight(20);
                button.setMinWidth(20);
                button.setMaxHeight(20);
                button.setMaxWidth(20);
                button.setPrefHeight(20);
                button.setPrefWidth(20);
                int finalI = i;
                int finalJ = j;
                button.setOnAction(event -> {
                    onButtonClick(finalI, finalJ);
                });
                setButtonColor(button, "#FFFFFF;");
                newButtons.add(button);
                ap.getChildren().add(button);
            }
            buttons.add(newButtons);
        }
    }

    public void setStage(Stage stage) {
        this.stage = stage;
        stage.setOnCloseRequest(e -> {
            if(simulationStarted)
                manager.stop_simulation();
            Platform.exit();
            System.exit(0);
        });
    }

    @FXML
    private void manageSimulation(){
        if(selectedScriptTextField.getText().length() > 0){
            message.setText("");
            if(!simulationStarted){
                manager.start_simulation(buttons);
                simulationStarted = true;
                simulation.setText("Stop simulation");
            }else{
                manager.stop_simulation();
                simulationStarted = false;
                simulation.setText("Start simulation");
            }
        }else{
            message.setText("Choose script first!");
        }
    }

    @FXML
    private void chooseScript(){
        if(!simulationStarted) {
            Stage stage = (Stage) ap.getScene().getWindow();
            FileChooser fileChooser = new FileChooser();
            fileChooser.setTitle("Choose script");
            fileChooser.setInitialDirectory(new File(System.getProperty("user.dir")));
            fileChooser.getExtensionFilters().add(new FileChooser.ExtensionFilter("JavaScript files", "*.js"));
            File file = null;
            file = fileChooser.showOpenDialog(stage);
            String sel = String.valueOf(file);
            if (file != null) {
                if (manager.readScriptFromFile(sel)) {
                    selectedScriptTextField.setText(String.valueOf(file));
                    message.setText("");
                } else {
                    selectedScriptTextField.setText("");
                    message.setText("That is not valid js file!");
                }
            } else {
                selectedScriptTextField.setText("");
                message.setText("Choose file first!");
            }
        }else{
            message.setText("You can not choose script during simulation!");
        }
    }

    @FXML
    private void onButtonClick(int i, int j){
        if(!simulationStarted){
            message.setText("");
            Button b = buttons.get(i).get(j);
            String style = b.getStyle();
            style = style.substring(style.length() - 7, style.length() - 1);
            if(style.equals("FFFFFF")){
                setButtonColor(b, "#000000;");
            }else if(style.equals("000000")){
                setButtonColor(b, "#FFFFFF;");
            }
        }else message.setText("You can not modify cells during simulation!");
    }

    public void setButtonColor(Button b, String color){
        b.setStyle("-fx-background-color: " + color);
    }
    public static void setButtonColorThreadsafe(Button b, String color){
        Platform.runLater(new Runnable() {
            @Override
            public void run() {
                b.setStyle("-fx-background-color: " + color);
            }
        });

    }
}