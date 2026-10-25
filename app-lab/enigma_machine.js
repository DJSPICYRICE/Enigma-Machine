// Simple Enigma Machine — Code.org App Lab version (April 2023)
// By Mouli Grandhi
// Transcribed from Enigma_Machine_Code.pdf. Runs in Code.org App Lab
// (uses App Lab functions: onEvent, setScreen, getText, setProperty,
// appendItem, removeItem).

//varibles are decleared
var Straightletters = ["A","B","C","D","E","F","G","H","I","J","K","L",
  "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
var r1stright = ["A","B","C","D","E","F","G","H","I","J",
  "K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
var r2stright = ["A","B","C","D","E","F","G","H","I","J",
  "K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
var r3stright = ["A","B","C","D","E","F","G","H","I","J",
  "K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
var Roter1=["E","K","M","F","L","G","D","Q","V","Z","N",
  "T","O","W","Y","H","X","U","S","P","A","I","B","R","C","J"];
var Roter2=["A","J","D","K","S","I","R","U","X","B","L",
  "H","W","T","M","C","Q","G","Z","N","P","Y","F","V","O","E"];
var Roter3=["B","D","F","H","J","L","C","P","R","T","X",
  "V","Z","N","Y","E","I","W","G","A","K","M","U","S","Q","O"];
var reflector=["Y","R","U","H","Q","S","L","D","P","X",
  "N","G","O","K","M","I","E","B","F","Z","C","W","V","J","A","T"];
var input = "Hello";
var r1offset=0;
var r2offset=0;
var r3offset=0;
var Roter2notch = 5;
var Roter3notch = 22;
var output = "";

//event handlers
onEvent("encode", "click", function( ) {
  setScreen("codingscreen");
});
onEvent("decode", "click", function( ) {
  setScreen("codingscreen");
});
onEvent("goencode", "click", function( ) {
  input = getText("encodetext");
  input = input.toUpperCase();
  for(var i=0;i<input.length;i++){
    output = output + encode(Roter1,Roter2,Roter3,input.substring(i,i+1));
  }
  setScreen("outputscrn");
  setProperty("outputbox","text",output);
});

//logic and functions
// this function actully changes the lettres based
//on the a historical enigma roters
function encode(r1, r2, r3, input) {
  if (input == " ") {
    input = " ";
  } else {
    rotate(Roter3,r3stright,r3offset);
    if (r3offset==Roter3notch){
      rotate(Roter2,r2stright,r2offset);
    } if (r2offset==Roter2notch){
      rotate(Roter1,r1stright,r1offset);
    }

    input = r3[Straightletters.indexOf(input)];
    input = r2[r3stright.indexOf(input)];
    input = r1[r2stright.indexOf(input)];

    input = reflector[r1stright.indexOf(input)];
    input = reflector[Straightletters.indexOf(input)];

    input = r1stright[reflector.indexOf(input)];
    input = r2stright[r1.indexOf(input)];
    input = r3stright[r2.indexOf(input)];
    input = Straightletters[r3.indexOf(input)];
  }
  return input;
}

// this function "rotates" the roters
function rotate(roter,stright,offstet){
  appendItem(roter, roter[0]);
  removeItem(roter,0);
  appendItem(stright, stright[0]);
  removeItem(stright,0);
  offstet = Straightletters.indexOf(stright[0]);
}
