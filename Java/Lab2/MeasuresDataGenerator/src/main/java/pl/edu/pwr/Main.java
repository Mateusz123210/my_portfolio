package pl.edu.pwr;


import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.Random;

public class Main extends Thread{
    private String data;
    private Main(String data){
        this.data = data;
    }

    private void generateRandomStartData(Integer startHour, Integer startMinute, Integer positionNumber, Integer numberOfRows){
        String startHourStr;
        String startMinutesStr;
        String positionNumberStr;
        String temp = startHour.toString();
        StringBuilder sb = new StringBuilder();
        Integer length = temp.length();
        for (Integer i = 0; i < 2 - length; i++)
            sb.append("0");
        sb.append(temp);
        startHourStr = sb.toString();
        sb.setLength(0);
        temp = startMinute.toString();
        length = temp.length();
        for (Integer i = 0; i < 2 - length; i++)
            sb.append("0");
        sb.append(temp);
        startMinutesStr = sb.toString();
        sb.setLength(0);
        temp = positionNumber.toString();
        length = temp.length();
        for (Integer i = 0; i < 4 - length; i++)
            sb.append("0");
        sb.append(temp);
        positionNumberStr = sb.toString();
        String pathToDirectory = "C:\\Users\\mateu\\Desktop\\Java2023\\sources\\maturb808_javata_2023\\Lab2\\MeasuresData\\" +
                data + "\\"+ "" + positionNumberStr + "_" + startHourStr + "_" + startMinutesStr + ".csv";
        File file = new File(pathToDirectory);
        try {
            file.createNewFile();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        Integer hours;
        Integer minutes;
        Float atmosphericPressure;
        Float temperature;
        Integer humidity;
        Random random = new Random();
        sb.setLength(0);
        sb.append("# godzina pomiaru; ciśnienie [hPa];  temperatura [stopnie C]; wilgotność [%]\n");
        String row = sb.toString();
        Path path = Paths.get(pathToDirectory);
        try {
            Files.writeString(path, row, StandardOpenOption.APPEND);
        }catch(IOException e){
            e.printStackTrace();
        }
        for(Integer i = 0; i < numberOfRows; i++){
            hours = random.nextInt(startHour,24);
            if(hours == startHour){
                minutes = random.nextInt(startMinute,60);
            }else{
                minutes = random.nextInt(0,60);
            }
            atmosphericPressure = random.nextFloat(980.00f, 1020.00f);
            temperature =  random.nextFloat(-50.00f, 50.00f);
            humidity = random.nextInt(0,100);
            sb.setLength(0);
            sb.append(hours + ":" + minutes + "; " + atmosphericPressure + "; " + temperature + "; " +
                    humidity + ";\n");
            row = sb.toString();
            try {
                Files.writeString(path, row, StandardOpenOption.APPEND);
            }catch(IOException e){
                e.printStackTrace();
            }
        }
    }
    private void generateDayRandomData(){
        Random r = new Random();
        for(Integer i = 0; i < 17; i ++){
            generateRandomStartData(r.nextInt(0, 10), r.nextInt(0, 60),i + 1,
                    150000);
        }
    }
    public void run(){
        generateDayRandomData();
    }

    public static void main(String[] args) {
        Main m1 = new Main("01.03.2023");
        Main m2 = new Main("03.02.2023");
        Main m3 = new Main("03.03.2023");
        Main m4 = new Main("05.02.2023");
        Main m5 = new Main("07.01.2023");
        Main m6 = new Main("08.02.2023");
        Main m7 = new Main("17.01.2023");
        Main m8 = new Main("22.02.2023");
        m1.start();
        m2.start();
        m3.start();
        m4.start();
        m5.start();
        m6.start();
        m7.start();
        m8.start();
    }
}