package pl.edu.pwr.cellsmachine;

import javafx.scene.control.Button;

import javax.script.Invocable;
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.List;

public class ScriptManager implements Runnable{

    private ScriptEngine engine = null;
    private Invocable invocable;
    private Thread thread;
    private Boolean stop = false;
    private List<List<Button>> buttons;

    public Boolean readScriptFromFile(String path){
        engine = new ScriptEngineManager().getEngineByName("nashorn");
        try {
            engine.eval(new FileReader(path));
        } catch (ScriptException | FileNotFoundException e) {
            engine = null;
            return false;
        }
        invocable = (Invocable) engine;
        return true;
    }

    public void start_simulation(List<List<Button>> buttons){
        this.buttons = buttons;
        stop = false;
        thread = new Thread(this);
        thread.start();
    }

    public void stop_simulation(){
        stop = true;
        if(thread.isAlive()) {
            try {
                thread.join();
            } catch (InterruptedException e) {
            }
        }
    }

    @Override
    public void run() {
        while(!stop){
            try {
                invocable.invokeFunction("simulate", buttons);
            } catch (ScriptException | NoSuchMethodException ignored) {
            }
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }
}
