import javafx.scene.control.Label;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;


public class UpperLetterChanger implements Processor{
    private String result = "";
    private int taskId = 0;

    @Override
    public boolean submitTask(String task, StatusListener sl, Label label) {
        sl = new MyStatusListener(); //bad style
        taskId ++;
        simulateDelationOfWork(sl, label, taskId);
        if(task == null || task.length() == 0){
            result = "Write string first";
            return false;
        }
        result = task.toUpperCase();
        return true;
    }

    @Override
    public String getInfo() {
        return new String("Zamiana małych liter na duże\n" +
                "Przykładowe dane wejściowe algorytmu:\nsniosenios3q23nk23");
    }

    @Override
    public String getResult() {
        return this.result;
    }
}
