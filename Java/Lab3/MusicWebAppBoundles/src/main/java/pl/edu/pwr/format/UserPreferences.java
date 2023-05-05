package pl.edu.pwr.format;

import java.util.prefs.Preferences;

public class UserPreferences {
    private Preferences preferences;

    public void setPreferences(String language){
        preferences= Preferences.userRoot().node(this.getClass().getName());
        preferences.put("Language",language);
    }
    public String getPreferences(String def){
        preferences=Preferences.userRoot().node(this.getClass().getName());
        String pref=preferences.get("Language", def);
        return pref;
    }
}


