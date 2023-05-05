package pl.edu.pwr.bundles;

import java.util.ListResourceBundle;

public class Bundles_en_EN extends ListResourceBundle {

    @Override
    protected Object[][] getContents() {
        return new Object[][]{
                {"chooseAuthorLabel", "Choose polish author"},
            {"recordingsQuestionLabel", "How many recordings has she/he?"},
            {"answerButton", "Answer"},
            {"validAnswerFirstPart", "Valid answer. Artist has "},
            {"invalidAnswerFirstPart", "Invalid answer. Artist has "},
                {"connectionError", "Error in connection!"},
                {"noAnswer", "Insert answer first!"},
                {"english", "english"},
                {"polish", "polish"}
        };
    }
}
