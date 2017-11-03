<!--
$(document).ready();

// count no chars in message text
$("#message").on('keyup', updateCount);

function updateCount() {
var count = $('#message').val().length;

  $('#count').html(count).toggleClass('looong', count > 160);
}


$(document).on("click", ".addtext", function(){
  $('#message').val($(this).parent().prev().text());
  updateCount();
  highlight('#message');

});






$(document).on("click", ".addnumbers", function(){

  var newNumbers = $(this).parent().prev().text();
  var newNumbers = newNumbers.replace(/\s+/g, '') ;
  console.log(newNumbers + '/');

  var oldNumbers = $('#recipient').val();
  if(oldNumbers != '') { newNumbers = oldNumbers + ' , ' + newNumbers; }

  $('#recipient').val(newNumbers);
  highlight('#recipient');


  });


function highlight(selector) {
    $(selector).effect('highlight', {}, 1000);
}



// Grab the HTML source that needs to be compiled
var menuSource = document.getElementById( 'menu-template' ).innerHTML;

// Compiles the source
var menuTemplate = Handlebars.compile( menuSource );


//Data that will replace the handlebars expressions in our template
$.ajax({
    url: 'http://127.0.0.1:8000/templatetext/',
    method: 'GET',
    crossDomain:true,
    dataType: 'json',
    async:true,
    success: function( resp ) {

      // Process Template with Data
      document.getElementById( 'menu-placeholder' ).innerHTML = menuTemplate( resp );

            }
  });


  // Grab the HTML source that needs to be compiled
  var menuSource1 = document.getElementById('numberstemplate').innerHTML;

  // Compiles the source
  var numberstemplate = Handlebars.compile( menuSource1 );

  $.ajax({
      url: 'http://127.0.0.1:8000/group/',
      method: 'GET',
      crossDomain:true,
      dataType: 'json',
      async:true,
      success: function (jsonObjs) {

        for (var key in jsonObjs) {
          if (jsonObjs.hasOwnProperty(key)) {
              console.log(jsonObjs[key].group_name + "   " );

              jQuery.each(jsonObjs[key].contacts, function(index, value)  {
              console.log(value.contact_name,"  ",value.contact_numbers); });
                                            }
                                        }
              // Process Template with Data
      document.getElementById( 'menu-placeholder1' ).innerHTML = numberstemplate( jsonObjs );
                                }
    });



$("#smsform").on('submit', function () {


        var form = $(this);
        form.find("input[type=submit]").attr("disabled", "disabled")

      console.log('submit hit ');

    $.ajax({
        url: 'http://127.0.0.1:5000/sms',
        method: 'GET',
        crossDomain:true,
        async:true,

        data: $('#smsform').serialize()
            }).done(function (responseText) {

        // display response details

        jsonData = JSON.stringify(responseText);
        $("#form_result").append($("<h3>").text("SMS-Versand").css("color", "#205791"));
        $("#form_result").append(jsonData);
      //  $("#form_result").toggle();



    }).fail(function(responseText ) {
        jsonData = JSON.stringify(responseText);
        $("#form_result").append($("<h3>").text("Error - 404 Requested Information / Is Unavailable. Failed to Connect to Server. ").css("color", "red"));
    //    $("#form_result").toggle();

      });

    return false;

});


//  -->
