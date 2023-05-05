package pl.edu.pwr.api;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.*;
import java.util.ArrayList;
import java.util.HashMap;

public class Api {
    private HttpURLConnection con;
    private String defaultUrl;
    private Parser parser;
    private HashMap<String, String> genres;
    private HashMap<String, String> polishAuthors;

    public Api(){
        defaultUrl = "https://musicbrainz.org/ws/2";
        parser = new Parser();
        genres = new HashMap<>();
        polishAuthors = new HashMap<>();
    }

    public ArrayList<String> getAllPolishAuthors(){
        Document document = connect(defaultUrl + "/artist/?query=country:PL&fmt=xml");
        Element root=document.getDocumentElement();
        Integer length = root.getChildNodes().
                item(0).getChildNodes().getLength();
        for(Integer i = 0; i < length; i++){
            polishAuthors.put(root.getChildNodes().
                    item(0).getChildNodes().item(i).getChildNodes().item(0).
                    getTextContent(), root.getChildNodes().item(0).getChildNodes().item(i).
                    getAttributes().item(0).getNodeValue());
        }
        return new ArrayList<>(polishAuthors.keySet());
    }

public String getNumberOfAuthorRecordings(String author){
    String numberOfRecordings;
    String encodedUrl = (defaultUrl + "/recording/?query=arid:" + polishAuthors.get(author)).replaceAll(" ","%20") + "&fmt=xml";
    Document document = connect(encodedUrl);
    numberOfRecordings = document.getElementsByTagName("recording-list").item(0).getAttributes().item(0).getNodeValue();
    return numberOfRecordings;
}

    public String getNumberOfEventsArtistTookPartIn(String author){
        String numberOfEvents;
        String encodedUrl = (defaultUrl + "/event/?query=arid:" + polishAuthors.get(author)).replaceAll(" ","%20") + "&fmt=xml";
        Document document = connect(encodedUrl);
        numberOfEvents = document.getElementsByTagName("event-list").item(0).getAttributes().item(0).getNodeValue();
        return numberOfEvents;
    }

    public Document connect(String path)  {
        try {
            URL url = new URL(path);
            con = (HttpURLConnection)url.openConnection();
            con.setRequestMethod("GET");

        } catch (ProtocolException e) {
            throw new RuntimeException(e);
        } catch (MalformedURLException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        BufferedReader br;
        StringBuilder sb;
        try {
            br = new BufferedReader(new InputStreamReader(con.getInputStream()));
            sb = new StringBuilder();
            String line;
            while((line=br.readLine()) != null) {
                sb.append(line);
            }
            br.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return parser.parse(sb.toString());
    }
}
