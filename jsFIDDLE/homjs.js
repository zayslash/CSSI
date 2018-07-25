function taskdone(ray){

var bullet = document.getElementById(ray).style.textDecoration;

if (bullet=='line-through'){

document.getElementById(ray).style.textDecoration='none';
}

else{

document.getElementById(ray).style.textDecoration='line-through';

}

}


function clearAll(){

greet= $('.task');
greet.css("text-decoration","none");
}


function createInput(){


    var  $input = $('<input type="button" value="Done" class="task" />');
    $input.appendTo($("ol"));


}




function addListItem(text)
{
  var liList = document.getElementsByClassName("task");
  var largo = liList.length;
var ln = 'task';
  list = document.querySelector('ol');
  item = document.createElement('li');
var largo = liList.length;
var ID = "todo" + (largo+1);

for (i=0; i < liList.length ; i++){
   item.setAttribute("id", ID );
   $('li').addClass('task');
 }

  item.innerHTML = text + ('<input type="button"  onclick="taskdone(' + ID + ')" value="Done"  class="task"       />  ');
  list.appendChild(item);


}


function aAlist()
{
var name = prompt("Enter new Item on your Bucket list:");

  addListItem(name);

}
