var simulate = function (buttons) {
  var buttonsLength = buttons.length;
  var button;
  var style;
  var hController = Java.type("pl.edu.pwr.cellsmachine.HelloController");
  for (var i = 0; i < buttonsLength; i++) {
    for (var j = 0; j < buttonsLength; j++) {
      var button = buttons.get(i).get(j);
      var style = button.getStyle();
      if (style === "-fx-background-color: #000000;")
        hController.setButtonColorThreadsafe(button, "#FFFFFF;");
      else hController.setButtonColorThreadsafe(button, "#000000;");
    }
  }
};
