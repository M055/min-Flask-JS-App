function goClickedFn() {
  document.getElementById("response_loc").innerHTML='computing..';
  document.getElementById("submit_form").click();

}

function submitClickedFn() {
  var var1 = document.getElementById("select1");
  var var1value= var1.options[var1.selectedIndex].value;
  var s1index = var1.selectedIndex;
  var var2 = document.getElementById("select2");
  var var2value= var2.options[var2.selectedIndex].value;
  var s2index = var2.selectedIndex;
  /* var output_to_POST = var1value+var2value+'>'+s1index+'>'+s2index */
  var output_dict = {'outValue':var1value+var2value, 'pyValue':-1, 'sel1':s1index, 'sel2':s2index};
  var output_to_POST = JSON.stringify(output_dict);
  console.log('POST submitted',output_to_POST);
  document.getElementById("submit_form").value=output_to_POST;
}
