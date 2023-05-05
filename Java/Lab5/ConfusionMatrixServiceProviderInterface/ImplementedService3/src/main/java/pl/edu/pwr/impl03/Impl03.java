package pl.edu.pwr.impl03;

import ex.api.AnalysisException;
import ex.api.AnalysisService;
import ex.api.DataSet;
import static java.lang.Math.sqrt;

public class Impl03 implements AnalysisService, Runnable {
    private DataSet result = null;
    private DataSet ds;
    private boolean errors = false;
    private boolean busy = false;

    @Override
    public void setOptions(String[] options) throws AnalysisException {

    }

    @Override
    public String getName() {
        return "Mattheus Correlation Coefficient";
    }

    @Override
    public void submit(DataSet ds) throws AnalysisException{
        if(busy) throw new AnalysisException("Service is busy");
        busy = true;
        this.ds = ds;
        Thread t1 = new Thread(this);
        t1.start();
    }

    @Override
    public DataSet retrieve(boolean clear) throws AnalysisException {
        if(errors) throw new AnalysisException("Error during processing occured!");
        if(clear){
            DataSet ds1 = result;
            result = null;
            return ds1;
        }
        return result;
    }

    public void calculate() throws AnalysisException{
        result = null;
        errors = false;
        String [][] data = ds.getData();
        int c = 0, s = 0;
        Integer tempNumber, tempNumber2;
        for(int i = 0; i < data.length; i++){
            for(int j = 0; j < data.length; j++) {
                try {
                    tempNumber =  Integer.parseInt(data[i][j]);
                    s += tempNumber.intValue();
                    if(i == j) c += tempNumber.intValue();
                }catch(NumberFormatException e){
                    errors = true;
                    throw new AnalysisException("Data contains characters, which are not numbers!");
                }
            }
        }
        int pkTkSum = 0, pk2Sum = 0, tk2Sum = 0;
        for(int i = 0; i < data.length; i++) {
            tempNumber = 0;
            tempNumber2 = 0;
            for(int j = 0; j < data.length; j++) {
                tempNumber += Integer.parseInt(data[i][j]);
                tempNumber2 += Integer.parseInt(data[j][i]);
            }
            pkTkSum += tempNumber.intValue() * tempNumber2.intValue();
            pk2Sum += tempNumber2.intValue() * tempNumber2.intValue();
            tk2Sum += tempNumber.intValue() * tempNumber.intValue();
        }
        int s2 = s * s;
        double correlation = (c * s - pkTkSum) / sqrt((s2 - pk2Sum) * (s2 - tk2Sum));
        if(Double.isNaN(correlation)){
            errors = true;
            throw new AnalysisException("Too many arguments. You can not use these big numbers!");
        }
        DataSet res = new DataSet();
        res.setData(new String[][]{{"Correlation = " + String.valueOf(correlation)}});
        result = res;
        busy = false;
    }

    @Override
    public void run() {
        try {
            calculate();
        } catch (AnalysisException e) {
        }
    }
}