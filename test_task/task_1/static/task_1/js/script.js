$(document).ready( function(){
    $('#duplicate').click( function(){
        $('#field').after('<br><input type="text" placeholder="Name" id="field">');
    });
    $('#add_data').click( function(){
    var form = $('#form_name');
    console.log(form);
    form.on('submit', function(e){
    e.preventDefault();
    console.log('123');
    var arr = [];
    data_1[str_n] = $(this).val();
  arr.push($(this).val());
   });
   console.log(arr.slice(1));


   data = {}
   data["names"] = arr.slice(1);
   var csrf_token = $('#form_name [name="csrfmiddlewaretoken"]').val();
   data["csrfmiddlewaretoken"] = csrf_token;
   var url = form.attr("action");
   $.ajax({
   url: url,
   type: 'POST',
   data: data,
   cache: true,
   success: function (data){
   console.log("Ok");
   },
   error: function(){
   console.log("Error");
   }
      });
//    var name = [];
//    name.push($('#field').val());
//    name.push($('#field1').val());
//    name.push($('#field1').val());
//    name.field = $('#field').val();
//    name.field_1 = $('#field1').val();

    });
    });