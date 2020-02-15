var index = 1;
    function newElement(){
        var todo = document.getElementById("input_task");
        var td1 = document.createElement("input");
        td1.type = "checkbox"; 
        td1.id = "chk"+index;
        var td2 = document.getElementById("input_task").value; 
        var txt = document.createElement("p");
        txt.id = "item_text";
        td1.onclick = function check_changed(){
            var parent = this.parentNode.id;
            var txt = document.getElementById(parent).querySelector("#item_text");
            if (this.checked){
                txt.style.textDecoration = "line-through";
            }
            else{
                txt.style.textDecoration = "none";
            }
        }
        if (td2 == ""){
            alert("Fill the task");
            return;
        }
        txt.innerHTML = td2;
        var td3 = document.createElement("button");
        td3.id = "delete"; // button
        td3.onclick = function deleteToDo()
        {
            var child = this.parentNode.id;
            if(confirm("Delete " + td2 + " ?"))
                document.getElementById(child).remove();
        }
        var newElement = document.createElement("div");
        newElement.id = "added" + index;
        index = index + 1;
        newElement.appendChild(td1);
        newElement.appendChild(txt);
        newElement.appendChild(td3);
        var todolist = document.getElementById("content");
        todolist.appendChild(newElement);
        todo.value = "";
        alert(td2+" -  new task was added");
    }
    
 
    