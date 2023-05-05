package pl.edu.pwr.format;

import java.text.ChoiceFormat;
import java.util.ResourceBundle;

public class ChoiceFormatter {
    public String getRecordingValidFormInPolish(String number, ResourceBundle rb1) {
        Integer x = Integer.parseInt(number);
        String number2;
        ChoiceFormat fmt;
        if (x > 100) {
            x = x % 100;
            number2 = x.toString();
            fmt = new ChoiceFormat(
                    rb1.getString("patternForBigNumbers"));
        } else {
            fmt = new ChoiceFormat(
                    "patternForSmallNumbers");
            number2 = number;
        }
        String result=""+number+" "+fmt.format(Integer.parseInt(number2));
        return result;
    }
    public String getRecordingValidForm(String number, ResourceBundle rb1) {
        var fmt = new ChoiceFormat(
                rb1.getString("pattern"));
        String result=""+number+" "+fmt.format(Integer.parseInt(number));
        return result;
    }
    public String getEventValidForm(String number, ResourceBundle rb1) {
        var fmt = new ChoiceFormat(
                rb1.getString("patternForEvents"));
        String result = "" + number + " " + fmt.format(Integer.parseInt(number));
        return result;
    }
}
