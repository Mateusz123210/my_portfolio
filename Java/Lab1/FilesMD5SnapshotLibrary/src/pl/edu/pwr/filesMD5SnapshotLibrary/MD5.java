package pl.edu.pwr.filesMD5SnapshotLibrary;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.HashMap;
import javax.xml.bind.DatatypeConverter;

public class MD5 {
    private FilesSearch filesSearch;
    private FileReader fileReader;
    private Snapshot snapshot;
    public MD5(){
        this.filesSearch = new FilesSearch();
        this.fileReader = new FileReader();
        this.snapshot = new Snapshot();
    }
    //Function returns md5 hash for one chosen file
    private String getFileMD5Hash(String path) {
        MessageDigest md = null;
        try {
            md = MessageDigest.getInstance("MD5");
        } catch (NoSuchAlgorithmException e) {
            return null;
        }
        byte[] readedFile = this.fileReader.getFileBytes(path);
        StringBuilder hash = new StringBuilder();
        if (readedFile == null) return null;
        md.update(readedFile);
        byte[] digest = md.digest();
        hash.append(DatatypeConverter.printHexBinary(digest));
        return hash.toString();
    }
    //Function returns md5 hash for all files in directory
    private HashMap<String, String> calculateMD5OfAllFiles(String directoryPath) throws IOException {
        HashMap<String, String> filesPathsAndMD5 = new HashMap<>();
        ArrayList<String> allFiles = this.filesSearch.getFilesPathsInDirectoryAndSubdirectories(directoryPath);
        String hashCode;
        if (allFiles.isEmpty()) return null;
        for(String i: allFiles){
            hashCode = getFileMD5Hash(i);
            if(hashCode == null) return null;
            if(hashCode.length() == 0) continue;
            filesPathsAndMD5.put(i, hashCode);
        }
        return filesPathsAndMD5;
    }
    //Function finds all changes in files in specified directory
    public HashMap<String, String> findFilesChanges(String directoryPath) throws IOException {
        HashMap<String, String> changes = new HashMap<>();
        if(! Files.exists(Paths.get(directoryPath))){
            changes.put("error", "Directory does not exist");
            return changes;
        }
        HashMap<String, String> newMD5Shortcuts;
        try {
            newMD5Shortcuts = calculateMD5OfAllFiles(directoryPath);
        }catch(Exception e){
            changes.put("error", "Calculating md5 failed");
            return changes;
        }
        HashMap<String, String> oldMD5Shortcuts = this.snapshot.readSnapshotfromFile(directoryPath);
        if(oldMD5Shortcuts == null) {
            changes.put("message", "Snapshot done first time");
        }else{
            changes.put("message", "Files checked");
            newMD5Shortcuts.forEach((key, value) -> {
                if(oldMD5Shortcuts.containsKey(key)){
                    if(oldMD5Shortcuts.get(key).equals(value)){
                        changes.put(key, "unchanged");
                    }else{
                        changes.put(key, "changed");
                    }
                    oldMD5Shortcuts.remove(key);
                }else{
                    changes.put(key, "File created");
                }
            });
            oldMD5Shortcuts.forEach((key, value) -> {
               changes.put(key, "File deleted");
            });
        }
        if(!this.snapshot.writeSnapshotToFile(directoryPath, newMD5Shortcuts)){
            changes.put("error", "Saving snapshot to file failed");
        }
        return changes;
    }

    public static void main(String[] args) throws IOException {
        MD5 md5 = new MD5();
        System.out.println(md5.findFilesChanges("C:\\Users").toString());
    }
}
