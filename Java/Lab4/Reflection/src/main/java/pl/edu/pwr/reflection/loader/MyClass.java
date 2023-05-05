package pl.edu.pwr.reflection.loader;

public class MyClass {
    private String path;
    private String fileName;
    private Class cl;
    private String status;
    private Object classObject = null;

    public Object getClassObject() {
        return classObject;
    }

    public void setClassObject(Object classObject) {
        this.classObject = classObject;
    }

    public MyClassLoader getClassLoader() {
        return classLoader;
    }

    public void setClassLoader(MyClassLoader classLoader) {
        this.classLoader = classLoader;
    }

    private MyClassLoader classLoader;

    public String getStatus() {
        return status;
    }
    public void setStatus(String status){
        this.status = status;
    }

    public MyClass(String path, String fileName, Class cl){
        this.path = path;
        this.fileName = fileName;
        this.cl = cl;
        this.status = "unloaded";
    }

    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }

    public String getFileName() {
        return fileName;
    }

    public void setFileName(String fileName) {
        this.fileName = fileName;
    }

    public Class getCl() {
        return cl;
    }

    public void setCl(Class cl) {
        this.cl = cl;
    }
}
