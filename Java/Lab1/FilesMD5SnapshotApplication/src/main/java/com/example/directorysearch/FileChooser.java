package com.example.directorysearch;

import javafx.scene.Scene;
import javafx.scene.layout.GridPane;
import javafx.stage.DirectoryChooser;
import javafx.stage.Modality;
import javafx.stage.Stage;

import java.io.File;

public class FileChooser {
    public String ChooseDirectory(Stage stage){
        Stage primaryStage = new Stage();
        primaryStage.initModality(Modality.WINDOW_MODAL);
        primaryStage.initOwner(stage);
        DirectoryChooser directoryChooser = new DirectoryChooser();
        String userCatalog = System.getProperty("user.home");
        directoryChooser.setInitialDirectory(new File(userCatalog));
        File selectedDirectory = directoryChooser.showDialog(primaryStage);
        if(selectedDirectory == null){
            return null;
        }
        else{
            return selectedDirectory.getAbsolutePath();
        }
    }
}
