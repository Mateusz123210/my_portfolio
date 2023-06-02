var checkNeighbours = function (buttons, buttonsCopy, x, y, hController) {
  var aliveCells = 0;
  if (buttonsCopy[x - 1][y - 1] === 1) aliveCells++;
  if (buttonsCopy[x - 1][y] === 1) aliveCells++;
  if (buttonsCopy[x - 1][y + 1] === 1) aliveCells++;
  if (buttonsCopy[x][y + 1] === 1) aliveCells++;
  if (buttonsCopy[x + 1][y + 1] === 1) aliveCells++;
  if (buttonsCopy[x + 1][y] === 1) aliveCells++;
  if (buttonsCopy[x + 1][y - 1] === 1) aliveCells++;
  if (buttonsCopy[x][y - 1] === 1) aliveCells++;
  if (buttonsCopy[x][y] === 1) {
    if (aliveCells !== 2 && aliveCells !== 3) {
      hController.setButtonColorThreadsafe(buttons.get(x).get(y), "#000000;");
    }
  } else {
    if (aliveCells === 3) {
      hController.setButtonColorThreadsafe(buttons.get(x).get(y), "#FFFFFF;");
    }
  }
};

var simulate = function (buttons) {
  var buttonsLength = buttons.length;
  var buttonsCopy = new Array(buttonsLength);
  for (var el = 0; el < buttonsLength; el++) {
    buttonsCopy[el] = new Array(buttonsCopy);
  }
  var button;
  var style;
  var hController = Java.type("pl.edu.pwr.cellsmachine.HelloController");
  for (var i = 0; i < buttonsLength; i++) {
    for (var j = 0; j < buttonsLength; j++) {
      var button = buttons.get(i).get(j);
      var style = button.getStyle();
      if (style === "-fx-background-color: #FFFFFF;") buttonsCopy[i][j] = 1;
      else buttonsCopy[i][j] = 0;
    }
  }
  for (i = 1; i < buttonsLength - 1; i++) {
    for (j = 1; j < buttonsLength - 1; j++) {
      checkNeighbours(buttons, buttonsCopy, i, j, hController);
    }
  }
};
