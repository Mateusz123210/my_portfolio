package com.example.directorysearch;
import pl.edu.pwr.filesMD5SnapshotLibrary.MD5;

import java.io.IOException;
import java.util.HashMap;

public class Checker {
    private MD5 md5;
    public Checker(){
        this.md5 = new MD5();
    }

    public HashMap<String, String> check(String path) throws IOException {
        return md5.findFilesChanges(path);
    }
}
