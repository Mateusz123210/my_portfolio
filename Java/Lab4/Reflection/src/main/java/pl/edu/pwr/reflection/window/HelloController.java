package pl.edu.pwr.reflection.window;

import javafx.application.Platform;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.DirectoryChooser;
import javafx.stage.Stage;
import pl.edu.pwr.reflection.loader.MyClass;
import pl.edu.pwr.reflection.loader.MyClassLoader;

import java.io.File;
import java.io.IOException;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.reflect.Parameter;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class HelloController implements Initializable, Runnable{
    private Worker worker;
    private MyClassLoader myClassLoader;
    private Object myStatusListener;
    private ArrayList<Class<?>> loadedAdditionalClasses;
    private static HelloController controller;
    private final String directoryMutex = "";
    private final String classesMutex = "";
    private  boolean runningMutex = false;
    private String directory;
    private List<MyClass> allClasses;
    private boolean endProgram;
    private Thread thread;
    @FXML
    private AnchorPane ap;
    @FXML
    private TextField chosenFolderTextField;
    @FXML
    private TextArea infoTextArea;
    @FXML
    private TextArea resultTextArea;
    @FXML
    private Label messageLabel;
    @FXML
    private Label statusLabel;
    @FXML
    private TextField parametersTextField;
    @FXML
    private ListView classesListView;
    private String lastClass;

    public HelloController(){
        this.loadedAdditionalClasses = new ArrayList<>();
        this.myClassLoader = new MyClassLoader();
        controller = this;
        this.allClasses = new ArrayList<>();
        this.directory = null;
        this.endProgram = false;
        this.lastClass = new String("");
    }

    public void disableRunningMutex(){
        this.runningMutex = false;
    }

    private boolean isValidFileExtension(String fileName){
        int index = fileName.lastIndexOf(".");
        if(index > 0 && index == fileName.length() - 6) {
            String extension = fileName.substring(index);
            if (extension.equals(".class")) return true;
        }
        return false;
    }

    private List<String> getAvailableClasses(){
        try(Stream<Path> filesStream = Files.list(Paths.get(this.directory))) {
            return filesStream
                .filter(file -> Files.isRegularFile(file))
                .filter(file -> file.toString().length() > 6)
                .filter(file -> isValidFileExtension(file.toString()))
                .map(Path::toString)
                .collect(Collectors.toList());
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    private void refreshClasses(){
        while(!endProgram) {
            synchronized (directoryMutex){
                if (directory == null) {
                    synchronized (classesMutex){
                        allClasses.forEach(cl -> {
                            unloadClass(cl);
                        });
                        allClasses.clear();
                        Platform.runLater(new Runnable() {
                            @Override
                            public void run() {
                                ObservableList<String> observableList = FXCollections.observableArrayList();
                                classesListView.setItems(observableList);
                            }
                        });
                    }
                } else {
                    synchronized(classesMutex){
                        List<String> newClasses = getAvailableClasses();
                        List<MyClass> deletedClasses = new ArrayList<>();
                        allClasses.forEach(cl -> {
                            if(!newClasses.contains(cl.getPath())) {
                                unloadClass(cl);
                                deletedClasses.add(cl);
                            }
                        });
                        deletedClasses.forEach(k -> {
                            allClasses.remove(k);
                        });
                        newClasses.forEach(value -> {
                            boolean contains = false;
                            for(int i = 0; i < allClasses.size(); i++) {
                                if (allClasses.get(i).getPath().equals(value)) {
                                    contains = true;
                                    break;
                                }
                            }
                            if(contains == false) {
                                String fileName = Paths.get(value).getFileName().toString();
                                fileName = fileName.substring(0, fileName.length() - 6);
                                allClasses.add(new MyClass(value, fileName, null));
                            }
                        });
                        showClasses();
                    }
                }
            }
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    private void showClasses(){
        ObservableList<String> observableList = FXCollections.observableArrayList();
        allClasses.forEach(cl -> {
            observableList.add(cl.getFileName() + "  [" + cl.getStatus() + "]");
        });
        Platform.runLater(new Runnable() {
            @Override
            public void run() {
                classesListView.setItems(observableList);
            }
        });
    }

    @FXML
    private void unloadClass(){
        synchronized(classesMutex){
            Object selectedClass = classesListView.getSelectionModel().getSelectedItem();
            if(selectedClass != null) {
                String selectedClassName = selectedClass.toString().split(" ")[0];
                MyClass cl = null;
                for(MyClass c: allClasses){
                    if(c.getFileName().equals(selectedClassName)){
                        cl =c;
                        break;
                    }
                }
                unloadClass(cl);
                showClasses();
            }else messageLabel.setText("Choose class first");
        }
    }
    private void unloadAllClasses(){
        synchronized(classesMutex) {
            for (MyClass myClass : allClasses) unloadClass(myClass);
        }
    }

    @FXML
    private void loadClass(){
        synchronized(classesMutex){
            Object selectedClass = classesListView.getSelectionModel().getSelectedItem();
            if(selectedClass != null) {
                String selectedClassName = selectedClass.toString().split(" ")[0];
                MyClassLoader tempClassLoader = new MyClassLoader();
                Class a = tempClassLoader.findClass(selectedClassName, allClasses);
                if(a != null){
                    messageLabel.setText("");
                    showClasses();
                }else{
                    messageLabel.setText("Error in loading class");
                }
            }else messageLabel.setText("Choose class first");
        }
    }

    @FXML
    private void getInfo(){
        synchronized(classesMutex){
            Object selectedClass = classesListView.getSelectionModel().getSelectedItem();
            if(selectedClass != null) {
                String selectedClassName = selectedClass.toString().split(" ")[0];
                MyClassLoader tempClassLoader = new MyClassLoader();
                Class a = tempClassLoader.findClass(selectedClassName, allClasses);
                if(a != null){
                    try {
                        MyClass c = findClassByName(selectedClassName);
                        Object object = c.getClassObject();
                        if(object == null) {
                            object = a.getConstructor().newInstance();
                            c.setClassObject(object);
                        }
                        Method m = object.getClass().getMethod("getInfo");
                        infoTextArea.setText(m.invoke(object).toString());
                    } catch (NoSuchMethodException | InstantiationException | IllegalAccessException |
                             InvocationTargetException e) {
                        e.printStackTrace();
                    }
                    messageLabel.setText("");
                    showClasses();
                }else{
                    messageLabel.setText("Error in loading class");
                }
            }

        }
    }
    private MyClass findClassByName(String name){
        for(int i = 0; i < allClasses.size(); i++){
            if(allClasses.get(i).getFileName().equals(name)){
                return allClasses.get(i);
            }
        }
        return null;
    }

    @FXML
    private void work(){
        if(runningMutex == true) return;
        runningMutex = true;
        synchronized(classesMutex){
            Object selectedClass = classesListView.getSelectionModel().getSelectedItem();
            if(selectedClass != null) {
                String selectedClassName = selectedClass.toString().split(" ")[0];
                MyClassLoader tempClassLoader = new MyClassLoader();
                Class a = tempClassLoader.findClass(selectedClassName, allClasses);
                if(a != null){
                    try {
                        MyClass c = findClassByName(selectedClassName);
                        Object object = c.getClassObject();
                        if(object == null) {
                            object = a.getConstructor().newInstance();
                            c.setClassObject(object);
                        }
                        Method[] methods = object.getClass().getMethods();
//                        for(Method b: methods){
//                            System.out.println(b.getName());
//                            Parameter[] ps = b.getParameters();
//                            for(Parameter p: ps){
//                                System.out.println(p.getType());
//                            }
//                        }
//                        System.out.println(loadedAdditionalClasses.get(1).getTypeName());
//                        Class[] parameterTypes = new Class[] {String.class, loadedAdditionalClasses.get(1),
//                                Label.class};
//                        Method m = object.getClass().getMethod("submitTask", parameterTypes);
//                        Class c1 =  loadedAdditionalClasses.get(3);
//                        System.out.println(c1.getName());
//                        System.out.println(c1.getTypeName());
//                        System.out.println(c1.getCanonicalName());
//                        System.out.println(c1.isInterface());
                        Method m = methods[2];
//                        System.out.println(m.getParameterCount());
//                        System.out.println(m.getParameterTypes());
//                        System.out.println(m.getParameters());
//                        Parameter[] ps = m.getParameters();
//                        System.out.println("a");
//                        System.out.println(ps[1].getType());
//                        System.out.println(ps[1].getName());
//                        System.out.println(ps[1].getClass());
//                        System.out.println(ps[1].getModifiers());
//                        System.out.println(myStatusListener.getClass());
//                        String type = loadedAdditionalClasses.get(1).getName();
//                        System.out.println(type);
//                        Class<?> tempClass = Class.forName(type);
//                        Object tempStatusListener = tempClass.cast(myStatusListener);
//                        System.out.println(tempStatusListener.getClass());

                        if(worker != null)
                            worker.join();
                        worker = new Worker(m, object, parametersTextField.getText(), null, statusLabel,
                                resultTextArea, this);
                        worker.start();
                    } catch (InstantiationException | IllegalAccessException | InterruptedException |
                             InvocationTargetException | NoSuchMethodException e) {
                        e.printStackTrace();
                        disableRunningMutex();
                    }
                    messageLabel.setText("");
                    showClasses();
                }else{
                    messageLabel.setText("Error in loading class");
                    disableRunningMutex();
                }
            }else{
                messageLabel.setText("Select class first");
                disableRunningMutex();
            }
        }
    }
//    private <T> T castObject(Class<T> clazz, Object object) {
//        return (T) object;
//    }

    @FXML
    protected void onListViewClick(){
        Object selectedClass = classesListView.getSelectionModel().getSelectedItem();
        if(selectedClass != null) {
            String selectedClassName = selectedClass.toString().split(" ")[0];
            if(!selectedClassName.equals(lastClass)){
                infoTextArea.setText("");
                resultTextArea.setText("");
                messageLabel.setText("");
                statusLabel.setText("");
                lastClass = selectedClassName;
            }
        }
    }

    private void unloadClass(MyClass myClass){
        myClass.setClassObject(null);
        myClass.setCl(null);
        myClass.setClassLoader(null);
        System.gc();
        myClass.setStatus("unloaded");
        messageLabel.setText("");
    }

    public void stopApplication(){
        this.endProgram = true;
        try {
            if(this.thread.isAlive()) this.thread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        loadedAdditionalClasses.clear();
        myClassLoader = null;
        System.gc();
        unloadAllClasses();
//        try {         //Uncomment to see unloading in JConsole
//            Thread.sleep(5000);
//        } catch (InterruptedException e) {
//            throw new RuntimeException(e);
//        }
    }

    @FXML
    protected void onChooseDirectoryClick() throws IOException {
        synchronized(directoryMutex){
            infoTextArea.setText("");
            resultTextArea.setText("");
            messageLabel.setText("");
            statusLabel.setText("");
            lastClass = "";
            Stage stage = (Stage) ap.getScene().getWindow();
            DirectoryChooser ch = new DirectoryChooser();
            ch.setInitialDirectory(new File(System.getProperty("user.dir")));
//            ch.setInitialDirectory(new File("C:\\Users\\mateu\\Desktop\\Java2023\\sources\\maturb808_javata_2023\\lab4\\ReflectionProcessors\\target\\classes"));
            File file = ch.showDialog(stage);
            if(file != null){
                this.directory = String.valueOf(file);
                chosenFolderTextField.setText(this.directory);
            }else{
                this.directory = null;
                chosenFolderTextField.setText("");
            }
        }
    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        thread = new Thread(this);
        thread.start();
        loadedAdditionalClasses.add(myClassLoader.findClass("Status"));
        loadedAdditionalClasses.add(myClassLoader.findClass("StatusListener"));
        loadedAdditionalClasses.add(myClassLoader.findClass("Processor"));
        loadedAdditionalClasses.add(myClassLoader.findClass("MyStatusListener"));
        if(!( loadedAdditionalClasses.get(0) != null || loadedAdditionalClasses.get(1)
         != null || loadedAdditionalClasses.get(2) != null || loadedAdditionalClasses.get(3) != null)){
            messageLabel.setText("Error in application occured");
        }
        try {
            myStatusListener = loadedAdditionalClasses.get(3).getConstructor().newInstance();
        } catch (NoSuchMethodException | InvocationTargetException | InstantiationException | IllegalAccessException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void run() {
        refreshClasses();
    }

    public static HelloController getController(){
        return controller;
    }
}