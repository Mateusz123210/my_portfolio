package pl.edu.pwr.reflection.window;

import javafx.scene.control.Label;
import javafx.scene.control.TextArea;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class Worker extends Thread{
    private Method m;
    private Object object;
    private String str;
    private Object a;
    private Label label;
    private TextArea textArea;
    private HelloController controllerReference;

    public Worker(Method m, Object object, String str, Object a, Label label, TextArea textArea,
                 HelloController controllerReference){
        this.m = m;
        this.object = object;
        this.str = str;
        this.a = a;
        this.label = label;
        this.textArea = textArea;
        this.controllerReference = controllerReference;
    }

    @Override
    public void run() {
            try {
                m.invoke(object, str, a, label);
                Method getResult = object.getClass().getMethod("getResult");
                textArea.setText(getResult.invoke(object).toString());
            } catch (IllegalAccessException | InvocationTargetException | NoSuchMethodException e) {
                e.printStackTrace();
            }finally{
                controllerReference.disableRunningMutex();
            }
    }
}
