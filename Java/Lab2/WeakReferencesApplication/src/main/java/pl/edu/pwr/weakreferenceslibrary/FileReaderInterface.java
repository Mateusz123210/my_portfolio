package pl.edu.pwr.weakreferenceslibrary;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public interface FileReaderInterface {

    default List<String> readFile(String path){
        List<String> readedFromFile;
        try {
            readedFromFile = Files.readAllLines(Paths.get(path), StandardCharsets.UTF_8);
        }
        catch(IOException e){
            return null;
        }
        return readedFromFile;
    }

}
