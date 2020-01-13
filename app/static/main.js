var submitBtn = document.getElementById('btnSubmit');
var form = document.forms;

submitBtn.addEventListener('click', predict())

function makeArray(collection) {
  var arr = []
  for (let i = 0; i < collection.length; i++) {
    arr.push(collection[i].value)
  }
  arr.push()
}

function predict() {
  var arr = makeArray(form);

  //Send Ajax call
  $.ajax({
      type: 'post',
      url: '/predict',
      data: {
          arrayForm : arr
      },

      success: function(data){
          $('#pred').text(data.prediction);
      }              
  }); 
}
 