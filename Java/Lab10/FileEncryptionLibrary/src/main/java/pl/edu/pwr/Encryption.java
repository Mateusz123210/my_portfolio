package pl.edu.pwr;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import java.io.ByteArrayOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.*;
import java.security.spec.EncodedKeySpec;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.PKCS8EncodedKeySpec;
import java.security.spec.X509EncodedKeySpec;

public class Encryption {

    public String encrypt(String inputFile, String outputFile,
                          String privateKeyFile) {
        String resp = getSize(privateKeyFile);
        if(resp == null) return "Error occurred";
        int keySize = 0;
        try{
            keySize = Integer.parseInt(resp);
        }catch(NumberFormatException e){
            return "Error occurred";
        }
        if(keySize <= 0) return "Error occurred";
        int dataSize = keySize / 8 - 12;
        byte[] readedBytes = null;
        try {
            readedBytes = Files.readAllBytes(Path.of(inputFile));
        } catch (IOException e) {
            return "Error in reading file to encryption from disk!";
        }
        byte[] readedKey = null;
        try {
            readedKey = Files.readAllBytes(Path.of(privateKeyFile));
        } catch (IOException e) {
            return "Error in reading private key from disk!";
        }
        KeyFactory keyFactory;
        try {
            keyFactory = KeyFactory.getInstance("RSA");
        } catch (NoSuchAlgorithmException e) {
            return "Error. Invalid algorithm name!";
        }
        EncodedKeySpec encodedKeySpec = new PKCS8EncodedKeySpec(readedKey);
        PrivateKey privateKey = null;
        try {
            privateKey = keyFactory.generatePrivate(encodedKeySpec);
        } catch (InvalidKeySpecException e) {
            return "Error! Key file is invalid!";
        }
        Cipher cipher;
        try {
            cipher = Cipher.getInstance("RSA");
            cipher.init(Cipher.ENCRYPT_MODE, privateKey);

        } catch (NoSuchAlgorithmException | NoSuchPaddingException | InvalidKeyException e) {
            return "Error occurred";
        }
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        int length = readedBytes.length;
        int temp_size = 0;
        byte[] temp;
        for (int i = 0; i < length; i += dataSize) {
            temp_size = Math.min(length - i, dataSize);
            temp = new byte[temp_size];
            System.arraycopy(readedBytes, i, temp, 0, temp_size);
            byte[] doFinal = null;
            try {
                doFinal = cipher.doFinal(temp);
            } catch (IllegalBlockSizeException | BadPaddingException e) {
                return "Error occurred";
            }
            try {
                outputStream.write(doFinal);
            } catch (IOException e) {
                return "Error occurred";
            }
        }
        byte[] resultBytes = outputStream.toByteArray();
        try (FileOutputStream stream = new FileOutputStream(String.valueOf(Path.of(outputFile)))) {
            stream.write(resultBytes);
        } catch (IOException e) {
            return "Error in writing encrypted file to disk!";
        }
        return "File encrypted!";
    }

    public String decrypt(String inputFile, String outputFile,
                          String publicKeyFile) {
        String resp = getSize(publicKeyFile);
        if(resp == null) return "Error occurred";
        int keySize = 0;
        try{
            keySize = Integer.parseInt(resp);
        }catch(NumberFormatException e){
            return "Error occurred";
        }
        if(keySize <= 0) return "Error occurred";
        int encryptedSize = keySize / 8;
        byte[] readedBytes = null;
        try {
            readedBytes = Files.readAllBytes(Path.of(inputFile));
        } catch (IOException e) {
            return "Error in reading file to decryption from disk!";
        }
        byte[] readedKey = null;
        try {
            readedKey = Files.readAllBytes(Path.of(publicKeyFile));
        } catch (IOException e) {
            return "Error in reading public key from disk!";
        }
        KeyFactory keyFactory;
        try {
            keyFactory = KeyFactory.getInstance("RSA");
        } catch (NoSuchAlgorithmException e) {
            return "Error. Invalid algorithm name!";
        }
        EncodedKeySpec encodedKeySpec = new X509EncodedKeySpec(readedKey);
        PublicKey publicKey = null;
        try {
            publicKey = keyFactory.generatePublic(encodedKeySpec);
        } catch (InvalidKeySpecException e) {
            return "Error! Key file is invalid!";
        }
        Cipher cipher;
        try {
            cipher = Cipher.getInstance("RSA");
            cipher.init(Cipher.DECRYPT_MODE, publicKey);
        } catch (NoSuchAlgorithmException | NoSuchPaddingException | InvalidKeyException e) {
            return "Error occurred";
        }
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        int length = readedBytes.length;
        int temp_size = 0;
        byte[] temp;
        for (int i = 0; i < length; i += encryptedSize) {
            temp_size = Math.min(length - i, encryptedSize);
            temp = new byte[temp_size];
            System.arraycopy(readedBytes, i, temp, 0, temp_size);
            byte[] doFinal = null;
            try {
                doFinal = cipher.doFinal(temp);
            } catch (IllegalBlockSizeException | BadPaddingException e) {
                return "Error occurred";
            }
            try {
                outputStream.write(doFinal);
            } catch (IOException e) {
                return "Error occurred";
            }
        }
        byte[] resultBytes = outputStream.toByteArray();
        try (FileOutputStream stream = new FileOutputStream(String.valueOf(Path.of(outputFile)))) {
            stream.write(resultBytes);
        } catch (IOException e) {
            return "Error in writing decrypted file to disk!";
        }
        return "File decrypted!";
    }

    private String getSize(String keyFile){
        char[] fileName = Paths.get(keyFile).getFileName().toString().toCharArray();
        StringBuilder stringBuilder = new StringBuilder();
        int i = 0;
        while(fileName[i] >= 'A' && fileName[i] <= 'Z') i++;

        for(i = i; i < fileName.length; i++){
            if(fileName[i] >= '0' && fileName[i] <= '9'){
                stringBuilder.append(fileName[i]);
            }else break;
        }
        String keySize = stringBuilder.toString();
        if(keySize.length() == 0) return null;
        return keySize;
    }
}