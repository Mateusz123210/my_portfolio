package pl.edu.pwr.bundles;

import java.util.ListResourceBundle;

public class Bundles_pl_PL extends ListResourceBundle {
    @Override
    protected Object[][] getContents() {
        return new Object[][]{
                {"chooseAuthorLabel", "Wybierz polskiego autora"},
                {"recordingsQuestionLabel", "Jak du\u017co nagra\u0144 ona/on ma?"},
                {"answerButton", "Odpowiedz"},
                {"validAnswerFirstPart", "Poprawna odpowied\u017a. Artysta ma "},
                {"invalidAnswerFirstPart", "B\u0142\u0119dna odpowied\u017a. Artysta ma "},
                {"connectionError", "B\u0142\u0105d po\u0142\u0105czenia!"},
                {"noAnswer", "Wprowad\u017a odpowied\u017a najpierw!"},
                {"english", "angielski"},
                {"polish", "polski"}
        };
    }
}
