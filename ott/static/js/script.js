//let a = 10;
//alert(a);
//console.log(a);
//document.write(a);
// let a = 10.2;
// //const b = 20;
// let b = 15;
// if (a > b) {
//   console.log("not");
// } else if (a == b) {
//   console.log("yes");
// } else {
//   console.log("Noo");
// }
// switch (a) {
//   case 1:
//     console.log("1");
//   //break;
//   case 10:
//     console.log("10");
//   //break;
//   case 15:
//     console.log("15");
//     break;
// }
// for (let index = 0; index < 10; index++) {
//   console.log(index);
// }
// let j = 0;
// while (j < 9) {
//   console.log(j);
//   j++;
// }
// j = 1;
// do {
//   console.log(j);
//   j++;
// } while (j < 6);
// function addTwoNums(a, b) {
//   let c = a + b;
//   console.log(c);
// }
// addTwoNums(2, 10);
// console.log(a);
// console.log(typeof a);
// let arr = ["2", 3];
// console.log(arr);
// console.log(arr.length);
// arr[50] = 1;
// console.log(arr);
// console.log(arr[10]);
//let v = document.getElementById("text").value="20";

// function add() {
//   let t1 = document.getElementById("t1").value;
//   let t2 = document.getElementById("t2").value;
//   if (t1 == "" || t2 == "") {
//     alert("Cannot be empty");
//   } else {
//     alert(parseInt(t1) + parseInt(t2));
//   }
// }
// function down(){
//   document.getElementById("t3").style.backgroundColor = "red";
// }
// function up(){
//   var x = document.getElementById("t4");
//   x.value = x.value.toUpperCase();
// }
// function change() {
//   alert("The input value has changed.")
// }
$(document).ready(function () {
  let v = $("#t1").val(20);
  //alert(v)
});
//alert("Outside JQuery")
$("#add").click(function () {
  //alert("button")
  //$("#hid").hide();
  //$("#hid").show();
  //$("#hid").toggle();
  //let b=$("#spanid").text()
  let h = $("#spanid").html();
  alert(h);
});
$("#aye,#ayee").click(function () {
  // let sr=$("#imag").attr("src");
  // let ah=$("#ahref").attr("href");
  // alert(sr)
  // alert(ah)
  //$("#imag").attr("src","static/media/unknown.png");
  //$("#spanid").text("Ramu the NOOB");
  $("#spanid").append("<br>Ramu the Manners byad enro");
  $("strong").css({ color: "red", "background-color": "black" });
});
