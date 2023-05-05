package pl.edu.pwr.reflection.loader;

import java.io.*;
import java.util.List;

public class MyClassLoader extends ClassLoader{

    public Class<?> findClass(String className, List<MyClass> classes){
        MyClass cl = null;
        for(int i = 0; i < classes.size(); i++){
            if(classes.get(i).getFileName().equals(className)){
                cl = classes.get(i);
                break;
            }
        }
        Class getClass = cl.getCl();
        if(getClass != null) return getClass;
        String path = cl.getPath();
        byte[] bytes = loadClassFromDisc(path);
        if(bytes == null) return null;
//        System.out.println("v");
//        System.out.println(cl.getPath());
//        System.out.println(cl.getFileName());
//        System.out.println(cl.getCl());
//        System.out.println(cl.getStatus());
//        System.out.println(bytes);
        cl.setCl(defineClass(className, bytes, 0, bytes.length));
        cl.setStatus("loaded");
        cl.setClassLoader(this);
//
//        System.out.println(cl.getPath());
//        System.out.println(cl.getFileName());
//        System.out.println(cl.getCl());
//        System.out.println(cl.getStatus());
//        System.out.println(cl.getCl().getMethods().length);

        return cl.getCl();
    }
    public Class<?> findClass(String className){
        File file = new File(System.getProperty("user.dir"));
        String tempPath = file.getAbsolutePath() + "//compiledClasses//" + className + ".class";
        byte[] bytes = loadClassFromDisc(tempPath);
        if(bytes == null) return null;
        return defineClass(className, bytes, 0, bytes.length);
    }


    public byte[] loadClassFromDisc(String path){
        try (
                InputStream inputStream = new FileInputStream(path);
        ) {
            long fileSize = new File(path).length();
            byte[] allBytes = new byte[(int) fileSize];
            int bytesRead = inputStream.read(allBytes);
            if(bytesRead <= 0) return null;
            else return allBytes;

        } catch (IOException  e) {
            e.printStackTrace();
            return null;
        }
    }
}
