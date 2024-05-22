function addtask() {
  var taskinput = document.getElementById("newTask");
  var tasktext = taskinput.value.trim();
  if (tasktext !== "") {
    let li = document.createElement("li");
    li.taskcontent = tasktext;
    document.getElementById("tasklist").appendChild(li);
    taskinput.value = "";
  } else {
    alert("please enter task");
  }
}
