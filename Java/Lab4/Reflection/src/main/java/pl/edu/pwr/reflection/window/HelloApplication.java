package pl.edu.pwr.reflection.window;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("hello-view.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 960, 600);
        stage.setTitle("Java reflection");
        stage.setScene(scene);
        stage.show();

    }
    @Override
    public void stop(){
        HelloController.getController().stopApplication();
    }

    public static void main(String[] args) {
        launch();
    }
}