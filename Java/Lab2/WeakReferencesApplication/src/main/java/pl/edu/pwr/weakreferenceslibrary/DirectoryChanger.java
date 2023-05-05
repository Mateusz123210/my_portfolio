package pl.edu.pwr.weakreferenceslibrary;

import javafx.stage.DirectoryChooser;
import javafx.stage.Modality;
import javafx.stage.Stage;

import java.io.File;

public class DirectoryChanger{
    private String path;

    public DirectoryChanger(){
        this.path = new String("");
    }

    public String changeDirectory(Stage stage){
        Stage primaryStage = new Stage();
        primaryStage.initModality(Modality.WINDOW_MODAL);
        primaryStage.initOwner(stage);
        DirectoryChooser directoryChooser = new DirectoryChooser();
        String userCatalog = System.getProperty("user.home");
        directoryChooser.setInitialDirectory(new File(userCatalog));
        File selectedDirectory = directoryChooser.showDialog(primaryStage);
        if(selectedDirectory == null){
            path = "";
        }
        else{
            path = selectedDirectory.getAbsolutePath();
        }
        return path;
    }

    public String getDirectory(){
        return path;
    }
}
