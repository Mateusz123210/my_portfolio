import javafx.application.Platform;
import javafx.scene.control.Label;

public class MyStatusListener implements StatusListener{

    @Override
    public void statusChanged(Status s, Label label) {
        Platform.runLater(() -> label.setText("Task id: " + String.valueOf(s.getTaskId()) + ", progress: " +
                String.valueOf(s.getProgress()) + " %"));

    }
}
