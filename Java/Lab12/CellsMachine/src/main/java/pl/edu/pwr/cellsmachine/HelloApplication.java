package pl.edu.pwr.cellsmachine;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {

    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("hello-view.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 900, 750);
        stage.setTitle("Cells machine");
        stage.setScene(scene);
        HelloController helloController = fxmlLoader.getController();
        helloController.setStage(stage);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}